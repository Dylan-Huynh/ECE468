from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any
from enum import Enum

if TYPE_CHECKING:
  from .visitor import ASTVisitor

class BinaryOpNode(ASTNode):
  class OpType(Enum):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4

  def getOpFromString(self, op: str):
    if op == '+':
      return self.OpType.ADD
    elif op == '-':
      return self.OpType.SUB
    elif op == '*':
      return self.OpType.MUL
    elif op == '/':
      return self.OpType.DIV
    else:
      raise Exception("Invalid opcode in BinaryOp")

  def __init__(self, left: ASTNode, right: ASTNode, op: str):
    self.setLeft(left)
    self.setRight(right)
    self.setOp(self.getOpFromString(op))
    self.setType(left.getType())

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitBinaryOpNode(self)

  def getLeft(self) -> ASTNode:
    return self.left

  def setLeft(self, left: ASTNode):
    self.left = left

  def getRight(self) -> ASTNode:
    return self.right

  def setRight(self, right: ASTNode):
    self.right = right

  def setOp(self, op):
    self.op = op

  def getOp(self) -> OpType:
    return self.op
