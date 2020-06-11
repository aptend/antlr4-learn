grammar SPL;

pipeline: headSearch (Vbar cmd)*;

cmd: replace | stats | search;

// Stats
stats: Stats statsAggTermList (By fieldList)?;

statsAggTerm
    : statsFunc LParen func_field = field RParen (
        As as_field = field
    )?;

statsAggTermList: statsAggTerm (COMMA? statsAggTerm)*;

statsFunc: Avg | Max | Min;

// Replace
replace: Replace replaceExprList (In fieldList)?;

replaceExpr: old_val = wcValue With new_val = wcValue;

replaceExprList: replaceExpr (COMMA? replaceExpr)*;

/// Search
headSearch: Search? (searchExpr)?;

search: Search (searchExpr)?;

searchExpr
    : Not searchExpr                            # NotSearch
    | left = searchExpr And? right = searchExpr # AndSearch
    | left = searchExpr Or right = searchExpr   # OrSearch
    | LParen searchExpr RParen                  # ParenSearch
    | field cmpOp wcValue                       # FieldCmpSearch
    | wcValue                                   # FullTextSearch;

// wcValue包含value
wcValue: value | WcUnquotedValue | WcQuotedString;
// wcField包含field
wcField: field | WcUnquotedValue;

value: UnquotedValue | QuotedString;
field: UnquotedValue;

fieldList: field (COMMA? field)*;

cmpOp: Eq | Le | Lt | Ge | Gt | Neq;

Search: 'search';

Replace: 'replace';

Stats: 'stats';

Avg: 'avg';
Max: 'max';
Min: 'min';

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

// KEYWORDS: Search | Replace | Stats | Avg | With | As | By | In; ID // : KEYWORDS :
// [\u4e00-\u9fa5a-zA-Z_][\u4e00-\u9fa5a-zA-Z0-9_.@]* | QuotedString;

// 无通配符优先匹配，在parser中处理 无通配符
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
