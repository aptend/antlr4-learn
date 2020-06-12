import sys
import argparse
from antlr4 import FileStream, InputStream, CommonTokenStream
from SimpleJavaLexer import SimpleJavaLexer
from SimpleJavaParser import SimpleJavaParser
from SimpleJavaErrorListener import VerboseListener

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('-f', '--file', default=None)
    p.add_argument('-t', '--tokens', action="store_true")

    args = p.parse_args()
    if args.file:
        input_stream = FileStream(args.file, encoding='utf8')
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = SimpleJavaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    if args.tokens:
        for tok in token_stream.tokens:
            print(tok)
    parser = SimpleJavaParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(VerboseListener())
    parser.prog()
