grammar SPL;

pipeline: cmd args=ID '=' '"' ID '"' ('|' pipeline)*;

cmd: 'search';

ID: [a-z]+;
WS: [ \t\r\n]+ -> skip;
