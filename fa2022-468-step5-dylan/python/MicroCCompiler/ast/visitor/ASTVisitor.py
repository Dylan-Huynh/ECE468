from abc import ABC, abstractmethod

from typing import TYPE_CHECKING, Any
if TYPE_CHECKING:
    from .. import *

class ASTVisitor(ABC):

    @abstractmethod
    def run(self, node: 'ASTNode') -> Any:
        pass

    @abstractmethod
    def visitVarNode(self, node: 'VarNode') -> Any:
        pass
    @abstractmethod
    def visitIntLitNode(self, node: 'IntLitNode') -> Any:
        pass
    @abstractmethod
    def visitFloatLitNode(self, node: 'FloatLitNode') -> Any:
        pass
    @abstractmethod
    def visitBinaryOpNode(self, node: 'BinaryOpNode') -> Any:
        pass
    @abstractmethod
    def visitUnaryOpNode(self, node: 'UnaryOpNode') -> Any:
        pass
    @abstractmethod
    def visitAssignNode(self, node: 'AssignNode') -> Any:
        pass
    @abstractmethod
    def visitStatementListNode(self, node: 'StatementListNode') -> Any:
        pass
    @abstractmethod
    def visitReadNode(self, node: 'ReadNode') -> Any:
        pass
    @abstractmethod
    def visitWriteNode(self, node: 'WriteNode') -> Any:
        pass
    @abstractmethod
    def visitIfStatementNode(self, node: 'IfStatementNode') -> Any:
        pass
    @abstractmethod
    def visitWhileNode(self, node: 'WhileNode') -> Any:
        pass
    @abstractmethod
    def visitReturnNode(self, node: 'ReturnNode') -> Any:
        pass
    @abstractmethod
    def visitCondNode(self, node: 'CondNode') -> Any:
        pass
    @abstractmethod
    def visitFunctionNode(self, node: 'FunctionNode') -> Any:
        pass
    @abstractmethod
    def visitFunctionListNode(self, node: 'FunctionListNode') -> Any:
        pass
    @abstractmethod
    def visitCallNode(self, node: 'CallNode') -> Any:
        pass
