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
from MicroCCompiler.ast.PtrDerefNode import PtrDerefNode
from MicroCCompiler.ast.AddrOfNode import AddrOfNode
from MicroCCompiler.ast.MallocNode import MallocNode
from MicroCCompiler.ast.FreeNode import FreeNode



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2(")
        buf.write("\u0100\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\5\"\u00c4")
        buf.write("\n\"\3\"\3\"\3\"\7\"\u00c9\n\"\f\"\16\"\u00cc\13\"\3#")
        buf.write("\6#\u00cf\n#\r#\16#\u00d0\3$\7$\u00d4\n$\f$\16$\u00d7")
        buf.write("\13$\3$\3$\6$\u00db\n$\r$\16$\u00dc\3%\3%\7%\u00e1\n%")
        buf.write("\f%\16%\u00e4\13%\3%\3%\3&\3&\3&\3&\7&\u00ec\n&\f&\16")
        buf.write("&\u00ef\13&\3&\3&\3&\3&\3&\3\'\6\'\u00f7\n\'\r\'\16\'")
        buf.write("\u00f8\3\'\3\'\3(\3(\3)\3)\3\u00ed\2*\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O\2Q\2\3\2\5\3\2")
        buf.write("$$\5\2\13\f\17\17\"\"\4\2C\\c|\2\u0107\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\3S\3\2\2\2\5U\3\2\2\2\7\\\3\2\2\2\t^\3\2\2\2")
        buf.write("\13`\3\2\2\2\rd\3\2\2\2\17j\3\2\2\2\21o\3\2\2\2\23q\3")
        buf.write("\2\2\2\25s\3\2\2\2\27u\3\2\2\2\31w\3\2\2\2\33y\3\2\2\2")
        buf.write("\35~\3\2\2\2\37\u0084\3\2\2\2!\u008b\3\2\2\2#\u008e\3")
        buf.write("\2\2\2%\u0093\3\2\2\2\'\u0099\3\2\2\2)\u009b\3\2\2\2+")
        buf.write("\u009d\3\2\2\2-\u009f\3\2\2\2/\u00a1\3\2\2\2\61\u00a8")
        buf.write("\3\2\2\2\63\u00ad\3\2\2\2\65\u00af\3\2\2\2\67\u00b1\3")
        buf.write("\2\2\29\u00b3\3\2\2\2;\u00b6\3\2\2\2=\u00b9\3\2\2\2?\u00bc")
        buf.write("\3\2\2\2A\u00bf\3\2\2\2C\u00c3\3\2\2\2E\u00ce\3\2\2\2")
        buf.write("G\u00d5\3\2\2\2I\u00de\3\2\2\2K\u00e7\3\2\2\2M\u00f6\3")
        buf.write("\2\2\2O\u00fc\3\2\2\2Q\u00fe\3\2\2\2ST\7=\2\2T\4\3\2\2")
        buf.write("\2UV\7u\2\2VW\7v\2\2WX\7t\2\2XY\7k\2\2YZ\7p\2\2Z[\7i\2")
        buf.write("\2[\6\3\2\2\2\\]\7?\2\2]\b\3\2\2\2^_\7,\2\2_\n\3\2\2\2")
        buf.write("`a\7k\2\2ab\7p\2\2bc\7v\2\2c\f\3\2\2\2de\7h\2\2ef\7n\2")
        buf.write("\2fg\7q\2\2gh\7c\2\2hi\7v\2\2i\16\3\2\2\2jk\7x\2\2kl\7")
        buf.write("q\2\2lm\7k\2\2mn\7f\2\2n\20\3\2\2\2op\7*\2\2p\22\3\2\2")
        buf.write("\2qr\7+\2\2r\24\3\2\2\2st\7}\2\2t\26\3\2\2\2uv\7\177\2")
        buf.write("\2v\30\3\2\2\2wx\7.\2\2x\32\3\2\2\2yz\7t\2\2z{\7g\2\2")
        buf.write("{|\7c\2\2|}\7f\2\2}\34\3\2\2\2~\177\7r\2\2\177\u0080\7")
        buf.write("t\2\2\u0080\u0081\7k\2\2\u0081\u0082\7p\2\2\u0082\u0083")
        buf.write("\7v\2\2\u0083\36\3\2\2\2\u0084\u0085\7t\2\2\u0085\u0086")
        buf.write("\7g\2\2\u0086\u0087\7v\2\2\u0087\u0088\7w\2\2\u0088\u0089")
        buf.write("\7t\2\2\u0089\u008a\7p\2\2\u008a \3\2\2\2\u008b\u008c")
        buf.write("\7k\2\2\u008c\u008d\7h\2\2\u008d\"\3\2\2\2\u008e\u008f")
        buf.write("\7g\2\2\u008f\u0090\7n\2\2\u0090\u0091\7u\2\2\u0091\u0092")
        buf.write("\7g\2\2\u0092$\3\2\2\2\u0093\u0094\7y\2\2\u0094\u0095")
        buf.write("\7j\2\2\u0095\u0096\7k\2\2\u0096\u0097\7n\2\2\u0097\u0098")
        buf.write("\7g\2\2\u0098&\3\2\2\2\u0099\u009a\7/\2\2\u009a(\3\2\2")
        buf.write("\2\u009b\u009c\7(\2\2\u009c*\3\2\2\2\u009d\u009e\7]\2")
        buf.write("\2\u009e,\3\2\2\2\u009f\u00a0\7_\2\2\u00a0.\3\2\2\2\u00a1")
        buf.write("\u00a2\7o\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4\7n\2\2\u00a4")
        buf.write("\u00a5\7n\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7\7e\2\2\u00a7")
        buf.write("\60\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa\7t\2\2\u00aa")
        buf.write("\u00ab\7g\2\2\u00ab\u00ac\7g\2\2\u00ac\62\3\2\2\2\u00ad")
        buf.write("\u00ae\7-\2\2\u00ae\64\3\2\2\2\u00af\u00b0\7\61\2\2\u00b0")
        buf.write("\66\3\2\2\2\u00b1\u00b2\7>\2\2\u00b28\3\2\2\2\u00b3\u00b4")
        buf.write("\7>\2\2\u00b4\u00b5\7?\2\2\u00b5:\3\2\2\2\u00b6\u00b7")
        buf.write("\7@\2\2\u00b7\u00b8\7?\2\2\u00b8<\3\2\2\2\u00b9\u00ba")
        buf.write("\7?\2\2\u00ba\u00bb\7?\2\2\u00bb>\3\2\2\2\u00bc\u00bd")
        buf.write("\7#\2\2\u00bd\u00be\7?\2\2\u00be@\3\2\2\2\u00bf\u00c0")
        buf.write("\7@\2\2\u00c0B\3\2\2\2\u00c1\u00c4\5O(\2\u00c2\u00c4\7")
        buf.write("a\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\u00ca")
        buf.write("\3\2\2\2\u00c5\u00c9\5O(\2\u00c6\u00c9\5Q)\2\u00c7\u00c9")
        buf.write("\7a\2\2\u00c8\u00c5\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8")
        buf.write("\u00c7\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2")
        buf.write("\u00ca\u00cb\3\2\2\2\u00cbD\3\2\2\2\u00cc\u00ca\3\2\2")
        buf.write("\2\u00cd\u00cf\5Q)\2\u00ce\u00cd\3\2\2\2\u00cf\u00d0\3")
        buf.write("\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1F")
        buf.write("\3\2\2\2\u00d2\u00d4\5Q)\2\u00d3\u00d2\3\2\2\2\u00d4\u00d7")
        buf.write("\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6")
        buf.write("\u00d8\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00da\7\60\2")
        buf.write("\2\u00d9\u00db\5Q)\2\u00da\u00d9\3\2\2\2\u00db\u00dc\3")
        buf.write("\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00ddH")
        buf.write("\3\2\2\2\u00de\u00e2\7$\2\2\u00df\u00e1\n\2\2\2\u00e0")
        buf.write("\u00df\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2")
        buf.write("\u00e2\u00e3\3\2\2\2\u00e3\u00e5\3\2\2\2\u00e4\u00e2\3")
        buf.write("\2\2\2\u00e5\u00e6\7$\2\2\u00e6J\3\2\2\2\u00e7\u00e8\7")
        buf.write("\61\2\2\u00e8\u00e9\7,\2\2\u00e9\u00ed\3\2\2\2\u00ea\u00ec")
        buf.write("\13\2\2\2\u00eb\u00ea\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed")
        buf.write("\u00ee\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00f0\3\2\2\2")
        buf.write("\u00ef\u00ed\3\2\2\2\u00f0\u00f1\7,\2\2\u00f1\u00f2\7")
        buf.write("\61\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\b&\2\2\u00f4L")
        buf.write("\3\2\2\2\u00f5\u00f7\t\3\2\2\u00f6\u00f5\3\2\2\2\u00f7")
        buf.write("\u00f8\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f9\u00fa\3\2\2\2\u00fa\u00fb\b\'\2\2\u00fbN\3\2\2")
        buf.write("\2\u00fc\u00fd\t\4\2\2\u00fdP\3\2\2\2\u00fe\u00ff\4\62")
        buf.write(";\2\u00ffR\3\2\2\2\f\2\u00c3\u00c8\u00ca\u00d0\u00d5\u00dc")
        buf.write("\u00e2\u00ed\u00f8\3\b\2\2")
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
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    IDENTIFIER = 33
    INT_LITERAL = 34
    FLOAT_LITERAL = 35
    STR_LITERAL = 36
    COMMENT = 37
    WS = 38

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'string'", "'='", "'*'", "'int'", "'float'", "'void'", 
            "'('", "')'", "'{'", "'}'", "','", "'read'", "'print'", "'return'", 
            "'if'", "'else'", "'while'", "'-'", "'&'", "'['", "']'", "'malloc'", 
            "'free'", "'+'", "'/'", "'<'", "'<='", "'>='", "'=='", "'!='", 
            "'>'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "INT_LITERAL", "FLOAT_LITERAL", "STR_LITERAL", 
            "COMMENT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
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



