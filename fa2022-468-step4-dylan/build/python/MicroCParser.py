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


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\"")
        buf.write("\u016e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3S\n\3\3\4\3\4\3\4")
        buf.write("\3\4\5\4Y\n\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\5\bm\n\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\5\n|\n\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\5\f\u008f\n\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\5\r\u0097\n\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00a2\n\17\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\5\20\u00ae\n\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00bc")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\5\26\u00ea\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u0107\n\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\33\3\33\3\33\3\33\3\33\5\33\u0118\n\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\5\34\u0120\n\34\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\7\35\u0130\n\35\f\35\16\35\u0133\13\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\7\36\u0143\n\36\f\36\16\36\u0146\13\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0166\n\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3\"\2\48:#\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@B\2\5\3\2\27\34\3\2")
        buf.write("\25\26\3\2\23\24\2\u016b\2D\3\2\2\2\4R\3\2\2\2\6X\3\2")
        buf.write("\2\2\bZ\3\2\2\2\n\\\3\2\2\2\fa\3\2\2\2\16l\3\2\2\2\20")
        buf.write("n\3\2\2\2\22{\3\2\2\2\24}\3\2\2\2\26\u008e\3\2\2\2\30")
        buf.write("\u0096\3\2\2\2\32\u0098\3\2\2\2\34\u00a1\3\2\2\2\36\u00ad")
        buf.write("\3\2\2\2 \u00bb\3\2\2\2\"\u00bd\3\2\2\2$\u00c3\3\2\2\2")
        buf.write("&\u00c9\3\2\2\2(\u00cd\3\2\2\2*\u00e9\3\2\2\2,\u00eb\3")
        buf.write("\2\2\2.\u0106\3\2\2\2\60\u0108\3\2\2\2\62\u010c\3\2\2")
        buf.write("\2\64\u0117\3\2\2\2\66\u011f\3\2\2\28\u0121\3\2\2\2:\u0134")
        buf.write("\3\2\2\2<\u0165\3\2\2\2>\u0167\3\2\2\2@\u0169\3\2\2\2")
        buf.write("B\u016b\3\2\2\2DE\5\4\3\2EF\5\22\n\2FG\b\2\1\2G\3\3\2")
        buf.write("\2\2HI\5\n\6\2IJ\5\4\3\2JS\3\2\2\2KL\5\f\7\2LM\5\4\3\2")
        buf.write("MS\3\2\2\2NO\5\20\t\2OP\5\4\3\2PS\3\2\2\2QS\3\2\2\2RH")
        buf.write("\3\2\2\2RK\3\2\2\2RN\3\2\2\2RQ\3\2\2\2S\5\3\2\2\2TU\5")
        buf.write("\n\6\2UV\5\6\4\2VY\3\2\2\2WY\3\2\2\2XT\3\2\2\2XW\3\2\2")
        buf.write("\2Y\7\3\2\2\2Z[\7\35\2\2[\t\3\2\2\2\\]\5\16\b\2]^\5\b")
        buf.write("\5\2^_\7\3\2\2_`\b\6\1\2`\13\3\2\2\2ab\7\4\2\2bc\5\b\5")
        buf.write("\2cd\7\5\2\2de\7 \2\2ef\7\3\2\2fg\b\7\1\2g\r\3\2\2\2h")
        buf.write("i\7\6\2\2im\b\b\1\2jk\7\7\2\2km\b\b\1\2lh\3\2\2\2lj\3")
        buf.write("\2\2\2m\17\3\2\2\2no\5\16\b\2op\5\b\5\2pq\7\b\2\2qr\5")
        buf.write("\26\f\2rs\7\t\2\2st\7\3\2\2tu\b\t\1\2u\21\3\2\2\2vw\5")
        buf.write("\24\13\2wx\5\22\n\2xy\b\n\1\2y|\3\2\2\2z|\b\n\1\2{v\3")
        buf.write("\2\2\2{z\3\2\2\2|\23\3\2\2\2}~\5\16\b\2~\177\5\b\5\2\177")
        buf.write("\u0080\7\b\2\2\u0080\u0081\5\26\f\2\u0081\u0082\7\t\2")
        buf.write("\2\u0082\u0083\b\13\1\2\u0083\u0084\7\n\2\2\u0084\u0085")
        buf.write("\5\6\4\2\u0085\u0086\5\34\17\2\u0086\u0087\7\13\2\2\u0087")
        buf.write("\u0088\b\13\1\2\u0088\25\3\2\2\2\u0089\u008a\5\32\16\2")
        buf.write("\u008a\u008b\5\30\r\2\u008b\u008c\b\f\1\2\u008c\u008f")
        buf.write("\3\2\2\2\u008d\u008f\b\f\1\2\u008e\u0089\3\2\2\2\u008e")
        buf.write("\u008d\3\2\2\2\u008f\27\3\2\2\2\u0090\u0091\7\f\2\2\u0091")
        buf.write("\u0092\5\32\16\2\u0092\u0093\5\30\r\2\u0093\u0094\b\r")
        buf.write("\1\2\u0094\u0097\3\2\2\2\u0095\u0097\b\r\1\2\u0096\u0090")
        buf.write("\3\2\2\2\u0096\u0095\3\2\2\2\u0097\31\3\2\2\2\u0098\u0099")
        buf.write("\5\16\b\2\u0099\u009a\5\b\5\2\u009a\u009b\b\16\1\2\u009b")
        buf.write("\33\3\2\2\2\u009c\u009d\5\36\20\2\u009d\u009e\5\34\17")
        buf.write("\2\u009e\u009f\b\17\1\2\u009f\u00a2\3\2\2\2\u00a0\u00a2")
        buf.write("\b\17\1\2\u00a1\u009c\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2")
        buf.write("\35\3\2\2\2\u00a3\u00a4\5 \21\2\u00a4\u00a5\7\3\2\2\u00a5")
        buf.write("\u00a6\b\20\1\2\u00a6\u00ae\3\2\2\2\u00a7\u00a8\5*\26")
        buf.write("\2\u00a8\u00a9\b\20\1\2\u00a9\u00ae\3\2\2\2\u00aa\u00ab")
        buf.write("\5,\27\2\u00ab\u00ac\b\20\1\2\u00ac\u00ae\3\2\2\2\u00ad")
        buf.write("\u00a3\3\2\2\2\u00ad\u00a7\3\2\2\2\u00ad\u00aa\3\2\2\2")
        buf.write("\u00ae\37\3\2\2\2\u00af\u00b0\5(\25\2\u00b0\u00b1\b\21")
        buf.write("\1\2\u00b1\u00bc\3\2\2\2\u00b2\u00b3\5\"\22\2\u00b3\u00b4")
        buf.write("\b\21\1\2\u00b4\u00bc\3\2\2\2\u00b5\u00b6\5$\23\2\u00b6")
        buf.write("\u00b7\b\21\1\2\u00b7\u00bc\3\2\2\2\u00b8\u00b9\5&\24")
        buf.write("\2\u00b9\u00ba\b\21\1\2\u00ba\u00bc\3\2\2\2\u00bb\u00af")
        buf.write("\3\2\2\2\u00bb\u00b2\3\2\2\2\u00bb\u00b5\3\2\2\2\u00bb")
        buf.write("\u00b8\3\2\2\2\u00bc!\3\2\2\2\u00bd\u00be\7\r\2\2\u00be")
        buf.write("\u00bf\7\b\2\2\u00bf\u00c0\5\b\5\2\u00c0\u00c1\7\t\2\2")
        buf.write("\u00c1\u00c2\b\22\1\2\u00c2#\3\2\2\2\u00c3\u00c4\7\16")
        buf.write("\2\2\u00c4\u00c5\7\b\2\2\u00c5\u00c6\58\35\2\u00c6\u00c7")
        buf.write("\7\t\2\2\u00c7\u00c8\b\23\1\2\u00c8%\3\2\2\2\u00c9\u00ca")
        buf.write("\7\17\2\2\u00ca\u00cb\58\35\2\u00cb\u00cc\b\24\1\2\u00cc")
        buf.write("\'\3\2\2\2\u00cd\u00ce\5\b\5\2\u00ce\u00cf\7\5\2\2\u00cf")
        buf.write("\u00d0\58\35\2\u00d0\u00d1\b\25\1\2\u00d1)\3\2\2\2\u00d2")
        buf.write("\u00d3\7\20\2\2\u00d3\u00d4\7\b\2\2\u00d4\u00d5\5<\37")
        buf.write("\2\u00d5\u00d6\7\t\2\2\u00d6\u00d7\7\n\2\2\u00d7\u00d8")
        buf.write("\5\34\17\2\u00d8\u00d9\7\13\2\2\u00d9\u00da\7\21\2\2\u00da")
        buf.write("\u00db\7\n\2\2\u00db\u00dc\5\34\17\2\u00dc\u00dd\7\13")
        buf.write("\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\b\26\1\2\u00df\u00ea")
        buf.write("\3\2\2\2\u00e0\u00e1\7\20\2\2\u00e1\u00e2\7\b\2\2\u00e2")
        buf.write("\u00e3\5<\37\2\u00e3\u00e4\7\t\2\2\u00e4\u00e5\7\n\2\2")
        buf.write("\u00e5\u00e6\5\34\17\2\u00e6\u00e7\7\13\2\2\u00e7\u00e8")
        buf.write("\b\26\1\2\u00e8\u00ea\3\2\2\2\u00e9\u00d2\3\2\2\2\u00e9")
        buf.write("\u00e0\3\2\2\2\u00ea+\3\2\2\2\u00eb\u00ec\7\22\2\2\u00ec")
        buf.write("\u00ed\7\b\2\2\u00ed\u00ee\5<\37\2\u00ee\u00ef\7\t\2\2")
        buf.write("\u00ef\u00f0\7\n\2\2\u00f0\u00f1\5\34\17\2\u00f1\u00f2")
        buf.write("\7\13\2\2\u00f2\u00f3\b\27\1\2\u00f3-\3\2\2\2\u00f4\u00f5")
        buf.write("\5\b\5\2\u00f5\u00f6\b\30\1\2\u00f6\u0107\3\2\2\2\u00f7")
        buf.write("\u00f8\7\b\2\2\u00f8\u00f9\58\35\2\u00f9\u00fa\7\t\2\2")
        buf.write("\u00fa\u00fb\b\30\1\2\u00fb\u0107\3\2\2\2\u00fc\u00fd")
        buf.write("\5\60\31\2\u00fd\u00fe\b\30\1\2\u00fe\u0107\3\2\2\2\u00ff")
        buf.write("\u0100\5\62\32\2\u0100\u0101\b\30\1\2\u0101\u0107\3\2")
        buf.write("\2\2\u0102\u0103\7\36\2\2\u0103\u0107\b\30\1\2\u0104\u0105")
        buf.write("\7\37\2\2\u0105\u0107\b\30\1\2\u0106\u00f4\3\2\2\2\u0106")
        buf.write("\u00f7\3\2\2\2\u0106\u00fc\3\2\2\2\u0106\u00ff\3\2\2\2")
        buf.write("\u0106\u0102\3\2\2\2\u0106\u0104\3\2\2\2\u0107/\3\2\2")
        buf.write("\2\u0108\u0109\7\23\2\2\u0109\u010a\58\35\2\u010a\u010b")
        buf.write("\b\31\1\2\u010b\61\3\2\2\2\u010c\u010d\5\b\5\2\u010d\u010e")
        buf.write("\7\b\2\2\u010e\u010f\5\64\33\2\u010f\u0110\7\t\2\2\u0110")
        buf.write("\u0111\b\32\1\2\u0111\63\3\2\2\2\u0112\u0113\58\35\2\u0113")
        buf.write("\u0114\5\66\34\2\u0114\u0115\b\33\1\2\u0115\u0118\3\2")
        buf.write("\2\2\u0116\u0118\b\33\1\2\u0117\u0112\3\2\2\2\u0117\u0116")
        buf.write("\3\2\2\2\u0118\65\3\2\2\2\u0119\u011a\7\f\2\2\u011a\u011b")
        buf.write("\58\35\2\u011b\u011c\5\66\34\2\u011c\u011d\b\34\1\2\u011d")
        buf.write("\u0120\3\2\2\2\u011e\u0120\b\34\1\2\u011f\u0119\3\2\2")
        buf.write("\2\u011f\u011e\3\2\2\2\u0120\67\3\2\2\2\u0121\u0122\b")
        buf.write("\35\1\2\u0122\u0123\5:\36\2\u0123\u0124\b\35\1\2\u0124")
        buf.write("\u0131\3\2\2\2\u0125\u0126\f\4\2\2\u0126\u0127\7\24\2")
        buf.write("\2\u0127\u0128\5:\36\2\u0128\u0129\b\35\1\2\u0129\u0130")
        buf.write("\3\2\2\2\u012a\u012b\f\3\2\2\u012b\u012c\7\23\2\2\u012c")
        buf.write("\u012d\5:\36\2\u012d\u012e\b\35\1\2\u012e\u0130\3\2\2")
        buf.write("\2\u012f\u0125\3\2\2\2\u012f\u012a\3\2\2\2\u0130\u0133")
        buf.write("\3\2\2\2\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132")
        buf.write("9\3\2\2\2\u0133\u0131\3\2\2\2\u0134\u0135\b\36\1\2\u0135")
        buf.write("\u0136\5.\30\2\u0136\u0137\b\36\1\2\u0137\u0144\3\2\2")
        buf.write("\2\u0138\u0139\f\4\2\2\u0139\u013a\7\25\2\2\u013a\u013b")
        buf.write("\5.\30\2\u013b\u013c\b\36\1\2\u013c\u0143\3\2\2\2\u013d")
        buf.write("\u013e\f\3\2\2\u013e\u013f\7\26\2\2\u013f\u0140\5.\30")
        buf.write("\2\u0140\u0141\b\36\1\2\u0141\u0143\3\2\2\2\u0142\u0138")
        buf.write("\3\2\2\2\u0142\u013d\3\2\2\2\u0143\u0146\3\2\2\2\u0144")
        buf.write("\u0142\3\2\2\2\u0144\u0145\3\2\2\2\u0145;\3\2\2\2\u0146")
        buf.write("\u0144\3\2\2\2\u0147\u0148\58\35\2\u0148\u0149\7\27\2")
        buf.write("\2\u0149\u014a\58\35\2\u014a\u014b\b\37\1\2\u014b\u0166")
        buf.write("\3\2\2\2\u014c\u014d\58\35\2\u014d\u014e\7\30\2\2\u014e")
        buf.write("\u014f\58\35\2\u014f\u0150\b\37\1\2\u0150\u0166\3\2\2")
        buf.write("\2\u0151\u0152\58\35\2\u0152\u0153\7\31\2\2\u0153\u0154")
        buf.write("\58\35\2\u0154\u0155\b\37\1\2\u0155\u0166\3\2\2\2\u0156")
        buf.write("\u0157\58\35\2\u0157\u0158\7\32\2\2\u0158\u0159\58\35")
        buf.write("\2\u0159\u015a\b\37\1\2\u015a\u0166\3\2\2\2\u015b\u015c")
        buf.write("\58\35\2\u015c\u015d\7\33\2\2\u015d\u015e\58\35\2\u015e")
        buf.write("\u015f\b\37\1\2\u015f\u0166\3\2\2\2\u0160\u0161\58\35")
        buf.write("\2\u0161\u0162\7\34\2\2\u0162\u0163\58\35\2\u0163\u0164")
        buf.write("\b\37\1\2\u0164\u0166\3\2\2\2\u0165\u0147\3\2\2\2\u0165")
        buf.write("\u014c\3\2\2\2\u0165\u0151\3\2\2\2\u0165\u0156\3\2\2\2")
        buf.write("\u0165\u015b\3\2\2\2\u0165\u0160\3\2\2\2\u0166=\3\2\2")
        buf.write("\2\u0167\u0168\t\2\2\2\u0168?\3\2\2\2\u0169\u016a\t\3")
        buf.write("\2\2\u016aA\3\2\2\2\u016b\u016c\t\4\2\2\u016cC\3\2\2\2")
        buf.write("\24RXl{\u008e\u0096\u00a1\u00ad\u00bb\u00e9\u0106\u0117")
        buf.write("\u011f\u012f\u0131\u0142\u0144\u0165")
        return buf.getvalue()


class MicroCParser ( Parser ):

    grammarFileName = "MicroC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'string'", "'='", "'int'", "'float'", 
                     "'('", "')'", "'{'", "'}'", "','", "'read'", "'print'", 
                     "'return'", "'if'", "'else'", "'while'", "'-'", "'+'", 
                     "'*'", "'/'", "'<'", "'<='", "'>='", "'=='", "'!='", 
                     "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "INT_LITERAL", "FLOAT_LITERAL", "STR_LITERAL", "COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_var_decls = 2
    RULE_ident = 3
    RULE_var_decl = 4
    RULE_str_decl = 5
    RULE_base_type = 6
    RULE_func_decl = 7
    RULE_functions = 8
    RULE_function = 9
    RULE_params = 10
    RULE_params_rest = 11
    RULE_param = 12
    RULE_statements = 13
    RULE_statement = 14
    RULE_base_stmt = 15
    RULE_read_stmt = 16
    RULE_print_stmt = 17
    RULE_return_stmt = 18
    RULE_assign_stmt = 19
    RULE_if_stmt = 20
    RULE_while_stmt = 21
    RULE_primary = 22
    RULE_unaryminus_expr = 23
    RULE_call_expr = 24
    RULE_arg_list = 25
    RULE_args_rest = 26
    RULE_expr = 27
    RULE_term = 28
    RULE_cond = 29
    RULE_cmpop = 30
    RULE_mulop = 31
    RULE_addop = 32

    ruleNames =  [ "program", "decls", "var_decls", "ident", "var_decl", 
                   "str_decl", "base_type", "func_decl", "functions", "function", 
                   "params", "params_rest", "param", "statements", "statement", 
                   "base_stmt", "read_stmt", "print_stmt", "return_stmt", 
                   "assign_stmt", "if_stmt", "while_stmt", "primary", "unaryminus_expr", 
                   "call_expr", "arg_list", "args_rest", "expr", "term", 
                   "cond", "cmpop", "mulop", "addop" ]

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
    IDENTIFIER=27
    INT_LITERAL=28
    FLOAT_LITERAL=29
    STR_LITERAL=30
    COMMENT=31
    WS=32

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
            self.state = 66
            self.decls()
            self.state = 67
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
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.var_decl()
                self.state = 71
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.str_decl()
                self.state = 74
                self.decls()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.func_decl()
                self.state = 77
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
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__3, MicroCParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.var_decl()
                self.state = 83
                self.var_decls()
                pass
            elif token in [MicroCParser.T__8, MicroCParser.T__10, MicroCParser.T__11, MicroCParser.T__12, MicroCParser.T__13, MicroCParser.T__15, MicroCParser.IDENTIFIER]:
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
            self.state = 88
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
            self._base_type = None # Base_typeContext
            self._ident = None # IdentContext

        def base_type(self):
            return self.getTypedRuleContext(MicroCParser.Base_typeContext,0)


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
            self.state = 90
            localctx._base_type = self.base_type()
            self.state = 91
            localctx._ident = self.ident()
            self.state = 92
            self.match(MicroCParser.T__0)
            self.st.addVariable(localctx._base_type.t, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
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
            self.state = 95
            self.match(MicroCParser.T__1)
            self.state = 96
            localctx._ident = self.ident()
            self.state = 97
            self.match(MicroCParser.T__2)
            self.state = 98
            localctx.val = self.match(MicroCParser.STR_LITERAL)
            self.state = 99
            self.match(MicroCParser.T__0)
            self.st.addVariable(Scope.Type.STRING, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), (None if localctx.val is None else localctx.val.text));
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 12, self.RULE_base_type)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(MicroCParser.T__3)
                localctx.t =  Scope.Type.INT
                pass
            elif token in [MicroCParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(MicroCParser.T__4)
                localctx.t =  Scope.Type.FLOAT
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
            self._base_type = None # Base_typeContext
            self._ident = None # IdentContext
            self._params = None # ParamsContext

        def base_type(self):
            return self.getTypedRuleContext(MicroCParser.Base_typeContext,0)


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
        self.enterRule(localctx, 14, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            localctx._base_type = self.base_type()
            self.state = 109
            localctx._ident = self.ident()
            self.state = 110
            self.match(MicroCParser.T__5)
            self.state = 111
            localctx._params = self.params()
            self.state = 112
            self.match(MicroCParser.T__6)
            self.state = 113
            self.match(MicroCParser.T__0)
            self.st.addFunction(localctx._base_type.t, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), localctx._params.types);
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
        self.enterRule(localctx, 16, self.RULE_functions)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__3, MicroCParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                localctx._function = self.function()
                self.state = 117
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
            self._base_type = None # Base_typeContext
            self._ident = None # IdentContext
            self._params = None # ParamsContext
            self._statements = None # StatementsContext

        def base_type(self):
            return self.getTypedRuleContext(MicroCParser.Base_typeContext,0)


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
        self.enterRule(localctx, 18, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            localctx._base_type = self.base_type()
            self.state = 124
            localctx._ident = self.ident()
            self.state = 125
            self.match(MicroCParser.T__5)
            self.state = 126
            localctx._params = self.params()
            self.state = 127
            self.match(MicroCParser.T__6)

            # Add FunctionSymbolTable entry to global scope
            ste = self.st.getSymbolTableEntry((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
            if (ste == None) or not ste.isDefined():
              self.st.addFunction(localctx._base_type.t, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), localctx._params.types);          
              ste = self.st.getSymbolTableEntry((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
              ste.setDefined(True);
            else:
              raise Exception("Function already defined");
            self.st.pushScope((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
            self.addParams(localctx._params.types, localctx._params.names);

            self.state = 129
            self.match(MicroCParser.T__7)
            self.state = 130
            self.var_decls()
            self.state = 131
            localctx._statements = self.statements()
            self.state = 132
            self.match(MicroCParser.T__8)

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
        self.enterRule(localctx, 20, self.RULE_params)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__3, MicroCParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                localctx._param = self.param()
                self.state = 136
                localctx._params_rest = self.params_rest()

                localctx.names =  []
                localctx.types =  []
                localctx.names.append(localctx._param.name);
                localctx.names.extend(localctx._params_rest.names);
                localctx.types.append(localctx._param.type);
                localctx.types.extend(localctx._params_rest.types);

                pass
            elif token in [MicroCParser.T__6]:
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
        self.enterRule(localctx, 22, self.RULE_params_rest)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(MicroCParser.T__9)
                self.state = 143
                localctx._param = self.param()
                self.state = 144
                localctx._params_rest = self.params_rest()

                localctx.names =  []
                localctx.types =  []
                localctx.names.append(localctx._param.name);
                localctx.names.extend(localctx._params_rest.names);
                localctx.types.append(localctx._param.type);
                localctx.types.extend(localctx._params_rest.types);

                pass
            elif token in [MicroCParser.T__6]:
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
            self.type = None
            self._base_type = None # Base_typeContext
            self._ident = None # IdentContext

        def base_type(self):
            return self.getTypedRuleContext(MicroCParser.Base_typeContext,0)


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
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            localctx._base_type = self.base_type()
            self.state = 151
            localctx._ident = self.ident()

            localctx.name =  (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop))
            localctx.type =  localctx._base_type.t

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
        self.enterRule(localctx, 26, self.RULE_statements)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__10, MicroCParser.T__11, MicroCParser.T__12, MicroCParser.T__13, MicroCParser.T__15, MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                localctx._statement = self.statement()
                self.state = 155
                localctx.s = self.statements()
                localctx.node =  StatementListNode(localctx._statement.node, localctx.s.node.getStatements())
                pass
            elif token in [MicroCParser.T__8]:
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
        self.enterRule(localctx, 28, self.RULE_statement)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__10, MicroCParser.T__11, MicroCParser.T__12, MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                localctx._base_stmt = self.base_stmt()
                self.state = 162
                self.match(MicroCParser.T__0)
                localctx.node =  localctx._base_stmt.node
                pass
            elif token in [MicroCParser.T__13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                localctx._if_stmt = self.if_stmt()
                localctx.node = localctx._if_stmt.node
                pass
            elif token in [MicroCParser.T__15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 168
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

        def assign_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Assign_stmtContext,0)


        def read_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Read_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Print_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Return_stmtContext,0)


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
        self.enterRule(localctx, 30, self.RULE_base_stmt)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                localctx._assign_stmt = self.assign_stmt()
                localctx.node =  localctx._assign_stmt.node
                pass
            elif token in [MicroCParser.T__10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                localctx._read_stmt = self.read_stmt()
                localctx.node =  localctx._read_stmt.node
                pass
            elif token in [MicroCParser.T__11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                localctx._print_stmt = self.print_stmt()
                localctx.node =  localctx._print_stmt.node
                pass
            elif token in [MicroCParser.T__12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 182
                localctx._return_stmt = self.return_stmt()
                localctx.node =  localctx._return_stmt.node
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
        self.enterRule(localctx, 32, self.RULE_read_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(MicroCParser.T__10)
            self.state = 188
            self.match(MicroCParser.T__5)
            self.state = 189
            localctx._ident = self.ident()
            self.state = 190
            self.match(MicroCParser.T__6)
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
        self.enterRule(localctx, 34, self.RULE_print_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(MicroCParser.T__11)
            self.state = 194
            self.match(MicroCParser.T__5)
            self.state = 195
            localctx._expr = self.expr(0)
            self.state = 196
            self.match(MicroCParser.T__6)
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
        self.enterRule(localctx, 36, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(MicroCParser.T__12)
            self.state = 200
            localctx._expr = self.expr(0)
            localctx.node =  ReturnNode(localctx._expr.node, self.st.getFunctionSymbol(self.st.currentScope().getName()))
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
            self._ident = None # IdentContext
            self._expr = None # ExprContext

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


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
        self.enterRule(localctx, 38, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            localctx._ident = self.ident()
            self.state = 204
            self.match(MicroCParser.T__2)
            self.state = 205
            localctx._expr = self.expr(0)
            localctx.node =  AssignNode(VarNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop))), localctx._expr.node)
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
        self.enterRule(localctx, 40, self.RULE_if_stmt)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(MicroCParser.T__13)
                self.state = 209
                self.match(MicroCParser.T__5)
                self.state = 210
                localctx._cond = self.cond()
                self.state = 211
                self.match(MicroCParser.T__6)
                self.state = 212
                self.match(MicroCParser.T__7)
                self.state = 213
                localctx.t1 = self.statements()
                self.state = 214
                self.match(MicroCParser.T__8)

                self.state = 215
                self.match(MicroCParser.T__14)
                self.state = 216
                self.match(MicroCParser.T__7)
                self.state = 217
                localctx.e1 = self.statements()
                self.state = 218
                self.match(MicroCParser.T__8)
                localctx.node =  IfStatementNode(localctx._cond.node, localctx.t1.node, localctx.e1.node)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.match(MicroCParser.T__13)
                self.state = 223
                self.match(MicroCParser.T__5)
                self.state = 224
                localctx._cond = self.cond()
                self.state = 225
                self.match(MicroCParser.T__6)
                self.state = 226
                self.match(MicroCParser.T__7)
                self.state = 227
                localctx.t1 = self.statements()
                self.state = 228
                self.match(MicroCParser.T__8)
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
        self.enterRule(localctx, 42, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(MicroCParser.T__15)
            self.state = 234
            self.match(MicroCParser.T__5)
            self.state = 235
            localctx._cond = self.cond()
            self.state = 236
            self.match(MicroCParser.T__6)
            self.state = 237
            self.match(MicroCParser.T__7)
            self.state = 238
            localctx._statements = self.statements()
            self.state = 239
            self.match(MicroCParser.T__8)
            localctx.node =  WhileNode(localctx._cond.node, localctx._statements.node)
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
            self._ident = None # IdentContext
            self._expr = None # ExprContext
            self._unaryminus_expr = None # Unaryminus_exprContext
            self._call_expr = None # Call_exprContext
            self.il = None # Token
            self.fl = None # Token

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def unaryminus_expr(self):
            return self.getTypedRuleContext(MicroCParser.Unaryminus_exprContext,0)


        def call_expr(self):
            return self.getTypedRuleContext(MicroCParser.Call_exprContext,0)


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
        self.enterRule(localctx, 44, self.RULE_primary)
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                localctx._ident = self.ident()
                localctx.node =  VarNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.match(MicroCParser.T__5)
                self.state = 246
                localctx._expr = self.expr(0)
                self.state = 247
                self.match(MicroCParser.T__6)
                localctx.node =  localctx._expr.node
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 250
                localctx._unaryminus_expr = self.unaryminus_expr()
                localctx.node =  localctx._unaryminus_expr.node
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 253
                localctx._call_expr = self.call_expr()
                localctx.node =  localctx._call_expr.node
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 256
                localctx.il = self.match(MicroCParser.INT_LITERAL)
                localctx.node =  IntLitNode((None if localctx.il is None else localctx.il.text))
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 258
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
        self.enterRule(localctx, 46, self.RULE_unaryminus_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(MicroCParser.T__16)
            self.state = 263
            localctx._expr = self.expr(0)
            localctx.node =  UnaryOpNode(localctx._expr.node, '-')
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
            self._ident = None # IdentContext
            self._arg_list = None # Arg_listContext

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
        self.enterRule(localctx, 48, self.RULE_call_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            localctx._ident = self.ident()
            self.state = 267
            self.match(MicroCParser.T__5)
            self.state = 268
            localctx._arg_list = self.arg_list()
            self.state = 269
            self.match(MicroCParser.T__6)
            localctx.node =  CallNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), localctx._arg_list.args)
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
        self.enterRule(localctx, 50, self.RULE_arg_list)
        try:
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__5, MicroCParser.T__16, MicroCParser.IDENTIFIER, MicroCParser.INT_LITERAL, MicroCParser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                localctx._expr = self.expr(0)
                self.state = 273
                localctx._args_rest = self.args_rest()

                localctx.args =  []
                localctx.args.append(localctx._expr.node);
                localctx.args.extend(localctx._args_rest.args);

                pass
            elif token in [MicroCParser.T__6]:
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
        self.enterRule(localctx, 52, self.RULE_args_rest)
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MicroCParser.T__9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.match(MicroCParser.T__9)
                self.state = 280
                localctx._expr = self.expr(0)
                self.state = 281
                localctx._args_rest = self.args_rest()

                localctx.args =  []
                localctx.args.append(localctx._expr.node);
                localctx.args.extend(localctx._args_rest.args);

                pass
            elif token in [MicroCParser.T__6]:
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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            localctx._term = self.term(0)
            localctx.node =  localctx._term.node
            self._ctx.stop = self._input.LT(-1)
            self.state = 303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 301
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = MicroCParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 291
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 292
                        self.match(MicroCParser.T__17)
                        self.state = 293
                        localctx._term = self.term(0)
                        localctx.node =  BinaryOpNode(localctx.e1.node, localctx._term.node, '+')
                        pass

                    elif la_ == 2:
                        localctx = MicroCParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e2 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 296
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 297
                        self.match(MicroCParser.T__16)
                        self.state = 298
                        localctx._term = self.term(0)
                        localctx.node =  BinaryOpNode(localctx.e2.node, localctx._term.node, '-')
                        pass

             
                self.state = 305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            localctx._primary = self.primary()
            localctx.node =  localctx._primary.node
            self._ctx.stop = self._input.LT(-1)
            self.state = 322
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 320
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = MicroCParser.TermContext(self, _parentctx, _parentState)
                        localctx.t1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 310
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 311
                        self.match(MicroCParser.T__18)
                        self.state = 312
                        localctx._primary = self.primary()
                        localctx.node =  BinaryOpNode(localctx.t1.node, localctx._primary.node, '*')
                        pass

                    elif la_ == 2:
                        localctx = MicroCParser.TermContext(self, _parentctx, _parentState)
                        localctx.t2 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 315
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 316
                        self.match(MicroCParser.T__19)
                        self.state = 317
                        localctx._primary = self.primary()
                        localctx.node =  BinaryOpNode(localctx.t2.node, localctx._primary.node, '/')
                        pass

             
                self.state = 324
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self.enterRule(localctx, 58, self.RULE_cond)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                localctx.e1 = self.expr(0)
                self.state = 326
                self.match(MicroCParser.T__20)
                self.state = 327
                localctx.e2 = self.expr(0)
                localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, '<')
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                localctx.e1 = self.expr(0)
                self.state = 331
                self.match(MicroCParser.T__21)
                self.state = 332
                localctx.e2 = self.expr(0)
                localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, '<=')
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 335
                localctx.e1 = self.expr(0)
                self.state = 336
                self.match(MicroCParser.T__22)
                self.state = 337
                localctx.e2 = self.expr(0)
                localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, '>=')
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 340
                localctx.e1 = self.expr(0)
                self.state = 341
                self.match(MicroCParser.T__23)
                self.state = 342
                localctx.e2 = self.expr(0)
                localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, '==')
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 345
                localctx.e1 = self.expr(0)
                self.state = 346
                self.match(MicroCParser.T__24)
                self.state = 347
                localctx.e2 = self.expr(0)
                localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, '!=')
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 350
                localctx.e1 = self.expr(0)
                self.state = 351
                self.match(MicroCParser.T__25)
                self.state = 352
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
        self.enterRule(localctx, 60, self.RULE_cmpop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MicroCParser.T__20) | (1 << MicroCParser.T__21) | (1 << MicroCParser.T__22) | (1 << MicroCParser.T__23) | (1 << MicroCParser.T__24) | (1 << MicroCParser.T__25))) != 0)):
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
        self.enterRule(localctx, 62, self.RULE_mulop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            _la = self._input.LA(1)
            if not(_la==MicroCParser.T__18 or _la==MicroCParser.T__19):
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
        self.enterRule(localctx, 64, self.RULE_addop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            _la = self._input.LA(1)
            if not(_la==MicroCParser.T__16 or _la==MicroCParser.T__17):
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
        self._predicates[27] = self.expr_sempred
        self._predicates[28] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




