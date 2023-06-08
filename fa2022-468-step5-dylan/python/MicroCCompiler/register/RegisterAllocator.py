import sys
import os
import copy

from ..compiler import *
from ..assembly import *
from ..assembly.instructions import *
from .Register import Register
from .RegisterFile import RegisterFile


class RegisterAllocator:
    def __init__(self, intRegCount: int, floatRegCount: float, body: InstructionList, scope:LocalScope):
        self.intRegCount = intRegCount
        self.floatRegCount = floatRegCount
        self.body = body
        self.scope = scope
        self.intFile = RegisterFile(Scope.Type.INT, intRegCount, scope)
        self.floatFile = RegisterFile(Scope.Type.FLOAT, floatRegCount, scope)
        self.BasicBlocks = [InstructionList()]

    def splitBlocks(self):
        block = 0
        for i in range(0, len(self.body.data) - 1):
            if not self.body.data[i].getOC and self.body.data[i].label is None or len(self.BasicBlocks[block].data) == 0:
                #first half is any new label start, second half triggers after block ends
                self.BasicBlocks[block].append(self.body.data[i])
            elif self.body.data[i].getOC().name in "BEQBGEBGTBLEBLTBNEJ": # If opCode is a branch then it will be seen as in this string combination of them all
                self.BasicBlocks[block].append(self.body.data[i])
                #print(self.BasicBlocks[block])
                block += 1
                self.BasicBlocks.append(InstructionList())
            #if i == (len(self.body.data) - 2):
                #self.BasicBlocks[block].append(self.body.data[i])
            else:
                self.BasicBlocks[block].append(self.body.data[i])
            
    
    def allocate(self) -> InstructionList:
        
        il = InstructionList()
        self.splitBlocks()
        for bb in self.BasicBlocks:
            #print(bb)
            insts = self.allocateBasicBlocks(bb)
            lastIntr = insts.code.getLast()
            if type(lastIntr) is Blank:
                continue
            if lastIntr.getOC().name in "BEQBGEBGTBLEBLTBNEJ": #Checks for Branching Instruction, although J does not inherit from InstructionBranch it does change how end of BB is written
                lastIntr = insts.data.pop()
                insts.code.append(Blank("Saving registers at end of BB"))
                for r in self.intFile.array:
                    if r.dirty is True:
                        insts.code.append(Sw("x" + str(r.num), "fp", r.getAddress()))
                for r in self.floatFile.array:
                    if r.dirty is True:
                        insts.code.append("fp", Fsw("x" + str(r.num), r.getAddress()))
                insts.extend(lastIntr)
            else:
                insts.code.append(Blank("Saving registers at end of BB"))
                for r in self.intFile.array:
                    if r.name is not None:
                        if r.dirty is True and r.name[1] == "l" or r.name[1] == "g":
                            insts.code.append(Sw(str(r), "fp", r.name[2:]))
                for r in self.floatFile.array:
                    if r.dirty is True:
                        fake = 1
                        #insts.code.append(Fsw("fp", "x" + str(r.num), r.getAddress()))
            insts.code.append(Blank("End of BB"))
            il.extend(insts.code)
        return il
    
    def allocateBasicBlocks(self, bb:InstructionList) -> CodeObject:
        co = CodeObject()
        co.code.append(Blank("Start of BB"))
        for i in bb.data:
            if i.isBranch():
                co.code.extend(self.macroExpandBranch(i))
            elif i.isPut():
                co.code.extend(self.macroExpandPut(i))
            elif i.is30():
                co.code.extend(self.macroExpand30(i))
            elif i.isLS():
                co.code.extend(self.macroExpandLS(i))
            elif i.getOC().name in "FMVFNEG":
                co.code.extend(self.macroExpandMVNEG(i))
            elif i.getOC().name in "GETIGETF":
                co.code.extend(self.macroExpandGet(i))
            elif i.getOC().name in "LALIFIMMS":
                co.code.extend(self.macroExpandLoad(i))
            elif i.getOC().name in "PUSHINTPOPINTPUSHFLOATPOPFLOAT":
                co.code.extend(self.macroExpandPushPop(i))

        return co

    def macroExpand30(self, i:Instruction) -> InstructionList:
        il = InstructionList()
        if i.oc.name[0] == "F":
            opType = Scope.Type.FLOAT
            src1 = self.floatFile.ensureSource(i.src1, opType, il, self.scope)
            #print(src1)
            src2 = self.floatFile.ensureSource(i.src2, opType, il, self.scope)
            #print(src2)
            dest = self.floatFile.ensureDest(i.dest, opType, il, self.scope)
            #print(dest)
            if i.oc.name == "FAdd":
                il.append(FAdd(str(src1), str(src2), str(dest)))
            if i.oc.name == "FSub":
                il.append(FSub(str(src1), str(src2), str(dest)))
            if i.oc.name == "FMul":
                il.append(FMul(str(src1), str(src2), str(dest)))
            if i.oc.name == "FDiv":
                il.append(FDiv(str(src1), str(src2), str(dest)))
            if i.oc.name == "Flt":
                il.append(Flt(str(src1), str(src2), str(dest)))
            if i.oc.name == "Fle":
                il.append(Fle(str(src1), str(src2), str(dest)))
            if i.oc.name == "Feq":
                il.append(Feq(str(src1), str(src2), str(dest)))
        else:
            opType = Scope.Type.INT
            src1 = self.intFile.ensureSource(i.src1, opType, il, self.scope)
            src2 = self.intFile.ensureSource(i.src2, opType, il, self.scope)
            dest = self.intFile.ensureDest(i.dest, opType, il, self.scope)
            if i.oc.name == "ADD":
                il.append(Add(str(src1), str(src2), str(dest)))
            if i.oc.name == "Sub":
                il.append(Sub(str(src1), str(src2), str(dest)))
            if i.oc.name == "Mul":
                il.append(Mul(str(src1), str(src2), str(dest)))
            if i.oc.name == "Div":
                il.append(Div(str(src1), str(src2), str(dest)))
            if i.oc.name == "Addi":
                il.append(Addi(str(src1), str(src2), str(dest)))
        dest.dirty = True
        return il
    
    def macroExpandBranch(self, i:Instruction) -> InstructionList:
        il = InstructionList()
        opType = Scope.Type.INT
        src1 = self.intFile.ensureSource(i.src1, opType, il, self.scope)
        src2 = self.intFile.ensureSource(i.src2, opType, il, self.scope)
        label = i.label
        il.append(InstructionBranch(str(src1), str(src2), str(label)))
        return il

    def macroExpandPut(self, i:Instruction) -> InstructionList:

        il = InstructionList()
        if i.oc.name == "PUTS":
            name = i.src1[2:]
            ste = self.scope.getSymbolTableEntry(name)
            address = ste.addressToString()
            il.append(La("x3", address))
            il.append(PutS("x3"))
        elif i.oc.name[0] == "F":
            opType = Scope.Type.FLOAT
            src1 = self.floatFile.ensureSource(i.src1, opType, il, self.scope)
            il.append(PutF(str(src1)))
            if src1.name is None:
                src1.free = True
        else:
            opType = Scope.Type.INT
            src1 = self.intFile.ensureSource(i.src1, opType, il, self.scope)
            il.append(PutI(str(src1)))
            if src1.name is None:
                src1.free = True
        
        return il

    def macroExpandLS(self, i:Instruction) -> InstructionList:
        il = InstructionList()
        if i.oc.name[0] == "F":
            opType = Scope.Type.FLOAT
            dest = self.floatFile.ensureDest(i.dest, opType, il, self.scope)
            src1 = self.floatFile.ensureSource(i.src1, opType, il, self.scope)
            label = i.label
            if i.oc.name == "FSW":
                il.append(Fsw(str(src1), str(dest), str(label)))
            if i.oc.name == "FLW":
                il.append(Flw(str(src1), str(dest), str(label)))
        else:
            opType = Scope.Type.INT
            src1 = self.intFile.ensureDest(i.src1, opType, il, self.scope)
            dest = self.intFile.ensureSource(i.dest, opType, il, self.scope)

            label = i.label
            if i.oc.name == "SW":
                il.append(Mv(str(src1), str(dest)))
                #dest.dirty = True
                dest.address = i.label
                #dest.name = "$l" + dest.address
                dest.assign("$l" + dest.address)
                dest._isLocal = True
                dest.dirty = True
                #dest.isLocal = True
                #il.append(Sw(str(src1), str(dest), str(label)))
            if i.oc.name == "LW":
                il.append(Lw(str(src1), str(dest), str(label)))

        
        return il

    def macroExpandLoad(self, i:Instruction) -> InstructionList:
        il = InstructionList()
        opType = Scope.Type.INT
        dest = self.intFile.ensureDest(i.dest, opType, il, self.scope)
        label = i.label
        if i.oc.name == "LA":
            il.append(La(str(dest), str(label)))
            return il
        elif i.oc.name == "FIMMS":
            il.append(FImm(str(dest), str(label)))
            return il
        elif i.oc.name == "LI":
            il.append(Li(str(dest), str(label)))
            dest.value = str(label)
            return il

        print("Something went wrong")
        return il

    def macroExpandGet(self, i:Instruction) -> InstructionList:
        il = InstructionList()
        if i.getOC().name[-1] == "F":
            opType = Scope.Type.FLOAT
            dest = self.floatFile.ensureDest(i.dest, opType, il, self.scope)
            il.append(GetF(str(dest)))
        else:
            opType = Scope.Type.INT
            dest = self.floatFile.ensureDest(i.dest, opType, il, self.scope)
            il.append(GetI(str(dest)))
        return il
    
    def macroExpandMVNEG(self, i:Instruction) -> InstructionList:
        il = InstructionList()
        if i.oc.name[0] == "F":
            opType = Scope.Type.FLOAT
            dest = self.floatFile.ensureDest(i.dest, opType, il, self.scope)
            src1 = self.floatFile.ensureSource(i.src1, opType, il, self.scope)
            label = i.label
            if i.oc.name == "FNeg":
                il.append(FNeg(str(src1), str(dest), str(label)))
            if i.oc.name == "FMv":
                il.append(FMv(str(src1), str(dest), str(label)))
        else:
            opType = Scope.Type.INT
            dest = self.floatFile.ensureDest(i.dest, opType, il, self.scope)
            src1 = self.floatFile.ensureSource(i.src1, opType, il, self.scope)
            label = i.label
            if i.oc.name == "Neg":
                il.append(Neg(str(src1), str(dest), str(label)))
            if i.oc.name == "Mv":
                il.append(Mv(str(src1), str(dest), str(label)))

        
        return il

        

