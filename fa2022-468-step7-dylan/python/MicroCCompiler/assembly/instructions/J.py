from .Instruction import Instruction, OpCode

class J(Instruction):
  def __init__(self, label: str):
    super().__init__()
    self.label = label
    self.oc = OpCode.J

  def __str__(self):
    return str(self.oc) + " " + self.label
