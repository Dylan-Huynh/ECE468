import sys
import os

from ..compiler import *
from .instructions.Instruction import Instruction
from .InstructionList import InstructionList

class CodeObject:
  def __init__(self, ste: Scope.SymbolTableEntry = None):
    self.ste = ste
    if ste is not None:
      self.type = ste.getType()
    else:
      self.type = None
    self.code = InstructionList()
    self.temp = None
    self.lval = None

  def __str__(self):
    sb = ";Current temp: " + (self.temp if self.temp is not None else "")  +  "\n" + ";IR Code: \n" + str(self.code)
    return sb

  def getCode(self):
    return self.code

  def getTemp(self):
    return self.temp

  def isVar(self):
    return self.ste is not None

  def getSTE(self):
    return self.ste
  
  def getType(self):
    return self.type
