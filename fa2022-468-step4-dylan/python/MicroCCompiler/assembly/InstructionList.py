from .instructions.Instruction import Instruction
from collections import UserList
from .instructions import *
from .instructions.La import La

class InstructionList(UserList):
  def __str__(self):
    #return "\n".join(self.data)
    return "\n".join([str(i) for i in self.data])
    #return "\n".join([(str(a) if a is not None else "") for a in self.data])

#  def __init__(self):
#    self.data = list()

#  def __str__(self):
#    return str(self.data) #."\n".join(self.data)

  def getLast(self) -> Instruction:
    return self.data[-1]
