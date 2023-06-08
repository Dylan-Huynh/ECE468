from .ASTNode import ASTNode
from typing import TYPE_CHECKING, Any
from .FunctionNode import FunctionNode

if TYPE_CHECKING:
  from .visitor import ASTVisitor

class FunctionListNode(ASTNode):
  def __init__(self, f: FunctionNode = None, fl: 'FunctionListNode' = None):
    self.functions = list()

    if f is not None:
      self.functions.append(f)

    if fl is not None:
      self.functions.extend(fl.functions)

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitFunctionListNode(self)
  
  def getFunctions(self) -> list:
    return self.functions
