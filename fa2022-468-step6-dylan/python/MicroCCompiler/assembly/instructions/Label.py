from .Instruction import Instruction

class Label(Instruction):
  def __init__(self, label: str):
    super().__init__()
    self.label = label

  def __str__(self):
    return self.label + ":"
