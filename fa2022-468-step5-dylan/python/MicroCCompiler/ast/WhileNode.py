from .ASTNode import ASTNode
from .CondNode import CondNode
from .StatementListNode import StatementListNode
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from .visitor.ASTVisitor import ASTVisitor

class WhileNode(ASTNode):
  def __init__(self, cond: CondNode, slist: StatementListNode):
    self.setCondExpr(cond)
    self.setSList(slist)

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitWhileNode(self)

  def getCondExpr(self) -> CondNode:
    return self.cond

  def setCondExpr(self, cond: CondNode):
    self.cond = cond

  def getSList(self) -> StatementListNode:
    return self.slist

  def setSList(self, li: StatementListNode):
    self.slist = li
