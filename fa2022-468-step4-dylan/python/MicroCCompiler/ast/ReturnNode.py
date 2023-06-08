from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any
from ..compiler import Scope

if TYPE_CHECKING:
  from .visitor.ASTVisitor import ASTVisitor

class ReturnNode(ASTNode):
  def __init__(self, retExpr: ASTNode, funcSymbol: Scope.FunctionSymbolTableEntry):
    self.setRetExpr(retExpr)
    self.setFuncSymbol(funcSymbol)

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitReturnNode(self)

  def getRetExpr(self) -> ASTNode:
    return self.retExpr

  def setRetExpr(self, expr: ASTNode):
    self.retExpr = expr

  def getFuncSymbol(self) -> Scope.FunctionSymbolTableEntry:
    return self.funcSymbol

  def setFuncSymbol(self, funcSymbol: Scope.FunctionSymbolTableEntry):
    self.funcSymbol = funcSymbol
