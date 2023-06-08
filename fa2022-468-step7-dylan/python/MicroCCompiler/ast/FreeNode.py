from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any

from ..compiler.Scope import Scope

if TYPE_CHECKING:
  from .visitor import ASTVisitor

class FreeNode(ASTNode):
  def __init__(self, arg: ASTNode):
    self.ste = None # Special function without STE
    self.arg = arg
    self.type = Scope.Type(Scope.InnerType.VOID)

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitFreeNode(self)

  def getArg(self) -> ASTNode:
    return self.arg

  def getFuncName(self) -> str:
    return self.funcName
