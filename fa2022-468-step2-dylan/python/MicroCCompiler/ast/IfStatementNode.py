from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any
from .StatementListNode import StatementListNode
from .CondNode import CondNode

if TYPE_CHECKING:
  from .visitor.ASTVisitor import ASTVisitor

class IfStatementNode(ASTNode):
  def __init__(self, cond: CondNode, tlist: StatementListNode, elist: StatementListNode):
    self.setCondExpr(cond)
    self.setThenBlock(tlist)
    self.setElseBlock(elist)

  def accept(self, visitor: 'ASTVisitor'):
    return visitor.visitIfStatementNode(self)

  def getCondExpr(self) -> CondNode:
    return self.condExpr

  def setCondExpr(self, condExpr: CondNode):
    self.condExpr = condExpr

  def getThenBlock(self) -> StatementListNode:
    return self.thenBlock
  
  def setThenBlock(self, thenBlock: StatementListNode):
    self.thenBlock = thenBlock

  def getElseBlock(self) -> StatementListNode:
    return self.elseBlock

  def setElseBlock(self, elseBlock):
    self.elseBlock = elseBlock


