from abc import ABC, abstractmethod
from .Instruction import Instruction

class InstructionPut(Instruction):
  def __init__(self, src: str):
    self.src1 = src

  def __str__(self):
    #if "t231" in self.src1:
    #    raise Exception("%d is wrong", self.oc)
    return str(self.oc) + " " + self.src1
