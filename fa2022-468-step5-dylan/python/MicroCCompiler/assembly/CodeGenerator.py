import sys
import os
from typing import List

from ..register import *
from .CodeObject import CodeObject
from .InstructionList import InstructionList
from .instructions import *
from ..compiler import *
from ..ast import *
from ..ast.visitor.AbstractASTVisitor import AbstractASTVisitor

class CodeGenerator(AbstractASTVisitor):

  def __init__(self):
    self.intRegCount = 0
    self.floatRegCount = 0
    self.intTempPrefix = '$t'
    self.floatTempPrefix = '$f'
    self.loopLabel = 0
    self.elseLabel = 0
    self.outLabel = 0
    self.currFunc = None

    self.numIntRegisters = 32
    self.numFloatRegisters = 32

  def getIntRegCount(self):
    return self.intRegCount

  def getFloatRegCount(self):
    return self.floatRegCount

  # Generate code for Variables
  #
  # Create a code object that just holds a variable
  # NOTE THAT THIS HAS CHANGED TO GENERATE 3AC INSTEAD
  # Important: add a pointer from the code object to the symbol table entry so
  # we know how to generate code for it later (we'll need it to find the
  # address)
  #
  # Mark the code object as holding a variable, and also as an lval

  def postprocessVarNode(self, node: VarNode) -> CodeObject:
    sym = node.getSymbol()

    co = CodeObject(sym)
    co.lval = True
    co.type = node.getType()

    if sym.isLocal():
      co.temp = "$l" + str(sym.getAddress())
    else:
      co.temp = "$g" + sym.getName()

    return co

  # Generate code for IntLiterals
  #
  # NOTE THAT THIS HAS CHANGED TO GENERATE 3AC INSTEAD
  
  def postprocessIntLitNode(self, node: IntLitNode) -> CodeObject:
    co = CodeObject()
    i = Li(self.generateTemp(Scope.Type.INT), node.getVal())
		
    #Load an immediate into a register
		#The li and la instructions are the same, but it's helpful to distinguish
		#for readability purposes.
		#li tmp' value

    co.code.append(i) #add this instruction to the code object
    co.lval = False #co holds an rval -- data
    co.temp = i.getDest()
    co.type = node.getType() # temp is in destination of li
    return co

  # Generate code for FloatLiterals
  #
  # NOTE THAT THIS HAS CHANGED TO GENERATE 3AC INSTEAD

  def postprocessFloatLitNode(self, node: FloatLitNode) -> CodeObject:
    co = CodeObject()

    #Load an immediate into a register
		#The li and la instructions are the same, but it's helpful to distinguish
		#for readability purposes.
		#li tmp' value
    i = FImm(self.generateTemp(Scope.Type.FLOAT), node.getVal())
    
    co.code.append(i) # add this instruction to the code object
    co.lval = False # co holds an rval -- data
    co.temp = i.getDest() # temp is in destination of li
    co.type = node.getType()
    return co

	 # Generate code for binary operations.
	 # 
	 # Step 0: create new code object
	 # Step 1: add code from left child
	 # Step 1a: if left child is an lval, add a load to get the data
	 # Step 2: add code from right child
	 # Step 2a: if right child is an lval, add a load to get the data
	 # Step 3: generate binary operation using temps from left and right
	 # 
	 # Don't forget to update the temp and lval fields of the code object!
	 # 	   Hint: where is the result stored? Is this data or an address?

  def postprocessBinaryOpNode(self, node: BinaryOpNode, left: CodeObject, right: CodeObject) -> CodeObject:
    co = CodeObject()
    #FILL CODE FOR STEP 2
    #MODIFY THIS TO GENERATE 3AC INSTEAD
    #step 1
    co.code.extend(left.code)
    #step 2
    co.code.extend(right.code)
    il = InstructionList()
    
    #step 3
    opType = node.getOp()
    leftType = node.getType()
    if (leftType is Scope.Type.FLOAT):
      co.temp = self.generateTemp(Scope.Type.FLOAT)
      if (opType == BinaryOpNode.OpType.ADD): #fadds
        il.append(FAdd(left.temp, right.temp, co.temp))
      elif (opType == BinaryOpNode.OpType.SUB): #fsubs
        il.append(FSub(left.temp, right.temp, co.temp))
      elif (opType == BinaryOpNode.OpType.MUL): #fmuls
        il.append(FMul(left.temp, right.temp, co.temp))
      elif (opType == BinaryOpNode.OpType.DIV): #fdivs
        il.append(FDiv(left.temp, right.temp, co.temp))
    else:
      co.temp = self.generateTemp(Scope.Type.INT)
      if (opType == BinaryOpNode.OpType.ADD): #adds
        il.append(Add(left.temp, right.temp, co.temp))
      elif (opType == BinaryOpNode.OpType.SUB): #subs
        il.append(Sub(left.temp, right.temp, co.temp))
      elif (opType == BinaryOpNode.OpType.MUL): #muls
        il.append(Mul(left.temp, right.temp, co.temp))
      elif (opType == BinaryOpNode.OpType.DIV): #divs
        il.append(Div(left.temp, right.temp, co.temp))
    co.code.extend(il)
    return co
	 
   #  Generate code for unary operations.
	 #  
	 #  Step 0: create new code object
	 #  Step 1: add code from child expression
	 #  Step 2: generate instruction to perform unary operation (don't forget to generate right type of op)
	 #  
	 #  Don't forget to update the temp and lval fields of the code object!
	 #  	   Hint: where is the result stored? Is this data or an address?
	  
  def postprocessUnaryOpNode(self, node: UnaryOpNode, expr: CodeObject) -> CodeObject:
    co = CodeObject()
    #FILL IN CODE FOR STEP 2
    #MODIFY THIS TO GENERATE 3AC INSTEAD

    #step 1
    co.code.extend(expr.code)
    il = InstructionList()

    #step 2
    opType = node.getOp()
    exprType = expr.getType()
    
    if (exprType is Scope.Type.FLOAT):
      co.temp = self.generateTemp(Scope.Type.FLOAT)
      if opType == UnaryOpNode.OpType.NEG:
        il.append(FNeg(expr.temp, co.temp))
    else:
      co.temp = self.generateTemp(Scope.Type.INT)
      if opType == UnaryOpNode.OpType.NEG:
        il.append(Neg(expr.temp, co.temp))
    co.code.extend(il)
    return co

	 # Generate code for assignment statements
	 # 
	 # Step 0: create new code object
	 # Step 1a: if LHS is a variable, generate a load instruction to get the address into a register
	 #          (see generateAddrFromVariable)
	 # Step 1b: add code from LHS of assignment (make sure it results in an lval!)
	 # Step 2: add code from RHS of assignment
	 # Step 2a: if right child is an lval, add a load to get the data
	 # Step 3: generate store (don't forget to generate the right type of store)
	 # 
	 # Hint: it is going to be easiest to just generate a store with a 0 immediate
	 # offset, and the complete store address in a register:
	 # 
	 # sw rhs 0(lhs)

  def postprocessAssignNode(self, node: AssignNode, left: CodeObject, right: CodeObject) -> CodeObject:
    co = CodeObject()
    assert(left.lval is True)

    #Step 1a
    if left.isVar():
      left = self.generateAddrFromVariable(left)
    #FILL IN CODE FOR STEP 2
    #MODIFY THIS CODE TO GENERATE 3AC INSTEAD
	  #Step 1b
    il = InstructionList()

    #step 2
    co.code.extend(right.code)

    #step 3
    nodeType = node.getType()
    if type(left) is InstructionList:
      if nodeType is Scope.Type.FLOAT:
        fsw = Fsw(left.getLast().getDest(), right.temp, "0")
        il.append(fsw)
      else:
        sw = Sw(left.getLast().getDest(), right.temp, "0")
        il.append(sw)
    else:
      if nodeType is Scope.Type.FLOAT:
        fsw = Fsw("fp", right.temp, left)
        il.append(fsw)
      else:
        sw = Sw("fp", right.temp, left)
        il.append(sw)
    co.code.extend(il)
    return co

  # Add together all the lists of instructions generated by the children

  def postprocessStatementListNode(self, node: StatementListNode, statements: list) -> CodeObject:
    co = CodeObject()

    for subcode in statements:
      co.code.extend(subcode.code)

    co.type = None
    return co

	 # Generate code for read
	 # 
	 # Step 0: create new code object
	 # Step 1: add code from VarNode (make sure it's an lval)
	 # Step 2: generate GetI instruction, storing into temp
	 # Step 3: generate store, to store temp in variable
   # NOTE THAT THIS HAS CHANGED TO GENERATE 3AC INSTEAD
	
  def postprocessReadNode(self, node: ReadNode, var: CodeObject) -> CodeObject:
    co = CodeObject()
    assert(var.getSTE() is not None)

    il = InstructionList()

    typ = node.getType()

    if typ == Scope.Type.INT:
 		  # Code to generate if INT:
			#	geti var.tmp
      geti: Instruction = GetI(var.temp)
      il.append(geti)
    elif typ == Scope.Type.FLOAT:
      # Code to generate if FLOAT:
			#	getf var.tmp
      getf = GetF(var.temp)
      il.append(getf)
    else:
      raise Exception("Shouldn't read into other variable")

    co.code.extend(il)

    co.lval = False #doesn't matter
    co.temp = None #set to None to trigger errors
    co.type = None #set to None to trigger errors

    return co
	 
   # Generate code for print
	 # 
	 # Step 0: create new code object
	 # 
	 # If printing a string:
	 # Step 1: add code from expression to be printed (make sure it's an lval)
	 # Step 2: generate a PutS instruction printing the result of the expression
	 # 
	 # If printing an integer:
	 # Step 1: add code from the expression to be printed
	 # Step 1a: if it's an lval, generate a load to get the data
	 # Step 2: Generate PutI that prints the temporary holding the expression
   # NOTE THAT THIS HAS CHANGED TO GENERATE 3AC INSTEAD

  def postprocessWriteNode(self, node: WriteNode, expr: CodeObject) -> CodeObject:
    co = CodeObject()
    #generating code for write(expr)

    #for strings, we expect a variable
    if node.getWriteExpr().getType() == Scope.Type.STRING:
      #Step 1:
      assert(expr.getSTE() is not None)
      #Step 2:
      write = PutS(expr.temp)
      co.code.append(write)
    else:
      #Step 1:
      co.code.extend(expr.code)

      #Step 2:
      #if type of writenode is int, use puti, if float, use putf
      write = None
      typ = node.getWriteExpr().getType()
      if typ == Scope.Type.STRING:
        raise Exception("Shouldn't have a STRING here")
      elif typ == Scope.Type.INT:
        write = PutI(expr.temp)
      elif typ == Scope.Type.FLOAT:
        write = PutF(expr.temp)
      else:
        raise Exception("WriteNode has a weird type")
      co.code.append(write)

    co.lval = False #doesn't matter
    co.temp = None #set to None to trigger errors
    co.type = None #set to None to trigger errors
    return co

	#  Generating an instruction sequence for a conditional expression
	#  
	#  Implement this however you like. One suggestion:
	# 
	#  Create the code for the left and right side of the conditional, but defer
	#  generating the branch until you process IfStatementNode or WhileNode (since you
	#  do not know the labels yet). Modify CodeObject so you can save the necessary
	#  information to generate the branch instruction in IfStatementNode or WhileNode
	#  
	#  Alternate idea 1:
	#  
	#  Don't do anything as part of CodeGenerator. Create a new visitor class
	#  that you invoke *within* your processing of IfStatementNode or WhileNode
	#  
	#  Alternate idea 2:
	#  
	#  Create the branch instruction in this function, then tweak it as necessary in
	#  IfStatementNode or WhileNode
	#  
	#  Hint: you may need to preserve extra information in the returned CodeObject to
	#  make sure you know the type of branch code to generate (int vs float)

  def postprocessCondNode(self, node: CondNode, left: CodeObject, right: CodeObject) -> CodeObject:
    co = CodeObject()
    #FILL IN CODE FROM STEP 3
    #MODIFY THIS CODE TO GENERATE 3AC INSTEAD
    varType = left.getType()
    #step 1
    co.code.extend(left.code)
    #step 2
    co.code.extend(right.code)
    il = InstructionList()

    condType = node.getOp()
    #condTypeString = node.getOpFromString(condType)
    #varType = left.getType()

    if (varType is Scope.Type.FLOAT):
      co.temp = self.generateTemp(Scope.Type.INT)
      co.type = Scope.Type.INT
      if (condType == '=='):
        il.append(Feq(left.temp, right.temp, co.temp))
        il.append(Beq(co.temp, 'x0', '0'))
      elif (condType == '!='):
        il.append(Feq(left.temp, right.temp, co.temp))
        il.append(Bne(co.temp, 'x0', '0'))
      elif (condType == '<'):
        il.append(Fle(left.temp, right.temp, co.temp))
        il.append(Beq(co.temp, 'x0', '0'))
      elif (condType == '<='):
        il.append(Flt(left.temp, right.temp, co.temp))
        il.append(Beq(co.temp, 'x0', '0'))
      elif (condType == '>'):
        il.append(Fle(left.temp, right.temp, co.temp))
        il.append(Bne(co.temp, 'x0', '0'))
      elif (condType == '>='):
        il.append(Flt(left.temp, right.temp, co.temp))
        il.append(Bne(co.temp, 'x0', '0'))
    else:
      if (condType == '=='):
        il.append(Bne(left.temp, right.temp, '0'))
      elif (condType == '!='):
        il.append(Beq(left.temp, right.temp, '0'))
      elif (condType == '<'):
        il.append(Bge(left.temp, right.temp, '0'))
      elif (condType == '<='):
        il.append(Bgt(left.temp, right.temp, '0'))
      elif (condType == '>'): 
        il.append(Ble(left.temp, right.temp, '0'))
      elif (condType == '>='):
        il.append(Blt(left.temp, right.temp, '0'))
    co.code.extend(il)
    co.branch = co.code.data.__len__() - 1
    return co

   # Code generation for IfStatement
	 # Step 0: Create code object
	 # 
	 # Step 1: generate labels
	 # 
	 # Step 2: add code from conditional expression
	 # 
	 # Step 3: create branch statement (if not created as part of step 2)
	 # 			don't forget to generate correct branch based on type
	 # 
	 # Step 4: generate code
	 # 		<cond code>
	 #		<flipped branch> elseLabel
	 #		<then code>
	 #		j outLabel
	 #		elseLabel:
	 #		<else code>
	 #		outLabel:
	 #
	 # Step 5 insert code into code object in appropriate order.

  def postprocessIfStatementNode(self, node: IfStatementNode, cond: CodeObject, tlist: CodeObject, elist: CodeObject) -> CodeObject:
    co = CodeObject()
    #FILL IN CODE FROM STEP 3
    #MODIFY THIS TO GENERATE 3AC INSTEAD
    elseBlock = node.getElseBlock()
    
    if len(elseBlock.getStatements()) == 0:
      co.code.extend(cond.code)
      print(code.branch)
      branchInstr = cond.code[cond.branch]
      #co.code.extend(cond.code)
      outLabel = self.generateOutLabel()
      branchInstr.label = outLabel
      cond.code[cond.branch] = branchInstr
      thenBlock = node.getThenBlock()
      for subcode in thenBlock.getStatements():
        co.code.extend(self.run(subcode).code)
      il3 = InstructionList()
      il3.append(Label(outLabel))
      co.code.extend(il3)
      return co
    

    branchInstr = cond.code[cond.branch]
    co.code.extend(cond.code)
    elseLabel = self.generateElseLabel()
    branchInstr.label = elseLabel
    cond.code[cond.branch] = branchInstr

    thenBlock = node.getThenBlock()
    co.code.extend(tlist.code)
    #for subcode in thenBlock.getStatements():
      #co.code.extend(self.run(subcode).code)
    
    #tlist = self.postprocessStatementListNode(thenBlock, thenBlock.getStatements())
    #co.code.extend(tlist)
    outLabel = self.generateOutLabel()
    il = InstructionList()
    il.append(J(outLabel))
    co.code.extend(il)
    il2 = InstructionList()
    il2.append(Label(elseLabel))
    co.code.extend(il2)
    #for subcode in elseBlock.getStatements():
      #co.code.extend(self.run(subcode).code)
    co.code.extend(elist.code)
    #elist = self.postprocessStatementListNode(elseBlock, elseBlock.getStatements())
    #co.code.extend(elist)
    il3 = InstructionList()
    il3.append(Label(outLabel))
    co.code.extend(il3)
    return co

   # Code generation for While statement
	 # Step 0: Create code object
	 # 
	 # Step 1: generate labels
	 # 
	 # Step 2: add code from conditional expression
	 # 
	 # Step 3: create branch statement (if not created as part of step 2)
	 # 			don't forget to generate correct branch based on type
	 # 
	 # Step 4: generate code
	 # 		loopLabel:
	 #		<cond code>
	 #		<flipped branch> outLabel
	 #		<body code>
	 #		j loopLabel
	 #		outLabel:
	 #
	 # Step 5 insert code into code object in appropriate order.

  def postprocessWhileNode(self, node: WhileNode, cond: CodeObject, wlist:
  CodeObject) -> CodeObject:
    co = CodeObject()
    #FILL IN CODE FROM STEP 3
    #MODIFY THIS TO GENERATE 3AC INSTEAD
    loopLabel = self.generateLoopLabel()
    il = InstructionList()
    il.append(Label(loopLabel))
    co.code.extend(il)
    branchInstr = cond.code[cond.branch]
    co.code.extend(cond.code)
    outLabel = self.generateOutLabel()
    branchInstr.label = outLabel
    cond.code[cond.branch] = branchInstr
    whileBlock = node.getSList()
    co.code.extend(wlist.code)
    #for subcode in whileBlock.getStatements():
      #co.code.extend(self.run(subcode).code)
    il2 = InstructionList()
    il2.append(J(loopLabel))
    co.code.extend(il2)
    il3 = InstructionList()
    il3.append(Label(outLabel))
    co.code.extend(il3)
    return co

	# FILL IN FOR STEP 4
	# 
	# Generating code for returns
	# 
	# Step 0: Generate new code object
	# 
	# Step 1: Add retExpr code to code object (rvalify if necessary)
	# 
	# Step 2: Store result of retExpr in appropriate place on stack (fp + 8)
	# 
	# Step 3: Jump to out label (use @link{generateFunctionOutLabel()})
  
  def postprocessReturnNode(self, node: ReturnNode, retExpr: CodeObject) -> CodeObject:
    co = CodeObject()

    # FILL IN
    # MODIFY THIS TO GENERATE 3AC INSTEAD
    #step 1
    co.code.extend(retExpr.code)

    #step 2
    retType = node.getFuncSymbol().getReturnType()
    if (retType is Scope.Type.FLOAT):
      co.code.append(Fsw("fp", retExpr.temp, "8"))
      #co.code.append(FMv("sp", "fp"))
      #co.code.append(Flw("fp", "0", "fp"))
    else:
      co.code.append(Sw("fp", retExpr.temp, "8"))
      #co.code.append(Mv("sp", "fp"))
      #co.code.append(Lw("fp", "0", "fp"))
    #step 3
    co.code.append(J(self.generateFunctionOutLabel()))

    return co
  
  def preprocessFunctionNode(self, node: FunctionNode):
		#Generate function label information, used for other labels inside function

    self.currFunc = node.getFuncName()

		# reset register counts; each function uses new registers!
    self.intRegCount = 0
    self.floatRegCount = 0

	# FILL IN FOR STEP 4
	# 
	# Generate code for functions
	# 
	# Step 1: add the label for the beginning of the function
	# 
	# Step 2: manage frame  pointer
	# 			a. Save old frame pointer
	# 			b. Move frame pointer to point to base of activation record (current sp)
	# 			c. Update stack pointer
	# 
	# Step 3: allocate new stack frame (use scope infromation from FunctionNode)
	# 
	# Step 4: save registers on stack (Can inspect intRegCount and floatRegCount to know what to save)
	# 
	# Step 5: add the code from the function body
	# 
	# Step 6: add post-processing code:
	# 			a. Label for `return` statements inside function body to jump to
	# 			b. Restore registers
	# 			c. Deallocate stack frame (set stack pointer to frame pointer)
	# 			d. Reset fp to old location
	# 			e. Return from function

  def postprocessFunctionNode(self, node: FunctionNode, body: CodeObject) -> CodeObject:
    co = CodeObject()

		# FILL IN FROM STEP 4
		# step 1
    funcName = node.getFuncName()
    il = InstructionList()
    co.code.append(Blank(""))
    co.code.append(Blank("Function: " + funcName))
    co.code.append(Label("func_" + funcName))
    co.code.extend(il)

    #step 2
    co.code.append(Sw("sp", "fp", "0"))
    co.code.append(Mv("sp", "fp"))
    co.code.append(Addi("sp", "-4", "sp"))

    #step 3
    offset = node.getScope().genSymbol(type(4), funcName).getAddress()
    co.code.append(Addi("sp", str(offset + 4), "sp"))


    #step 4
    co.code.append(Blank("Saving registers"))
    for i in range(4, self.intRegCount + 5):
      co.code.append(Sw("x"+str(i), "sp", "0"))
      co.code.append(Addi("sp", "-4", "sp"))
    for i in range(0, self.floatRegCount):
      co.code.append(Fsw("f"+str(i), "sp", "0"))
      co.code.append(Addi("sp", "-4", "sp"))
    co.code.append(Blank(""))
    co.code.append(Blank(""))

    #step 5
    
    ra = RegisterAllocator(self.numIntRegisters, self.numFloatRegisters, body.getCode(), node.getScope())
    bodyInstructions = ra.allocate()
    co.code.extend(bodyInstructions)
    #co.code.extend(body.code)

    #step 6
    co.code.append(Label(self.generateFunctionOutLabel()))
    co.code.append(Blank("Restore registers"))
    while self.floatRegCount != 0:
      self.floatRegCount -= 1
      co.code.append(Addi("sp", "4", "sp"))
      co.code.append(Flw("f"+str(self.floatRegCount), "sp", "0"))
    while self.intRegCount >= 0:
      self.intRegCount -= 1
      co.code.append(Addi("sp", "4", "sp"))
      co.code.append(Lw("x"+str(self.intRegCount + 5), "sp", "0"))
    co.code.append(Mv("fp", "sp"))
    co.code.append(Lw("fp", "fp", "0"))
    co.code.append(Ret())
    co.code.append(Blank("End of function " + funcName))


		# ADD REGISTER ALLOCATION HERE
		
		# You may find it useful to do this in the following way:
		
		# 1. Write a register allocator class that is initialized with the number of int/fp registers to use, the code from
		# 		`body`, and the function scope from `node` (the function scope gives you access to local/global variables)
		# 2. Within the register allocator class, do the following
		# 		a. Split the code in body into basic blocks
		# 		b. (573 version) Perform liveness analysis on each basic block (assume globals and locals are live)
		# 		b. (468/595 version) Assume all locals/globals/temporaries are live all the time
		# 		c. Perform register allocation on each basic block using the algorithms presented in class,
		# 			converting 3AC into assembly code with macro expansion
		# 			i. Add code to track the state of the registers for each basic block (what is assigned to the register, whether it's dirty)
		# 			ii. As you perform register allocation within a basic block, spill registers to memory as necessary. Use any
		# 				heuristic you want to determine which registers to allocate and which to spill
		# 			iii. If you need to spill a temporary to memory, you'll find it easiest to add the temporary as a new "local" variable
		# 				to the local scope (you can just use the temporary name as the variable name); that will automatically allocate a spot
		# 				in the activation record for it.
		# 			iv. At the end of each basic block, save all dirty/live registers that hold globals/locals back to the stack
		# 3. Once register allocation is done, track:
		# 		a. How big the local scope is after spilling temporaries -- this affects allocating the stack frame
		# 		b. How many total registers you used -- this affects the register save/restore code
		# 4. Now generate code for your function as before, but using the updated information for register save/restore and frame allocation


    return co

	# Generate code for the list of functions. This is the "top level" code generation function
	# 
	# Step 1: Set fp to point to sp
	# 
	# Step 2: Insert a JR to main
	# 
	# Step 3: Insert a HALT
	# 
	# Step 4: Include all the code of the functions

  def postprocessFunctionListNode(self, node: FunctionListNode, functions: List[CodeObject]) -> CodeObject:
    co = CodeObject()

    co.code.append(Mv("sp", "fp"))
    co.code.append(Jr(self.generateFunctionLabel("main")))
    co.code.append(Halt())
    co.code.append(Blank())

    # Add code for each of the functions
    for c in functions:
      co.code.extend(c.code)
      co.code.append(Blank())
    
    return co

	# FILL IN FOR STEP 4
	# 
	# Generate code for a call expression
	# 
	# Step 1: For each argument:
	# 
	# 	Step 1a: insert code of argument (don't forget to rvalify!)
	# 
	# 	Step 1b: push result of argument onto stack 
	# 
	# Step 2: alloate space for return value
	# 
	# Step 3: push current return address onto stack
	# 
	# Step 4: jump to function
	# 
	# Step 5: pop return address back from stack
	# 
	# Step 6: pop return value into fresh temporary (destination of call expression)
	# 
	# Step 7: remove arguments from stack (move sp)

  def postprocessCallNode(self, node: CallNode, args: List[CodeObject]) -> CodeObject:
    co = CodeObject()

    # FILL IN FROM STEP 4
    # MODIFY THIS CODE TO GENERATE 3AC
    #step 1
    retType = node.type
    for i in args:
      co.code.extend(i.code)
      if (i.getType() is Scope.Type.FLOAT):
        co.code.append(Fsw("sp", i.temp, "0"))
        co.code.append(Addi("sp", "-4", "sp"))
      else:
        co.code.append(Sw("sp", i.temp, "0"))
        co.code.append(Addi("sp", "-4", "sp"))
    
    #step 2
    
    if (retType is Scope.Type.FLOAT):
      co.temp = self.generateTemp(Scope.Type.FLOAT)
      co.code.append(Addi("sp", "-4", "sp"))
    else:
      co.temp = self.generateTemp(Scope.Type.INT)
      co.code.append(Addi("sp", "-4", "sp"))

    #step 3
    co.code.append(Sw("sp", "ra", "0"))
    co.code.append(Addi("sp", "-4", "sp"))

    #step 4
    funcName = node.getFuncName()
    co.code.append(Jr("func_" + funcName))
    
    #step 5
    co.code.append(Addi("sp", "4", "sp"))
    co.code.append(Lw("ra", "sp", "0"))

    #step 6
    if (retType is Scope.Type.FLOAT):
      co.code.append(Addi("sp", "4", "sp"))
      co.code.append(Flw(co.temp, "sp", "0"))
    else:
      co.code.append(Addi("sp", "4", "sp"))
      co.code.append(Lw(co.temp, "sp", "0"))

    #step 7
    stackSpace = len(args)
    if (retType is Scope.Type.FLOAT):
      co.code.append(Addi("sp", "" + str(stackSpace * 4), "sp"))
      #co.code.append(Fsw(co.temp, "sp", "0"))
    else:
      co.code.append(Addi("sp", "" + str(stackSpace * 4), "sp"))
      #co.code.append(Sw(co.temp, "sp", "0"))
	  
    return co

	# Generate a fresh temporary
	# 
	# @return new temporary register name
  
  def generateTemp(self, t: Scope.Type) -> str:
    if t == Scope.Type.INT:
      s = self.intTempPrefix + str(self.intRegCount)
      self.intRegCount += 1
      return s
    elif t == Scope.Type.FLOAT:
      s = self.floatTempPrefix + str(self.floatRegCount)
      self.floatRegCount += 1
      return s
    else:
      raise Exception("Generating temp for bad type")

  def generateLoopLabel(self) -> str:
    self.loopLabel += 1
    return "loop_" + str(self.loopLabel)

  def generateElseLabel(self) -> str:
    self.elseLabel += 1
    return "else_" + str(self.elseLabel)

  def generateOutLabel(self) -> str:
    self.outLabel += 1
    return "out_" + str(self.outLabel)
  
  def generateFunctionLabel(self, func = None) -> str:
    if func is None:
      return "func_" + self.currFunc
    else:
      return "func_" + func
    
  def generateFunctionOutLabel(self) -> str:
    return "func_ret_" + self.currFunc
  

	 # Take a code object that results in an lval, and create a new code
	 # object that adds a load to generate the rval.
	 # 
	 # Step 0: Create new code object
	 # 
	 # Step 1: Add all the lco code to the new code object
	 # 		   (If lco is just a variable, create a new code object that
	 #          stores the address of variable in a code object; see
	 #          generateAddrFromVariable)
	 # 
	 # Step 2: Generate a load to load from lco's temp into a new temporary
	 # 		   Hint: it'll be easiest to generate a load with no offset:
	 # 				lw newtemp 0(oldtemp)
	 #         Don't forget to generate the right kind of load based on the type
	 #         stored in the address
	 # 
	 # Don't forget to update the temp and lval fields of the code object!
	 # 		   Hint: where is the result stored? Is this data or an address?
	 # 
	 # @param lco The code object resulting in an address
	 # @return A code object with all the code of <code>lco</code> followed by a load
	 #         to generate an rval

  def rvalify(self, lco : CodeObject) -> CodeObject:
    # Step 0
    co = CodeObject()
    assert(lco.lval is True)
    # THIS WON'T BE NECESSARY IF YOU'RE GENERATING 3AC */

		# DON'T FORGET TO ADD CODE TO GENERATE LOADS FOR LOCAL VARIABLES
    return co

	# Generate an instruction sequence that holds the address of the variable in a code object
	# 
	# If it's a global variable, just get the address from the symbol table
	# 
	# If it's a local variable, compute the address relative to the frame pointer (fp)
	# 
	# @param lco The code object holding a variable
	# @return a list of instructions that puts the address of the variable in a register

  def generateAddrFromVariable(self, lco: CodeObject) -> InstructionList:
    il = InstructionList()

    #Step 1:
    symbol = lco.getSTE()
    address = symbol.addressToString()

    #Step 2:
    if symbol.isLocal():
      # If local, address is offset
			# need to load fp + offset
			# addi tmp' fp offset
      compAddr = Addi("fp", address, self.generateTemp(Scope.Type.INT))
    else:
			#If global, address in symbol table is the right location
      #la tmp' addr // Register type needs to be an int
      compAddr = La(self.generateTemp(Scope.Type.INT), address)
    il.append(compAddr) # add instruction

    return il
