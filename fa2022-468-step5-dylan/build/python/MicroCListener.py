# Generated from python/MicroC.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MicroCParser import MicroCParser
else:
    from MicroCParser import MicroCParser


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


# This class defines a complete listener for a parse tree produced by MicroCParser.
class MicroCListener(ParseTreeListener):

    # Enter a parse tree produced by MicroCParser#program.
    def enterProgram(self, ctx:MicroCParser.ProgramContext):
        pass

    # Exit a parse tree produced by MicroCParser#program.
    def exitProgram(self, ctx:MicroCParser.ProgramContext):
        pass


    # Enter a parse tree produced by MicroCParser#decls.
    def enterDecls(self, ctx:MicroCParser.DeclsContext):
        pass

    # Exit a parse tree produced by MicroCParser#decls.
    def exitDecls(self, ctx:MicroCParser.DeclsContext):
        pass


    # Enter a parse tree produced by MicroCParser#var_decls.
    def enterVar_decls(self, ctx:MicroCParser.Var_declsContext):
        pass

    # Exit a parse tree produced by MicroCParser#var_decls.
    def exitVar_decls(self, ctx:MicroCParser.Var_declsContext):
        pass


    # Enter a parse tree produced by MicroCParser#ident.
    def enterIdent(self, ctx:MicroCParser.IdentContext):
        pass

    # Exit a parse tree produced by MicroCParser#ident.
    def exitIdent(self, ctx:MicroCParser.IdentContext):
        pass


    # Enter a parse tree produced by MicroCParser#var_decl.
    def enterVar_decl(self, ctx:MicroCParser.Var_declContext):
        pass

    # Exit a parse tree produced by MicroCParser#var_decl.
    def exitVar_decl(self, ctx:MicroCParser.Var_declContext):
        pass


    # Enter a parse tree produced by MicroCParser#str_decl.
    def enterStr_decl(self, ctx:MicroCParser.Str_declContext):
        pass

    # Exit a parse tree produced by MicroCParser#str_decl.
    def exitStr_decl(self, ctx:MicroCParser.Str_declContext):
        pass


    # Enter a parse tree produced by MicroCParser#base_type.
    def enterBase_type(self, ctx:MicroCParser.Base_typeContext):
        pass

    # Exit a parse tree produced by MicroCParser#base_type.
    def exitBase_type(self, ctx:MicroCParser.Base_typeContext):
        pass


    # Enter a parse tree produced by MicroCParser#func_decl.
    def enterFunc_decl(self, ctx:MicroCParser.Func_declContext):
        pass

    # Exit a parse tree produced by MicroCParser#func_decl.
    def exitFunc_decl(self, ctx:MicroCParser.Func_declContext):
        pass


    # Enter a parse tree produced by MicroCParser#functions.
    def enterFunctions(self, ctx:MicroCParser.FunctionsContext):
        pass

    # Exit a parse tree produced by MicroCParser#functions.
    def exitFunctions(self, ctx:MicroCParser.FunctionsContext):
        pass


    # Enter a parse tree produced by MicroCParser#function.
    def enterFunction(self, ctx:MicroCParser.FunctionContext):
        pass

    # Exit a parse tree produced by MicroCParser#function.
    def exitFunction(self, ctx:MicroCParser.FunctionContext):
        pass


    # Enter a parse tree produced by MicroCParser#params.
    def enterParams(self, ctx:MicroCParser.ParamsContext):
        pass

    # Exit a parse tree produced by MicroCParser#params.
    def exitParams(self, ctx:MicroCParser.ParamsContext):
        pass


    # Enter a parse tree produced by MicroCParser#params_rest.
    def enterParams_rest(self, ctx:MicroCParser.Params_restContext):
        pass

    # Exit a parse tree produced by MicroCParser#params_rest.
    def exitParams_rest(self, ctx:MicroCParser.Params_restContext):
        pass


    # Enter a parse tree produced by MicroCParser#param.
    def enterParam(self, ctx:MicroCParser.ParamContext):
        pass

    # Exit a parse tree produced by MicroCParser#param.
    def exitParam(self, ctx:MicroCParser.ParamContext):
        pass


    # Enter a parse tree produced by MicroCParser#statements.
    def enterStatements(self, ctx:MicroCParser.StatementsContext):
        pass

    # Exit a parse tree produced by MicroCParser#statements.
    def exitStatements(self, ctx:MicroCParser.StatementsContext):
        pass


    # Enter a parse tree produced by MicroCParser#statement.
    def enterStatement(self, ctx:MicroCParser.StatementContext):
        pass

    # Exit a parse tree produced by MicroCParser#statement.
    def exitStatement(self, ctx:MicroCParser.StatementContext):
        pass


    # Enter a parse tree produced by MicroCParser#base_stmt.
    def enterBase_stmt(self, ctx:MicroCParser.Base_stmtContext):
        pass

    # Exit a parse tree produced by MicroCParser#base_stmt.
    def exitBase_stmt(self, ctx:MicroCParser.Base_stmtContext):
        pass


    # Enter a parse tree produced by MicroCParser#read_stmt.
    def enterRead_stmt(self, ctx:MicroCParser.Read_stmtContext):
        pass

    # Exit a parse tree produced by MicroCParser#read_stmt.
    def exitRead_stmt(self, ctx:MicroCParser.Read_stmtContext):
        pass


    # Enter a parse tree produced by MicroCParser#print_stmt.
    def enterPrint_stmt(self, ctx:MicroCParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by MicroCParser#print_stmt.
    def exitPrint_stmt(self, ctx:MicroCParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by MicroCParser#return_stmt.
    def enterReturn_stmt(self, ctx:MicroCParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by MicroCParser#return_stmt.
    def exitReturn_stmt(self, ctx:MicroCParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by MicroCParser#assign_stmt.
    def enterAssign_stmt(self, ctx:MicroCParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by MicroCParser#assign_stmt.
    def exitAssign_stmt(self, ctx:MicroCParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by MicroCParser#if_stmt.
    def enterIf_stmt(self, ctx:MicroCParser.If_stmtContext):
        pass

    # Exit a parse tree produced by MicroCParser#if_stmt.
    def exitIf_stmt(self, ctx:MicroCParser.If_stmtContext):
        pass


    # Enter a parse tree produced by MicroCParser#while_stmt.
    def enterWhile_stmt(self, ctx:MicroCParser.While_stmtContext):
        pass

    # Exit a parse tree produced by MicroCParser#while_stmt.
    def exitWhile_stmt(self, ctx:MicroCParser.While_stmtContext):
        pass


    # Enter a parse tree produced by MicroCParser#primary.
    def enterPrimary(self, ctx:MicroCParser.PrimaryContext):
        pass

    # Exit a parse tree produced by MicroCParser#primary.
    def exitPrimary(self, ctx:MicroCParser.PrimaryContext):
        pass


    # Enter a parse tree produced by MicroCParser#unaryminus_expr.
    def enterUnaryminus_expr(self, ctx:MicroCParser.Unaryminus_exprContext):
        pass

    # Exit a parse tree produced by MicroCParser#unaryminus_expr.
    def exitUnaryminus_expr(self, ctx:MicroCParser.Unaryminus_exprContext):
        pass


    # Enter a parse tree produced by MicroCParser#call_expr.
    def enterCall_expr(self, ctx:MicroCParser.Call_exprContext):
        pass

    # Exit a parse tree produced by MicroCParser#call_expr.
    def exitCall_expr(self, ctx:MicroCParser.Call_exprContext):
        pass


    # Enter a parse tree produced by MicroCParser#arg_list.
    def enterArg_list(self, ctx:MicroCParser.Arg_listContext):
        pass

    # Exit a parse tree produced by MicroCParser#arg_list.
    def exitArg_list(self, ctx:MicroCParser.Arg_listContext):
        pass


    # Enter a parse tree produced by MicroCParser#args_rest.
    def enterArgs_rest(self, ctx:MicroCParser.Args_restContext):
        pass

    # Exit a parse tree produced by MicroCParser#args_rest.
    def exitArgs_rest(self, ctx:MicroCParser.Args_restContext):
        pass


    # Enter a parse tree produced by MicroCParser#expr.
    def enterExpr(self, ctx:MicroCParser.ExprContext):
        pass

    # Exit a parse tree produced by MicroCParser#expr.
    def exitExpr(self, ctx:MicroCParser.ExprContext):
        pass


    # Enter a parse tree produced by MicroCParser#term.
    def enterTerm(self, ctx:MicroCParser.TermContext):
        pass

    # Exit a parse tree produced by MicroCParser#term.
    def exitTerm(self, ctx:MicroCParser.TermContext):
        pass


    # Enter a parse tree produced by MicroCParser#cond.
    def enterCond(self, ctx:MicroCParser.CondContext):
        pass

    # Exit a parse tree produced by MicroCParser#cond.
    def exitCond(self, ctx:MicroCParser.CondContext):
        pass


    # Enter a parse tree produced by MicroCParser#cmpop.
    def enterCmpop(self, ctx:MicroCParser.CmpopContext):
        pass

    # Exit a parse tree produced by MicroCParser#cmpop.
    def exitCmpop(self, ctx:MicroCParser.CmpopContext):
        pass


    # Enter a parse tree produced by MicroCParser#mulop.
    def enterMulop(self, ctx:MicroCParser.MulopContext):
        pass

    # Exit a parse tree produced by MicroCParser#mulop.
    def exitMulop(self, ctx:MicroCParser.MulopContext):
        pass


    # Enter a parse tree produced by MicroCParser#addop.
    def enterAddop(self, ctx:MicroCParser.AddopContext):
        pass

    # Exit a parse tree produced by MicroCParser#addop.
    def exitAddop(self, ctx:MicroCParser.AddopContext):
        pass



del MicroCParser