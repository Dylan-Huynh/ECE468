// Generated from /Users/chief/Documents/GitHub/fa2022-468-step3-dylan/python/MicroC.g4 by ANTLR 4.9.2


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
from MicroCCompiler.ast.StatementListNode import StatementListNode
from MicroCCompiler.ast.ASTNode import ASTNode
from MicroCCompiler.ast.BinaryOpNode import BinaryOpNode
from MicroCCompiler.ast.UnaryOpNode import UnaryOpNode
from MicroCCompiler.ast.IfStatementNode import IfStatementNode
from MicroCCompiler.ast.WhileNode import WhileNode

import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MicroCParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, IDENTIFIER=27, INT_LITERAL=28, FLOAT_LITERAL=29, STR_LITERAL=30, 
		COMMENT=31, WS=32;
	public static final int
		RULE_program = 0, RULE_decls = 1, RULE_var_decls = 2, RULE_ident = 3, 
		RULE_var_decl = 4, RULE_str_decl = 5, RULE_base_type = 6, RULE_function = 7, 
		RULE_statements = 8, RULE_statement = 9, RULE_base_stmt = 10, RULE_read_stmt = 11, 
		RULE_print_stmt = 12, RULE_return_stmt = 13, RULE_assign_stmt = 14, RULE_if_stmt = 15, 
		RULE_while_stmt = 16, RULE_primary = 17, RULE_unaryminus_expr = 18, RULE_expr = 19, 
		RULE_term = 20, RULE_cond = 21, RULE_cmpop = 22, RULE_mulop = 23, RULE_addop = 24;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "decls", "var_decls", "ident", "var_decl", "str_decl", "base_type", 
			"function", "statements", "statement", "base_stmt", "read_stmt", "print_stmt", 
			"return_stmt", "assign_stmt", "if_stmt", "while_stmt", "primary", "unaryminus_expr", 
			"expr", "term", "cond", "cmpop", "mulop", "addop"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'string'", "'='", "'int'", "'float'", "'main'", "'('", 
			"')'", "'{'", "'}'", "'read'", "'print'", "'return'", "'if'", "'else'", 
			"'while'", "'-'", "'+'", "'*'", "'/'", "'<'", "'<='", "'>='", "'=='", 
			"'!='", "'>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "IDENTIFIER", "INT_LITERAL", "FLOAT_LITERAL", "STR_LITERAL", 
			"COMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "MicroC.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }


	def setSymbolTable(self, st: SymbolTable):
	  self.st = st

	def getSymbolTable(self) -> SymbolTable:
	  return self.st

	def setAST(self, node: ASTNode):
	  self.ast = node

	def getAST(self) -> ASTNode:
	  return self.ast

	public MicroCParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public FunctionContext function;
		public DeclsContext decls() {
			return getRuleContext(DeclsContext.class,0);
		}
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			decls();
			setState(51);
			((ProgramContext)_localctx).function = function();
			self.setAST(((ProgramContext)_localctx).function.node);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclsContext extends ParserRuleContext {
		public Var_declContext var_decl() {
			return getRuleContext(Var_declContext.class,0);
		}
		public DeclsContext decls() {
			return getRuleContext(DeclsContext.class,0);
		}
		public Str_declContext str_decl() {
			return getRuleContext(Str_declContext.class,0);
		}
		public DeclsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decls; }
	}

	public final DeclsContext decls() throws RecognitionException {
		DeclsContext _localctx = new DeclsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_decls);
		try {
			setState(61);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(54);
				var_decl();
				setState(55);
				decls();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(57);
				str_decl();
				setState(58);
				decls();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_declsContext extends ParserRuleContext {
		public Var_declContext var_decl() {
			return getRuleContext(Var_declContext.class,0);
		}
		public Var_declsContext var_decls() {
			return getRuleContext(Var_declsContext.class,0);
		}
		public Var_declsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_decls; }
	}

	public final Var_declsContext var_decls() throws RecognitionException {
		Var_declsContext _localctx = new Var_declsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_var_decls);
		try {
			setState(67);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(63);
				var_decl();
				setState(64);
				var_decls();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdentContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(MicroCParser.IDENTIFIER, 0); }
		public IdentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ident; }
	}

	public final IdentContext ident() throws RecognitionException {
		IdentContext _localctx = new IdentContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_ident);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_declContext extends ParserRuleContext {
		public Base_typeContext base_type;
		public IdentContext ident;
		public Base_typeContext base_type() {
			return getRuleContext(Base_typeContext.class,0);
		}
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public Var_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_decl; }
	}

	public final Var_declContext var_decl() throws RecognitionException {
		Var_declContext _localctx = new Var_declContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_var_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			((Var_declContext)_localctx).base_type = base_type();
			setState(72);
			((Var_declContext)_localctx).ident = ident();
			setState(73);
			match(T__0);
			self.st.addVariable(((Var_declContext)_localctx).base_type.t, (((Var_declContext)_localctx).ident!=null?_input.getText(((Var_declContext)_localctx).ident.start,((Var_declContext)_localctx).ident.stop):null));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Str_declContext extends ParserRuleContext {
		public IdentContext ident;
		public Token val;
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public TerminalNode STR_LITERAL() { return getToken(MicroCParser.STR_LITERAL, 0); }
		public Str_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_str_decl; }
	}

	public final Str_declContext str_decl() throws RecognitionException {
		Str_declContext _localctx = new Str_declContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_str_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			match(T__1);
			setState(77);
			((Str_declContext)_localctx).ident = ident();
			setState(78);
			match(T__2);
			setState(79);
			((Str_declContext)_localctx).val = match(STR_LITERAL);
			setState(80);
			match(T__0);
			self.st.addVariable(Scope.Type.STRING, (((Str_declContext)_localctx).ident!=null?_input.getText(((Str_declContext)_localctx).ident.start,((Str_declContext)_localctx).ident.stop):null), (((Str_declContext)_localctx).val!=null?((Str_declContext)_localctx).val.getText():null));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Base_typeContext extends ParserRuleContext {
		public Scope.Type t;
		public Base_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_base_type; }
	}

	public final Base_typeContext base_type() throws RecognitionException {
		Base_typeContext _localctx = new Base_typeContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_base_type);
		try {
			setState(87);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				enterOuterAlt(_localctx, 1);
				{
				setState(83);
				match(T__3);
				((Base_typeContext)_localctx).t =  Scope.Type.INT;
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(85);
				match(T__4);
				((Base_typeContext)_localctx).t =  Scope.Type.FLOAT;
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionContext extends ParserRuleContext {
		public StatementListNode node;
		public StatementsContext statements;
		public StatementsContext statements() {
			return getRuleContext(StatementsContext.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_function);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			match(T__3);
			setState(90);
			match(T__5);
			setState(91);
			match(T__6);
			setState(92);
			match(T__7);
			setState(93);
			match(T__8);
			setState(94);
			((FunctionContext)_localctx).statements = statements();
			setState(95);
			match(T__9);
			((FunctionContext)_localctx).node =  ((FunctionContext)_localctx).statements.node;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementsContext extends ParserRuleContext {
		public StatementListNode node;
		public StatementContext statement;
		public StatementsContext s;
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public StatementsContext statements() {
			return getRuleContext(StatementsContext.class,0);
		}
		public StatementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statements; }
	}

	public final StatementsContext statements() throws RecognitionException {
		StatementsContext _localctx = new StatementsContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_statements);
		try {
			setState(103);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
			case T__11:
			case T__12:
			case T__13:
			case T__15:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(98);
				((StatementsContext)_localctx).statement = statement();
				setState(99);
				((StatementsContext)_localctx).s = statements();
				((StatementsContext)_localctx).node =  StatementListNode(((StatementsContext)_localctx).statement.node, ((StatementsContext)_localctx).s.node.getStatements());
				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 2);
				{
				((StatementsContext)_localctx).node =  StatementListNode();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public StatementNode node;
		public Base_stmtContext base_stmt;
		public If_stmtContext if_stmt;
		public While_stmtContext while_stmt;
		public Base_stmtContext base_stmt() {
			return getRuleContext(Base_stmtContext.class,0);
		}
		public If_stmtContext if_stmt() {
			return getRuleContext(If_stmtContext.class,0);
		}
		public While_stmtContext while_stmt() {
			return getRuleContext(While_stmtContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_statement);
		try {
			setState(115);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
			case T__11:
			case T__12:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(105);
				((StatementContext)_localctx).base_stmt = base_stmt();
				setState(106);
				match(T__0);
				((StatementContext)_localctx).node =  ((StatementContext)_localctx).base_stmt.node;
				}
				break;
			case T__13:
				enterOuterAlt(_localctx, 2);
				{
				setState(109);
				((StatementContext)_localctx).if_stmt = if_stmt();
				_localctx.node = ((StatementContext)_localctx).if_stmt.node
				}
				break;
			case T__15:
				enterOuterAlt(_localctx, 3);
				{
				setState(112);
				((StatementContext)_localctx).while_stmt = while_stmt();
				_localctx.node = ((StatementContext)_localctx).while_stmt.node
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Base_stmtContext extends ParserRuleContext {
		public StatementNode node;
		public Assign_stmtContext assign_stmt;
		public Read_stmtContext read_stmt;
		public Print_stmtContext print_stmt;
		public Return_stmtContext return_stmt;
		public Assign_stmtContext assign_stmt() {
			return getRuleContext(Assign_stmtContext.class,0);
		}
		public Read_stmtContext read_stmt() {
			return getRuleContext(Read_stmtContext.class,0);
		}
		public Print_stmtContext print_stmt() {
			return getRuleContext(Print_stmtContext.class,0);
		}
		public Return_stmtContext return_stmt() {
			return getRuleContext(Return_stmtContext.class,0);
		}
		public Base_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_base_stmt; }
	}

	public final Base_stmtContext base_stmt() throws RecognitionException {
		Base_stmtContext _localctx = new Base_stmtContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_base_stmt);
		try {
			setState(129);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(117);
				((Base_stmtContext)_localctx).assign_stmt = assign_stmt();
				((Base_stmtContext)_localctx).node =  ((Base_stmtContext)_localctx).assign_stmt.node;
				}
				break;
			case T__10:
				enterOuterAlt(_localctx, 2);
				{
				setState(120);
				((Base_stmtContext)_localctx).read_stmt = read_stmt();
				((Base_stmtContext)_localctx).node =  ((Base_stmtContext)_localctx).read_stmt.node;
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 3);
				{
				setState(123);
				((Base_stmtContext)_localctx).print_stmt = print_stmt();
				((Base_stmtContext)_localctx).node =  ((Base_stmtContext)_localctx).print_stmt.node;
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 4);
				{
				setState(126);
				((Base_stmtContext)_localctx).return_stmt = return_stmt();
				((Base_stmtContext)_localctx).node =  ((Base_stmtContext)_localctx).return_stmt.node;
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Read_stmtContext extends ParserRuleContext {
		public ReadNode node;
		public IdentContext ident;
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public Read_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read_stmt; }
	}

	public final Read_stmtContext read_stmt() throws RecognitionException {
		Read_stmtContext _localctx = new Read_stmtContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_read_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			match(T__10);
			setState(132);
			match(T__6);
			setState(133);
			((Read_stmtContext)_localctx).ident = ident();
			setState(134);
			match(T__7);
			((Read_stmtContext)_localctx).node =  ReadNode(VarNode((((Read_stmtContext)_localctx).ident!=null?_input.getText(((Read_stmtContext)_localctx).ident.start,((Read_stmtContext)_localctx).ident.stop):null)));
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Print_stmtContext extends ParserRuleContext {
		public WriteNode node;
		public ExprContext expr;
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Print_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_stmt; }
	}

	public final Print_stmtContext print_stmt() throws RecognitionException {
		Print_stmtContext _localctx = new Print_stmtContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_print_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			match(T__11);
			setState(138);
			match(T__6);
			setState(139);
			((Print_stmtContext)_localctx).expr = expr(0);
			setState(140);
			match(T__7);
			((Print_stmtContext)_localctx).node =  WriteNode(((Print_stmtContext)_localctx).expr.node);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_stmtContext extends ParserRuleContext {
		public ReturnNode node;
		public ExprContext expr;
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Return_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_stmt; }
	}

	public final Return_stmtContext return_stmt() throws RecognitionException {
		Return_stmtContext _localctx = new Return_stmtContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_return_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			match(T__12);
			setState(144);
			((Return_stmtContext)_localctx).expr = expr(0);
			((Return_stmtContext)_localctx).node =  ReturnNode(((Return_stmtContext)_localctx).expr.node);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_stmtContext extends ParserRuleContext {
		public AssignNode node;
		public IdentContext ident;
		public ExprContext expr;
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Assign_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_stmt; }
	}

	public final Assign_stmtContext assign_stmt() throws RecognitionException {
		Assign_stmtContext _localctx = new Assign_stmtContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(147);
			((Assign_stmtContext)_localctx).ident = ident();
			setState(148);
			match(T__2);
			setState(149);
			((Assign_stmtContext)_localctx).expr = expr(0);
			((Assign_stmtContext)_localctx).node =  AssignNode(VarNode((((Assign_stmtContext)_localctx).ident!=null?_input.getText(((Assign_stmtContext)_localctx).ident.start,((Assign_stmtContext)_localctx).ident.stop):null)), ((Assign_stmtContext)_localctx).expr.node);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_stmtContext extends ParserRuleContext {
		public IfStatementNode node;
		public CondContext cond;
		public StatementsContext t1;
		public StatementsContext e1;
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public List<StatementsContext> statements() {
			return getRuleContexts(StatementsContext.class);
		}
		public StatementsContext statements(int i) {
			return getRuleContext(StatementsContext.class,i);
		}
		public If_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stmt; }
	}

	public final If_stmtContext if_stmt() throws RecognitionException {
		If_stmtContext _localctx = new If_stmtContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_if_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			match(T__13);
			setState(153);
			match(T__6);
			setState(154);
			((If_stmtContext)_localctx).cond = cond();
			setState(155);
			match(T__7);
			setState(156);
			match(T__8);
			setState(157);
			((If_stmtContext)_localctx).t1 = statements();
			setState(158);
			match(T__9);
			setState(164);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__14) {
				{
				setState(159);
				match(T__14);
				setState(160);
				match(T__8);
				setState(161);
				((If_stmtContext)_localctx).e1 = statements();
				setState(162);
				match(T__9);
				}
			}

			((If_stmtContext)_localctx).node =  IfStatementNode(((If_stmtContext)_localctx).cond.node, ((If_stmtContext)_localctx).t1.node, ((If_stmtContext)_localctx).e1.node);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class While_stmtContext extends ParserRuleContext {
		public WhileNode node;
		public CondContext cond;
		public StatementsContext statements;
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public StatementsContext statements() {
			return getRuleContext(StatementsContext.class,0);
		}
		public While_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_stmt; }
	}

	public final While_stmtContext while_stmt() throws RecognitionException {
		While_stmtContext _localctx = new While_stmtContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			match(T__15);
			setState(169);
			match(T__6);
			setState(170);
			((While_stmtContext)_localctx).cond = cond();
			setState(171);
			match(T__7);
			setState(172);
			match(T__8);
			setState(173);
			((While_stmtContext)_localctx).statements = statements();
			setState(174);
			match(T__9);
			((While_stmtContext)_localctx).node =  WhileNode(((While_stmtContext)_localctx).cond.node, ((While_stmtContext)_localctx).statements.node);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrimaryContext extends ParserRuleContext {
		public ExpressionNode node;
		public IdentContext ident;
		public ExprContext expr;
		public Unaryminus_exprContext unaryminus_expr;
		public Token il;
		public Token fl;
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Unaryminus_exprContext unaryminus_expr() {
			return getRuleContext(Unaryminus_exprContext.class,0);
		}
		public TerminalNode INT_LITERAL() { return getToken(MicroCParser.INT_LITERAL, 0); }
		public TerminalNode FLOAT_LITERAL() { return getToken(MicroCParser.FLOAT_LITERAL, 0); }
		public PrimaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary; }
	}

	public final PrimaryContext primary() throws RecognitionException {
		PrimaryContext _localctx = new PrimaryContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_primary);
		try {
			setState(192);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(177);
				((PrimaryContext)_localctx).ident = ident();
				((PrimaryContext)_localctx).node =  VarNode((((PrimaryContext)_localctx).ident!=null?_input.getText(((PrimaryContext)_localctx).ident.start,((PrimaryContext)_localctx).ident.stop):null));
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 2);
				{
				setState(180);
				match(T__6);
				setState(181);
				((PrimaryContext)_localctx).expr = expr(0);
				setState(182);
				match(T__7);
				((PrimaryContext)_localctx).node =  ((PrimaryContext)_localctx).expr.node;
				}
				break;
			case T__16:
				enterOuterAlt(_localctx, 3);
				{
				setState(185);
				((PrimaryContext)_localctx).unaryminus_expr = unaryminus_expr();
				((PrimaryContext)_localctx).node =  ((PrimaryContext)_localctx).unaryminus_expr.node;
				}
				break;
			case INT_LITERAL:
				enterOuterAlt(_localctx, 4);
				{
				setState(188);
				((PrimaryContext)_localctx).il = match(INT_LITERAL);
				((PrimaryContext)_localctx).node =  IntLitNode((((PrimaryContext)_localctx).il!=null?((PrimaryContext)_localctx).il.getText():null));
				}
				break;
			case FLOAT_LITERAL:
				enterOuterAlt(_localctx, 5);
				{
				setState(190);
				((PrimaryContext)_localctx).fl = match(FLOAT_LITERAL);
				((PrimaryContext)_localctx).node =  FloatLitNode((((PrimaryContext)_localctx).fl!=null?((PrimaryContext)_localctx).fl.getText():null));
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Unaryminus_exprContext extends ParserRuleContext {
		public ExpressionNode node;
		public ExprContext expr;
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Unaryminus_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryminus_expr; }
	}

	public final Unaryminus_exprContext unaryminus_expr() throws RecognitionException {
		Unaryminus_exprContext _localctx = new Unaryminus_exprContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_unaryminus_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(194);
			match(T__16);
			setState(195);
			((Unaryminus_exprContext)_localctx).expr = expr(0);
			((Unaryminus_exprContext)_localctx).node =  UnaryOpNode(((Unaryminus_exprContext)_localctx).expr.node, '-');
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ExpressionNode node;
		public ExprContext e1;
		public ExprContext e2;
		public TermContext term;
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 38;
		enterRecursionRule(_localctx, 38, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(199);
			((ExprContext)_localctx).term = term(0);
			((ExprContext)_localctx).node =  ((ExprContext)_localctx).term.node;
			}
			_ctx.stop = _input.LT(-1);
			setState(214);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(212);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						_localctx.e1 = _prevctx;
						_localctx.e1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(202);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(203);
						match(T__17);
						setState(204);
						((ExprContext)_localctx).term = term(0);
						((ExprContext)_localctx).node =  BinaryOpNode(((ExprContext)_localctx).e1.node, ((ExprContext)_localctx).term.node, '+');
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						_localctx.e2 = _prevctx;
						_localctx.e2 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(207);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(208);
						match(T__16);
						setState(209);
						((ExprContext)_localctx).term = term(0);
						((ExprContext)_localctx).node =  BinaryOpNode(((ExprContext)_localctx).e2.node, ((ExprContext)_localctx).term.node, '-');
						}
						break;
					}
					} 
				}
				setState(216);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class TermContext extends ParserRuleContext {
		public ExpressionNode node;
		public TermContext t1;
		public TermContext t2;
		public PrimaryContext primary;
		public PrimaryContext primary() {
			return getRuleContext(PrimaryContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		return term(0);
	}

	private TermContext term(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		TermContext _localctx = new TermContext(_ctx, _parentState);
		TermContext _prevctx = _localctx;
		int _startState = 40;
		enterRecursionRule(_localctx, 40, RULE_term, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(218);
			((TermContext)_localctx).primary = primary();
			((TermContext)_localctx).node =  ((TermContext)_localctx).primary.node;
			}
			_ctx.stop = _input.LT(-1);
			setState(233);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(231);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
					case 1:
						{
						_localctx = new TermContext(_parentctx, _parentState);
						_localctx.t1 = _prevctx;
						_localctx.t1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_term);
						setState(221);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(222);
						match(T__18);
						setState(223);
						((TermContext)_localctx).primary = primary();
						((TermContext)_localctx).node =  BinaryOpNode(((TermContext)_localctx).t1.node, ((TermContext)_localctx).primary.node, '*');
						}
						break;
					case 2:
						{
						_localctx = new TermContext(_parentctx, _parentState);
						_localctx.t2 = _prevctx;
						_localctx.t2 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_term);
						setState(226);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(227);
						match(T__19);
						setState(228);
						((TermContext)_localctx).primary = primary();
						((TermContext)_localctx).node =  BinaryOpNode(((TermContext)_localctx).t2.node, ((TermContext)_localctx).primary.node, '/');
						}
						break;
					}
					} 
				}
				setState(235);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class CondContext extends ParserRuleContext {
		public CondNode node;
		public ExprContext e1;
		public ExprContext e2;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public CondContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cond; }
	}

	public final CondContext cond() throws RecognitionException {
		CondContext _localctx = new CondContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_cond);
		try {
			setState(266);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(236);
				((CondContext)_localctx).e1 = expr(0);
				setState(237);
				match(T__20);
				setState(238);
				((CondContext)_localctx).e2 = expr(0);
				((CondContext)_localctx).node =  CondNode(((CondContext)_localctx).e1.node, ((CondContext)_localctx).e2.node, '<');
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(241);
				((CondContext)_localctx).e1 = expr(0);
				setState(242);
				match(T__21);
				setState(243);
				((CondContext)_localctx).e2 = expr(0);
				((CondContext)_localctx).node =  CondNode(((CondContext)_localctx).e1.node, ((CondContext)_localctx).e2.node, '<=');
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(246);
				((CondContext)_localctx).e1 = expr(0);
				setState(247);
				match(T__22);
				setState(248);
				((CondContext)_localctx).e2 = expr(0);
				((CondContext)_localctx).node =  CondNode(((CondContext)_localctx).e1.node, ((CondContext)_localctx).e2.node, '>=');
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(251);
				((CondContext)_localctx).e1 = expr(0);
				setState(252);
				match(T__23);
				setState(253);
				((CondContext)_localctx).e2 = expr(0);
				((CondContext)_localctx).node =  CondNode(((CondContext)_localctx).e1.node, ((CondContext)_localctx).e2.node, '==');
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(256);
				((CondContext)_localctx).e1 = expr(0);
				setState(257);
				match(T__24);
				setState(258);
				((CondContext)_localctx).e2 = expr(0);
				((CondContext)_localctx).node =  CondNode(((CondContext)_localctx).e1.node, ((CondContext)_localctx).e2.node, '!=');
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(261);
				((CondContext)_localctx).e1 = expr(0);
				setState(262);
				match(T__25);
				setState(263);
				((CondContext)_localctx).e2 = expr(0);
				((CondContext)_localctx).node =  CondNode(((CondContext)_localctx).e1.node, ((CondContext)_localctx).e2.node, '>');
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CmpopContext extends ParserRuleContext {
		public CmpopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cmpop; }
	}

	public final CmpopContext cmpop() throws RecognitionException {
		CmpopContext _localctx = new CmpopContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_cmpop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(268);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__20) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << T__25))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MulopContext extends ParserRuleContext {
		public MulopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mulop; }
	}

	public final MulopContext mulop() throws RecognitionException {
		MulopContext _localctx = new MulopContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_mulop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(270);
			_la = _input.LA(1);
			if ( !(_la==T__18 || _la==T__19) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AddopContext extends ParserRuleContext {
		public AddopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_addop; }
	}

	public final AddopContext addop() throws RecognitionException {
		AddopContext _localctx = new AddopContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_addop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(272);
			_la = _input.LA(1);
			if ( !(_la==T__16 || _la==T__17) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 19:
			return expr_sempred((ExprContext)_localctx, predIndex);
		case 20:
			return term_sempred((TermContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		case 1:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean term_sempred(TermContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		case 3:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\"\u0115\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3@\n\3\3\4\3"+
		"\4\3\4\3\4\5\4F\n\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\b\3\b\3\b\3\b\5\bZ\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3"+
		"\n\3\n\3\n\3\n\3\n\5\nj\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3"+
		"\13\3\13\5\13v\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5"+
		"\f\u0084\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17"+
		"\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00a7\n\21\3\21\3\21\3\22\3\22\3\22"+
		"\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23"+
		"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00c3\n\23\3\24\3\24\3\24\3\24"+
		"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25"+
		"\7\25\u00d7\n\25\f\25\16\25\u00da\13\25\3\26\3\26\3\26\3\26\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u00ea\n\26\f\26\16\26\u00ed"+
		"\13\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\5\27\u010d\n\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\2\4"+
		"(*\33\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\2\5\3\2\27"+
		"\34\3\2\25\26\3\2\23\24\2\u0113\2\64\3\2\2\2\4?\3\2\2\2\6E\3\2\2\2\bG"+
		"\3\2\2\2\nI\3\2\2\2\fN\3\2\2\2\16Y\3\2\2\2\20[\3\2\2\2\22i\3\2\2\2\24"+
		"u\3\2\2\2\26\u0083\3\2\2\2\30\u0085\3\2\2\2\32\u008b\3\2\2\2\34\u0091"+
		"\3\2\2\2\36\u0095\3\2\2\2 \u009a\3\2\2\2\"\u00aa\3\2\2\2$\u00c2\3\2\2"+
		"\2&\u00c4\3\2\2\2(\u00c8\3\2\2\2*\u00db\3\2\2\2,\u010c\3\2\2\2.\u010e"+
		"\3\2\2\2\60\u0110\3\2\2\2\62\u0112\3\2\2\2\64\65\5\4\3\2\65\66\5\20\t"+
		"\2\66\67\b\2\1\2\67\3\3\2\2\289\5\n\6\29:\5\4\3\2:@\3\2\2\2;<\5\f\7\2"+
		"<=\5\4\3\2=@\3\2\2\2>@\3\2\2\2?8\3\2\2\2?;\3\2\2\2?>\3\2\2\2@\5\3\2\2"+
		"\2AB\5\n\6\2BC\5\6\4\2CF\3\2\2\2DF\3\2\2\2EA\3\2\2\2ED\3\2\2\2F\7\3\2"+
		"\2\2GH\7\35\2\2H\t\3\2\2\2IJ\5\16\b\2JK\5\b\5\2KL\7\3\2\2LM\b\6\1\2M\13"+
		"\3\2\2\2NO\7\4\2\2OP\5\b\5\2PQ\7\5\2\2QR\7 \2\2RS\7\3\2\2ST\b\7\1\2T\r"+
		"\3\2\2\2UV\7\6\2\2VZ\b\b\1\2WX\7\7\2\2XZ\b\b\1\2YU\3\2\2\2YW\3\2\2\2Z"+
		"\17\3\2\2\2[\\\7\6\2\2\\]\7\b\2\2]^\7\t\2\2^_\7\n\2\2_`\7\13\2\2`a\5\22"+
		"\n\2ab\7\f\2\2bc\b\t\1\2c\21\3\2\2\2de\5\24\13\2ef\5\22\n\2fg\b\n\1\2"+
		"gj\3\2\2\2hj\b\n\1\2id\3\2\2\2ih\3\2\2\2j\23\3\2\2\2kl\5\26\f\2lm\7\3"+
		"\2\2mn\b\13\1\2nv\3\2\2\2op\5 \21\2pq\b\13\1\2qv\3\2\2\2rs\5\"\22\2st"+
		"\b\13\1\2tv\3\2\2\2uk\3\2\2\2uo\3\2\2\2ur\3\2\2\2v\25\3\2\2\2wx\5\36\20"+
		"\2xy\b\f\1\2y\u0084\3\2\2\2z{\5\30\r\2{|\b\f\1\2|\u0084\3\2\2\2}~\5\32"+
		"\16\2~\177\b\f\1\2\177\u0084\3\2\2\2\u0080\u0081\5\34\17\2\u0081\u0082"+
		"\b\f\1\2\u0082\u0084\3\2\2\2\u0083w\3\2\2\2\u0083z\3\2\2\2\u0083}\3\2"+
		"\2\2\u0083\u0080\3\2\2\2\u0084\27\3\2\2\2\u0085\u0086\7\r\2\2\u0086\u0087"+
		"\7\t\2\2\u0087\u0088\5\b\5\2\u0088\u0089\7\n\2\2\u0089\u008a\b\r\1\2\u008a"+
		"\31\3\2\2\2\u008b\u008c\7\16\2\2\u008c\u008d\7\t\2\2\u008d\u008e\5(\25"+
		"\2\u008e\u008f\7\n\2\2\u008f\u0090\b\16\1\2\u0090\33\3\2\2\2\u0091\u0092"+
		"\7\17\2\2\u0092\u0093\5(\25\2\u0093\u0094\b\17\1\2\u0094\35\3\2\2\2\u0095"+
		"\u0096\5\b\5\2\u0096\u0097\7\5\2\2\u0097\u0098\5(\25\2\u0098\u0099\b\20"+
		"\1\2\u0099\37\3\2\2\2\u009a\u009b\7\20\2\2\u009b\u009c\7\t\2\2\u009c\u009d"+
		"\5,\27\2\u009d\u009e\7\n\2\2\u009e\u009f\7\13\2\2\u009f\u00a0\5\22\n\2"+
		"\u00a0\u00a6\7\f\2\2\u00a1\u00a2\7\21\2\2\u00a2\u00a3\7\13\2\2\u00a3\u00a4"+
		"\5\22\n\2\u00a4\u00a5\7\f\2\2\u00a5\u00a7\3\2\2\2\u00a6\u00a1\3\2\2\2"+
		"\u00a6\u00a7\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9\b\21\1\2\u00a9!\3"+
		"\2\2\2\u00aa\u00ab\7\22\2\2\u00ab\u00ac\7\t\2\2\u00ac\u00ad\5,\27\2\u00ad"+
		"\u00ae\7\n\2\2\u00ae\u00af\7\13\2\2\u00af\u00b0\5\22\n\2\u00b0\u00b1\7"+
		"\f\2\2\u00b1\u00b2\b\22\1\2\u00b2#\3\2\2\2\u00b3\u00b4\5\b\5\2\u00b4\u00b5"+
		"\b\23\1\2\u00b5\u00c3\3\2\2\2\u00b6\u00b7\7\t\2\2\u00b7\u00b8\5(\25\2"+
		"\u00b8\u00b9\7\n\2\2\u00b9\u00ba\b\23\1\2\u00ba\u00c3\3\2\2\2\u00bb\u00bc"+
		"\5&\24\2\u00bc\u00bd\b\23\1\2\u00bd\u00c3\3\2\2\2\u00be\u00bf\7\36\2\2"+
		"\u00bf\u00c3\b\23\1\2\u00c0\u00c1\7\37\2\2\u00c1\u00c3\b\23\1\2\u00c2"+
		"\u00b3\3\2\2\2\u00c2\u00b6\3\2\2\2\u00c2\u00bb\3\2\2\2\u00c2\u00be\3\2"+
		"\2\2\u00c2\u00c0\3\2\2\2\u00c3%\3\2\2\2\u00c4\u00c5\7\23\2\2\u00c5\u00c6"+
		"\5(\25\2\u00c6\u00c7\b\24\1\2\u00c7\'\3\2\2\2\u00c8\u00c9\b\25\1\2\u00c9"+
		"\u00ca\5*\26\2\u00ca\u00cb\b\25\1\2\u00cb\u00d8\3\2\2\2\u00cc\u00cd\f"+
		"\4\2\2\u00cd\u00ce\7\24\2\2\u00ce\u00cf\5*\26\2\u00cf\u00d0\b\25\1\2\u00d0"+
		"\u00d7\3\2\2\2\u00d1\u00d2\f\3\2\2\u00d2\u00d3\7\23\2\2\u00d3\u00d4\5"+
		"*\26\2\u00d4\u00d5\b\25\1\2\u00d5\u00d7\3\2\2\2\u00d6\u00cc\3\2\2\2\u00d6"+
		"\u00d1\3\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2"+
		"\2\2\u00d9)\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00dc\b\26\1\2\u00dc\u00dd"+
		"\5$\23\2\u00dd\u00de\b\26\1\2\u00de\u00eb\3\2\2\2\u00df\u00e0\f\4\2\2"+
		"\u00e0\u00e1\7\25\2\2\u00e1\u00e2\5$\23\2\u00e2\u00e3\b\26\1\2\u00e3\u00ea"+
		"\3\2\2\2\u00e4\u00e5\f\3\2\2\u00e5\u00e6\7\26\2\2\u00e6\u00e7\5$\23\2"+
		"\u00e7\u00e8\b\26\1\2\u00e8\u00ea\3\2\2\2\u00e9\u00df\3\2\2\2\u00e9\u00e4"+
		"\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec"+
		"+\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00ef\5(\25\2\u00ef\u00f0\7\27\2\2"+
		"\u00f0\u00f1\5(\25\2\u00f1\u00f2\b\27\1\2\u00f2\u010d\3\2\2\2\u00f3\u00f4"+
		"\5(\25\2\u00f4\u00f5\7\30\2\2\u00f5\u00f6\5(\25\2\u00f6\u00f7\b\27\1\2"+
		"\u00f7\u010d\3\2\2\2\u00f8\u00f9\5(\25\2\u00f9\u00fa\7\31\2\2\u00fa\u00fb"+
		"\5(\25\2\u00fb\u00fc\b\27\1\2\u00fc\u010d\3\2\2\2\u00fd\u00fe\5(\25\2"+
		"\u00fe\u00ff\7\32\2\2\u00ff\u0100\5(\25\2\u0100\u0101\b\27\1\2\u0101\u010d"+
		"\3\2\2\2\u0102\u0103\5(\25\2\u0103\u0104\7\33\2\2\u0104\u0105\5(\25\2"+
		"\u0105\u0106\b\27\1\2\u0106\u010d\3\2\2\2\u0107\u0108\5(\25\2\u0108\u0109"+
		"\7\34\2\2\u0109\u010a\5(\25\2\u010a\u010b\b\27\1\2\u010b\u010d\3\2\2\2"+
		"\u010c\u00ee\3\2\2\2\u010c\u00f3\3\2\2\2\u010c\u00f8\3\2\2\2\u010c\u00fd"+
		"\3\2\2\2\u010c\u0102\3\2\2\2\u010c\u0107\3\2\2\2\u010d-\3\2\2\2\u010e"+
		"\u010f\t\2\2\2\u010f/\3\2\2\2\u0110\u0111\t\3\2\2\u0111\61\3\2\2\2\u0112"+
		"\u0113\t\4\2\2\u0113\63\3\2\2\2\17?EYiu\u0083\u00a6\u00c2\u00d6\u00d8"+
		"\u00e9\u00eb\u010c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}