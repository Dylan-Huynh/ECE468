from .ASTNode import ASTNode
from .StatementListNode import StatementListNode
from ..compiler import LocalScope

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from .visitor import ASTVisitor

class FunctionNode(ASTNode):
  def __init__(self, funcBody: StatementListNode, funcName: str, scope: LocalScope):
    self.funcBody = funcBody
    self.funcName = funcName
    self.scope = scope

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitFunctionNode(self)
  
  def getFuncBody(self) -> StatementListNode:
    return self.funcBody

  def setFuncBody(self, funcBody: StatementListNode):
    self.funcBody = funcBody

  def getFuncName(self) -> str:
    return self.funcName

  def getScope(self) -> LocalScope:
    return self.scope
