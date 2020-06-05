import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from HelloLexer import HelloLexer
from HelloParser import HelloParser
from TestListener import TestListener


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = HelloLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    tree = parser.r()

    listener = TestListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


if __name__ == '__main__':
    main(sys.argv)
