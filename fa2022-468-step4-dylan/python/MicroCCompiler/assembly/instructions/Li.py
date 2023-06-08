from .Instruction import Instruction, OpCode

class Li(Instruction):
  def __init__(self, dest: str, value: str):
    super().__init__()
    self.dest = dest
    self.label = value
    self.oc = OpCode.LI

  def __str__(self):
    return str(self.oc) + " " + self.dest + ", " + self.label
