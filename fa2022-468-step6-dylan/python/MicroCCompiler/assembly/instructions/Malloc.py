from .Instruction import Instruction, OpCode

class Malloc(Instruction):
  def __init__(self, src: str, dst: str):
    super().__init__()
    self.src = src
    self.dst = dst
    self.oc = OpCode.MALLOC

  def __str__(self):
    return str(self.oc) + " " + self.dst + ", " + self.src
