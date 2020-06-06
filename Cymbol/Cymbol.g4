grammar Cymbol;

file: (varDecl | functionDecl)+ ;

varDecl: type ID ('=' expr)? ';' ;

type: 'int' | 'float' | 'void';

functionDecl: type ID '(' formalParameters ')' block;

formalParameters: type ID (',' type ID)*;

block: '{' stat* '}';

stat: block
    | varDecl
    | ifstat            // 结构化的语句优先级更高
    | retstat
    | assginstat        // 赋值 a = 2;
    | expr ';'          // 函数调用 f(a+1);
    ;

ifstat: 'if' expr 'then' stat ('else' stat)?;

retstat: 'return' expr? ';' ;

assginstat: expr '=' expr ';' ;

expr: ID '(' exprList? ')' // 函数调用
    | ID '[' expr ']'      // 数组索引, 优先级高于一元'-'，-a[0]
    | '-' ID               // 一元操作符
    | '!' ID
    | expr '*' expr        // 四则运算
    | expr ('+'|'-') expr
    | expr '==' expr  // 最低优先级
    | ID
    | INT
    | '(' expr ')'   // 括号
    ;

exprList: expr (',' expr)* ;


ID: LETTER(LETTER|DIGIT)*;
INT: '0' | [1-9] (DIGIT)*;

fragment LETTER: [a-zA-Z_];
fragment DIGIT: [0-9];


COMMENTS: '//' .*? '\r'?'\n' -> skip;

WS: [ \t\r\n]+ -> skip;
