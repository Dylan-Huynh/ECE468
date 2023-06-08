# Generated from python/MicroC.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



from typing import List

from MicroCCompiler.compiler.SymbolTable import SymbolTable
from MicroCCompiler.compiler.Scope import Scope
from MicroCCompiler.ast.IntLitNode import IntLitNode
from MicroCCompiler.ast.FloatLitNode import FloatLitNode
from MicroCCompiler.ast.AssignNode import AssignNode
from MicroCCompiler.ast.VarNode import VarNode
from MicroCCompiler.ast.WriteNode import WriteNode
from MicroCCompiler.ast.ReadNode import ReadNode
from MicroCCompiler.ast.ReturnNode import ReturnNode
from MicroCCompiler.ast.CondNode import CondNode
from MicroCCompiler.ast.CallNode import CallNode
from MicroCCompiler.ast.IfStatementNode import IfStatementNode
from MicroCCompiler.ast.WhileNode import WhileNode
from MicroCCompiler.ast.StatementListNode import StatementListNode
from MicroCCompiler.ast.ASTNode import ASTNode
from MicroCCompiler.ast.BinaryOpNode import BinaryOpNode
from MicroCCompiler.ast.UnaryOpNode import UnaryOpNode
from MicroCCompiler.ast.FunctionListNode import FunctionListNode
from MicroCCompiler.ast.FunctionNode import FunctionNode



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\"")
        buf.write("\u00d9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\34\7\34\u00a2\n\34\f\34\16\34\u00a5\13\34")
        buf.write("\3\35\6\35\u00a8\n\35\r\35\16\35\u00a9\3\36\7\36\u00ad")
        buf.write("\n\36\f\36\16\36\u00b0\13\36\3\36\3\36\6\36\u00b4\n\36")
        buf.write("\r\36\16\36\u00b5\3\37\3\37\7\37\u00ba\n\37\f\37\16\37")
        buf.write("\u00bd\13\37\3\37\3\37\3 \3 \3 \3 \7 \u00c5\n \f \16 ")
        buf.write("\u00c8\13 \3 \3 \3 \3 \3 \3!\6!\u00d0\n!\r!\16!\u00d1")
        buf.write("\3!\3!\3\"\3\"\3#\3#\3\u00c6\2$\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C\2E\2\3\2\5\3\2$$\5\2\13\f\17\17\"")
        buf.write("\"\4\2C\\c|\2\u00de\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\3G\3\2\2\2\5I\3\2\2\2\7P")
        buf.write("\3\2\2\2\tR\3\2\2\2\13V\3\2\2\2\r\\\3\2\2\2\17^\3\2\2")
        buf.write("\2\21`\3\2\2\2\23b\3\2\2\2\25d\3\2\2\2\27f\3\2\2\2\31")
        buf.write("k\3\2\2\2\33q\3\2\2\2\35x\3\2\2\2\37{\3\2\2\2!\u0080\3")
        buf.write("\2\2\2#\u0086\3\2\2\2%\u0088\3\2\2\2\'\u008a\3\2\2\2)")
        buf.write("\u008c\3\2\2\2+\u008e\3\2\2\2-\u0090\3\2\2\2/\u0093\3")
        buf.write("\2\2\2\61\u0096\3\2\2\2\63\u0099\3\2\2\2\65\u009c\3\2")
        buf.write("\2\2\67\u009e\3\2\2\29\u00a7\3\2\2\2;\u00ae\3\2\2\2=\u00b7")
        buf.write("\3\2\2\2?\u00c0\3\2\2\2A\u00cf\3\2\2\2C\u00d5\3\2\2\2")
        buf.write("E\u00d7\3\2\2\2GH\7=\2\2H\4\3\2\2\2IJ\7u\2\2JK\7v\2\2")
        buf.write("KL\7t\2\2LM\7k\2\2MN\7p\2\2NO\7i\2\2O\6\3\2\2\2PQ\7?\2")
        buf.write("\2Q\b\3\2\2\2RS\7k\2\2ST\7p\2\2TU\7v\2\2U\n\3\2\2\2VW")
        buf.write("\7h\2\2WX\7n\2\2XY\7q\2\2YZ\7c\2\2Z[\7v\2\2[\f\3\2\2\2")
        buf.write("\\]\7*\2\2]\16\3\2\2\2^_\7+\2\2_\20\3\2\2\2`a\7}\2\2a")
        buf.write("\22\3\2\2\2bc\7\177\2\2c\24\3\2\2\2de\7.\2\2e\26\3\2\2")
        buf.write("\2fg\7t\2\2gh\7g\2\2hi\7c\2\2ij\7f\2\2j\30\3\2\2\2kl\7")
        buf.write("r\2\2lm\7t\2\2mn\7k\2\2no\7p\2\2op\7v\2\2p\32\3\2\2\2")
        buf.write("qr\7t\2\2rs\7g\2\2st\7v\2\2tu\7w\2\2uv\7t\2\2vw\7p\2\2")
        buf.write("w\34\3\2\2\2xy\7k\2\2yz\7h\2\2z\36\3\2\2\2{|\7g\2\2|}")
        buf.write("\7n\2\2}~\7u\2\2~\177\7g\2\2\177 \3\2\2\2\u0080\u0081")
        buf.write("\7y\2\2\u0081\u0082\7j\2\2\u0082\u0083\7k\2\2\u0083\u0084")
        buf.write("\7n\2\2\u0084\u0085\7g\2\2\u0085\"\3\2\2\2\u0086\u0087")
        buf.write("\7/\2\2\u0087$\3\2\2\2\u0088\u0089\7-\2\2\u0089&\3\2\2")
        buf.write("\2\u008a\u008b\7,\2\2\u008b(\3\2\2\2\u008c\u008d\7\61")
        buf.write("\2\2\u008d*\3\2\2\2\u008e\u008f\7>\2\2\u008f,\3\2\2\2")
        buf.write("\u0090\u0091\7>\2\2\u0091\u0092\7?\2\2\u0092.\3\2\2\2")
        buf.write("\u0093\u0094\7@\2\2\u0094\u0095\7?\2\2\u0095\60\3\2\2")
        buf.write("\2\u0096\u0097\7?\2\2\u0097\u0098\7?\2\2\u0098\62\3\2")
        buf.write("\2\2\u0099\u009a\7#\2\2\u009a\u009b\7?\2\2\u009b\64\3")
        buf.write("\2\2\2\u009c\u009d\7@\2\2\u009d\66\3\2\2\2\u009e\u00a3")
        buf.write("\5C\"\2\u009f\u00a2\5C\"\2\u00a0\u00a2\5E#\2\u00a1\u009f")
        buf.write("\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a48\3\2\2\2\u00a5")
        buf.write("\u00a3\3\2\2\2\u00a6\u00a8\5E#\2\u00a7\u00a6\3\2\2\2\u00a8")
        buf.write("\u00a9\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2")
        buf.write("\u00aa:\3\2\2\2\u00ab\u00ad\5E#\2\u00ac\u00ab\3\2\2\2")
        buf.write("\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3")
        buf.write("\2\2\2\u00af\u00b1\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b3")
        buf.write("\7\60\2\2\u00b2\u00b4\5E#\2\u00b3\u00b2\3\2\2\2\u00b4")
        buf.write("\u00b5\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2")
        buf.write("\u00b6<\3\2\2\2\u00b7\u00bb\7$\2\2\u00b8\u00ba\n\2\2\2")
        buf.write("\u00b9\u00b8\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb\u00b9\3")
        buf.write("\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00be\3\2\2\2\u00bd\u00bb")
        buf.write("\3\2\2\2\u00be\u00bf\7$\2\2\u00bf>\3\2\2\2\u00c0\u00c1")
        buf.write("\7\61\2\2\u00c1\u00c2\7,\2\2\u00c2\u00c6\3\2\2\2\u00c3")
        buf.write("\u00c5\13\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c8\3\2\2")
        buf.write("\2\u00c6\u00c7\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c9")
        buf.write("\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00ca\7,\2\2\u00ca")
        buf.write("\u00cb\7\61\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\b \2\2")
        buf.write("\u00cd@\3\2\2\2\u00ce\u00d0\t\3\2\2\u00cf\u00ce\3\2\2")
        buf.write("\2\u00d0\u00d1\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2")
        buf.write("\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\b!\2\2\u00d4")
        buf.write("B\3\2\2\2\u00d5\u00d6\t\4\2\2\u00d6D\3\2\2\2\u00d7\u00d8")
        buf.write("\4\62;\2\u00d8F\3\2\2\2\13\2\u00a1\u00a3\u00a9\u00ae\u00b5")
        buf.write("\u00bb\u00c6\u00d1\3\b\2\2")
        return buf.getvalue()


class MicroCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    IDENTIFIER = 27
    INT_LITERAL = 28
    FLOAT_LITERAL = 29
    STR_LITERAL = 30
    COMMENT = 31
    WS = 32

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'string'", "'='", "'int'", "'float'", "'('", "')'", 
            "'{'", "'}'", "','", "'read'", "'print'", "'return'", "'if'", 
            "'else'", "'while'", "'-'", "'+'", "'*'", "'/'", "'<'", "'<='", 
            "'>='", "'=='", "'!='", "'>'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "INT_LITERAL", "FLOAT_LITERAL", "STR_LITERAL", 
            "COMMENT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "IDENTIFIER", "INT_LITERAL", "FLOAT_LITERAL", "STR_LITERAL", 
                  "COMMENT", "WS", "LETTER", "DIGIT" ]

    grammarFileName = "MicroC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def setSymbolTable(self, st: SymbolTable):
      self.st = st

    def getSymbolTable(self) -> SymbolTable:
      return self.st

    def setAST(self, node: ASTNode):
      self.ast = node

    def getAST(self) -> ASTNode:
      return self.ast

    def addParams(self, types: List[Scope.Type], names: List[str]):
      for i in reversed(range(len(types))):
        self.st.addArgument(types[i], names[i])



