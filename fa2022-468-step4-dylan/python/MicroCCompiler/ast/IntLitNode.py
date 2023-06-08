from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any

from ..compiler.Scope import Scope

if TYPE_CHECKING:
  from .visitor import ASTVisitor

class IntLitNode(ASTNode):
  def __init__(self, val: str):
    self.setVal(val)
    self.setType(Scope.Type.INT)

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitIntLitNode(self)
