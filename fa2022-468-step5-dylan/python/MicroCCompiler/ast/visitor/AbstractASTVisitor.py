from .ASTVisitor import ASTVisitor

from typing import TYPE_CHECKING, Any, List
if TYPE_CHECKING:
    from .. import *

class AbstractASTVisitor(ASTVisitor):

    def run(self, node: 'ASTNode') -> Any:
        return node.accept(self)

    def visitVarNode(self, node: 'VarNode') -> Any:
        self.preprocessVarNode(node)
        return self.postprocessVarNode(node)

    def visitIntLitNode(self, node: 'IntLitNode') -> Any:
        self.preprocessIntLitNode(node)
        return self.postprocessIntLitNode(node)

    def visitFloatLitNode(self, node: 'FloatLitNode') -> Any:
        self.preprocessFloatLitNode(node)
        return self.postprocessFloatLitNode(node)

    def visitBinaryOpNode(self, node: 'BinaryOpNode') -> Any:
        self.preprocessBinaryOpNode(node)
        left = node.getLeft().accept(self)
        right = node.getRight().accept(self)
        return self.postprocessBinaryOpNode(node, left, right)

    def visitUnaryOpNode(self, node: 'UnaryOpNode') -> Any:
        self.preprocessUnaryOpNode(node)
        child = node.getExpr().accept(self)
        return self.postprocessUnaryOpNode(node, child)

    def visitAssignNode(self, node: 'AssignNode') -> Any:
        self.preprocessAssignNode(node)
        left = node.getLeft().accept(self)
        right = node.getRight().accept(self)
        return self.postprocessAssignNode(node, left, right)

    def visitStatementListNode(self, node: 'StatementListNode') -> Any:
        self.preprocessStatementListNode(node)
        rs = [n.accept(self) for n in node.getStatements()]
        return self.postprocessStatementListNode(node, rs)

    def visitReadNode(self, node: 'ReadNode') -> Any:
        self.preprocessReadNode(node)
        var = node.getVarNode().accept(self)
        return self.postprocessReadNode(node, var)

    def visitWriteNode(self, node: 'WriteNode') -> Any:
        self.preprocessWriteNode(node)
        writeExpr = node.getWriteExpr().accept(self)
        return self.postprocessWriteNode(node, writeExpr)

    def visitIfStatementNode(self, node: 'IfStatementNode') -> Any:
        self.preprocessIfStatementNode(node)
        cond = node.getCondExpr().accept(self)
        tlist = node.getThenBlock().accept(self)
        elist = None
        if not node.getElseBlock() is None:
            elist = node.getElseBlock().accept(self)
        return self.postprocessIfStatementNode(node, cond, tlist, elist)

    def visitWhileNode(self, node: 'WhileNode') -> Any:
        self.preprocessWhileNode(node)
        cond = node.getCondExpr().accept(self)
        slist = node.getSList().accept(self)
        return self.postprocessWhileNode(node, cond, slist)

    def visitReturnNode(self, node: 'ReturnNode') -> Any:
        self.preprocessReturnNode(node)
        retExpr = node.getRetExpr().accept(self)
        return self.postprocessReturnNode(node, retExpr)

    def visitCondNode(self, node: 'CondNode') -> Any:
        self.preprocessCondNode(node)
        left = node.getLeft().accept(self)
        right = node.getRight().accept(self)
        return self.postprocessCondNode(node, left, right)

    def visitFunctionNode(self, node: 'FunctionNode') -> Any:
        self.preprocessFunctionNode(node)
        body = node.getFuncBody().accept(self)
        return self.postprocessFunctionNode(node, body)

    def visitFunctionListNode(self, node: 'FunctionListNode') -> Any:
        self.preprocessFunctionListNode(node)
        li = []
        for n in node.getFunctions():
          li.append(n.accept(self))
        return self.postprocessFunctionListNode(node, li)

    def visitCallNode(self, node: 'CallNode') -> Any:
        self.preprocessCallNode(node)
        li = []
        for arg in node.getArgs():
          li.append(arg.accept(self))
        return self.postprocessCallNode(node, li)

    def preprocessVarNode(self, node: 'VarNode'):
        return
    
    def postprocessVarNode(self, node: 'VarNode') -> Any:
        return None

    def preprocessIntLitNode(self, node: 'IntLitNode'):
        return
    
    def postprocessIntLitNode(self, node: 'IntLitNode') -> Any:
        return None

    def preprocessFloatLitNode(self, node: 'FloatLitNode'):
        return
    
    def postprocessFloatLitNode(self, node: 'FloatLitNode') -> Any:
        return None

    def preprocessBinaryOpNode(self, node: 'BinaryOpNode'):
        return
    
    def postprocessBinaryOpNode(self, node: 'BinaryOpNode', left: Any, right: Any) -> Any:
        return None

    def preprocessUnaryOpNode(self, node: 'UnaryOpNode'):
        return
    
    def postprocessUnaryOpNode(self, node: 'UnaryOpNode', expr: Any) -> Any:
        return None

    def preprocessAssignNode(self, node: 'AssignNode'):
        return
    
    def postprocessAssignNode(self, node: 'AssignNode', left: Any, right: Any) -> Any:
        return None

    def preprocessStatementListNode(self, node: 'StatementListNode'):
        return
    
    def postprocessStatementListNode(self, node: 'StatementListNode', statements: List[Any]) -> Any:
        return None

    def preprocessReadNode(self, node: 'ReadNode'):
        return
    
    def postprocessReadNode(self, node: 'ReadNode', var: Any) -> Any:
        return None

    def preprocessWriteNode(self, node: 'WriteNode'):
        return
    
    def postprocessWriteNode(self, node: 'WriteNode', writeExpr: Any) -> Any:
        return None

    def preprocessIfStatementNode(self, node: 'IfStatementNode'):
        return
    
    def postprocessIfStatementNode(self, node: 'IfStatementNode', cond: Any, tlist: Any, elist: Any) -> Any:
        return None

    def preprocessWhileNode(self, node: 'WhileNode'):
        return
    
    def postprocessWhileNode(self, node: 'WhileNode', cond: Any, slist: Any) -> Any:
        return None

    def preprocessReturnNode(self, node: 'ReturnNode'):
        return
    
    def postprocessReturnNode(self, node: 'ReturnNode', retExpr: Any) -> Any:
        return None

    def preprocessCondNode(self, node: 'CondNode'):
        return
    
    def postprocessCondNode(self, node: 'CondNode', left: Any, right: Any) -> Any:
        return None

    def preprocessFunctionNode(self, node: 'FunctionNode'):
        return

    def postprocessFunctionNode(self, node: 'FunctionNode', body: Any) -> Any:
        return None

    def preprocessFunctionListNode(self, node: 'FunctionListNode'):
        return

    def postprocessFunctionListNode(self, node: 'FunctionListNode', functions: Any) -> Any:
        return None

    def preprocessCallNode(self, node: 'CallNode'):
        return

    def postprocessCallNode(self, node: 'CallNode', args: Any) -> Any:
        return None

