import sys
from antlr4 import FileStream, InputStream, CommonTokenStream
from SimplePyLexer import SimplePyLexer

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = SimplePyLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    for tok in token_stream.tokens:
        print(tok)
