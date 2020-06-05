from antlr4 import *

import argparse
import sys
from ArrayInitLexer import ArrayInitLexer
from ArrayInitParser import ArrayInitParser


def main(args):
    input_stream = FileStream(args.filename)
    lexer = ArrayInitLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ArrayInitParser(token_stream)
    tree = parser.init()

    if args.visitor:
        print('Visitor Mode')
    else:
        print('Listener Mode')
        from TransListener import TransListener
        calc = TransListener()
        walker = ParseTreeWalker()
        walker.walk(calc, tree)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('-v', dest='visitor', action='store_true')
    args = parser.parse_args()
    main(args)
