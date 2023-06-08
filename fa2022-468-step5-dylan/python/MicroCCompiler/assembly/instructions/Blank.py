from .Instruction import Instruction

from typing import Union

class Blank(Instruction):
  def __init__(self, c: Union[str, None]=None):
    if c is not None:
      self.comment = c
    else:
      self.comment = ""
  
  def __str__(self):
    return ";" + self.comment
