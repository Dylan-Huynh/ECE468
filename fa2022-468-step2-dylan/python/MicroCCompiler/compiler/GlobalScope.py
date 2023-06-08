from .Scope import Scope

class GlobalScope(Scope):
    def __init__(self, stringBase: int, globalBase: int):
        super().__init__(None)
        self.globalBase: int = globalBase
        self.stringBase: int = stringBase
    
    def genSymbol(self, type: Scope.Type, name: str) -> Scope.SymbolTableEntry:
        addr: int = self.globalBase
        ste: Scope.SymbolTableEntry = Scope.SymbolTableEntry(type, name, addr, False)
        self.globalBase += 4
        return ste
    
    def genStringSymbol(self, type: Scope.Type, name: str, value: str) -> Scope.StringSymbolTableEntry:
        addr: int = self.stringBase
        ste: Scope.StringSymbolTableEntry = Scope.StringSymbolTableEntry(type, name, value, addr, False)
        self.stringBase += 4
        return ste

    def searchLocalScope(self, name: str) -> Scope.SymbolTableEntry:
        retval: Scope.SymbolTableEntry = self.table.get(name)
        return retval
