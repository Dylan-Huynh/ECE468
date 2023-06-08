from .Instruction import Instruction, OpCode

class La(Instruction):
  def __init__(self, dest: str, address: str):
    super().__init__()
    self.dest = dest
    self.label = address
    self.oc = OpCode.LA

  def __str__(self):
    return str(self.oc) + " " + self.dest + ", " + self.label
