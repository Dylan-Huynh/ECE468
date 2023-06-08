from .InstructionLS import InstructionLS
from .Instruction import OpCode

class Fsw(InstructionLS):
  def __init__(self,baseAddress: str,  src: str, offset: str):
    super().__init__(baseAddress, src, offset)
    self.oc = OpCode.FSW
