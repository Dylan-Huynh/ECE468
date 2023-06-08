from .Instruction import Instruction, OpCode

class Halt(Instruction):
  def __init__(self):
    super().__init__()
    self.oc = OpCode.HALT

  def __str__(self):
    return self.oc.value
