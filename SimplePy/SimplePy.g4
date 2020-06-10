/** Explore Python newline and comment processing */
grammar SimplePy;

options {
	tokenVocab = SimplePyLexer;
}

file: stat+;

stat:
	assign NEWLINE
	| expr NEWLINE
	| NEWLINE; // ignore blank lines

assign: ID EQ expr;

expr:
	expr PLUS expr
	| LPAREN expr RPAREN
	| call
	| list
	| ID
	| INT;

call:
	ID LPAREN (expr (COMMA expr)*)? RPAREN; // foo(bar, baz)

list: LBRACK (expr (COMMA expr)*)? RBRACK; // [bar, baz]
