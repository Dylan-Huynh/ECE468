from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from .visitor.ASTVisitor import ASTVisitor

class ReturnNode(ASTNode):
  def __init__(self, retExpr: ASTNode):
    self.setRetExpr(retExpr)

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitReturnNode(self)

  def getRetExpr(self) -> ASTNode:
    return self.retExpr

  def setRetExpr(self, expr: ASTNode):
    self.retExpr = expr
