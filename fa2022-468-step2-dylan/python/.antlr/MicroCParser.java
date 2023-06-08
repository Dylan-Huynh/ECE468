// Generated from c:\Users\dylan\OneDrive\Documents\GitHub\fa2022-468-step2-dylan\python\MicroC.g4 by ANTLR 4.9.2


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
		public Base_stmtContext base_stmt() {
			return getRuleContext(Base_stmtContext.class,0);
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
			setState(110);
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
			case T__15:
				enterOuterAlt(_localctx, 2);
				{
				setState(109);
				while_stmt();
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
			setState(124);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(112);
				((Base_stmtContext)_localctx).assign_stmt = assign_stmt();
				((Base_stmtContext)_localctx).node =  ((Base_stmtContext)_localctx).assign_stmt.node;
				}
				break;
			case T__10:
				enterOuterAlt(_localctx, 2);
				{
				setState(115);
				((Base_stmtContext)_localctx).read_stmt = read_stmt();
				((Base_stmtContext)_localctx).node =  ((Base_stmtContext)_localctx).read_stmt.node;
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 3);
				{
				setState(118);
				((Base_stmtContext)_localctx).print_stmt = print_stmt();
				((Base_stmtContext)_localctx).node =  ((Base_stmtContext)_localctx).print_stmt.node;
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 4);
				{
				setState(121);
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
			setState(126);
			match(T__10);
			setState(127);
			match(T__6);
			setState(128);
			((Read_stmtContext)_localctx).ident = ident();
			setState(129);
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
			setState(132);
			match(T__11);
			setState(133);
			match(T__6);
			setState(134);
			((Print_stmtContext)_localctx).expr = expr(0);
			setState(135);
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
			setState(138);
			match(T__12);
			setState(139);
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
			setState(142);
			((Assign_stmtContext)_localctx).ident = ident();
			setState(143);
			match(T__2);
			setState(144);
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
			setState(147);
			match(T__13);
			setState(148);
			match(T__6);
			setState(149);
			cond();
			setState(150);
			match(T__7);
			setState(151);
			match(T__8);
			setState(152);
			statements();
			setState(153);
			match(T__9);
			setState(159);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__14) {
				{
				setState(154);
				match(T__14);
				setState(155);
				match(T__8);
				setState(156);
				statements();
				setState(157);
				match(T__9);
				}
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

	public static class While_stmtContext extends ParserRuleContext {
		public WhileNode node;
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
			setState(161);
			match(T__15);
			setState(162);
			match(T__6);
			setState(163);
			cond();
			setState(164);
			match(T__7);
			setState(165);
			match(T__8);
			setState(166);
			statements();
			setState(167);
			match(T__9);
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
			setState(184);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(169);
				((PrimaryContext)_localctx).ident = ident();
				((PrimaryContext)_localctx).node =  VarNode((((PrimaryContext)_localctx).ident!=null?_input.getText(((PrimaryContext)_localctx).ident.start,((PrimaryContext)_localctx).ident.stop):null));
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 2);
				{
				setState(172);
				match(T__6);
				setState(173);
				((PrimaryContext)_localctx).expr = expr(0);
				setState(174);
				match(T__7);
				((PrimaryContext)_localctx).node =  ((PrimaryContext)_localctx).expr.node;
				}
				break;
			case T__16:
				enterOuterAlt(_localctx, 3);
				{
				setState(177);
				((PrimaryContext)_localctx).unaryminus_expr = unaryminus_expr();
				((PrimaryContext)_localctx).node =  ((PrimaryContext)_localctx).unaryminus_expr.node;
				}
				break;
			case INT_LITERAL:
				enterOuterAlt(_localctx, 4);
				{
				setState(180);
				((PrimaryContext)_localctx).il = match(INT_LITERAL);
				((PrimaryContext)_localctx).node =  IntLitNode((((PrimaryContext)_localctx).il!=null?((PrimaryContext)_localctx).il.getText():null));
				}
				break;
			case FLOAT_LITERAL:
				enterOuterAlt(_localctx, 5);
				{
				setState(182);
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
		public Token op;
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
			setState(186);
			((Unaryminus_exprContext)_localctx).op = match(T__16);
			setState(187);
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
			setState(191);
			((ExprContext)_localctx).term = term(0);
			((ExprContext)_localctx).node =  ((ExprContext)_localctx).term.node;
			}
			_ctx.stop = _input.LT(-1);
			setState(206);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(204);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						_localctx.e1 = _prevctx;
						_localctx.e1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(194);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(195);
						match(T__17);
						setState(196);
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
						setState(199);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(200);
						match(T__16);
						setState(201);
						((ExprContext)_localctx).term = term(0);
						((ExprContext)_localctx).node =  BinaryOpNode(((ExprContext)_localctx).e2.node, ((ExprContext)_localctx).term.node, '-');
						}
						break;
					}
					} 
				}
				setState(208);
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
			setState(210);
			((TermContext)_localctx).primary = primary();
			((TermContext)_localctx).node =  ((TermContext)_localctx).primary.node;
			}
			_ctx.stop = _input.LT(-1);
			setState(225);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(223);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
					case 1:
						{
						_localctx = new TermContext(_parentctx, _parentState);
						_localctx.t1 = _prevctx;
						_localctx.t1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_term);
						setState(213);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(214);
						match(T__18);
						setState(215);
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
						setState(218);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(219);
						match(T__19);
						setState(220);
						((TermContext)_localctx).primary = primary();
						((TermContext)_localctx).node =  BinaryOpNode(((TermContext)_localctx).t2.node, ((TermContext)_localctx).primary.node, '/');
						}
						break;
					}
					} 
				}
				setState(227);
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
		public CmpopContext cmpop() {
			return getRuleContext(CmpopContext.class,0);
		}
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
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			((CondContext)_localctx).e1 = expr(0);
			setState(229);
			cmpop();
			setState(230);
			((CondContext)_localctx).e2 = expr(0);
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
			setState(232);
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
			setState(234);
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
			setState(236);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\"\u00f1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3@\n\3\3\4\3"+
		"\4\3\4\3\4\5\4F\n\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\b\3\b\3\b\3\b\5\bZ\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3"+
		"\n\3\n\3\n\3\n\3\n\5\nj\n\n\3\13\3\13\3\13\3\13\3\13\5\13q\n\13\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\177\n\f\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3"+
		"\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3"+
		"\21\5\21\u00a2\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23"+
		"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23"+
		"\u00bb\n\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00cf\n\25\f\25\16\25\u00d2\13\25"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26"+
		"\7\26\u00e2\n\26\f\26\16\26\u00e5\13\26\3\27\3\27\3\27\3\27\3\30\3\30"+
		"\3\31\3\31\3\32\3\32\3\32\2\4(*\33\2\4\6\b\n\f\16\20\22\24\26\30\32\34"+
		"\36 \"$&(*,.\60\62\2\5\3\2\27\34\3\2\25\26\3\2\23\24\2\u00e9\2\64\3\2"+
		"\2\2\4?\3\2\2\2\6E\3\2\2\2\bG\3\2\2\2\nI\3\2\2\2\fN\3\2\2\2\16Y\3\2\2"+
		"\2\20[\3\2\2\2\22i\3\2\2\2\24p\3\2\2\2\26~\3\2\2\2\30\u0080\3\2\2\2\32"+
		"\u0086\3\2\2\2\34\u008c\3\2\2\2\36\u0090\3\2\2\2 \u0095\3\2\2\2\"\u00a3"+
		"\3\2\2\2$\u00ba\3\2\2\2&\u00bc\3\2\2\2(\u00c0\3\2\2\2*\u00d3\3\2\2\2,"+
		"\u00e6\3\2\2\2.\u00ea\3\2\2\2\60\u00ec\3\2\2\2\62\u00ee\3\2\2\2\64\65"+
		"\5\4\3\2\65\66\5\20\t\2\66\67\b\2\1\2\67\3\3\2\2\289\5\n\6\29:\5\4\3\2"+
		":@\3\2\2\2;<\5\f\7\2<=\5\4\3\2=@\3\2\2\2>@\3\2\2\2?8\3\2\2\2?;\3\2\2\2"+
		"?>\3\2\2\2@\5\3\2\2\2AB\5\n\6\2BC\5\6\4\2CF\3\2\2\2DF\3\2\2\2EA\3\2\2"+
		"\2ED\3\2\2\2F\7\3\2\2\2GH\7\35\2\2H\t\3\2\2\2IJ\5\16\b\2JK\5\b\5\2KL\7"+
		"\3\2\2LM\b\6\1\2M\13\3\2\2\2NO\7\4\2\2OP\5\b\5\2PQ\7\5\2\2QR\7 \2\2RS"+
		"\7\3\2\2ST\b\7\1\2T\r\3\2\2\2UV\7\6\2\2VZ\b\b\1\2WX\7\7\2\2XZ\b\b\1\2"+
		"YU\3\2\2\2YW\3\2\2\2Z\17\3\2\2\2[\\\7\6\2\2\\]\7\b\2\2]^\7\t\2\2^_\7\n"+
		"\2\2_`\7\13\2\2`a\5\22\n\2ab\7\f\2\2bc\b\t\1\2c\21\3\2\2\2de\5\24\13\2"+
		"ef\5\22\n\2fg\b\n\1\2gj\3\2\2\2hj\b\n\1\2id\3\2\2\2ih\3\2\2\2j\23\3\2"+
		"\2\2kl\5\26\f\2lm\7\3\2\2mn\b\13\1\2nq\3\2\2\2oq\5\"\22\2pk\3\2\2\2po"+
		"\3\2\2\2q\25\3\2\2\2rs\5\36\20\2st\b\f\1\2t\177\3\2\2\2uv\5\30\r\2vw\b"+
		"\f\1\2w\177\3\2\2\2xy\5\32\16\2yz\b\f\1\2z\177\3\2\2\2{|\5\34\17\2|}\b"+
		"\f\1\2}\177\3\2\2\2~r\3\2\2\2~u\3\2\2\2~x\3\2\2\2~{\3\2\2\2\177\27\3\2"+
		"\2\2\u0080\u0081\7\r\2\2\u0081\u0082\7\t\2\2\u0082\u0083\5\b\5\2\u0083"+
		"\u0084\7\n\2\2\u0084\u0085\b\r\1\2\u0085\31\3\2\2\2\u0086\u0087\7\16\2"+
		"\2\u0087\u0088\7\t\2\2\u0088\u0089\5(\25\2\u0089\u008a\7\n\2\2\u008a\u008b"+
		"\b\16\1\2\u008b\33\3\2\2\2\u008c\u008d\7\17\2\2\u008d\u008e\5(\25\2\u008e"+
		"\u008f\b\17\1\2\u008f\35\3\2\2\2\u0090\u0091\5\b\5\2\u0091\u0092\7\5\2"+
		"\2\u0092\u0093\5(\25\2\u0093\u0094\b\20\1\2\u0094\37\3\2\2\2\u0095\u0096"+
		"\7\20\2\2\u0096\u0097\7\t\2\2\u0097\u0098\5,\27\2\u0098\u0099\7\n\2\2"+
		"\u0099\u009a\7\13\2\2\u009a\u009b\5\22\n\2\u009b\u00a1\7\f\2\2\u009c\u009d"+
		"\7\21\2\2\u009d\u009e\7\13\2\2\u009e\u009f\5\22\n\2\u009f\u00a0\7\f\2"+
		"\2\u00a0\u00a2\3\2\2\2\u00a1\u009c\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2!"+
		"\3\2\2\2\u00a3\u00a4\7\22\2\2\u00a4\u00a5\7\t\2\2\u00a5\u00a6\5,\27\2"+
		"\u00a6\u00a7\7\n\2\2\u00a7\u00a8\7\13\2\2\u00a8\u00a9\5\22\n\2\u00a9\u00aa"+
		"\7\f\2\2\u00aa#\3\2\2\2\u00ab\u00ac\5\b\5\2\u00ac\u00ad\b\23\1\2\u00ad"+
		"\u00bb\3\2\2\2\u00ae\u00af\7\t\2\2\u00af\u00b0\5(\25\2\u00b0\u00b1\7\n"+
		"\2\2\u00b1\u00b2\b\23\1\2\u00b2\u00bb\3\2\2\2\u00b3\u00b4\5&\24\2\u00b4"+
		"\u00b5\b\23\1\2\u00b5\u00bb\3\2\2\2\u00b6\u00b7\7\36\2\2\u00b7\u00bb\b"+
		"\23\1\2\u00b8\u00b9\7\37\2\2\u00b9\u00bb\b\23\1\2\u00ba\u00ab\3\2\2\2"+
		"\u00ba\u00ae\3\2\2\2\u00ba\u00b3\3\2\2\2\u00ba\u00b6\3\2\2\2\u00ba\u00b8"+
		"\3\2\2\2\u00bb%\3\2\2\2\u00bc\u00bd\7\23\2\2\u00bd\u00be\5(\25\2\u00be"+
		"\u00bf\b\24\1\2\u00bf\'\3\2\2\2\u00c0\u00c1\b\25\1\2\u00c1\u00c2\5*\26"+
		"\2\u00c2\u00c3\b\25\1\2\u00c3\u00d0\3\2\2\2\u00c4\u00c5\f\4\2\2\u00c5"+
		"\u00c6\7\24\2\2\u00c6\u00c7\5*\26\2\u00c7\u00c8\b\25\1\2\u00c8\u00cf\3"+
		"\2\2\2\u00c9\u00ca\f\3\2\2\u00ca\u00cb\7\23\2\2\u00cb\u00cc\5*\26\2\u00cc"+
		"\u00cd\b\25\1\2\u00cd\u00cf\3\2\2\2\u00ce\u00c4\3\2\2\2\u00ce\u00c9\3"+
		"\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1"+
		")\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d4\b\26\1\2\u00d4\u00d5\5$\23\2"+
		"\u00d5\u00d6\b\26\1\2\u00d6\u00e3\3\2\2\2\u00d7\u00d8\f\4\2\2\u00d8\u00d9"+
		"\7\25\2\2\u00d9\u00da\5$\23\2\u00da\u00db\b\26\1\2\u00db\u00e2\3\2\2\2"+
		"\u00dc\u00dd\f\3\2\2\u00dd\u00de\7\26\2\2\u00de\u00df\5$\23\2\u00df\u00e0"+
		"\b\26\1\2\u00e0\u00e2\3\2\2\2\u00e1\u00d7\3\2\2\2\u00e1\u00dc\3\2\2\2"+
		"\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4+\3"+
		"\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00e7\5(\25\2\u00e7\u00e8\5.\30\2\u00e8"+
		"\u00e9\5(\25\2\u00e9-\3\2\2\2\u00ea\u00eb\t\2\2\2\u00eb/\3\2\2\2\u00ec"+
		"\u00ed\t\3\2\2\u00ed\61\3\2\2\2\u00ee\u00ef\t\4\2\2\u00ef\63\3\2\2\2\16"+
		"?EYip~\u00a1\u00ba\u00ce\u00d0\u00e1\u00e3";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}