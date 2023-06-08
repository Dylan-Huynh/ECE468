from .Instruction import Instruction, OpCode

class Free(Instruction):
  def __init__(self, src: str):
    super().__init__()
    self.src = src
    self.oc = OpCode.FREE

  def __str__(self):
    return str(self.oc) + " " + self.src
