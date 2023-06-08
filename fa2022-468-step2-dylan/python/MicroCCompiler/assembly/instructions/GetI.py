from .Instruction import Instruction, OpCode

class GetI(Instruction):
  def __init__(self, dest: str):
    super().__init__()
    self.dest = dest
    self.oc = OpCode.GETI

  def __str__(self):
    return str(self.oc) + " " + self.dest
