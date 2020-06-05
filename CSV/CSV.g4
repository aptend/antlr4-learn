grammar CSV;

file: hdr row+;

hdr: row;

row: field (',' field)* '\r'?'\n';

field: STRING
     | TEXT
     |
     ;
TEXT: ~[,\n\r"]+;
STRING: '"' ('""' | ~'"')* '"';

