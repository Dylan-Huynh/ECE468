from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any

from ..compiler.Scope import Scope

if TYPE_CHECKING:
  from .visitor import ASTVisitor

class PtrDerefNode(ASTNode):
  def __init__(self, expr: ASTNode):
    self.setExpr(expr)
    assert(expr.getType().type == Scope.InnerType.PTR)
    self.setType(expr.getType().getWrappedType())

  def accept(self, visitor: 'ASTVisitor'):
    return visitor.visitPtrDerefNode(self)

  def getExpr(self):
    return self.expr

  def setExpr(self, right):
    self.expr = right
