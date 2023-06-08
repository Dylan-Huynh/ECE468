from .InstructionLS import InstructionLS
from .Instruction import OpCode

class Flw(InstructionLS):
  def __init__(self, dest: str, baseAddress: str, offset: str):
    super().__init__(dest, baseAddress, offset)
    self.oc = OpCode.FLW
