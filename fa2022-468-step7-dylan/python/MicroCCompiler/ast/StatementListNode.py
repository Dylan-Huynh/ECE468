from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from .visitor.ASTVisitor import ASTVisitor

class StatementListNode(ASTNode):
  def __init__(self, node: ASTNode = None, li: list = None): #list of CodeObject
    self.statements = list()
    if node is not None:
      self.statements.append(node)
    if li is not None:
      self.statements.extend(li)

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitStatementListNode(self)

  def getStatements(self) -> list:
    return self.statements
