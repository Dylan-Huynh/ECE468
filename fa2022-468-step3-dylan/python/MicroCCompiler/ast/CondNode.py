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
    return visitor.visitCondNode(self)

  def getLeft(self) -> ASTNode:
    return self.left

  def setLeft(self, left: ASTNode):
    self.left = left

  def getRight(self) -> ASTNode:
    return self.right

  def setRight(self, right: ASTNode):
    self.right = right

  def getOp(self) -> OpType:
    return self.oc

  def setOp(self, op: OpType):
    self.oc = op

  def getReversedOp(self, op: OpType) -> OpType:
    if op == OpType.LE:
      return OpType.GT
    elif op == OpType.LT:
      return OpType.GE
    elif op == OpType.GE:
      return OpType.LT
    elif op == OpType.GT:
      return OpType.LE
    elif op == OpType.EQ:
      return OpType.NE
    elif op == OpType.NE:
      return OpType.EQ
    else:
      raise Exception("Bad op type")

