from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any
from .VarNode import VarNode

if TYPE_CHECKING:
  from .visitor.ASTVisitor import ASTVisitor

class ReadNode(ASTNode):
  def __init__(self, node: VarNode):
    self.setVarNode(node)
    self.setType(node.getType())

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitReadNode(self)

  def getVarNode(self) -> VarNode:
    return self.varNode

  def setVarNode(self, node: VarNode):
    self.varNode = node
