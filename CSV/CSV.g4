grammar CSV;

csvfile: hdr row+;

hdr: row;

row: field (',' field)* '\r'?'\n';

field: STRING # string
     | TEXT   # text
     |        # none
     ;
TEXT: ~[,\n\r"]+;
STRING: '"' ('""' | ~'"')* '"';

