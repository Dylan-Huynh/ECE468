from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any
from enum import Enum

if TYPE_CHECKING:
  from .visitor.ASTVisitor import ASTVisitor

class UnaryOpNode(ASTNode):
  class OpType(Enum):
    NEG = 1

  def getOpFromString(self, op) -> OpType:
    if op == '-':
      return self.OpType.NEG
    else:
      raise Exception("Unrecognized op type")

  def __init__(self, expr: ASTNode, op: str):
    self.setExpr(expr)
    self.setOp(self.getOpFromString(op))
    self.setType(expr.getType())

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitUnaryOpNode(self)

  def getExpr(self) -> ASTNode:
    return self.expr

  def setExpr(self, expr: ASTNode):
    self.expr = expr

  def getOp(self) -> OpType:
    return self.op

  def setOp(self, op: OpType):
    self.op = op
