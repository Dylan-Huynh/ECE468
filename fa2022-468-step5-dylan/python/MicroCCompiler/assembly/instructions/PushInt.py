from .Instruction import Instruction, OpCode

class PushInt(Instruction):
  def __init__(self, src: str):
    super().__init__()
    self.src1 = src

  def __str__(self):
    return "PUSH " + self.src1

  def is3AC(self, o=None):
    return True
