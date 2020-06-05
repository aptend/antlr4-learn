grammar DOT;

graph: STRICT? (GRAPH | DIGRAPH) id? '{' stmt_list '}';
stmt_list: (stmt ';'?)*;

stmt: node_stmt | edge_stmt | attr_stmt | id '=' id | subgraph;

attr_stmt: (GRAPH | NODE | EDGE) attr_list;

// 匹配 [shape=box x=y] [color=blue]
attr_list: ('[' (a_list)? ']')+;

// 和书中的不同，按照最新的规范写的，必须有等号
a_list: (id '=' id (';' | ',')?)+;

edge_stmt: (node_id | subgraph) edgeRHS attr_list?;
edgeRHS: (edgeop (node_id | subgraph))+;

edgeop: '->' | '--';
node_stmt: node_id attr_list?;

node_id: id port?;
port: ':' id (':' id)?;

subgraph: (SUBGRAPH id?)? '{' stmt_list '}';

id: ID | NUM | STRING | HTML;

// 终点关键字大小写无关，因为也可以被捕获为ID，所以要放在ID之前
STRICT: [Ss][Tt][Rr][Ii][Cc][Tt];
GRAPH: [Gg][Rr][Aa][Pp][Hh];
DIGRAPH: [Dd][Ii][Gg][Rr][Aa][Pp][Hh];
NODE: [Nn][Oo][Dd][Ee];
EDGE: [Ee][Dd][Gg][Ee];
SUBGRAPH: [Ss][Uu][Bb][Gg][Rr][Aa][Pp][Hh];

/* identifier 字符+数字，不以数字开头 */
ID: LETTER (LETTER | DIGIT)*;

NUM: '-'? (.DIGIT+ | DIGIT+ ('.' DIGIT+)?);
fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z\u0080-\u00FF_];

/* 双引号的string，可能包含转义的引号\" " */
STRING: '"' ('\\"' | .)*? '"';

// 非递归地确定识别开始和结束的尖括号
HTML: '<' (TAG | ~[<>])* '>';
fragment TAG: '<' .*? '>';

/* 注释和预处理 */
COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' .*? '\r'? '\n' -> skip;
PREPROC: '#' .*? '\n' -> skip;

WS: [ \n\r\t]+ -> skip;
