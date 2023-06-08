from abc import ABC, abstractmethod
from .Instruction import Instruction

class InstructionLS(Instruction):
  def __init__(self, reg1: str, reg2: str, offset: str):
    super()
    
    self.dest = reg1
    self.src1 = reg2
    self.label = offset
    #print("oc")
    #print(type(self))
    #print("dest")
    #print(self.dest)
    #print("src1")
    #print(self.src1)
    #print("label")
    #print(self.label)

  def __str__(self):
    #if "t231" in self.dest or "t231" in self.src1 or "t231" in self.label:
    #  raise Exception("%d is wrong: %d, %d, %d", self.oc, self.dest, self.src1, self.label)
    if "F" in str(self.oc):
      if "FLE" not in str(self.oc) and "FEQ" not in str(self.oc) and "FLT" not in str(self.oc):
        if "t" in self.dest or "t" in self.src1 or "t" in self.label:
          raise Exception("%d is wrong: %d, %d, %d", self.oc, self.dest, self.src1, self.label)
    #if "F" in str(self.oc):
    #  if "t" in self.dest or "t" in self.src1 or "t" in self.label:
    #    raise Exception("%d is wrong: %d, %d, %d", self.oc, self.dest, self.src1, self.label)
    #else:
    #  if "f" in self.dest and "fp" not in self.dest or "f" in self.src1 and "fp" not in self.src1 or "f" in self.label and "fp" not in self.label:
    #    raise Exception("%d is wrong: %d, %d, %d", self.oc, self.dest, self.src1, self.label)
    return str(self.oc) + " " + self.dest + ", " + self.label + "(" + self.src1 + ")"
