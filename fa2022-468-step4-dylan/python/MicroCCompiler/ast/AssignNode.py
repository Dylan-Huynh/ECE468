from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from .visitor.ASTVisitor import ASTVisitor

class AssignNode(ASTNode):
  def __init__(self, left: ASTNode, right: ASTNode):
    self.setLeft(left)
    self.setRight(right)
    self.setType(left.getType())

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitAssignNode(self)

  def getLeft(self) -> ASTNode:
    return self.left

  def setLeft(self, left: ASTNode):
    self.left = left

  def getRight(self) -> ASTNode:
    return self.right

  def setRight(self, right: ASTNode):
    self.right = right
