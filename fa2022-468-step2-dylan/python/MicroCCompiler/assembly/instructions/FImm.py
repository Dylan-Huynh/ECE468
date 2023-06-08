from .Instruction import Instruction, OpCode

class FImm(Instruction):
  def __init__(self, dest: str, value: str):
    super().__init__()
    self.dest = dest
    self.label = value
    self.oc = OpCode.FIMMS

  def __str__(self):
    return str(self.oc) + " " + self.dest + ", " + self.label
