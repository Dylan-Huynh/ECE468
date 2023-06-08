from .InstructionPut import InstructionPut
from .Instruction import OpCode

class PutS(InstructionPut):
  def __init__(self, srcAddress: str):
    super().__init__(srcAddress)
    self.oc = OpCode.PUTS
