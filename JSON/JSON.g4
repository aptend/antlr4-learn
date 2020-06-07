grammar JSON;

obj
    : '{' pair (',' pair)* '}' # AnObj
    | '{' '}'                  # EmptyObj
    ;

array
    : '[' value (',' value)* ']'  # AnArray
    | '[' ']'                     # EmptyArray
    ;
pair: STRING ':' value;

value
    : STRING  # String
    | NUMBER  # Atom
    | array   # Skip
    | obj     # Skip
    | BOOLEAN # Atom
    | NULL    # Atom
    ;
BOOLEAN: 'true'|'false';

NULL: 'null';


STRING: '"' (ESC | ~[\\"])*? '"'; // ~[\\"]排除引号和斜杠
fragment ESC: '\\' (["\\/bfnrt] | UNICODE); // 单独列出转义项
fragment UNICODE: 'u' HEX HEX HEX HEX;
fragment HEX: [0-9a-fA-F];


NUMBER: '-'? INT? '.' [0-9]+ EXP? // .3  1.25E7 -4.5 浮点数
      | '-'? INT EXP // 指数型
      | '-'? INT ; // 整型
fragment INT: '0' | [1-9] [0-9]*; // 无前导0
fragment EXP: [Ee] [+\-]? INT; // 指数部分;

WS: [ \t\r\n]+ -> skip;
