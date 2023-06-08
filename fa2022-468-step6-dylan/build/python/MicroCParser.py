# Generated from python/MicroC.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO



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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3(")
        buf.write("\u01da\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\3a\n\3\3\4\3\4\3\4\3\4\5\4")
        buf.write("g\n\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b~\n\b\f\b\16\b")
        buf.write("\u0081\13\b\3\t\3\t\3\t\3\t\5\t\u0087\n\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\5\n\u008e\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\5\f\u009d\n\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\5\16\u00b0\n\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u00b8\n\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\5\21\u00c3\n\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u00cf\n\22\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u00e0\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\5\26\u00f4\n\26\3\27\3\27\3\27\3\27\3\27\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\5\30\u0101\n\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u011a")
        buf.write("\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\5\33\u012b\n\33\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\5\34\u0145\n\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0157")
        buf.write("\n\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \7 \u0166")
        buf.write("\n \f \16 \u0169\13 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!")
        buf.write("\3!\3!\3!\3!\3!\3!\3!\5!\u017d\n!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\5\"\u0184\n\"\3#\3#\3#\3#\3#\3#\5#\u018c\n#\3$\3$\3$")
        buf.write("\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\7$\u019c\n$\f$\16$\u019f")
        buf.write("\13$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\7%\u01af")
        buf.write("\n%\f%\16%\u01b2\13%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&")
        buf.write("\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\5&\u01d2\n&\3\'\3\'\3(\3(\3)\3)\3)\2\6\16>FH*\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNP\2\5\3\2\35\"\4\2\6\6\34\34\4\2\25\25")
        buf.write("\33\33\2\u01dc\2R\3\2\2\2\4`\3\2\2\2\6f\3\2\2\2\bh\3\2")
        buf.write("\2\2\nj\3\2\2\2\fo\3\2\2\2\16v\3\2\2\2\20\u0086\3\2\2")
        buf.write("\2\22\u008d\3\2\2\2\24\u008f\3\2\2\2\26\u009c\3\2\2\2")
        buf.write("\30\u009e\3\2\2\2\32\u00af\3\2\2\2\34\u00b7\3\2\2\2\36")
        buf.write("\u00b9\3\2\2\2 \u00c2\3\2\2\2\"\u00ce\3\2\2\2$\u00df\3")
        buf.write("\2\2\2&\u00e1\3\2\2\2(\u00e7\3\2\2\2*\u00f3\3\2\2\2,\u00f5")
        buf.write("\3\2\2\2.\u0100\3\2\2\2\60\u0119\3\2\2\2\62\u011b\3\2")
        buf.write("\2\2\64\u012a\3\2\2\2\66\u0144\3\2\2\28\u0146\3\2\2\2")
        buf.write(":\u014a\3\2\2\2<\u0156\3\2\2\2>\u0158\3\2\2\2@\u017c\3")
        buf.write("\2\2\2B\u0183\3\2\2\2D\u018b\3\2\2\2F\u018d\3\2\2\2H\u01a0")
        buf.write("\3\2\2\2J\u01d1\3\2\2\2L\u01d3\3\2\2\2N\u01d5\3\2\2\2")
        buf.write("P\u01d7\3\2\2\2RS\5\4\3\2ST\5\26\f\2TU\b\2\1\2U\3\3\2")
        buf.write("\2\2VW\5\n\6\2WX\5\4\3\2Xa\3\2\2\2YZ\5\f\7\2Z[\5\4\3\2")
        buf.write("[a\3\2\2\2\\]\5\24\13\2]^\5\4\3\2^a\3\2\2\2_a\3\2\2\2")
        buf.write("`V\3\2\2\2`Y\3\2\2\2`\\\3\2\2\2`_\3\2\2\2a\5\3\2\2\2b")
        buf.write("c\5\n\6\2cd\5\6\4\2dg\3\2\2\2eg\3\2\2\2fb\3\2\2\2fe\3")
        buf.write("\2\2\2g\7\3\2\2\2hi\7#\2\2i\t\3\2\2\2jk\5\16\b\2kl\5\b")
        buf.write("\5\2lm\7\3\2\2mn\b\6\1\2n\13\3\2\2\2op\7\4\2\2pq\5\b\5")
        buf.write("\2qr\7\5\2\2rs\7&\2\2st\7\3\2\2tu\b\7\1\2u\r\3\2\2\2v")
        buf.write("w\b\b\1\2wx\5\20\t\2xy\b\b\1\2y\177\3\2\2\2z{\f\3\2\2")
        buf.write("{|\7\6\2\2|~\b\b\1\2}z\3\2\2\2~\u0081\3\2\2\2\177}\3\2")
        buf.write("\2\2\177\u0080\3\2\2\2\u0080\17\3\2\2\2\u0081\177\3\2")
        buf.write("\2\2\u0082\u0083\7\7\2\2\u0083\u0087\b\t\1\2\u0084\u0085")
        buf.write("\7\b\2\2\u0085\u0087\b\t\1\2\u0086\u0082\3\2\2\2\u0086")
        buf.write("\u0084\3\2\2\2\u0087\21\3\2\2\2\u0088\u0089\5\16\b\2\u0089")
        buf.write("\u008a\b\n\1\2\u008a\u008e\3\2\2\2\u008b\u008c\7\t\2\2")
        buf.write("\u008c\u008e\b\n\1\2\u008d\u0088\3\2\2\2\u008d\u008b\3")
        buf.write("\2\2\2\u008e\23\3\2\2\2\u008f\u0090\5\22\n\2\u0090\u0091")
        buf.write("\5\b\5\2\u0091\u0092\7\n\2\2\u0092\u0093\5\32\16\2\u0093")
        buf.write("\u0094\7\13\2\2\u0094\u0095\7\3\2\2\u0095\u0096\b\13\1")
        buf.write("\2\u0096\25\3\2\2\2\u0097\u0098\5\30\r\2\u0098\u0099\5")
        buf.write("\26\f\2\u0099\u009a\b\f\1\2\u009a\u009d\3\2\2\2\u009b")
        buf.write("\u009d\b\f\1\2\u009c\u0097\3\2\2\2\u009c\u009b\3\2\2\2")
        buf.write("\u009d\27\3\2\2\2\u009e\u009f\5\22\n\2\u009f\u00a0\5\b")
        buf.write("\5\2\u00a0\u00a1\7\n\2\2\u00a1\u00a2\5\32\16\2\u00a2\u00a3")
        buf.write("\7\13\2\2\u00a3\u00a4\b\r\1\2\u00a4\u00a5\7\f\2\2\u00a5")
        buf.write("\u00a6\5\6\4\2\u00a6\u00a7\5 \21\2\u00a7\u00a8\7\r\2\2")
        buf.write("\u00a8\u00a9\b\r\1\2\u00a9\31\3\2\2\2\u00aa\u00ab\5\36")
        buf.write("\20\2\u00ab\u00ac\5\34\17\2\u00ac\u00ad\b\16\1\2\u00ad")
        buf.write("\u00b0\3\2\2\2\u00ae\u00b0\b\16\1\2\u00af\u00aa\3\2\2")
        buf.write("\2\u00af\u00ae\3\2\2\2\u00b0\33\3\2\2\2\u00b1\u00b2\7")
        buf.write("\16\2\2\u00b2\u00b3\5\36\20\2\u00b3\u00b4\5\34\17\2\u00b4")
        buf.write("\u00b5\b\17\1\2\u00b5\u00b8\3\2\2\2\u00b6\u00b8\b\17\1")
        buf.write("\2\u00b7\u00b1\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\35\3")
        buf.write("\2\2\2\u00b9\u00ba\5\16\b\2\u00ba\u00bb\5\b\5\2\u00bb")
        buf.write("\u00bc\b\20\1\2\u00bc\37\3\2\2\2\u00bd\u00be\5\"\22\2")
        buf.write("\u00be\u00bf\5 \21\2\u00bf\u00c0\b\21\1\2\u00c0\u00c3")
        buf.write("\3\2\2\2\u00c1\u00c3\b\21\1\2\u00c2\u00bd\3\2\2\2\u00c2")
        buf.write("\u00c1\3\2\2\2\u00c3!\3\2\2\2\u00c4\u00c5\5$\23\2\u00c5")
        buf.write("\u00c6\7\3\2\2\u00c6\u00c7\b\22\1\2\u00c7\u00cf\3\2\2")
        buf.write("\2\u00c8\u00c9\5\60\31\2\u00c9\u00ca\b\22\1\2\u00ca\u00cf")
        buf.write("\3\2\2\2\u00cb\u00cc\5\62\32\2\u00cc\u00cd\b\22\1\2\u00cd")
        buf.write("\u00cf\3\2\2\2\u00ce\u00c4\3\2\2\2\u00ce\u00c8\3\2\2\2")
        buf.write("\u00ce\u00cb\3\2\2\2\u00cf#\3\2\2\2\u00d0\u00d1\5,\27")
        buf.write("\2\u00d1\u00d2\b\23\1\2\u00d2\u00e0\3\2\2\2\u00d3\u00d4")
        buf.write("\5&\24\2\u00d4\u00d5\b\23\1\2\u00d5\u00e0\3\2\2\2\u00d6")
        buf.write("\u00d7\5(\25\2\u00d7\u00d8\b\23\1\2\u00d8\u00e0\3\2\2")
        buf.write("\2\u00d9\u00da\5*\26\2\u00da\u00db\b\23\1\2\u00db\u00e0")
        buf.write("\3\2\2\2\u00dc\u00dd\5@!\2\u00dd\u00de\b\23\1\2\u00de")
        buf.write("\u00e0\3\2\2\2\u00df\u00d0\3\2\2\2\u00df\u00d3\3\2\2\2")
        buf.write("\u00df\u00d6\3\2\2\2\u00df\u00d9\3\2\2\2\u00df\u00dc\3")
        buf.write("\2\2\2\u00e0%\3\2\2\2\u00e1\u00e2\7\17\2\2\u00e2\u00e3")
        buf.write("\7\n\2\2\u00e3\u00e4\5\b\5\2\u00e4\u00e5\7\13\2\2\u00e5")
        buf.write("\u00e6\b\24\1\2\u00e6\'\3\2\2\2\u00e7\u00e8\7\20\2\2\u00e8")
        buf.write("\u00e9\7\n\2\2\u00e9\u00ea\5F$\2\u00ea\u00eb\7\13\2\2")
        buf.write("\u00eb\u00ec\b\25\1\2\u00ec)\3\2\2\2\u00ed\u00ee\7\21")
        buf.write("\2\2\u00ee\u00ef\5F$\2\u00ef\u00f0\b\26\1\2\u00f0\u00f4")
        buf.write("\3\2\2\2\u00f1\u00f2\7\21\2\2\u00f2\u00f4\b\26\1\2\u00f3")
        buf.write("\u00ed\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4+\3\2\2\2\u00f5")
        buf.write("\u00f6\5.\30\2\u00f6\u00f7\7\5\2\2\u00f7\u00f8\5F$\2\u00f8")
        buf.write("\u00f9\b\27\1\2\u00f9-\3\2\2\2\u00fa\u00fb\5\64\33\2\u00fb")
        buf.write("\u00fc\b\30\1\2\u00fc\u0101\3\2\2\2\u00fd\u00fe\5> \2")
        buf.write("\u00fe\u00ff\b\30\1\2\u00ff\u0101\3\2\2\2\u0100\u00fa")
        buf.write("\3\2\2\2\u0100\u00fd\3\2\2\2\u0101/\3\2\2\2\u0102\u0103")
        buf.write("\7\22\2\2\u0103\u0104\7\n\2\2\u0104\u0105\5J&\2\u0105")
        buf.write("\u0106\7\13\2\2\u0106\u0107\7\f\2\2\u0107\u0108\5 \21")
        buf.write("\2\u0108\u0109\7\r\2\2\u0109\u010a\7\23\2\2\u010a\u010b")
        buf.write("\7\f\2\2\u010b\u010c\5 \21\2\u010c\u010d\7\r\2\2\u010d")
        buf.write("\u010e\3\2\2\2\u010e\u010f\b\31\1\2\u010f\u011a\3\2\2")
        buf.write("\2\u0110\u0111\7\22\2\2\u0111\u0112\7\n\2\2\u0112\u0113")
        buf.write("\5J&\2\u0113\u0114\7\13\2\2\u0114\u0115\7\f\2\2\u0115")
        buf.write("\u0116\5 \21\2\u0116\u0117\7\r\2\2\u0117\u0118\b\31\1")
        buf.write("\2\u0118\u011a\3\2\2\2\u0119\u0102\3\2\2\2\u0119\u0110")
        buf.write("\3\2\2\2\u011a\61\3\2\2\2\u011b\u011c\7\24\2\2\u011c\u011d")
        buf.write("\7\n\2\2\u011d\u011e\5J&\2\u011e\u011f\7\13\2\2\u011f")
        buf.write("\u0120\7\f\2\2\u0120\u0121\5 \21\2\u0121\u0122\7\r\2\2")
        buf.write("\u0122\u0123\b\32\1\2\u0123\63\3\2\2\2\u0124\u0125\5\b")
        buf.write("\5\2\u0125\u0126\b\33\1\2\u0126\u012b\3\2\2\2\u0127\u0128")
        buf.write("\5:\36\2\u0128\u0129\b\33\1\2\u0129\u012b\3\2\2\2\u012a")
        buf.write("\u0124\3\2\2\2\u012a\u0127\3\2\2\2\u012b\65\3\2\2\2\u012c")
        buf.write("\u012d\5\64\33\2\u012d\u012e\b\34\1\2\u012e\u0145\3\2")
        buf.write("\2\2\u012f\u0130\5<\37\2\u0130\u0131\b\34\1\2\u0131\u0145")
        buf.write("\3\2\2\2\u0132\u0133\7\n\2\2\u0133\u0134\5F$\2\u0134\u0135")
        buf.write("\7\13\2\2\u0135\u0136\b\34\1\2\u0136\u0145\3\2\2\2\u0137")
        buf.write("\u0138\58\35\2\u0138\u0139\b\34\1\2\u0139\u0145\3\2\2")
        buf.write("\2\u013a\u013b\5@!\2\u013b\u013c\b\34\1\2\u013c\u0145")
        buf.write("\3\2\2\2\u013d\u013e\5> \2\u013e\u013f\b\34\1\2\u013f")
        buf.write("\u0145\3\2\2\2\u0140\u0141\7$\2\2\u0141\u0145\b\34\1\2")
        buf.write("\u0142\u0143\7%\2\2\u0143\u0145\b\34\1\2\u0144\u012c\3")
        buf.write("\2\2\2\u0144\u012f\3\2\2\2\u0144\u0132\3\2\2\2\u0144\u0137")
        buf.write("\3\2\2\2\u0144\u013a\3\2\2\2\u0144\u013d\3\2\2\2\u0144")
        buf.write("\u0140\3\2\2\2\u0144\u0142\3\2\2\2\u0145\67\3\2\2\2\u0146")
        buf.write("\u0147\7\25\2\2\u0147\u0148\5F$\2\u0148\u0149\b\35\1\2")
        buf.write("\u01499\3\2\2\2\u014a\u014b\7\6\2\2\u014b\u014c\5\66\34")
        buf.write("\2\u014c\u014d\b\36\1\2\u014d;\3\2\2\2\u014e\u014f\7\26")
        buf.write("\2\2\u014f\u0150\5\64\33\2\u0150\u0151\b\37\1\2\u0151")
        buf.write("\u0157\3\2\2\2\u0152\u0153\7\26\2\2\u0153\u0154\5> \2")
        buf.write("\u0154\u0155\b\37\1\2\u0155\u0157\3\2\2\2\u0156\u014e")
        buf.write("\3\2\2\2\u0156\u0152\3\2\2\2\u0157=\3\2\2\2\u0158\u0159")
        buf.write("\b \1\2\u0159\u015a\5\64\33\2\u015a\u015b\7\27\2\2\u015b")
        buf.write("\u015c\5F$\2\u015c\u015d\7\30\2\2\u015d\u015e\b \1\2\u015e")
        buf.write("\u0167\3\2\2\2\u015f\u0160\f\3\2\2\u0160\u0161\7\27\2")
        buf.write("\2\u0161\u0162\5F$\2\u0162\u0163\7\30\2\2\u0163\u0164")
        buf.write("\b \1\2\u0164\u0166\3\2\2\2\u0165\u015f\3\2\2\2\u0166")
        buf.write("\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2")
        buf.write("\u0168?\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016b\7\31\2")
        buf.write("\2\u016b\u016c\7\n\2\2\u016c\u016d\5F$\2\u016d\u016e\7")
        buf.write("\13\2\2\u016e\u016f\b!\1\2\u016f\u017d\3\2\2\2\u0170\u0171")
        buf.write("\7\32\2\2\u0171\u0172\7\n\2\2\u0172\u0173\5F$\2\u0173")
        buf.write("\u0174\7\13\2\2\u0174\u0175\b!\1\2\u0175\u017d\3\2\2\2")
        buf.write("\u0176\u0177\5\b\5\2\u0177\u0178\7\n\2\2\u0178\u0179\5")
        buf.write("B\"\2\u0179\u017a\7\13\2\2\u017a\u017b\b!\1\2\u017b\u017d")
        buf.write("\3\2\2\2\u017c\u016a\3\2\2\2\u017c\u0170\3\2\2\2\u017c")
        buf.write("\u0176\3\2\2\2\u017dA\3\2\2\2\u017e\u017f\5F$\2\u017f")
        buf.write("\u0180\5D#\2\u0180\u0181\b\"\1\2\u0181\u0184\3\2\2\2\u0182")
        buf.write("\u0184\b\"\1\2\u0183\u017e\3\2\2\2\u0183\u0182\3\2\2\2")
        buf.write("\u0184C\3\2\2\2\u0185\u0186\7\16\2\2\u0186\u0187\5F$\2")
        buf.write("\u0187\u0188\5D#\2\u0188\u0189\b#\1\2\u0189\u018c\3\2")
        buf.write("\2\2\u018a\u018c\b#\1\2\u018b\u0185\3\2\2\2\u018b\u018a")
        buf.write("\3\2\2\2\u018cE\3\2\2\2\u018d\u018e\b$\1\2\u018e\u018f")
        buf.write("\5H%\2\u018f\u0190\b$\1\2\u0190\u019d\3\2\2\2\u0191\u0192")
        buf.write("\f\4\2\2\u0192\u0193\7\33\2\2\u0193\u0194\5H%\2\u0194")
        buf.write("\u0195\b$\1\2\u0195\u019c\3\2\2\2\u0196\u0197\f\3\2\2")
        buf.write("\u0197\u0198\7\25\2\2\u0198\u0199\5H%\2\u0199\u019a\b")
        buf.write("$\1\2\u019a\u019c\3\2\2\2\u019b\u0191\3\2\2\2\u019b\u0196")
        buf.write("\3\2\2\2\u019c\u019f\3\2\2\2\u019d\u019b\3\2\2\2\u019d")
        buf.write("\u019e\3\2\2\2\u019eG\3\2\2\2\u019f\u019d\3\2\2\2\u01a0")
        buf.write("\u01a1\b%\1\2\u01a1\u01a2\5\66\34\2\u01a2\u01a3\b%\1\2")
        buf.write("\u01a3\u01b0\3\2\2\2\u01a4\u01a5\f\4\2\2\u01a5\u01a6\7")
        buf.write("\6\2\2\u01a6\u01a7\5\66\34\2\u01a7\u01a8\b%\1\2\u01a8")
        buf.write("\u01af\3\2\2\2\u01a9\u01aa\f\3\2\2\u01aa\u01ab\7\34\2")
        buf.write("\2\u01ab\u01ac\5\66\34\2\u01ac\u01ad\b%\1\2\u01ad\u01af")
        buf.write("\3\2\2\2\u01ae\u01a4\3\2\2\2\u01ae\u01a9\3\2\2\2\u01af")
        buf.write("\u01b2\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2")
        buf.write("\u01b1I\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b3\u01b4\5F$\2")
        buf.write("\u01b4\u01b5\7\35\2\2\u01b5\u01b6\5F$\2\u01b6\u01b7\b")
        buf.write("&\1\2\u01b7\u01d2\3\2\2\2\u01b8\u01b9\5F$\2\u01b9\u01ba")
        buf.write("\7\36\2\2\u01ba\u01bb\5F$\2\u01bb\u01bc\b&\1\2\u01bc\u01d2")
        buf.write("\3\2\2\2\u01bd\u01be\5F$\2\u01be\u01bf\7\37\2\2\u01bf")
        buf.write("\u01c0\5F$\2\u01c0\u01c1\b&\1\2\u01c1\u01d2\3\2\2\2\u01c2")
        buf.write("\u01c3\5F$\2\u01c3\u01c4\7 \2\2\u01c4\u01c5\5F$\2\u01c5")
        buf.write("\u01c6\b&\1\2\u01c6\u01d2\3\2\2\2\u01c7\u01c8\5F$\2\u01c8")
        buf.write("\u01c9\7!\2\2\u01c9\u01ca\5F$\2\u01ca\u01cb\b&\1\2\u01cb")
        buf.write("\u01d2\3\2\2\2\u01cc\u01cd\5F$\2\u01cd\u01ce\7\"\2\2\u01ce")
        buf.write("\u01cf\5F$\2\u01cf\u01d0\b&\1\2\u01d0\u01d2\3\2\2\2\u01d1")
        buf.write("\u01b3\3\2\2\2\u01d1\u01b8\3\2\2\2\u01d1\u01bd\3\2\2\2")
        buf.write("\u01d1\u01c2\3\2\2\2\u01d1\u01c7\3\2\2\2\u01d1\u01cc\3")
        buf.write("\2\2\2\u01d2K\3\2\2\2\u01d3\u01d4\t\2\2\2\u01d4M\3\2\2")
        buf.write("\2\u01d5\u01d6\t\3\2\2\u01d6O\3\2\2\2\u01d7\u01d8\t\4")
        buf.write("\2\2\u01d8Q\3\2\2\2\34`f\177\u0086\u008d\u009c\u00af\u00b7")
        buf.write("\u00c2\u00ce\u00df\u00f3\u0100\u0119\u012a\u0144\u0156")
        buf.write("\u0167\u017c\u0183\u018b\u019b\u019d\u01ae\u01b0\u01d1")
        return buf.getvalue()


class MicroCParser ( Parser ):

    grammarFileName = "MicroC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'string'", "'='", "'*'", "'int'", 
                     "'float'", "'void'", "'('", "')'", "'{'", "'}'", "','", 
                     "'read'", "'print'", "'return'", "'if'", "'else'", 
                     "'while'", "'-'", "'&'", "'['", "']'", "'malloc'", 
                     "'free'", "'+'", "'/'", "'<'", "'<='", "'>='", "'=='", 
                     "'!='", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IDENTIFIER", "INT_LITERAL", "FLOAT_LITERAL", 
                      "STR_LITERAL", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_var_decls = 2
    RULE_ident = 3
    RULE_var_decl = 4
    RULE_str_decl = 5
    RULE_true_type = 6
    RULE_base_type = 7
    RULE_func_type = 8
    RULE_func_decl = 9
    RULE_functions = 10
    RULE_function = 11
    RULE_params = 12
    RULE_params_rest = 13
    RULE_param = 14
    RULE_statements = 15
    RULE_statement = 16
    RULE_base_stmt = 17
    RULE_read_stmt = 18
    RULE_print_stmt = 19
    RULE_return_stmt = 20
    RULE_assign_stmt = 21
    RULE_lhs = 22
    RULE_if_stmt = 23
    RULE_while_stmt = 24
    RULE_lval = 25
    RULE_primary = 26
    RULE_unaryminus_expr = 27
    RULE_ptr_expr = 28
    RULE_addr_of_expr = 29
    RULE_array_expr = 30
    RULE_call_expr = 31
    RULE_arg_list = 32
    RULE_args_rest = 33
    RULE_expr = 34
    RULE_term = 35
    RULE_cond = 36
    RULE_cmpop = 37
    RULE_mulop = 38
    RULE_addop = 39

    ruleNames =  [ "program", "decls", "var_decls", "ident", "var_decl", 
                   "str_decl", "true_type", "base_type", "func_type", "func_decl", 
                   "functions", "function", "params", "params_rest", "param", 
                   "statements", "statement", "base_stmt", "read_stmt", 
                   "print_stmt", "return_stmt", "assign_stmt", "lhs", "if_stmt", 
                   "while_stmt", "lval", "primary", "unaryminus_expr", "ptr_expr", 
                   "addr_of_expr", "array_expr", "call_expr", "arg_list", 
                   "args_rest", "expr", "term", "cond", "cmpop", "mulop", 
                   "addop" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    IDENTIFIER=33
    INT_LITERAL=34
    FLOAT_LITERAL=35
    STR_LITERAL=36
    COMMENT=37
    WS=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
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




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._functions = None # FunctionsContext

        def decls(self):
            return self.getTypedRuleContext(MicroCParser.DeclsContext,0)


        def functions(self):
            return self.getTypedRuleContext(MicroCParser.FunctionsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MicroCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.decls()
            self.state = 81
            localctx._functions = self.functions()
            self.setAST(localctx._functions.node);
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MicroCParser.Var_declContext,0)


        def decls(self):
            return self.getTypedRuleContext(MicroCParser.DeclsContext,0)


        def str_decl(self):
            return self.getTypedRuleContext(MicroCParser.Str_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MicroCParser.Func_declContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_decls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecls" ):
                listener.enterDecls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecls" ):
                listener.exitDecls(self)




    def decls(self):

        localctx = MicroCParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.var_decl()
                self.state = 85
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.str_decl()
                self.state = 88
                self.decls()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.func_decl()
                self.state = 91
                self.decls()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MicroCParser.Var_declContext,0)


        def var_decls(self):
            return self.getTypedRuleContext(MicroCParser.Var_declsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_var_decls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decls" ):
                listener.enterVar_decls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decls" ):
                listener.exitVar_decls(self)




    def var_decls(self):

        localctx = MicroCParser.Var_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_decls)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__4, MicroCParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.var_decl()
                self.state = 97
                self.var_decls()
                pass
            elif token in [MicroCParser.T__3, MicroCParser.T__10, MicroCParser.T__12, MicroCParser.T__13, MicroCParser.T__14, MicroCParser.T__15, MicroCParser.T__17, MicroCParser.T__22, MicroCParser.T__23, MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MicroCParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MicroCParser.RULE_ident

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent" ):
                listener.enterIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent" ):
                listener.exitIdent(self)




    def ident(self):

        localctx = MicroCParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ident)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(MicroCParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._true_type = None # True_typeContext
            self._ident = None # IdentContext

        def true_type(self):
            return self.getTypedRuleContext(MicroCParser.True_typeContext,0)


        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)




    def var_decl(self):

        localctx = MicroCParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            localctx._true_type = self.true_type(0)
            self.state = 105
            localctx._ident = self.ident()
            self.state = 106
            self.match(MicroCParser.T__0)
            self.st.addVariable(localctx._true_type.t, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Str_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ident = None # IdentContext
            self.val = None # Token

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def STR_LITERAL(self):
            return self.getToken(MicroCParser.STR_LITERAL, 0)

        def getRuleIndex(self):
            return MicroCParser.RULE_str_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr_decl" ):
                listener.enterStr_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr_decl" ):
                listener.exitStr_decl(self)




    def str_decl(self):

        localctx = MicroCParser.Str_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_str_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(MicroCParser.T__1)
            self.state = 110
            localctx._ident = self.ident()
            self.state = 111
            self.match(MicroCParser.T__2)
            self.state = 112
            localctx.val = self.match(MicroCParser.STR_LITERAL)
            self.state = 113
            self.match(MicroCParser.T__0)
            self.st.addVariable(Scope.Type(Scope.InnerType.STRING), (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), (None if localctx.val is None else localctx.val.text));
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class True_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t = None
            self.t1 = None # True_typeContext
            self._base_type = None # Base_typeContext

        def base_type(self):
            return self.getTypedRuleContext(MicroCParser.Base_typeContext,0)


        def true_type(self):
            return self.getTypedRuleContext(MicroCParser.True_typeContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_true_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrue_type" ):
                listener.enterTrue_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrue_type" ):
                listener.exitTrue_type(self)



    def true_type(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MicroCParser.True_typeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_true_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            localctx._base_type = self.base_type()
            localctx.t =  localctx._base_type.t
            self._ctx.stop = self._input.LT(-1)
            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MicroCParser.True_typeContext(self, _parentctx, _parentState)
                    localctx.t1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_true_type)
                    self.state = 120
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 121
                    self.match(MicroCParser.T__3)
                    localctx.t =  Scope.Type.pointerToType(localctx.t1.t) 
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Base_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t = None


        def getRuleIndex(self):
            return MicroCParser.RULE_base_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_type" ):
                listener.enterBase_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_type" ):
                listener.exitBase_type(self)




    def base_type(self):

        localctx = MicroCParser.Base_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_base_type)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(MicroCParser.T__4)
                localctx.t =  Scope.Type(Scope.InnerType.INT)
                pass
            elif token in [MicroCParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.match(MicroCParser.T__5)
                localctx.t =  Scope.Type(Scope.InnerType.FLOAT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t = None
            self._true_type = None # True_typeContext

        def true_type(self):
            return self.getTypedRuleContext(MicroCParser.True_typeContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_func_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_type" ):
                listener.enterFunc_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_type" ):
                listener.exitFunc_type(self)




    def func_type(self):

        localctx = MicroCParser.Func_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_type)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__4, MicroCParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                localctx._true_type = self.true_type(0)
                localctx.t =  localctx._true_type.t
                pass
            elif token in [MicroCParser.T__6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(MicroCParser.T__6)
                localctx.t =  Scope.Type(Scope.InnerType.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._func_type = None # Func_typeContext
            self._ident = None # IdentContext
            self._params = None # ParamsContext

        def func_type(self):
            return self.getTypedRuleContext(MicroCParser.Func_typeContext,0)


        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def params(self):
            return self.getTypedRuleContext(MicroCParser.ParamsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_func_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_decl" ):
                listener.enterFunc_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_decl" ):
                listener.exitFunc_decl(self)




    def func_decl(self):

        localctx = MicroCParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            localctx._func_type = self.func_type()
            self.state = 142
            localctx._ident = self.ident()
            self.state = 143
            self.match(MicroCParser.T__7)
            self.state = 144
            localctx._params = self.params()
            self.state = 145
            self.match(MicroCParser.T__8)
            self.state = 146
            self.match(MicroCParser.T__0)
            self.st.addFunction(localctx._func_type.t, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), localctx._params.types);
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._function = None # FunctionContext
            self._functions = None # FunctionsContext

        def function(self):
            return self.getTypedRuleContext(MicroCParser.FunctionContext,0)


        def functions(self):
            return self.getTypedRuleContext(MicroCParser.FunctionsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_functions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctions" ):
                listener.enterFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctions" ):
                listener.exitFunctions(self)




    def functions(self):

        localctx = MicroCParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_functions)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__4, MicroCParser.T__5, MicroCParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                localctx._function = self.function()
                self.state = 150
                localctx._functions = self.functions()
                localctx.node =  FunctionListNode(localctx._function.node, localctx._functions.node)
                pass
            elif token in [MicroCParser.EOF]:
                self.enterOuterAlt(localctx, 2)
                localctx.node =  FunctionListNode()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._func_type = None # Func_typeContext
            self._ident = None # IdentContext
            self._params = None # ParamsContext
            self._statements = None # StatementsContext

        def func_type(self):
            return self.getTypedRuleContext(MicroCParser.Func_typeContext,0)


        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def params(self):
            return self.getTypedRuleContext(MicroCParser.ParamsContext,0)


        def var_decls(self):
            return self.getTypedRuleContext(MicroCParser.Var_declsContext,0)


        def statements(self):
            return self.getTypedRuleContext(MicroCParser.StatementsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = MicroCParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            localctx._func_type = self.func_type()
            self.state = 157
            localctx._ident = self.ident()
            self.state = 158
            self.match(MicroCParser.T__7)
            self.state = 159
            localctx._params = self.params()
            self.state = 160
            self.match(MicroCParser.T__8)

            # Add FunctionSymbolTable entry to global scope
            ste = self.st.getSymbolTableEntry((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
            if ste is None or not ste.isDefined():
              self.st.addFunction(localctx._func_type.t, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), localctx._params.types);          
              ste = self.st.getSymbolTableEntry((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
              ste.setDefined(True);
            else:
              raise Exception("Function already defined");
            self.st.pushScope((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
            self.addParams(localctx._params.types, localctx._params.names);

            self.state = 162
            self.match(MicroCParser.T__9)
            self.state = 163
            self.var_decls()
            self.state = 164
            localctx._statements = self.statements()
            self.state = 165
            self.match(MicroCParser.T__10)

            # Create FunctionNode
            funcScope = self.st.currentScope();
            localctx.node =  FunctionNode(localctx._statements.node, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), funcScope)

            # Done with this scope, so pop the scope
            self.st.popScope();

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.names = None
            self.types = None
            self._param = None # ParamContext
            self._params_rest = None # Params_restContext

        def param(self):
            return self.getTypedRuleContext(MicroCParser.ParamContext,0)


        def params_rest(self):
            return self.getTypedRuleContext(MicroCParser.Params_restContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = MicroCParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_params)
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__4, MicroCParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                localctx._param = self.param()
                self.state = 169
                localctx._params_rest = self.params_rest()

                localctx.names =  []
                localctx.types =  []
                localctx.names.append(localctx._param.name);
                localctx.names.extend(localctx._params_rest.names);
                localctx.types.append(localctx._param.param_type);
                localctx.types.extend(localctx._params_rest.types);

                pass
            elif token in [MicroCParser.T__8]:
                self.enterOuterAlt(localctx, 2)

                localctx.names =  []
                localctx.types =  []

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.names = None
            self.types = None
            self._param = None # ParamContext
            self._params_rest = None # Params_restContext

        def param(self):
            return self.getTypedRuleContext(MicroCParser.ParamContext,0)


        def params_rest(self):
            return self.getTypedRuleContext(MicroCParser.Params_restContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_params_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams_rest" ):
                listener.enterParams_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams_rest" ):
                listener.exitParams_rest(self)




    def params_rest(self):

        localctx = MicroCParser.Params_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_params_rest)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(MicroCParser.T__11)
                self.state = 176
                localctx._param = self.param()
                self.state = 177
                localctx._params_rest = self.params_rest()

                localctx.names =  []
                localctx.types =  []
                localctx.names.append(localctx._param.name);
                localctx.names.extend(localctx._params_rest.names);
                localctx.types.append(localctx._param.param_type);
                localctx.types.extend(localctx._params_rest.types);

                pass
            elif token in [MicroCParser.T__8]:
                self.enterOuterAlt(localctx, 2)

                localctx.names =  []
                localctx.types =  []

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None
            self.param_type = None
            self._true_type = None # True_typeContext
            self._ident = None # IdentContext

        def true_type(self):
            return self.getTypedRuleContext(MicroCParser.True_typeContext,0)


        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = MicroCParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            localctx._true_type = self.true_type(0)
            self.state = 184
            localctx._ident = self.ident()

            localctx.name =  (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop))
            localctx.param_type =  localctx._true_type.t

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._statement = None # StatementContext
            self.s = None # StatementsContext

        def statement(self):
            return self.getTypedRuleContext(MicroCParser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(MicroCParser.StatementsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = MicroCParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statements)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__3, MicroCParser.T__12, MicroCParser.T__13, MicroCParser.T__14, MicroCParser.T__15, MicroCParser.T__17, MicroCParser.T__22, MicroCParser.T__23, MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                localctx._statement = self.statement()
                self.state = 188
                localctx.s = self.statements()
                localctx.node =  StatementListNode(localctx._statement.node, localctx.s.node.getStatements())
                pass
            elif token in [MicroCParser.T__10]:
                self.enterOuterAlt(localctx, 2)
                localctx.node =  StatementListNode()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._base_stmt = None # Base_stmtContext
            self._if_stmt = None # If_stmtContext
            self._while_stmt = None # While_stmtContext

        def base_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Base_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MicroCParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(MicroCParser.While_stmtContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MicroCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_statement)
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__3, MicroCParser.T__12, MicroCParser.T__13, MicroCParser.T__14, MicroCParser.T__22, MicroCParser.T__23, MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                localctx._base_stmt = self.base_stmt()
                self.state = 195
                self.match(MicroCParser.T__0)
                localctx.node =  localctx._base_stmt.node
                pass
            elif token in [MicroCParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                localctx._if_stmt = self.if_stmt()
                localctx.node = localctx._if_stmt.node
                pass
            elif token in [MicroCParser.T__17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 201
                localctx._while_stmt = self.while_stmt()
                localctx.node = localctx._while_stmt.node
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Base_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._assign_stmt = None # Assign_stmtContext
            self._read_stmt = None # Read_stmtContext
            self._print_stmt = None # Print_stmtContext
            self._return_stmt = None # Return_stmtContext
            self._call_expr = None # Call_exprContext

        def assign_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Assign_stmtContext,0)


        def read_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Read_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Print_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Return_stmtContext,0)


        def call_expr(self):
            return self.getTypedRuleContext(MicroCParser.Call_exprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_base_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_stmt" ):
                listener.enterBase_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_stmt" ):
                listener.exitBase_stmt(self)




    def base_stmt(self):

        localctx = MicroCParser.Base_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_base_stmt)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                localctx._assign_stmt = self.assign_stmt()
                localctx.node =  localctx._assign_stmt.node
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                localctx._read_stmt = self.read_stmt()
                localctx.node =  localctx._read_stmt.node
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 212
                localctx._print_stmt = self.print_stmt()
                localctx.node =  localctx._print_stmt.node
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 215
                localctx._return_stmt = self.return_stmt()
                localctx.node =  localctx._return_stmt.node
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 218
                localctx._call_expr = self.call_expr()
                localctx.node =  localctx._call_expr.node
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._ident = None # IdentContext

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_read_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead_stmt" ):
                listener.enterRead_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead_stmt" ):
                listener.exitRead_stmt(self)




    def read_stmt(self):

        localctx = MicroCParser.Read_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_read_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(MicroCParser.T__12)
            self.state = 224
            self.match(MicroCParser.T__7)
            self.state = 225
            localctx._ident = self.ident()
            self.state = 226
            self.match(MicroCParser.T__8)
            localctx.node =  ReadNode(VarNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop))))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)




    def print_stmt(self):

        localctx = MicroCParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_print_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(MicroCParser.T__13)
            self.state = 230
            self.match(MicroCParser.T__7)
            self.state = 231
            localctx._expr = self.expr(0)
            self.state = 232
            self.match(MicroCParser.T__8)
            localctx.node =  WriteNode(localctx._expr.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)




    def return_stmt(self):

        localctx = MicroCParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_return_stmt)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(MicroCParser.T__14)
                self.state = 236
                localctx._expr = self.expr(0)
                localctx.node =  ReturnNode(localctx._expr.node, self.st.getFunctionSymbol(self.st.currentScope().getName()))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(MicroCParser.T__14)
                localctx.node =  ReturnNode(None, self.st.getFunctionSymbol(self.st.currentScope().getName()))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._lhs = None # LhsContext
            self._expr = None # ExprContext

        def lhs(self):
            return self.getTypedRuleContext(MicroCParser.LhsContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_assign_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_stmt" ):
                listener.enterAssign_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_stmt" ):
                listener.exitAssign_stmt(self)




    def assign_stmt(self):

        localctx = MicroCParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            localctx._lhs = self.lhs()
            self.state = 244
            self.match(MicroCParser.T__2)
            self.state = 245
            localctx._expr = self.expr(0)
            localctx.node =  AssignNode(localctx._lhs.node, localctx._expr.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._lval = None # LvalContext
            self._array_expr = None # Array_exprContext

        def lval(self):
            return self.getTypedRuleContext(MicroCParser.LvalContext,0)


        def array_expr(self):
            return self.getTypedRuleContext(MicroCParser.Array_exprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_lhs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLhs" ):
                listener.enterLhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLhs" ):
                listener.exitLhs(self)




    def lhs(self):

        localctx = MicroCParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_lhs)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                localctx._lval = self.lval()
                localctx.node =  localctx._lval.node
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                localctx._array_expr = self.array_expr(0)
                localctx.node =  localctx._array_expr.node
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._cond = None # CondContext
            self.t1 = None # StatementsContext
            self.e1 = None # StatementsContext

        def cond(self):
            return self.getTypedRuleContext(MicroCParser.CondContext,0)


        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MicroCParser.StatementsContext)
            else:
                return self.getTypedRuleContext(MicroCParser.StatementsContext,i)


        def getRuleIndex(self):
            return MicroCParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)




    def if_stmt(self):

        localctx = MicroCParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_stmt)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(MicroCParser.T__15)
                self.state = 257
                self.match(MicroCParser.T__7)
                self.state = 258
                localctx._cond = self.cond()
                self.state = 259
                self.match(MicroCParser.T__8)
                self.state = 260
                self.match(MicroCParser.T__9)
                self.state = 261
                localctx.t1 = self.statements()
                self.state = 262
                self.match(MicroCParser.T__10)

                self.state = 263
                self.match(MicroCParser.T__16)
                self.state = 264
                self.match(MicroCParser.T__9)
                self.state = 265
                localctx.e1 = self.statements()
                self.state = 266
                self.match(MicroCParser.T__10)
                localctx.node =  IfStatementNode(localctx._cond.node, localctx.t1.node, localctx.e1.node)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.match(MicroCParser.T__15)
                self.state = 271
                self.match(MicroCParser.T__7)
                self.state = 272
                localctx._cond = self.cond()
                self.state = 273
                self.match(MicroCParser.T__8)
                self.state = 274
                self.match(MicroCParser.T__9)
                self.state = 275
                localctx.t1 = self.statements()
                self.state = 276
                self.match(MicroCParser.T__10)
                localctx.node = IfStatementNode(localctx._cond.node, localctx.t1.node, StatementListNode())
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._cond = None # CondContext
            self._statements = None # StatementsContext

        def cond(self):
            return self.getTypedRuleContext(MicroCParser.CondContext,0)


        def statements(self):
            return self.getTypedRuleContext(MicroCParser.StatementsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)




    def while_stmt(self):

        localctx = MicroCParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(MicroCParser.T__17)
            self.state = 282
            self.match(MicroCParser.T__7)
            self.state = 283
            localctx._cond = self.cond()
            self.state = 284
            self.match(MicroCParser.T__8)
            self.state = 285
            self.match(MicroCParser.T__9)
            self.state = 286
            localctx._statements = self.statements()
            self.state = 287
            self.match(MicroCParser.T__10)
            localctx.node =  WhileNode(localctx._cond.node, localctx._statements.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._ident = None # IdentContext
            self._ptr_expr = None # Ptr_exprContext

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def ptr_expr(self):
            return self.getTypedRuleContext(MicroCParser.Ptr_exprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_lval

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLval" ):
                listener.enterLval(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLval" ):
                listener.exitLval(self)




    def lval(self):

        localctx = MicroCParser.LvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_lval)
        try:
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                localctx._ident = self.ident()
                localctx.node =  VarNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)))
                pass
            elif token in [MicroCParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                localctx._ptr_expr = self.ptr_expr()
                localctx.node =  localctx._ptr_expr.node
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._lval = None # LvalContext
            self._addr_of_expr = None # Addr_of_exprContext
            self._expr = None # ExprContext
            self._unaryminus_expr = None # Unaryminus_exprContext
            self._call_expr = None # Call_exprContext
            self._array_expr = None # Array_exprContext
            self.il = None # Token
            self.fl = None # Token

        def lval(self):
            return self.getTypedRuleContext(MicroCParser.LvalContext,0)


        def addr_of_expr(self):
            return self.getTypedRuleContext(MicroCParser.Addr_of_exprContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def unaryminus_expr(self):
            return self.getTypedRuleContext(MicroCParser.Unaryminus_exprContext,0)


        def call_expr(self):
            return self.getTypedRuleContext(MicroCParser.Call_exprContext,0)


        def array_expr(self):
            return self.getTypedRuleContext(MicroCParser.Array_exprContext,0)


        def INT_LITERAL(self):
            return self.getToken(MicroCParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(MicroCParser.FLOAT_LITERAL, 0)

        def getRuleIndex(self):
            return MicroCParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = MicroCParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_primary)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                localctx._lval = self.lval()
                localctx.node =  localctx._lval.node
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                localctx._addr_of_expr = self.addr_of_expr()
                localctx.node =  localctx._addr_of_expr.node
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 304
                self.match(MicroCParser.T__7)
                self.state = 305
                localctx._expr = self.expr(0)
                self.state = 306
                self.match(MicroCParser.T__8)
                localctx.node =  localctx._expr.node
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 309
                localctx._unaryminus_expr = self.unaryminus_expr()
                localctx.node =  localctx._unaryminus_expr.node
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 312
                localctx._call_expr = self.call_expr()
                localctx.node =  localctx._call_expr.node
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 315
                localctx._array_expr = self.array_expr(0)
                localctx.node =  localctx._array_expr.node
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 318
                localctx.il = self.match(MicroCParser.INT_LITERAL)
                localctx.node =  IntLitNode((None if localctx.il is None else localctx.il.text))
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 320
                localctx.fl = self.match(MicroCParser.FLOAT_LITERAL)
                localctx.node =  FloatLitNode((None if localctx.fl is None else localctx.fl.text))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unaryminus_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_unaryminus_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryminus_expr" ):
                listener.enterUnaryminus_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryminus_expr" ):
                listener.exitUnaryminus_expr(self)




    def unaryminus_expr(self):

        localctx = MicroCParser.Unaryminus_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_unaryminus_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(MicroCParser.T__18)
            self.state = 325
            localctx._expr = self.expr(0)
            localctx.node =  UnaryOpNode(localctx._expr.node, '-')
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ptr_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._primary = None # PrimaryContext

        def primary(self):
            return self.getTypedRuleContext(MicroCParser.PrimaryContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_ptr_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPtr_expr" ):
                listener.enterPtr_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPtr_expr" ):
                listener.exitPtr_expr(self)




    def ptr_expr(self):

        localctx = MicroCParser.Ptr_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_ptr_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(MicroCParser.T__3)
            self.state = 329
            localctx._primary = self.primary()
            localctx.node =  PtrDerefNode(localctx._primary.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Addr_of_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._lval = None # LvalContext
            self._array_expr = None # Array_exprContext

        def lval(self):
            return self.getTypedRuleContext(MicroCParser.LvalContext,0)


        def array_expr(self):
            return self.getTypedRuleContext(MicroCParser.Array_exprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_addr_of_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddr_of_expr" ):
                listener.enterAddr_of_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddr_of_expr" ):
                listener.exitAddr_of_expr(self)




    def addr_of_expr(self):

        localctx = MicroCParser.Addr_of_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_addr_of_expr)
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.match(MicroCParser.T__19)
                self.state = 333
                localctx._lval = self.lval()
                localctx.node =  AddrOfNode(localctx._lval.node)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.match(MicroCParser.T__19)
                self.state = 337
                localctx._array_expr = self.array_expr(0)
                localctx.node =  AddrOfNode(localctx._array_expr.node)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.ae = None # Array_exprContext
            self._lval = None # LvalContext
            self._expr = None # ExprContext

        def lval(self):
            return self.getTypedRuleContext(MicroCParser.LvalContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def array_expr(self):
            return self.getTypedRuleContext(MicroCParser.Array_exprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_array_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_expr" ):
                listener.enterArray_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_expr" ):
                listener.exitArray_expr(self)



    def array_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MicroCParser.Array_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_array_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            localctx._lval = self.lval()
            self.state = 344
            self.match(MicroCParser.T__20)
            self.state = 345
            localctx._expr = self.expr(0)
            self.state = 346
            self.match(MicroCParser.T__21)
            localctx.node =  PtrDerefNode(BinaryOpNode(localctx._lval.node, BinaryOpNode(IntLitNode('4'), localctx._expr.node, '*'), '+'))
            self._ctx.stop = self._input.LT(-1)
            self.state = 357
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MicroCParser.Array_exprContext(self, _parentctx, _parentState)
                    localctx.ae = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_array_expr)
                    self.state = 349
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 350
                    self.match(MicroCParser.T__20)
                    self.state = 351
                    localctx._expr = self.expr(0)
                    self.state = 352
                    self.match(MicroCParser.T__21)
                    localctx.node =  PtrDerefNode(BinaryOpNode(localctx.ae.node, BinaryOpNode(IntLitNode('4'), localctx._expr.node, '*'), '+')) 
                self.state = 359
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expr = None # ExprContext
            self._ident = None # IdentContext
            self._arg_list = None # Arg_listContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def arg_list(self):
            return self.getTypedRuleContext(MicroCParser.Arg_listContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_call_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_expr" ):
                listener.enterCall_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_expr" ):
                listener.exitCall_expr(self)




    def call_expr(self):

        localctx = MicroCParser.Call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_call_expr)
        try:
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.match(MicroCParser.T__22)
                self.state = 361
                self.match(MicroCParser.T__7)
                self.state = 362
                localctx._expr = self.expr(0)
                self.state = 363
                self.match(MicroCParser.T__8)
                localctx.node =  MallocNode(localctx._expr.node)
                pass
            elif token in [MicroCParser.T__23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.match(MicroCParser.T__23)
                self.state = 367
                self.match(MicroCParser.T__7)
                self.state = 368
                localctx._expr = self.expr(0)
                self.state = 369
                self.match(MicroCParser.T__8)
                localctx.node =  FreeNode(localctx._expr.node)
                pass
            elif token in [MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 372
                localctx._ident = self.ident()
                self.state = 373
                self.match(MicroCParser.T__7)
                self.state = 374
                localctx._arg_list = self.arg_list()
                self.state = 375
                self.match(MicroCParser.T__8)
                localctx.node =  CallNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), localctx._arg_list.args)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.args = None
            self._expr = None # ExprContext
            self._args_rest = None # Args_restContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def args_rest(self):
            return self.getTypedRuleContext(MicroCParser.Args_restContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_arg_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_list" ):
                listener.enterArg_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_list" ):
                listener.exitArg_list(self)




    def arg_list(self):

        localctx = MicroCParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_arg_list)
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__3, MicroCParser.T__7, MicroCParser.T__18, MicroCParser.T__19, MicroCParser.T__22, MicroCParser.T__23, MicroCParser.IDENTIFIER, MicroCParser.INT_LITERAL, MicroCParser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                localctx._expr = self.expr(0)
                self.state = 381
                localctx._args_rest = self.args_rest()

                localctx.args =  []
                localctx.args.append(localctx._expr.node);
                localctx.args.extend(localctx._args_rest.args);

                pass
            elif token in [MicroCParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                localctx.args =  []
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Args_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.args = None
            self._expr = None # ExprContext
            self._args_rest = None # Args_restContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def args_rest(self):
            return self.getTypedRuleContext(MicroCParser.Args_restContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_args_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs_rest" ):
                listener.enterArgs_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs_rest" ):
                listener.exitArgs_rest(self)




    def args_rest(self):

        localctx = MicroCParser.Args_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_args_rest)
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(MicroCParser.T__11)
                self.state = 388
                localctx._expr = self.expr(0)
                self.state = 389
                localctx._args_rest = self.args_rest()

                localctx.args =  []
                localctx.args.append(localctx._expr.node);
                localctx.args.extend(localctx._args_rest.args);

                pass
            elif token in [MicroCParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                localctx.args =  []
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExprContext
            self.e2 = None # ExprContext
            self._term = None # TermContext

        def term(self):
            return self.getTypedRuleContext(MicroCParser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MicroCParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            localctx._term = self.term(0)
            localctx.node =  localctx._term.node
            self._ctx.stop = self._input.LT(-1)
            self.state = 411
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 409
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = MicroCParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 399
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 400
                        self.match(MicroCParser.T__24)
                        self.state = 401
                        localctx._term = self.term(0)
                        localctx.node =  BinaryOpNode(localctx.e1.node, localctx._term.node, '+')
                        pass

                    elif la_ == 2:
                        localctx = MicroCParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e2 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 404
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 405
                        self.match(MicroCParser.T__18)
                        self.state = 406
                        localctx._term = self.term(0)
                        localctx.node =  BinaryOpNode(localctx.e2.node, localctx._term.node, '-')
                        pass

             
                self.state = 413
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.t1 = None # TermContext
            self.t2 = None # TermContext
            self._primary = None # PrimaryContext

        def primary(self):
            return self.getTypedRuleContext(MicroCParser.PrimaryContext,0)


        def term(self):
            return self.getTypedRuleContext(MicroCParser.TermContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MicroCParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            localctx._primary = self.primary()
            localctx.node =  localctx._primary.node
            self._ctx.stop = self._input.LT(-1)
            self.state = 430
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 428
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = MicroCParser.TermContext(self, _parentctx, _parentState)
                        localctx.t1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 418
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 419
                        self.match(MicroCParser.T__3)
                        self.state = 420
                        localctx._primary = self.primary()
                        localctx.node =  BinaryOpNode(localctx.t1.node, localctx._primary.node, '*')
                        pass

                    elif la_ == 2:
                        localctx = MicroCParser.TermContext(self, _parentctx, _parentState)
                        localctx.t2 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 423
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 424
                        self.match(MicroCParser.T__25)
                        self.state = 425
                        localctx._primary = self.primary()
                        localctx.node =  BinaryOpNode(localctx.t2.node, localctx._primary.node, '/')
                        pass

             
                self.state = 432
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExprContext
            self.e2 = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MicroCParser.ExprContext)
            else:
                return self.getTypedRuleContext(MicroCParser.ExprContext,i)


        def getRuleIndex(self):
            return MicroCParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)




    def cond(self):

        localctx = MicroCParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_cond)
        try:
            self.state = 463
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                localctx.e1 = self.expr(0)
                self.state = 434
                self.match(MicroCParser.T__26)
                self.state = 435
                localctx.e2 = self.expr(0)
                localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, '<')
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                localctx.e1 = self.expr(0)
                self.state = 439
                self.match(MicroCParser.T__27)
                self.state = 440
                localctx.e2 = self.expr(0)
                localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, '<=')
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 443
                localctx.e1 = self.expr(0)
                self.state = 444
                self.match(MicroCParser.T__28)
                self.state = 445
                localctx.e2 = self.expr(0)
                localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, '>=')
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 448
                localctx.e1 = self.expr(0)
                self.state = 449
                self.match(MicroCParser.T__29)
                self.state = 450
                localctx.e2 = self.expr(0)
                localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, '==')
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 453
                localctx.e1 = self.expr(0)
                self.state = 454
                self.match(MicroCParser.T__30)
                self.state = 455
                localctx.e2 = self.expr(0)
                localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, '!=')
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 458
                localctx.e1 = self.expr(0)
                self.state = 459
                self.match(MicroCParser.T__31)
                self.state = 460
                localctx.e2 = self.expr(0)
                localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, '>')
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmpopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MicroCParser.RULE_cmpop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmpop" ):
                listener.enterCmpop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmpop" ):
                listener.exitCmpop(self)




    def cmpop(self):

        localctx = MicroCParser.CmpopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_cmpop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MicroCParser.T__26) | (1 << MicroCParser.T__27) | (1 << MicroCParser.T__28) | (1 << MicroCParser.T__29) | (1 << MicroCParser.T__30) | (1 << MicroCParser.T__31))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MicroCParser.RULE_mulop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulop" ):
                listener.enterMulop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulop" ):
                listener.exitMulop(self)




    def mulop(self):

        localctx = MicroCParser.MulopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_mulop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            _la = self._input.LA(1)
            if not(_la==MicroCParser.T__3 or _la==MicroCParser.T__25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MicroCParser.RULE_addop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddop" ):
                listener.enterAddop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddop" ):
                listener.exitAddop(self)




    def addop(self):

        localctx = MicroCParser.AddopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_addop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            _la = self._input.LA(1)
            if not(_la==MicroCParser.T__18 or _la==MicroCParser.T__24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.true_type_sempred
        self._predicates[30] = self.array_expr_sempred
        self._predicates[34] = self.expr_sempred
        self._predicates[35] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def true_type_sempred(self, localctx:True_typeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def array_expr_sempred(self, localctx:Array_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         




