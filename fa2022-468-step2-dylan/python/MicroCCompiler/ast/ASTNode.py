from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .visitor.ASTVisitor import ASTVisitor

#from ..compiler.Scope import Scope

class ASTNode(ABC):
    def __init__(self):
      self.val = None
      self.type = None

    def getVal(self) -> str:
      return self.val

    def setVal(self, val: str):
      self.val = val

    def getType(self):# -> Scope.Type:
      return self.type
  
    def setType(self, type):#: Scope.Type):
      self.type = type
    
    @abstractmethod
    def accept(self, visitor: 'ASTVisitor') -> Any:
        pass
