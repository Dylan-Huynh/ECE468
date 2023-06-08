from .Instruction import Instruction, OpCode

class Ret(Instruction):
  def __init__(self):
    super().__init__()
    self.oc = OpCode.RET

  def __str__(self):
    return str(self.oc)
