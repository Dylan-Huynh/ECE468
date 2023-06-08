from .InstructionBranch import InstructionBranch
from .Instruction import OpCode

class Bge(InstructionBranch):
  def __init__(self, src1: str, src2: str, label: str):
    super().__init__(src1, src2, label)
    self.oc = OpCode.BGE
