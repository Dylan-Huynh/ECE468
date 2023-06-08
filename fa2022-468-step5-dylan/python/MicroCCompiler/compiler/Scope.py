from abc import ABC, abstractmethod
from enum import Enum
from symtable import SymbolTable
from typing import Dict, List, Union, Collection

class Scope(ABC):
    class Type(Enum):
        STRING=1
        INT=2
        FLOAT=3
        VOID=4
    class ErrorType(Enum):
        SHADOW=1
        ERROR=2
        REDEC=3
        NONE=4

    class SymbolTableEntry(object):
        def __init__(self, type: 'Scope.Type', name: str, address: int, isLocal: bool=False):
            self.setName(name)
            self.setType(type)
            self.setAddress(address)
            self._isLocal = isLocal
        
        def __str__(self) -> str:
            return f"; name {self.getName()} type {self.getType()} location {self.addressToString()}"
        def getType(self) -> 'Scope.Type':
            return self.type
        def setType(self, type: 'Scope.Type'):
            self.type = type
        def getName(self) -> str:
            return self.name
        def setName(self, name: str):
            self.name = name
        def getAddress(self) -> int:
            return self.address
        def setAddress(self, address: int):
            self.address = address
        def addressToString(self) -> str:
            return (str(self.getAddress())) if self._isLocal else ("{}".format(hex(int(self.getAddress()))))
        def isLocal(self) -> bool:
            return self._isLocal
    
    class StringSymbolTableEntry(SymbolTableEntry):
        def __init__(self, type: 'Scope.Type', name: str, value: str, address: int, isLocal: bool=False):
            super().__init__(type, name, address, isLocal)
            self.setValue(value)
        
        def __str__(self) -> str:
            return super().__str__() + " value " + self.getValue()
        def getValue(self) -> str:
            return self.value
        def setValue(self, value: str):
            self.value = value
    
    class FunctionSymbolTableEntry(SymbolTableEntry):
        def __init__(self, returnType: 'Scope.Type', name: str, argTypes: List['Scope.Type']):
            super().__init__(returnType, name, 0)
            self.argTypes = argTypes
            self._isDefined = False

        def getArgTypes(self) -> List['Scope.Type']:
            return self.argTypes
        def getReturnType(self) -> 'Scope.Type':
            return self.getType()
        def isDefined(self) -> bool:
            return self._isDefined
        def setDefined(self, defined: bool):
            self._isDefined = defined
        def __str__(self) -> str:
            return f"; Function: {self.getReturnType()} {self.getName()}({self.getArgTypes()})"

    def __init__(self, parent: Union['Scope', None]=None):
        self.table: Dict[str, Scope.SymbolTableEntry] = {}
        self.subScopes: List[Scope] = []
        self.name: str = ""
        self.parentTable: Scope = parent

    def setName(self, name: str):
        self.name: str = name
    def getName(self) -> str:
        return self.name

    def addSymbol(self, type: Type, name: str, value: Union[str, None]=None) -> ErrorType:
        retVal: Scope.ErrorType = self.checkSymbol(name)
        if value is None:
            self.table[name] = self.genSymbol(type, name)
        else:
            self.table[name] = self.genStringSymbol(type, name, value)
        return retVal
    
    @abstractmethod
    def genSymbol(self, type: Type, name: str) -> SymbolTableEntry:
        pass
    
    @abstractmethod
    def genStringSymbol(self, type: Type, name: str, value: str) -> StringSymbolTableEntry:
        pass

    def addSubScope(self, name: str) -> 'Scope':
        newScope: Scope = LocalScope(self)
        newScope.setName(name)
        self.subScopes.append(newScope)
        return newScope
    
    def getSymbolTableEntry(self, name: str) -> SymbolTableEntry:
        retval: Scope.SymbolTableEntry = None;

        retval = self.searchLocalScope(name)
        if not retval is None:
            return retval
        else:
            if self.parentTable is None:
                return None;
            else:
                return self.parentTable.getSymbolTableEntry(name)

    @abstractmethod
    def searchLocalScope(self, name: str) -> SymbolTableEntry:
        pass

    def checkSymbol(self, name: str) -> ErrorType:
        ste: Scope.SymbolTableEntry = self.searchLocalScope(name)
        if not ste is None:
            if isinstance(ste, Scope.FunctionSymbolTableEntry):
                if not ste.isDefined():
                    return Scope.ErrorType.REDEC
            return Scope.ErrorType.ERROR
        else:
            if self.parentTable is None:
                return Scope.ErrorType.NONE
            if self.parentTable.checkSymbol(name) != Scope.ErrorType.NONE:
                return Scope.ErrorType.SHADOW
        return Scope.ErrorType.NONE

    def printTable(self):
        self.printLocalTable()
        for st in self.subScopes:
            st.printTable()
    
    def printLocalTable(self):
        print("; Symbol table " + self.name)

        for ste in self.table.values():
            print(ste)
        
        print("")
    
    def getEntries(self) -> Collection[SymbolTableEntry]:
        return self.table.values()

class LocalScope(Scope):
    startingLocalsOffset: int = -4  # start local var offset with room for old frame pointer
    startingArgsOffset: int = 12 # start argument offset with room for old fp, old return address and return value

    def __init__(self, parent: Scope=None):
        super().__init__(parent)
        self.numLocals: int = 0
        self.numArgs: int = 0
        self.name: str = "FUNCTION NAME NOT SET"
        self.localsOffset: int = LocalScope.startingLocalsOffset
        self.argsOffset: int = LocalScope.startingArgsOffset 
    
    def addArgument(self, type: Scope.Type, name: str) -> Scope.ErrorType:
        retVal: Scope.ErrorType = self.checkSymbol(name)
        self.table[name] = self.genArgument(type, name)
        return retVal
    def genArgument(self, type: Scope.Type, name: str) -> Scope.SymbolTableEntry:
        addr: int = self.argsOffset
        ste: Scope.SymbolTableEntry = Scope.SymbolTableEntry(type, name, addr, True)
        self.argsOffset += 4
        self.numArgs += 1
        return ste

    def genSymbol(self, type: Scope.Type, name: str) -> Scope.SymbolTableEntry:
        addr: int = self.localsOffset
        ste: Scope.SymbolTableEntry = Scope.SymbolTableEntry(type, name, addr, True)
        self.localsOffset -= 4
        self.numLocals += 1
        return ste
    
    def genStringSymbol(self, type: Scope.Type, name: str, value: str) -> Scope.StringSymbolTableEntry:
        raise Exception("Should never try to create a string symbol in a local scope")
    
    def searchLocalScope(self, name: str) -> Scope.SymbolTableEntry:
        retval: Scope.SymbolTableEntry = self.table.get(name)
        return retval
    
    def getNumLocals(self) -> int :
        return self.numLocals
