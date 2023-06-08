from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any
from ..compiler.SymbolTable import StaticVariables
from ..compiler import Scope

if TYPE_CHECKING:
  from .visitor import ASTVisitor

class CastNode(ASTNode):

  def __init__(self, base_type: Scope.Type, expr: ASTNode):
    self.setExpr(expr)
    self.setType(base_type)

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitCastNode(self)

  def getExpr(self) -> ASTNode:
    return self.expr

  def setExpr(self, expr: ASTNode):
    self.expr = expr

  def setType(self, base_type: Scope.Type):
    self.type = base_type

  def getType(self):
    return self.type
