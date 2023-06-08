from .InstructionLS import InstructionLS
from .Instruction import OpCode

class Sw(InstructionLS):
  def __init__(self, src: str, baseAddress: str, offset: str):
    super().__init__(src, baseAddress, offset)
    self.oc = OpCode.SW
