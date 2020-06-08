lexer grammar CymbolLexer;

channels {
    COMMENTS_CHAN,
    WHITESPACE
}

AHHH: '!';

EQ: '=';
DEQ: '==';

SEMICOLON: ';';
COMMA: ',';

TVOID: 'void';
TFLOAT: 'float';
TINT: 'int';

LPAREN: '(';
RPAREN: ')';

LBRACKET: '[';
RBRACKET: ']';

LBRACE: '{';
RBRACE: '}';

MULT: '*';
MINUS: '-';
PLUS: '+';

IF: 'if';
THEN: 'then';
ELSE: 'else';
RET: 'return';

ID: LETTER (LETTER | DIGIT)*;
INT: '0' | [1-9] (DIGIT)*;

fragment LETTER: [a-zA-Z_];
fragment DIGIT: [0-9];

COMMENTS: '//' .*? '\r'? '\n' -> channel(COMMENTS_CHAN);

WS: [ \t\r\n]+ -> channel(WHITESPACE);
