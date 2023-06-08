from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any
from ..compiler.SymbolTable import StaticVariables

if TYPE_CHECKING:
  from .visitor import ASTVisitor

class CallNode(ASTNode):
  def __init__(self, funcName: str, args: list):
    self.ste = StaticVariables.getSymbolTableSingleton().getFunctionSymbol(funcName)
    self.funcName = funcName
    self.args = args
    self.type = self.ste.getReturnType()

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitCallNode(self)

  def getArgs(self) -> list:
    return self.args

  def getFuncName(self) -> str:
    return self.funcName
