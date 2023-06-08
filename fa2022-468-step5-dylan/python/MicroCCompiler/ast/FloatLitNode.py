from .ASTNode import ASTNode
from ..compiler.Scope import Scope
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from .visitor import ASTVisitor

class FloatLitNode(ASTNode):
  def __init__(self, val: str):
    self.setVal(val)
    self.setType(Scope.Type.FLOAT)

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitFloatLitNode(self)
