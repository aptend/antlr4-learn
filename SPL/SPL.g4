grammar SPL;

pipeline: head_search (Vbar cmds)*;

cmds: replace | stats | search;

stats:
    Stats stats_agg_term (COMMA? stats_agg_term)* (By field+);

stats_agg_term: stats_func LParen field RParen (As field);

stats_func: Avg;

replace: Replace (value With value (In field)?)+;

head_search: Search? (search_expr)*;

search: Search (search_expr)*;

search_expr:
    Not search_expr
    | search_expr And? search_expr
    | search_expr Or search_expr
    | LParen search_expr RParen
    | field cmp_op wc_value
    | wc_value;

// wc_value包含value
wc_value: value | WcUnquotedValue | WcQuotedString;
// wc_field包含field
wc_field: field | WcUnquotedValue;

value: UnquotedValue | QuotedString;
field: UnquotedValue;

cmp_op: Eq | Le | Lt | Ge | Gt | Neq;

Search: 'search';

Replace: 'replace';

Stats: 'stats';

Avg: 'avg';

As: 'as';
By: 'by';
In: 'in';
Over: 'over';
With: 'with';

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

// 无通配符优先匹配，在parser中处理
// 无通配符
UnquotedValue: [\u4e00-\u9fa5a-zA-Z0-9_.@]+; // 不含特殊字符，暂时包含数字
// 可含有通配符
WcUnquotedValue: [\u4e00-\u9fa5a-zA-Z0-9_.@*]+;

// Json的字符串的转义处理
QuotedString: DQuotes (ESC | ~[\\"*])*? DQuotes;
WcQuotedString: DQuotes (ESC | ~[\\"])*? DQuotes;

fragment ESC: '\\' (["\\/bfnrt] | UNICODE); // 单独列出转义项
fragment UNICODE: 'u' HEX HEX HEX HEX;
fragment HEX: [0-9a-fA-F];

WS: [ \t\r\n]+ -> skip; //channel(HIDDEN);
