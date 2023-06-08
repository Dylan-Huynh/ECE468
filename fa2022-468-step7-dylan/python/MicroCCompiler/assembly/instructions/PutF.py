from .InstructionPut import InstructionPut
from .Instruction import OpCode

class PutF(InstructionPut):
  def __init__(self, srcValue: str):
    super().__init__(srcValue)
    self.oc = OpCode.PUTF
