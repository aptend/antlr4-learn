parser grammar SPLParser;

options {
    tokenVocab = SPLLexer;
}

pipeline: head_search (Vbar cmds)*;

cmds: replace | stats | search;

stats: Stats stats_agg_term (COMMA? stats_agg_term)* (By field+);

stats_agg_term: stats_func LParen field RParen (As field);

stats_func: Avg;

replace: Replace (value With value (In field)?)+;

head_search: Search? (search_expr)*;

search: Search (search_expr)*;

search_expr
    : Not search_expr
    | search_expr And? search_expr
    | search_expr Or search_expr
    | field cmp_op value
    | value;

value: UnquotedValue | QuotedString;
field: UnquotedValue;

cmp_op: Eq | Le | Lt | Ge | Gt | Neq;

