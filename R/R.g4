grammar R;

prog: (expr_or_assign (';'|NL))*;

expr_or_assign: expr ('<-'|'='|'<<-') expr_or_assign
              | expr
              ;

expr: '{' exprList '}'
    |
    ;
exprList: expr_or_assign ((';' | NL) expr_or_assign?)* |;

NL: '\r'?'\n';

