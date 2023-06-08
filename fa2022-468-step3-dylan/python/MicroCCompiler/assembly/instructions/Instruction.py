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
