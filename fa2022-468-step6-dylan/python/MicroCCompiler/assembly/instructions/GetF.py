from .Instruction import Instruction, OpCode

class GetF(Instruction):
  def __init__(self, dest: str):
    super().__init__()
    self.dest = dest
    self.oc = OpCode.GETF

  def __str__(self):
    return str(self.oc) + " " + self.dest
