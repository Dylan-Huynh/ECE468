from ..compiler import *
from ..assembly import *
from ..assembly.instructions import *

class Register:
    def __init__(self, regType:type, num:int, scope:LocalScope):
        self.num = num
        self.free = True
        self.regType = regType
        self.dirty = False
        self.scope = scope
        self.name = None
        self._isLocal = False

    def assign(self, opr:str):
        if opr[1] == "t":
            self.type = Scope.Type.INT
            self.name = opr
        if opr[1] == "f":
            self.type = Scope.Type.FLOAT
            self.name = opr
        if opr[1] == "g":
            self.name = opr
            self.ste = self.scope.getSymbolTableEntry(self.name)
            self._isLocal = False
        if opr[1] == "l":
            self.name = opr
            self.ste = None
            self._isLocal = True
        self.free = False

    def __str__(self):
        return "x" + str(self.num) if self.regType is Scope.Type.INT else "f" + str(self.num)

    def isLocal(self) -> bool:
        return self._isLocal

    def isGlobal(self) -> bool:
        return not self._isLocal

    def getLocalAddress(self) -> str:
        if not self._isLocal:
            return None
        else:
            self.address = self.name[2:]
    
    def getGlobalAddress(self) -> str:
        if self._isLocal:
            return None
        else:
            address = self.ste.addressToString()
    
    def getAddress(self) -> str:
        if not self.isLocal:
            return self.getGlobalAddress()
        else:
            return self.getLocalAddress()

    


