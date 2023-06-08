from abc import ABC, abstractmethod
from enum import Enum

class OpCode(Enum):
  LI = "LI"
  LA = "LA"
  ADD = "ADD"
  SUB = "SUB"
  DIV = "DIV"
  MUL = "MUL"
  NEG = "NEG"
  MV = "MV"
  LW = "LW"
  SW = "SW"
  PUTS = "PUTS"
  PUTI = "PUTI"
  GETI = "GETI"
  HALT = "HALT"
  ADDI = "ADDI"

  # BRANCH INSTRUCTIONS
  BEQ = "BEQ"
  BGE = "BGE"
  BGT = "BGT"
  BLE = "BLE"
  BLT = "BLT"
  BNE = "BNE"
  J = "J"

  # FLOAT INSTRUCTIONS
  FADDS = "FADD.S"
  FSUBS = "FSUB.S"
  FDIVS = "FDIV.S"
  FMULS = "FMUL.S"
  FMVS = "FMV.S"
  FNEGS = "FNEG.S"
  FLW = "FLW"
  FSW = "FSW"
  GETF = "GETF"
  PUTF = "PUTF"
  FIMMS = "FIMM.S"
  FLT = "FLT.S"
  FLE = "FLE.S"
  FEQ = "FEQ.S"

  # FUNCTION CALL AND RETURN
  JR = "JR"
  RET = "RET"

  def __init__(self, name: str):
    self.opCodeName = name

  def __str__(self):
    return self.opCodeName


class Instruction(ABC):
  def __init__(self):
    self.src1  = None
    self.src2  = None
    self.dest  = None
    self.label = None
    self.oc    = None

  def getDest(self):
    return self.dest

  class Operand(Enum):
    SRC1 = "SRC1"
    SRC2 = "SRC2"
    DEST = "DEST"

  def getOC(self) -> OpCode:
    return self.oc

  def getOperand(self, o: Operand) -> str:
    if o == self.Operand.SRC1:
      return self.src1
    elif o == self.Operand.SRC2:
      return self.src2
    elif o == self.Operand.DEST:
      return self.dest
    else:
      raise Exception("Shouldn't get here")

  def getLabel(self) -> str:
    return self.label

  # Accepted signatures:
  # Instruction.is3AC(str)
  # inst.is3AC()
  # inst.is3AC(Operand)
  def is3AC(*args) -> bool:
    # Instruction.is3AC(str)
    if len(args) == 1 and isinstance(args[0], str):
      s = args[0]
      return (s is not None) and (s[0] == '$')
    # inst.is3AC()
    elif len(args) == 1 and isinstance(args[0], Instruction):
      self = args[0]
      return self.is3AC(self.Operand.SRC1) or self.is3AC(self.Operand.SRC2) or self.is3AC(self.Operand.DEST)
    # inst.is3AC(Operand)
    elif len(args) == 2 and isinstance(args[0], Instruction) and isinstance(args[1], Instruction.Operand):
      self = args[0]
      o = args[1]
      if o == self.Operand.SRC1:
        return Instruction.is3AC(self.src1)
      elif o == self.Operand.SRC2:
        return Instruction.is3AC(self.src2)
      elif o == self.Operand.DEST:
        return Instruction.is3AC(self.dest)
      else:
        raise Exception("Shouldn't get here")
    else:
      raise Exception("Unknown function overload")

  def isBranch(self) -> bool:
    if self.getOC().name in "BEQBGEBGTBLEBLTBNE":
      return True
    return False

  def isPut(self) -> bool:
    if self.getOC().name in "PUTIPUTFPUTS":
      return True
    return False
  
  def isLS(self) -> bool:
    if self.getOC().name in "FLWFSW":
      return True
    return False
  
  def is30(self) -> bool:
    if self.getOC().name in "FADDIFMULFDIVFSUBFNEFEQFLTFLE":
      return True
    return False

