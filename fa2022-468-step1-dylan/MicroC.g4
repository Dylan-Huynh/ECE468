grammar MicroC;

@header {
 
}

program : decls function;

/* Declarations */
decls : var_decl decls
      | str_decl decls
	 | /* empty */ ;

var_decls : var_decl var_decls 
          | /* empty */ ;

/* Identifiers and types */		  
ident : IDENTIFIER ;
		  
var_decl : base_type ident ';' ;

str_decl : 'string' ident '=' STR_LITERAL ';' ;

base_type : 'int' | 'float';

/* Functions */

function : 'int' 'main' '(' ')' '{' statements '}' ;
		 		 
/* Statements */
		 
statements : statement statements
            | /* empty */ ;
			
statement : base_stmt ';'
		  | if_stmt
		  | while_stmt ;
		  
base_stmt : assign_stmt
          | read_stmt
		| print_stmt
		| return_stmt ;
		 
read_stmt : 'read' '(' ident ')' ;

print_stmt : 'print' '(' expr ')' ;

return_stmt : 'return' expr ;

assign_stmt : ident '=' expr ;

/* if_stmt rules go here */

if_stmt : 'if' '(' cond ')' '{' statements '}'
          ('else' '{' statements '}')? ;

while_stmt : 'while' '(' cond ')' '{' statements '}' ;
	 
/* Expressions */

primary : ident
        | '(' expr ')'
        | unaryminus_expr
        | INT_LITERAL
        | FLOAT_LITERAL;

unaryminus_expr : '-' expr ;
		 
/* This is left recursive, but ANTLR will clean this up */ 
expr : term
     | expr addop term ;
	 
/* This is left recursive, but ANTLR will clean this up */
term : primary
     | term mulop primary ;
	   	   
cond : expr cmpop expr ;

cmpop : '<' | '<=' | '>=' | '==' | '!=' | '>' ;

mulop : '*' | '/' ;

addop : '+' | '-' ;

/* Tokens */

IDENTIFIER : LETTER (LETTER | ZERO | DIGIT)* ;

INT_LITERAL : ZERO | DIGIT (ZERO | DIGIT)* ;

FLOAT_LITERAL : INT_LITERAL '.' (ZERO | DIGIT)+;

STR_LITERAL : '"' (~('"'))* '"' ;

COMMENT : '/*' .*? '*/' -> skip;

WS : [ \t\n\r]+ -> skip;

fragment LETTER : ('a'..'z' | 'A'..'Z') ;

fragment ZERO : ('0') ;

fragment DIGIT : ('1'..'9') ;
