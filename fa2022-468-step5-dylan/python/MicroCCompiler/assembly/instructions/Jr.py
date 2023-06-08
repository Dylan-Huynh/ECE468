from .Instruction import Instruction, OpCode

class Jr(Instruction):
  def __init__(self, label: str):
    super().__init__()
    self.label = label
    self.oc = OpCode.JR

  def __str__(self):
    return str(self.oc) + " " + self.label
