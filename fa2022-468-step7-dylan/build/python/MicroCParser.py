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
from MicroCCompiler.ast.CastNode import CastNode


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3(")
        buf.write("\u01e5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3c\n\3\3\4\3\4\3\4\3")
        buf.write("\4\5\4i\n\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u0080\n")
        buf.write("\b\f\b\16\b\u0083\13\b\3\t\3\t\3\t\3\t\5\t\u0089\n\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\5\n\u0090\n\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\5\f\u009f\n\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\5\16\u00b2\n\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00ba\n\17\3\20\3\20\3\20\3\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\5\21\u00c5\n\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00d1\n\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u00e2\n\23\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u00f6\n\26\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0103\n\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u011c\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u012d\n\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\5\34\u014a\n\34\3\35\3\35\3")
        buf.write("\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\5\37\u015c\n\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \7 \u016b\n \f \16 \u016e\13 \3!\3!\3")
        buf.write("!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0188\n\"\3#\3#\3#\3")
        buf.write("#\3#\5#\u018f\n#\3$\3$\3$\3$\3$\3$\5$\u0197\n$\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\7%\u01a7\n%\f%\16%")
        buf.write("\u01aa\13%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\7")
        buf.write("&\u01ba\n&\f&\16&\u01bd\13&\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u01dd\n\'")
        buf.write("\3(\3(\3)\3)\3*\3*\3*\2\6\16>HJ+\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("\2\5\3\2\35\"\4\2\6\6\34\34\4\2\25\25\33\33\2\u01e7\2")
        buf.write("T\3\2\2\2\4b\3\2\2\2\6h\3\2\2\2\bj\3\2\2\2\nl\3\2\2\2")
        buf.write("\fq\3\2\2\2\16x\3\2\2\2\20\u0088\3\2\2\2\22\u008f\3\2")
        buf.write("\2\2\24\u0091\3\2\2\2\26\u009e\3\2\2\2\30\u00a0\3\2\2")
        buf.write("\2\32\u00b1\3\2\2\2\34\u00b9\3\2\2\2\36\u00bb\3\2\2\2")
        buf.write(" \u00c4\3\2\2\2\"\u00d0\3\2\2\2$\u00e1\3\2\2\2&\u00e3")
        buf.write("\3\2\2\2(\u00e9\3\2\2\2*\u00f5\3\2\2\2,\u00f7\3\2\2\2")
        buf.write(".\u0102\3\2\2\2\60\u011b\3\2\2\2\62\u011d\3\2\2\2\64\u012c")
        buf.write("\3\2\2\2\66\u0149\3\2\2\28\u014b\3\2\2\2:\u014f\3\2\2")
        buf.write("\2<\u015b\3\2\2\2>\u015d\3\2\2\2@\u016f\3\2\2\2B\u0187")
        buf.write("\3\2\2\2D\u018e\3\2\2\2F\u0196\3\2\2\2H\u0198\3\2\2\2")
        buf.write("J\u01ab\3\2\2\2L\u01dc\3\2\2\2N\u01de\3\2\2\2P\u01e0\3")
        buf.write("\2\2\2R\u01e2\3\2\2\2TU\5\4\3\2UV\5\26\f\2VW\b\2\1\2W")
        buf.write("\3\3\2\2\2XY\5\n\6\2YZ\5\4\3\2Zc\3\2\2\2[\\\5\f\7\2\\")
        buf.write("]\5\4\3\2]c\3\2\2\2^_\5\24\13\2_`\5\4\3\2`c\3\2\2\2ac")
        buf.write("\3\2\2\2bX\3\2\2\2b[\3\2\2\2b^\3\2\2\2ba\3\2\2\2c\5\3")
        buf.write("\2\2\2de\5\n\6\2ef\5\6\4\2fi\3\2\2\2gi\3\2\2\2hd\3\2\2")
        buf.write("\2hg\3\2\2\2i\7\3\2\2\2jk\7#\2\2k\t\3\2\2\2lm\5\16\b\2")
        buf.write("mn\5\b\5\2no\7\3\2\2op\b\6\1\2p\13\3\2\2\2qr\7\4\2\2r")
        buf.write("s\5\b\5\2st\7\5\2\2tu\7&\2\2uv\7\3\2\2vw\b\7\1\2w\r\3")
        buf.write("\2\2\2xy\b\b\1\2yz\5\20\t\2z{\b\b\1\2{\u0081\3\2\2\2|")
        buf.write("}\f\3\2\2}~\7\6\2\2~\u0080\b\b\1\2\177|\3\2\2\2\u0080")
        buf.write("\u0083\3\2\2\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082")
        buf.write("\17\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u0085\7\7\2\2\u0085")
        buf.write("\u0089\b\t\1\2\u0086\u0087\7\b\2\2\u0087\u0089\b\t\1\2")
        buf.write("\u0088\u0084\3\2\2\2\u0088\u0086\3\2\2\2\u0089\21\3\2")
        buf.write("\2\2\u008a\u008b\5\16\b\2\u008b\u008c\b\n\1\2\u008c\u0090")
        buf.write("\3\2\2\2\u008d\u008e\7\t\2\2\u008e\u0090\b\n\1\2\u008f")
        buf.write("\u008a\3\2\2\2\u008f\u008d\3\2\2\2\u0090\23\3\2\2\2\u0091")
        buf.write("\u0092\5\22\n\2\u0092\u0093\5\b\5\2\u0093\u0094\7\n\2")
        buf.write("\2\u0094\u0095\5\32\16\2\u0095\u0096\7\13\2\2\u0096\u0097")
        buf.write("\7\3\2\2\u0097\u0098\b\13\1\2\u0098\25\3\2\2\2\u0099\u009a")
        buf.write("\5\30\r\2\u009a\u009b\5\26\f\2\u009b\u009c\b\f\1\2\u009c")
        buf.write("\u009f\3\2\2\2\u009d\u009f\b\f\1\2\u009e\u0099\3\2\2\2")
        buf.write("\u009e\u009d\3\2\2\2\u009f\27\3\2\2\2\u00a0\u00a1\5\22")
        buf.write("\n\2\u00a1\u00a2\5\b\5\2\u00a2\u00a3\7\n\2\2\u00a3\u00a4")
        buf.write("\5\32\16\2\u00a4\u00a5\7\13\2\2\u00a5\u00a6\b\r\1\2\u00a6")
        buf.write("\u00a7\7\f\2\2\u00a7\u00a8\5\6\4\2\u00a8\u00a9\5 \21\2")
        buf.write("\u00a9\u00aa\7\r\2\2\u00aa\u00ab\b\r\1\2\u00ab\31\3\2")
        buf.write("\2\2\u00ac\u00ad\5\36\20\2\u00ad\u00ae\5\34\17\2\u00ae")
        buf.write("\u00af\b\16\1\2\u00af\u00b2\3\2\2\2\u00b0\u00b2\b\16\1")
        buf.write("\2\u00b1\u00ac\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\33\3")
        buf.write("\2\2\2\u00b3\u00b4\7\16\2\2\u00b4\u00b5\5\36\20\2\u00b5")
        buf.write("\u00b6\5\34\17\2\u00b6\u00b7\b\17\1\2\u00b7\u00ba\3\2")
        buf.write("\2\2\u00b8\u00ba\b\17\1\2\u00b9\u00b3\3\2\2\2\u00b9\u00b8")
        buf.write("\3\2\2\2\u00ba\35\3\2\2\2\u00bb\u00bc\5\16\b\2\u00bc\u00bd")
        buf.write("\5\b\5\2\u00bd\u00be\b\20\1\2\u00be\37\3\2\2\2\u00bf\u00c0")
        buf.write("\5\"\22\2\u00c0\u00c1\5 \21\2\u00c1\u00c2\b\21\1\2\u00c2")
        buf.write("\u00c5\3\2\2\2\u00c3\u00c5\b\21\1\2\u00c4\u00bf\3\2\2")
        buf.write("\2\u00c4\u00c3\3\2\2\2\u00c5!\3\2\2\2\u00c6\u00c7\5$\23")
        buf.write("\2\u00c7\u00c8\7\3\2\2\u00c8\u00c9\b\22\1\2\u00c9\u00d1")
        buf.write("\3\2\2\2\u00ca\u00cb\5\60\31\2\u00cb\u00cc\b\22\1\2\u00cc")
        buf.write("\u00d1\3\2\2\2\u00cd\u00ce\5\62\32\2\u00ce\u00cf\b\22")
        buf.write("\1\2\u00cf\u00d1\3\2\2\2\u00d0\u00c6\3\2\2\2\u00d0\u00ca")
        buf.write("\3\2\2\2\u00d0\u00cd\3\2\2\2\u00d1#\3\2\2\2\u00d2\u00d3")
        buf.write("\5,\27\2\u00d3\u00d4\b\23\1\2\u00d4\u00e2\3\2\2\2\u00d5")
        buf.write("\u00d6\5&\24\2\u00d6\u00d7\b\23\1\2\u00d7\u00e2\3\2\2")
        buf.write("\2\u00d8\u00d9\5(\25\2\u00d9\u00da\b\23\1\2\u00da\u00e2")
        buf.write("\3\2\2\2\u00db\u00dc\5*\26\2\u00dc\u00dd\b\23\1\2\u00dd")
        buf.write("\u00e2\3\2\2\2\u00de\u00df\5B\"\2\u00df\u00e0\b\23\1\2")
        buf.write("\u00e0\u00e2\3\2\2\2\u00e1\u00d2\3\2\2\2\u00e1\u00d5\3")
        buf.write("\2\2\2\u00e1\u00d8\3\2\2\2\u00e1\u00db\3\2\2\2\u00e1\u00de")
        buf.write("\3\2\2\2\u00e2%\3\2\2\2\u00e3\u00e4\7\17\2\2\u00e4\u00e5")
        buf.write("\7\n\2\2\u00e5\u00e6\5\b\5\2\u00e6\u00e7\7\13\2\2\u00e7")
        buf.write("\u00e8\b\24\1\2\u00e8\'\3\2\2\2\u00e9\u00ea\7\20\2\2\u00ea")
        buf.write("\u00eb\7\n\2\2\u00eb\u00ec\5H%\2\u00ec\u00ed\7\13\2\2")
        buf.write("\u00ed\u00ee\b\25\1\2\u00ee)\3\2\2\2\u00ef\u00f0\7\21")
        buf.write("\2\2\u00f0\u00f1\5H%\2\u00f1\u00f2\b\26\1\2\u00f2\u00f6")
        buf.write("\3\2\2\2\u00f3\u00f4\7\21\2\2\u00f4\u00f6\b\26\1\2\u00f5")
        buf.write("\u00ef\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6+\3\2\2\2\u00f7")
        buf.write("\u00f8\5.\30\2\u00f8\u00f9\7\5\2\2\u00f9\u00fa\5H%\2\u00fa")
        buf.write("\u00fb\b\27\1\2\u00fb-\3\2\2\2\u00fc\u00fd\5\64\33\2\u00fd")
        buf.write("\u00fe\b\30\1\2\u00fe\u0103\3\2\2\2\u00ff\u0100\5> \2")
        buf.write("\u0100\u0101\b\30\1\2\u0101\u0103\3\2\2\2\u0102\u00fc")
        buf.write("\3\2\2\2\u0102\u00ff\3\2\2\2\u0103/\3\2\2\2\u0104\u0105")
        buf.write("\7\22\2\2\u0105\u0106\7\n\2\2\u0106\u0107\5L\'\2\u0107")
        buf.write("\u0108\7\13\2\2\u0108\u0109\7\f\2\2\u0109\u010a\5 \21")
        buf.write("\2\u010a\u010b\7\r\2\2\u010b\u010c\7\23\2\2\u010c\u010d")
        buf.write("\7\f\2\2\u010d\u010e\5 \21\2\u010e\u010f\7\r\2\2\u010f")
        buf.write("\u0110\3\2\2\2\u0110\u0111\b\31\1\2\u0111\u011c\3\2\2")
        buf.write("\2\u0112\u0113\7\22\2\2\u0113\u0114\7\n\2\2\u0114\u0115")
        buf.write("\5L\'\2\u0115\u0116\7\13\2\2\u0116\u0117\7\f\2\2\u0117")
        buf.write("\u0118\5 \21\2\u0118\u0119\7\r\2\2\u0119\u011a\b\31\1")
        buf.write("\2\u011a\u011c\3\2\2\2\u011b\u0104\3\2\2\2\u011b\u0112")
        buf.write("\3\2\2\2\u011c\61\3\2\2\2\u011d\u011e\7\24\2\2\u011e\u011f")
        buf.write("\7\n\2\2\u011f\u0120\5L\'\2\u0120\u0121\7\13\2\2\u0121")
        buf.write("\u0122\7\f\2\2\u0122\u0123\5 \21\2\u0123\u0124\7\r\2\2")
        buf.write("\u0124\u0125\b\32\1\2\u0125\63\3\2\2\2\u0126\u0127\5\b")
        buf.write("\5\2\u0127\u0128\b\33\1\2\u0128\u012d\3\2\2\2\u0129\u012a")
        buf.write("\5:\36\2\u012a\u012b\b\33\1\2\u012b\u012d\3\2\2\2\u012c")
        buf.write("\u0126\3\2\2\2\u012c\u0129\3\2\2\2\u012d\65\3\2\2\2\u012e")
        buf.write("\u012f\5\64\33\2\u012f\u0130\b\34\1\2\u0130\u014a\3\2")
        buf.write("\2\2\u0131\u0132\5<\37\2\u0132\u0133\b\34\1\2\u0133\u014a")
        buf.write("\3\2\2\2\u0134\u0135\7\n\2\2\u0135\u0136\5H%\2\u0136\u0137")
        buf.write("\7\13\2\2\u0137\u0138\b\34\1\2\u0138\u014a\3\2\2\2\u0139")
        buf.write("\u013a\58\35\2\u013a\u013b\b\34\1\2\u013b\u014a\3\2\2")
        buf.write("\2\u013c\u013d\5B\"\2\u013d\u013e\b\34\1\2\u013e\u014a")
        buf.write("\3\2\2\2\u013f\u0140\5> \2\u0140\u0141\b\34\1\2\u0141")
        buf.write("\u014a\3\2\2\2\u0142\u0143\5@!\2\u0143\u0144\b\34\1\2")
        buf.write("\u0144\u014a\3\2\2\2\u0145\u0146\7$\2\2\u0146\u014a\b")
        buf.write("\34\1\2\u0147\u0148\7%\2\2\u0148\u014a\b\34\1\2\u0149")
        buf.write("\u012e\3\2\2\2\u0149\u0131\3\2\2\2\u0149\u0134\3\2\2\2")
        buf.write("\u0149\u0139\3\2\2\2\u0149\u013c\3\2\2\2\u0149\u013f\3")
        buf.write("\2\2\2\u0149\u0142\3\2\2\2\u0149\u0145\3\2\2\2\u0149\u0147")
        buf.write("\3\2\2\2\u014a\67\3\2\2\2\u014b\u014c\7\25\2\2\u014c\u014d")
        buf.write("\5H%\2\u014d\u014e\b\35\1\2\u014e9\3\2\2\2\u014f\u0150")
        buf.write("\7\6\2\2\u0150\u0151\5\66\34\2\u0151\u0152\b\36\1\2\u0152")
        buf.write(";\3\2\2\2\u0153\u0154\7\26\2\2\u0154\u0155\5\64\33\2\u0155")
        buf.write("\u0156\b\37\1\2\u0156\u015c\3\2\2\2\u0157\u0158\7\26\2")
        buf.write("\2\u0158\u0159\5> \2\u0159\u015a\b\37\1\2\u015a\u015c")
        buf.write("\3\2\2\2\u015b\u0153\3\2\2\2\u015b\u0157\3\2\2\2\u015c")
        buf.write("=\3\2\2\2\u015d\u015e\b \1\2\u015e\u015f\5\64\33\2\u015f")
        buf.write("\u0160\7\27\2\2\u0160\u0161\5H%\2\u0161\u0162\7\30\2\2")
        buf.write("\u0162\u0163\b \1\2\u0163\u016c\3\2\2\2\u0164\u0165\f")
        buf.write("\3\2\2\u0165\u0166\7\27\2\2\u0166\u0167\5H%\2\u0167\u0168")
        buf.write("\7\30\2\2\u0168\u0169\b \1\2\u0169\u016b\3\2\2\2\u016a")
        buf.write("\u0164\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2")
        buf.write("\u016c\u016d\3\2\2\2\u016d?\3\2\2\2\u016e\u016c\3\2\2")
        buf.write("\2\u016f\u0170\7\n\2\2\u0170\u0171\5\20\t\2\u0171\u0172")
        buf.write("\7\13\2\2\u0172\u0173\5\66\34\2\u0173\u0174\b!\1\2\u0174")
        buf.write("A\3\2\2\2\u0175\u0176\7\31\2\2\u0176\u0177\7\n\2\2\u0177")
        buf.write("\u0178\5H%\2\u0178\u0179\7\13\2\2\u0179\u017a\b\"\1\2")
        buf.write("\u017a\u0188\3\2\2\2\u017b\u017c\7\32\2\2\u017c\u017d")
        buf.write("\7\n\2\2\u017d\u017e\5H%\2\u017e\u017f\7\13\2\2\u017f")
        buf.write("\u0180\b\"\1\2\u0180\u0188\3\2\2\2\u0181\u0182\5\b\5\2")
        buf.write("\u0182\u0183\7\n\2\2\u0183\u0184\5D#\2\u0184\u0185\7\13")
        buf.write("\2\2\u0185\u0186\b\"\1\2\u0186\u0188\3\2\2\2\u0187\u0175")
        buf.write("\3\2\2\2\u0187\u017b\3\2\2\2\u0187\u0181\3\2\2\2\u0188")
        buf.write("C\3\2\2\2\u0189\u018a\5H%\2\u018a\u018b\5F$\2\u018b\u018c")
        buf.write("\b#\1\2\u018c\u018f\3\2\2\2\u018d\u018f\b#\1\2\u018e\u0189")
        buf.write("\3\2\2\2\u018e\u018d\3\2\2\2\u018fE\3\2\2\2\u0190\u0191")
        buf.write("\7\16\2\2\u0191\u0192\5H%\2\u0192\u0193\5F$\2\u0193\u0194")
        buf.write("\b$\1\2\u0194\u0197\3\2\2\2\u0195\u0197\b$\1\2\u0196\u0190")
        buf.write("\3\2\2\2\u0196\u0195\3\2\2\2\u0197G\3\2\2\2\u0198\u0199")
        buf.write("\b%\1\2\u0199\u019a\5J&\2\u019a\u019b\b%\1\2\u019b\u01a8")
        buf.write("\3\2\2\2\u019c\u019d\f\4\2\2\u019d\u019e\7\33\2\2\u019e")
        buf.write("\u019f\5J&\2\u019f\u01a0\b%\1\2\u01a0\u01a7\3\2\2\2\u01a1")
        buf.write("\u01a2\f\3\2\2\u01a2\u01a3\7\25\2\2\u01a3\u01a4\5J&\2")
        buf.write("\u01a4\u01a5\b%\1\2\u01a5\u01a7\3\2\2\2\u01a6\u019c\3")
        buf.write("\2\2\2\u01a6\u01a1\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9I\3\2\2\2\u01aa\u01a8")
        buf.write("\3\2\2\2\u01ab\u01ac\b&\1\2\u01ac\u01ad\5\66\34\2\u01ad")
        buf.write("\u01ae\b&\1\2\u01ae\u01bb\3\2\2\2\u01af\u01b0\f\4\2\2")
        buf.write("\u01b0\u01b1\7\6\2\2\u01b1\u01b2\5\66\34\2\u01b2\u01b3")
        buf.write("\b&\1\2\u01b3\u01ba\3\2\2\2\u01b4\u01b5\f\3\2\2\u01b5")
        buf.write("\u01b6\7\34\2\2\u01b6\u01b7\5\66\34\2\u01b7\u01b8\b&\1")
        buf.write("\2\u01b8\u01ba\3\2\2\2\u01b9\u01af\3\2\2\2\u01b9\u01b4")
        buf.write("\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb")
        buf.write("\u01bc\3\2\2\2\u01bcK\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be")
        buf.write("\u01bf\5H%\2\u01bf\u01c0\7\35\2\2\u01c0\u01c1\5H%\2\u01c1")
        buf.write("\u01c2\b\'\1\2\u01c2\u01dd\3\2\2\2\u01c3\u01c4\5H%\2\u01c4")
        buf.write("\u01c5\7\36\2\2\u01c5\u01c6\5H%\2\u01c6\u01c7\b\'\1\2")
        buf.write("\u01c7\u01dd\3\2\2\2\u01c8\u01c9\5H%\2\u01c9\u01ca\7\37")
        buf.write("\2\2\u01ca\u01cb\5H%\2\u01cb\u01cc\b\'\1\2\u01cc\u01dd")
        buf.write("\3\2\2\2\u01cd\u01ce\5H%\2\u01ce\u01cf\7 \2\2\u01cf\u01d0")
        buf.write("\5H%\2\u01d0\u01d1\b\'\1\2\u01d1\u01dd\3\2\2\2\u01d2\u01d3")
        buf.write("\5H%\2\u01d3\u01d4\7!\2\2\u01d4\u01d5\5H%\2\u01d5\u01d6")
        buf.write("\b\'\1\2\u01d6\u01dd\3\2\2\2\u01d7\u01d8\5H%\2\u01d8\u01d9")
        buf.write("\7\"\2\2\u01d9\u01da\5H%\2\u01da\u01db\b\'\1\2\u01db\u01dd")
        buf.write("\3\2\2\2\u01dc\u01be\3\2\2\2\u01dc\u01c3\3\2\2\2\u01dc")
        buf.write("\u01c8\3\2\2\2\u01dc\u01cd\3\2\2\2\u01dc\u01d2\3\2\2\2")
        buf.write("\u01dc\u01d7\3\2\2\2\u01ddM\3\2\2\2\u01de\u01df\t\2\2")
        buf.write("\2\u01dfO\3\2\2\2\u01e0\u01e1\t\3\2\2\u01e1Q\3\2\2\2\u01e2")
        buf.write("\u01e3\t\4\2\2\u01e3S\3\2\2\2\34bh\u0081\u0088\u008f\u009e")
        buf.write("\u00b1\u00b9\u00c4\u00d0\u00e1\u00f5\u0102\u011b\u012c")
        buf.write("\u0149\u015b\u016c\u0187\u018e\u0196\u01a6\u01a8\u01b9")
        buf.write("\u01bb\u01dc")
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
    RULE_cast_expr = 31
    RULE_call_expr = 32
    RULE_arg_list = 33
    RULE_args_rest = 34
    RULE_expr = 35
    RULE_term = 36
    RULE_cond = 37
    RULE_cmpop = 38
    RULE_mulop = 39
    RULE_addop = 40

    ruleNames =  [ "program", "decls", "var_decls", "ident", "var_decl", 
                   "str_decl", "true_type", "base_type", "func_type", "func_decl", 
                   "functions", "function", "params", "params_rest", "param", 
                   "statements", "statement", "base_stmt", "read_stmt", 
                   "print_stmt", "return_stmt", "assign_stmt", "lhs", "if_stmt", 
                   "while_stmt", "lval", "primary", "unaryminus_expr", "ptr_expr", 
                   "addr_of_expr", "array_expr", "cast_expr", "call_expr", 
                   "arg_list", "args_rest", "expr", "term", "cond", "cmpop", 
                   "mulop", "addop" ]

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
            self.state = 82
            self.decls()
            self.state = 83
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
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.var_decl()
                self.state = 87
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.str_decl()
                self.state = 90
                self.decls()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.func_decl()
                self.state = 93
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
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__4, MicroCParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.var_decl()
                self.state = 99
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
            self.state = 104
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
            self.state = 106
            localctx._true_type = self.true_type(0)
            self.state = 107
            localctx._ident = self.ident()
            self.state = 108
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
            self.state = 111
            self.match(MicroCParser.T__1)
            self.state = 112
            localctx._ident = self.ident()
            self.state = 113
            self.match(MicroCParser.T__2)
            self.state = 114
            localctx.val = self.match(MicroCParser.STR_LITERAL)
            self.state = 115
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
            self.state = 119
            localctx._base_type = self.base_type()
            localctx.t =  localctx._base_type.t
            self._ctx.stop = self._input.LT(-1)
            self.state = 127
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
                    self.state = 122
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 123
                    self.match(MicroCParser.T__3)
                    localctx.t =  Scope.Type.pointerToType(localctx.t1.t) 
                self.state = 129
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
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(MicroCParser.T__4)
                localctx.t =  Scope.Type(Scope.InnerType.INT)
                pass
            elif token in [MicroCParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
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
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__4, MicroCParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                localctx._true_type = self.true_type(0)
                localctx.t =  localctx._true_type.t
                pass
            elif token in [MicroCParser.T__6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
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
            self.state = 143
            localctx._func_type = self.func_type()
            self.state = 144
            localctx._ident = self.ident()
            self.state = 145
            self.match(MicroCParser.T__7)
            self.state = 146
            localctx._params = self.params()
            self.state = 147
            self.match(MicroCParser.T__8)
            self.state = 148
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
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__4, MicroCParser.T__5, MicroCParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                localctx._function = self.function()
                self.state = 152
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
            self.state = 158
            localctx._func_type = self.func_type()
            self.state = 159
            localctx._ident = self.ident()
            self.state = 160
            self.match(MicroCParser.T__7)
            self.state = 161
            localctx._params = self.params()
            self.state = 162
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

            self.state = 164
            self.match(MicroCParser.T__9)
            self.state = 165
            self.var_decls()
            self.state = 166
            localctx._statements = self.statements()
            self.state = 167
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
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__4, MicroCParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                localctx._param = self.param()
                self.state = 171
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
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(MicroCParser.T__11)
                self.state = 178
                localctx._param = self.param()
                self.state = 179
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
            self.state = 185
            localctx._true_type = self.true_type(0)
            self.state = 186
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
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__3, MicroCParser.T__12, MicroCParser.T__13, MicroCParser.T__14, MicroCParser.T__15, MicroCParser.T__17, MicroCParser.T__22, MicroCParser.T__23, MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                localctx._statement = self.statement()
                self.state = 190
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
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__3, MicroCParser.T__12, MicroCParser.T__13, MicroCParser.T__14, MicroCParser.T__22, MicroCParser.T__23, MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                localctx._base_stmt = self.base_stmt()
                self.state = 197
                self.match(MicroCParser.T__0)
                localctx.node =  localctx._base_stmt.node
                pass
            elif token in [MicroCParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                localctx._if_stmt = self.if_stmt()
                localctx.node = localctx._if_stmt.node
                pass
            elif token in [MicroCParser.T__17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
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
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                localctx._assign_stmt = self.assign_stmt()
                localctx.node =  localctx._assign_stmt.node
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                localctx._read_stmt = self.read_stmt()
                localctx.node =  localctx._read_stmt.node
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
                localctx._print_stmt = self.print_stmt()
                localctx.node =  localctx._print_stmt.node
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 217
                localctx._return_stmt = self.return_stmt()
                localctx.node =  localctx._return_stmt.node
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 220
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
            self.state = 225
            self.match(MicroCParser.T__12)
            self.state = 226
            self.match(MicroCParser.T__7)
            self.state = 227
            localctx._ident = self.ident()
            self.state = 228
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
            self.state = 231
            self.match(MicroCParser.T__13)
            self.state = 232
            self.match(MicroCParser.T__7)
            self.state = 233
            localctx._expr = self.expr(0)
            self.state = 234
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
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(MicroCParser.T__14)
                self.state = 238
                localctx._expr = self.expr(0)
                localctx.node =  ReturnNode(localctx._expr.node, self.st.getFunctionSymbol(self.st.currentScope().getName()))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
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
            self.state = 245
            localctx._lhs = self.lhs()
            self.state = 246
            self.match(MicroCParser.T__2)
            self.state = 247
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
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                localctx._lval = self.lval()
                localctx.node =  localctx._lval.node
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
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
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(MicroCParser.T__15)
                self.state = 259
                self.match(MicroCParser.T__7)
                self.state = 260
                localctx._cond = self.cond()
                self.state = 261
                self.match(MicroCParser.T__8)
                self.state = 262
                self.match(MicroCParser.T__9)
                self.state = 263
                localctx.t1 = self.statements()
                self.state = 264
                self.match(MicroCParser.T__10)

                self.state = 265
                self.match(MicroCParser.T__16)
                self.state = 266
                self.match(MicroCParser.T__9)
                self.state = 267
                localctx.e1 = self.statements()
                self.state = 268
                self.match(MicroCParser.T__10)
                localctx.node =  IfStatementNode(localctx._cond.node, localctx.t1.node, localctx.e1.node)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.match(MicroCParser.T__15)
                self.state = 273
                self.match(MicroCParser.T__7)
                self.state = 274
                localctx._cond = self.cond()
                self.state = 275
                self.match(MicroCParser.T__8)
                self.state = 276
                self.match(MicroCParser.T__9)
                self.state = 277
                localctx.t1 = self.statements()
                self.state = 278
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
            self.state = 283
            self.match(MicroCParser.T__17)
            self.state = 284
            self.match(MicroCParser.T__7)
            self.state = 285
            localctx._cond = self.cond()
            self.state = 286
            self.match(MicroCParser.T__8)
            self.state = 287
            self.match(MicroCParser.T__9)
            self.state = 288
            localctx._statements = self.statements()
            self.state = 289
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
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                localctx._ident = self.ident()
                localctx.node =  VarNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)))
                pass
            elif token in [MicroCParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
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
            self._cast_expr = None # Cast_exprContext
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


        def cast_expr(self):
            return self.getTypedRuleContext(MicroCParser.Cast_exprContext,0)


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
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                localctx._lval = self.lval()
                localctx.node =  localctx._lval.node
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                localctx._addr_of_expr = self.addr_of_expr()
                localctx.node =  localctx._addr_of_expr.node
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 306
                self.match(MicroCParser.T__7)
                self.state = 307
                localctx._expr = self.expr(0)
                self.state = 308
                self.match(MicroCParser.T__8)
                localctx.node =  localctx._expr.node
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 311
                localctx._unaryminus_expr = self.unaryminus_expr()
                localctx.node =  localctx._unaryminus_expr.node
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 314
                localctx._call_expr = self.call_expr()
                localctx.node =  localctx._call_expr.node
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 317
                localctx._array_expr = self.array_expr(0)
                localctx.node =  localctx._array_expr.node
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 320
                localctx._cast_expr = self.cast_expr()
                localctx.node =  localctx._cast_expr.node
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 323
                localctx.il = self.match(MicroCParser.INT_LITERAL)
                localctx.node =  IntLitNode((None if localctx.il is None else localctx.il.text))
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 325
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
            self.state = 329
            self.match(MicroCParser.T__18)
            self.state = 330
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
            self.state = 333
            self.match(MicroCParser.T__3)
            self.state = 334
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
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(MicroCParser.T__19)
                self.state = 338
                localctx._lval = self.lval()
                localctx.node =  AddrOfNode(localctx._lval.node)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.match(MicroCParser.T__19)
                self.state = 342
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
            self.state = 348
            localctx._lval = self.lval()
            self.state = 349
            self.match(MicroCParser.T__20)
            self.state = 350
            localctx._expr = self.expr(0)
            self.state = 351
            self.match(MicroCParser.T__21)
            localctx.node =  PtrDerefNode(BinaryOpNode(localctx._lval.node, BinaryOpNode(IntLitNode('4'), localctx._expr.node, '*'), '+'))
            self._ctx.stop = self._input.LT(-1)
            self.state = 362
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
                    self.state = 354
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 355
                    self.match(MicroCParser.T__20)
                    self.state = 356
                    localctx._expr = self.expr(0)
                    self.state = 357
                    self.match(MicroCParser.T__21)
                    localctx.node =  PtrDerefNode(BinaryOpNode(localctx.ae.node, BinaryOpNode(IntLitNode('4'), localctx._expr.node, '*'), '+')) 
                self.state = 364
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Cast_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._base_type = None # Base_typeContext
            self._primary = None # PrimaryContext

        def base_type(self):
            return self.getTypedRuleContext(MicroCParser.Base_typeContext,0)


        def primary(self):
            return self.getTypedRuleContext(MicroCParser.PrimaryContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_cast_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCast_expr" ):
                listener.enterCast_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCast_expr" ):
                listener.exitCast_expr(self)




    def cast_expr(self):

        localctx = MicroCParser.Cast_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_cast_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(MicroCParser.T__7)
            self.state = 366
            localctx._base_type = self.base_type()
            self.state = 367
            self.match(MicroCParser.T__8)
            self.state = 368
            localctx._primary = self.primary()
            localctx.node =  CastNode(localctx._base_type.t, localctx._primary.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 64, self.RULE_call_expr)
        try:
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.match(MicroCParser.T__22)
                self.state = 372
                self.match(MicroCParser.T__7)
                self.state = 373
                localctx._expr = self.expr(0)
                self.state = 374
                self.match(MicroCParser.T__8)
                localctx.node =  MallocNode(localctx._expr.node)
                pass
            elif token in [MicroCParser.T__23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.match(MicroCParser.T__23)
                self.state = 378
                self.match(MicroCParser.T__7)
                self.state = 379
                localctx._expr = self.expr(0)
                self.state = 380
                self.match(MicroCParser.T__8)
                localctx.node =  FreeNode(localctx._expr.node)
                pass
            elif token in [MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 383
                localctx._ident = self.ident()
                self.state = 384
                self.match(MicroCParser.T__7)
                self.state = 385
                localctx._arg_list = self.arg_list()
                self.state = 386
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
        self.enterRule(localctx, 66, self.RULE_arg_list)
        try:
            self.state = 396
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__3, MicroCParser.T__7, MicroCParser.T__18, MicroCParser.T__19, MicroCParser.T__22, MicroCParser.T__23, MicroCParser.IDENTIFIER, MicroCParser.INT_LITERAL, MicroCParser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                localctx._expr = self.expr(0)
                self.state = 392
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
        self.enterRule(localctx, 68, self.RULE_args_rest)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(MicroCParser.T__11)
                self.state = 399
                localctx._expr = self.expr(0)
                self.state = 400
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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            localctx._term = self.term(0)
            localctx.node =  localctx._term.node
            self._ctx.stop = self._input.LT(-1)
            self.state = 422
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 420
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = MicroCParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 410
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 411
                        self.match(MicroCParser.T__24)
                        self.state = 412
                        localctx._term = self.term(0)
                        localctx.node =  BinaryOpNode(localctx.e1.node, localctx._term.node, '+')
                        pass

                    elif la_ == 2:
                        localctx = MicroCParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e2 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 415
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 416
                        self.match(MicroCParser.T__18)
                        self.state = 417
                        localctx._term = self.term(0)
                        localctx.node =  BinaryOpNode(localctx.e2.node, localctx._term.node, '-')
                        pass

             
                self.state = 424
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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            localctx._primary = self.primary()
            localctx.node =  localctx._primary.node
            self._ctx.stop = self._input.LT(-1)
            self.state = 441
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 439
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = MicroCParser.TermContext(self, _parentctx, _parentState)
                        localctx.t1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 429
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 430
                        self.match(MicroCParser.T__3)
                        self.state = 431
                        localctx._primary = self.primary()
                        localctx.node =  BinaryOpNode(localctx.t1.node, localctx._primary.node, '*')
                        pass

                    elif la_ == 2:
                        localctx = MicroCParser.TermContext(self, _parentctx, _parentState)
                        localctx.t2 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 434
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 435
                        self.match(MicroCParser.T__25)
                        self.state = 436
                        localctx._primary = self.primary()
                        localctx.node =  BinaryOpNode(localctx.t2.node, localctx._primary.node, '/')
                        pass

             
                self.state = 443
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
        self.enterRule(localctx, 74, self.RULE_cond)
        try:
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                localctx.e1 = self.expr(0)
                self.state = 445
                self.match(MicroCParser.T__26)
                self.state = 446
                localctx.e2 = self.expr(0)
                localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, '<')
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 449
                localctx.e1 = self.expr(0)
                self.state = 450
                self.match(MicroCParser.T__27)
                self.state = 451
                localctx.e2 = self.expr(0)
                localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, '<=')
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 454
                localctx.e1 = self.expr(0)
                self.state = 455
                self.match(MicroCParser.T__28)
                self.state = 456
                localctx.e2 = self.expr(0)
                localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, '>=')
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 459
                localctx.e1 = self.expr(0)
                self.state = 460
                self.match(MicroCParser.T__29)
                self.state = 461
                localctx.e2 = self.expr(0)
                localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, '==')
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 464
                localctx.e1 = self.expr(0)
                self.state = 465
                self.match(MicroCParser.T__30)
                self.state = 466
                localctx.e2 = self.expr(0)
                localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, '!=')
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 469
                localctx.e1 = self.expr(0)
                self.state = 470
                self.match(MicroCParser.T__31)
                self.state = 471
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
        self.enterRule(localctx, 76, self.RULE_cmpop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
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
        self.enterRule(localctx, 78, self.RULE_mulop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
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
        self.enterRule(localctx, 80, self.RULE_addop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
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
        self._predicates[35] = self.expr_sempred
        self._predicates[36] = self.term_sempred
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
         




