from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any

from ..compiler.Scope import Scope

if TYPE_CHECKING:
  from .visitor import ASTVisitor

class AddrOfNode(ASTNode):
  def __init__(self, expr: ASTNode):
    self.setExpr(expr)
    self.setType(Scope.Type.pointerToType(expr.getType()))

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitAddrOfNode(self)

  def getExpr(self) -> ASTNode:
    return self.expr

  def setExpr(self, expr: ASTNode):
    self.expr = expr
