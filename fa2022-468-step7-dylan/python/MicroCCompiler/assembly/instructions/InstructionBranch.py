from .Instruction import Instruction

class InstructionBranch(Instruction):
  def __init__(self, src1: str, src2: str, label: str):
    super().__init__()

    self.src1 = src1
    self.src2 = src2
    self.label = label

  def __str__(self):

    #if "t231" in self.label or "t231" in self.src1 or "t231" in self.src2:
    #  raise Exception("%d is wrong: %d, %d, %d", self.oc, self.dest, self.src1, self.src2)
    #if "F" in str(self.oc):
    #  if "t" in self.src1 or "t" in self.src2 or "t" in self.label:
    #    raise Exception("%d is wrong: %d, %d, %d", self.oc, self.label, self.src1, self.src2)
    #else:
    #  if "f" in self.dest and "fp" not in self.dest or "f" in self.src1 and "fp" not in self.src1 or "f" in self.src2 and "fp" not in self.src2:
    #    raise Exception("%d is wrong", self.oc)
    if self.oc is None:
      raise Exception("its oc")
    if self.src1 is None:
      raise Exception("its src1")
    if self.src2 is None:
      raise Exception("its src2")
    if self.label is None:
      raise Exception("its label")
    return str(self.oc) + " " + self.src1 + ", " + self.src2 + ", " + self.label
