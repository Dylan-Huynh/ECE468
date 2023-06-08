from .ASTNode import ASTNode
from enum import Enum
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from .visitor import ASTVisitor

class CondNode(ASTNode):
  class OpType(Enum):
    EQ = 1
    NE = 2
    LT = 3
    LE = 4
    GT = 5
    GE = 6

  def getOpFromString(self, op: str):
    if op == '==':
      return OpType.EQ
    elif op == '!=':
      return OpType.NE
    elif op == '<':
      return OpType.LT
    elif op == '<=':
      return OpType.LE
    elif op == '>':
      return OpType.GT
    elif op == '>=':
      return OpType.GE
    else:
      raise Exception("invalid op in CondNode")

  def __init__(self, left: ASTNode, right: ASTNode, op: str):
    self.setLeft(left)
    self.setRight(right)
    self.setOp(op)

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitCondOpNode(self)

  def getLeft(self) -> ASTNode:
    return self.left

  def setLeft(self, left: ASTNode):
    self.left = left

  def getRight(self) -> ASTNode:
    return self.right

  def setLeft(self, right: ASTNode):
    self.left = right  

