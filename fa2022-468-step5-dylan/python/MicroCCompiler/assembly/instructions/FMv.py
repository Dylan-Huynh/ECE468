from .Instruction import Instruction, OpCode

class FMv(Instruction):
  def __init__(self, src: str, dest: str):
    super().__init__()
    self.src1 = src1
    self.dest = dest
    self.oc = OpCode.FMVS

  def __str__(self):
    return str(self.oc) + " " + self.dest + ", " + self.src1
