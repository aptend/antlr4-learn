lexer grammar SimplePyLexer;

@members {
    self.nesting = 0
}

EQ: '=';
PLUS: '+';
COMMA: ',';

ID: [a-zA-Z_][a-zA-Z_0-9]*;

INT: [0-9]+;

LPAREN: '(' {self.nesting += 1};

RPAREN: ')' {self.nesting -= 1};

LBRACK: '[' {self.nesting += 1};

RBRACK: ']' {self.nesting -= 1};

/** 在嵌套结构中的换行符被忽略，也就是在()或[]中，必须置于NEWLINE之前处理 */
IGNORE_NEWLINE: '\r'? '\n' {self.nesting>0}? -> skip;

NEWLINE: '\r'? '\n';

/** 警告: 这里直接抛弃了空格符，也就是不处理缩进的代码块，单一作用域的语句执行 */
WS: [ \t]+ -> skip;

/** 忽略换行转义 */
LINE_ESCAPE: '\\' '\r'? '\n' -> skip;

/** 处理语句后的注释，注意不能处理换行符，换行符留着给语句分段用 */
COMMENT: '#' ~[\r\n]* -> skip;
