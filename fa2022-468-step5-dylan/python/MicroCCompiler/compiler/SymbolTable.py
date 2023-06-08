from typing import List
import sys

from .Scope import Scope
from .GlobalScope import GlobalScope
from .LocalScope import LocalScope

class SymbolTable(object):
    def __init__(self, stringBase=0x10000000, globalBase=0x20000000):
        self.setGlobalScope(GlobalScope(stringBase, globalBase))

        self.scopeStack: List[Scope] = []
        self.scopeStack.append(self.getGlobalScope())
        
        self.errors: List[str] = []
    
    def currentScope(self) -> Scope:
        if len(self.scopeStack) > 0:
            return self.scopeStack[-1]
        else:
            return None
        
    def addVariable(self, type: Scope.Type, name: str, value: str=None):
        if value is None:
            assert (type != Scope.Type.STRING)
        else:
            assert (type == Scope.Type.STRING)

        e: Scope.ErrorType = self.currentScope().addSymbol(type, name, value)
        if e != Scope.ErrorType.NONE:
            print(f"Found {e} adding {type} {name}",file=sys.stderr)
        self.processError(name, e)
    
    def addArgument(self, type: Scope.Type, name: str):
        assert (isinstance(self.currentScope(), LocalScope))

        e: Scope.ErrorType = self.currentScope().addArgument(type, name)
        self.processError(name, e)
    
    def addFunction(self, returnType: Scope.Type, name: str, argTypes: List[Scope.Type]):
        assert isinstance(self.currentScope(), GlobalScope)
        gs: GlobalScope = self.currentScope()
        e: Scope.ErrorType = gs.addFunctionSymbol(returnType, name, argTypes)
        self.processError(name, e)
    
    def getSymbolTableEntry(self, name: str) -> Scope.SymbolTableEntry:
        return self.currentScope().getSymbolTableEntry(name)
    
    def getFunctionSymbol(self, name: str) -> Scope.FunctionSymbolTableEntry:
        ste: Scope.SymbolTableEntry = self.globalScope.getSymbolTableEntry(name)

        assert ste != None
        assert isinstance(ste, Scope.FunctionSymbolTableEntry)

        return ste
    
    def pushScope(self, name: str):
        s: Scope = self.currentScope().addSubScope(name)
        self.scopeStack.append(s)
    
    def popScope(self):
        self.scopeStack.pop()

    def processError(self, name: str, e: Scope.ErrorType):
        if e == Scope.ErrorType.NONE:
            return
        elif e == Scope.ErrorType.REDEC:
            return
        elif e == Scope.ErrorType.SHADOW:
            self.errors.append(f"SHADOW WARNING {name}")
        elif e == Scope.ErrorType.ERROR:
            self.errors.append(f"DECLARATION ERROR {name}")
            self.printErrors()
            sys.exit(1)
        
    def printErrors(self):
        for error in self.errors:
            print(error)
    
    def printTable(self):
        self.getGlobalScope().printTable()
    
    def getGlobalScope(self) -> Scope:
        return self.globalScope
    
    def setGlobalScope(self, globalScope: Scope):
        self.globalScope = globalScope

class StaticVariables:
  symbolTable = SymbolTable()
  def getSymbolTableSingleton():
    return StaticVariables.symbolTable

if __name__ == "__main__":
    st = SymbolTable()
    st.addVariable(Scope.Type.INT, "x")
    st.addVariable(Scope.Type.INT, "y")
    st.addVariable(Scope.Type.STRING, "z", "Hello")
    st.addVariable(Scope.Type.STRING, "w", "World")

    st.printTable()
