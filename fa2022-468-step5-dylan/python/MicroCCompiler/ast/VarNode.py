from .ASTNode import ASTNode
from ..compiler import Scope
from ..compiler.SymbolTable import StaticVariables

from typing import TYPE_CHECKING, Any
if TYPE_CHECKING:
    from .visitor import ASTVisitor

class VarNode(ASTNode):

    def __init__(self, ident: str):
        self.setIdent(ident)
        self.setSymbol(StaticVariables.getSymbolTableSingleton().getSymbolTableEntry(ident))
        self.setType(self.ste.getType())

    def accept(self, visitor: 'ASTVisitor') -> Any:
        return visitor.visitVarNode(self)

    def getIdent(self) -> str:
        return self.ident
    
    def setIdent(self, ident: str):
        self.ident = ident

    def getSymbol(self) -> Scope.SymbolTableEntry:
        return self.ste
    
    def setSymbol(self, ste: Scope.SymbolTableEntry):
        self.ste = ste
