grammar Hello;
r: 'hello' (ID | NUM);
ID: [a-z]+;
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;
