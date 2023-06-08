from .Instruction import Instruction, OpCode

class PopFloat(Instruction):
  def __init__(self, src: str):
    super().__init__()
    self.src1 = src

  def __str__(self):
    return "POPFLOAT " + self.src1

  def is3AC(self, o=None):
    return True
