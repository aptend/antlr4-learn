lexer grammar SPLLexer;

Search: 'search';

Replace: 'replace';
In: 'in';

With: 'with';

Stats: 'stats';

Avg: 'avg';

As: 'as';

By: 'by';

// 符号
Vbar: '|';
LParen: '(';
RParen: ')';
DQuotes: '"';
COMMA: ',';
Eq: '=';
Neq: '!=';
Lt: '<';
Gt: '>';
Le: '<=';
Ge: '>=';

// 逻辑
And: [aA][nN][dD];
Or: [oO][rR];
Not: [nN][oO][tT];

// KEYWORDS: Search | Replace | Stats | Avg | With | As | By | In;

// ID // : KEYWORDS : [\u4e00-\u9fa5a-zA-Z_][\u4e00-\u9fa5a-zA-Z0-9_.@]* | QuotedString;

// 无通配符
// UnquotedValue: [\u4e00-\u9fa5a-zA-Z0-9_.@]+; // 不含转义字符、空格，暂时包含数字
UnquotedValue: [0-9]+; // 不含转义字符、空格，暂时包含数字

// 可含有通配符 WcValue: [\u4e00-\u9fa5a-zA-Z0-9_.@*]+ | WcQuotedString;

// Json的字符串的转义处理 
QuotedString: DQuotes (ESC | ~[\\"*])*? DQuotes;

//WcQuotedString: DQuotes (ESC | ~[\\"])*? DQuotes; 
fragment ESC: '\\' (["\\/bfnrt] | UNICODE); // 单独列出转义项
fragment UNICODE: 'u' HEX HEX HEX HEX;
fragment HEX: [0-9a-fA-F];

WS: [ \t\r\n]+ -> skip ; //channel(HIDDEN);
