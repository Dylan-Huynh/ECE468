from ..compiler import *
from ..assembly import *
from ..assembly.instructions import *
from .Register import Register
import string

class RegisterFile:
    def __init__(self, regType: Scope.Type, num: int, scope:LocalScope):
        self.type = regType
        if self.type == Scope.Type.INT:
            self.array = [None] * (num - 5)
            for i in range(4, 8): #Using x0-3, and 8 for other sutff
                self.array[i - 4] = Register(Scope.Type.INT, i, scope)
            for i in range(9, num):
                self.array[i - 5] = Register(Scope.Type.INT, i, scope)
        else:
            self.array = [None] * num
            for i in range(0, num):
                self.array[i] = Register(Scope.Type.FLOAT, i, scope)
        self.free = True

    def findMappedReg(self, variable:str) -> Register:
        for i in self.array:
            if i is not None:
                if i.name is variable:
                    return i
        return None

    def findReg(self, il:InstructionList) -> Register:
        for i in self.array:
            if i.free is True:
                return i
        for i in self.array:
            if i.dirty is False:
                return i
        free(4, il)
        self.array[4].Free = False
        return self.array[4]

    
    def free(self, reg:int, il:InstructionList):
        if self.array[reg].dirty is True:
            if self.type is Scope.Type.INT:
                if self.array[reg].isLocal():
                    il.append(Sw(self.array[reg].getLocalAddress(), "x" + str(self.array[reg].num), "fp"))
                else:
                    il.append(La("x3", 0, self.array[reg].getGlobalAddress()))
                    il.append(Sw(0, "x" + str(self.array[reg].num), "x3"))
            else:
                if self.array[reg].isLocal():
                    il.append(Sw(self.array[reg].getLocalAddress(), "f" + str(self.array[reg].num), "fp"))
                else:
                    il.append(La("x3", 0, self.array[reg].getGlobalAddress()))
                    il.append(Sw(0, "f" + str(self.array[reg].num), "x3"))
                
        self.array[reg].free = True
        self.array[reg].dirty = False

    def ensureSource(self, opr:str, opType:Scope.Type, il:InstructionList, scope:LocalScope) -> Register:
        #print(opr)
        newIL = InstructionList()
        if(opr[0].isdigit()):
            if opType == Scope.Type.INT:
                r = self.findReg(il)
                il.append(Li(str(r), opr))
                return r
            else:
                r = self.findReg(il)

                il.append(FImm(str(r), opr))
                return r
            
        if (opr[1] == "t" or opr[1] == "f"):
            
            r = self.findMappedReg(opr)
            if r is not None:
                return r
            else:
                r = self.findReg(il)
        else:
            r = self.findMappedReg(opr)
            
            if r is not None:
                
                return r
            else:
                r = self.findReg(il)
                
        
        if opr[1] == "l":
            if opType is Scope.Type.FLOAT:
                address = opr[2:]
                flw = Flw(str(r), "fp", address)
                newIL.append(flw)
            else:
                address = opr[2:]
                lw = Lw(str(r), "fp", address)
                newIL.append(lw)
            il.extend(newIL)
        elif opr[1] == "g":
            ste = scope.getSymbolTableEntry(opr[2:])
            address = ste.addressToString()
            newIL.append(La("x3", address))

            if opType is Scope.Type.FLOAT:
                flw = Flw(str(r), "x3", "0")
                newIL.append(flw)
            else:
                lw = Lw(str(r), "x3", "0")
                newIL.append(lw)
            il.extend(newIL)
        r.assign(opr)
        return r

    def ensureDest(self, opr:str, opType:Scope.Type, il:InstructionList, scope:LocalScope) -> Register:
        #print(opr)
        newIL = InstructionList()
        if (opr[1] == "t" or opr[1] == "f"):
            r = self.findMappedReg(opr)
            if r is not None:
                return r
        else:
            r = self.findMappedReg(opr)
            if r is not None:
                return r
            else:
                r = self.findReg(il)
        r = self.findReg(il)

        if opr[1] == "l":
            if opType is Scope.Type.FLOAT:
                address = opr[2:]
                flw = Flw(str(r), "fp", address)
                newIL.append(flw)
            else:
                address = opr[2:]
                lw = Lw(str(r), "fp", address)
                newIL.append(lw)
            il.extend(newIL)
        elif opr[1] == "g":
            ste = scope.getSymbolTableEntry(opr[2:])
            address = ste.addressToString()
            newIL.append(La("x3", address))

            if opType is Scope.Type.FLOAT:
                flw = Flw(str(r), "x3", "0")
                newIL.append(flw)
            else:
                lw = Lw(str(r), "x3", "0")
                newIL.append(lw)
            il.extend(newIL)
        r.assign(opr)
        #print(r.name)
        if r.name is not None:
            r.dirty = True
        return r