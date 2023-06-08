from .Instruction import Instruction, OpCode

class IMovF(Instruction):
  def __init__(self, src: str, dest: str):
    super().__init__()
    self.src1 = src
    self.dest = dest
    self.oc = OpCode.IMOVFS

  def __str__(self):
    return str(self.oc) + " " + self.dest + ", " + self.src1