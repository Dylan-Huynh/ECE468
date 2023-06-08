from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any

from ..compiler.Scope import Scope

if TYPE_CHECKING:
  from .visitor import ASTVisitor

class MallocNode(ASTNode):
  def __init__(self, arg: ASTNode):
    self.ste = None # Special function without STE
    self.arg = arg
    self.type = Scope.Type(Scope.InnerType.INFER)

  def accept(self, visitor: 'ASTVisitor'):
    return visitor.visitMallocNode(self)

  def getArg(self):
    return self.arg

  def getFuncName(self):
    return self.funcName
