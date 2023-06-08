from .Instruction3O import Instruction3O
from .Instruction import OpCode

class FMul(Instruction3O):
  def __init__(self, src1: str, src2: str, dest: str):
    super().__init__(src1, src2, dest)
    self.oc = OpCode.FMULS
