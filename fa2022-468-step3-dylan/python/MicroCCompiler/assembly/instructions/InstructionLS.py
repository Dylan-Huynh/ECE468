from abc import ABC, abstractmethod
from .Instruction import Instruction

class InstructionLS(Instruction):
  def __init__(self, reg1: str, reg2: str, offset: str):
    super()

    self.dest = reg1
    self.src1 = reg2
    self.label = offset

  def __str__(self):
    return str(self.oc) + " " + self.dest + ", " + self.label + "(" + self.src1 + ")"
