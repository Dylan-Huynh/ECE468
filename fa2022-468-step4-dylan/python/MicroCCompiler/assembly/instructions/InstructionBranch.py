from .Instruction import Instruction

class InstructionBranch(Instruction):
  def __init__(self, src1: str, src2: str, label: str):
    super().__init__()

    self.src1 = src1
    self.src2 = src2
    self.label = label

  def __str__(self):
    return str(self.oc) + " " + self.src1 + ", " + self.src2 + ", " + self.label
