parser grammar Cymbol;

options {
	tokenVocab = CymbolLexer;
}

src: (varDecl | functionDecl)+ ;

varDecl: typeT ID (EQ expr)? SEMICOLON ;

typeT: TINT | TFLOAT | TVOID;

functionDecl: typeT ID LPAREN formalParameters RPAREN block;

formalParameters: typeT ID (COMMA typeT ID)*;

block: LBRACE stat* RBRACE;

stat: block
    | varDecl
    | ifstat            // 结构化的语句优先级更高
    | retstat
    | assginstat        // 赋值 a = 2;
	| expr SEMICOLON          // 函数调用 f(a+1);
    ;

ifstat: IF expr THEN stat (ELSE stat)?;

retstat: RET expr? SEMICOLON ;

assginstat: expr EQ expr SEMICOLON ;

expr: ID LPAREN exprList? RPAREN // 函数调用
    | ID LBRACKET expr RBRACKET      // 数组索引, 优先级高于一元'-'，-a[0]
    | MINUS ID               // 一元操作符
    | AHHH ID
    | expr MULT expr        // 四则运算
    | expr (PLUS|MINUS) expr
    | expr DEQ expr  // 最低优先级
    | ID
    | INT
    | LPAREN expr RPAREN   // 括号
    ;

exprList: expr (COMMA expr)* ;

