from abc import ABC, abstractmethod
from .Instruction import Instruction

class Instruction3O(Instruction):
  def __init__(self, src1: str, src2: str, dest: str):
    super().__init__()
    self.src1 = src1
    self.src2 = src2
    self.dest = dest

  def __str__(self):
    return str(self.oc) + " " + self.dest + ", " + self.src1 + ", " + self.src2
