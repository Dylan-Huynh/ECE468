from abc import ABC, abstractmethod
from .Instruction import Instruction

class Instruction3O(Instruction):
  def __init__(self, src1: str, src2: str, dest: str):
    super().__init__()
    self.src1 = src1
    self.src2 = src2
    self.dest = dest

  def __str__(self):
    #if "t231" in self.dest or "t231" in self.src1 or "t231" in self.src2:
      #raise Exception("%d is wrong: %d, %d, %d", self.oc, self.dest, self.src1, self.src2)
    if "F" in str(self.oc):
      if "FLE" not in str(self.oc) and "FEQ" not in str(self.oc) and "FLT" not in str(self.oc):
        if "t" in self.dest or "t" in self.src1 or "t" in self.src2:
          raise Exception("%d is wrong: %d, %d, %d", self.oc, self.dest, self.src1, self.src2)
      
    #else:
    #  if "f" in self.dest and "fp" not in self.dest or "f" in self.src1 and "fp" not in self.src1 or "f" in self.src2 and "fp" not in self.src2:
    #    raise Exception("%d is wrong", self.oc)
    return str(self.oc) + " " + self.dest + ", " + self.src1 + ", " + self.src2
