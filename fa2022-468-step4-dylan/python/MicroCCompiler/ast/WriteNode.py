from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from .visitor.ASTVisitor import ASTVisitor

class WriteNode(ASTNode):
  def __init__(self, writeExpr: ASTNode):
    self.setWriteExpr(writeExpr)

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitWriteNode(self)

  def getWriteExpr(self) -> ASTNode:
    return self.writeExpr

  def setWriteExpr(self, expr: ASTNode):
    self.writeExpr = expr
