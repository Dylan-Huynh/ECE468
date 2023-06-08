from .Instruction import Instruction

class Blank(Instruction):
  def __init__(self):
    pass
  
  def __str__(self):
    return ""
