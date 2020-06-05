from antlr4 import *

import argparse
import sys
from LExprLexer import LExprLexer
from LExprParser import LExprParser


def main(args):
    input_stream = FileStream(args.filename)
    lexer = LExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LExprParser(token_stream)
    tree = parser.s()

    if args.visitor:
        print('Visitor Mode')
        from CalcVisitor import CalcVisitor
        calc = CalcVisitor()
        print('result: ', calc.visit(tree))
    else:
        print('Listener Mode')
        from CalcListener import CalcListener
        calc = CalcListener()
        walker = ParseTreeWalker()
        walker.walk(calc, tree)
        print('result: ', calc.result())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('-v', dest='visitor', action='store_true')
    args = parser.parse_args()
    main(args)
