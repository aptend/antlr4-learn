from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

import argparse
from CSVLexer import CSVLexer
from CSVParser import CSVParser
from tableListener import TableListener


def main(args):
    input_stream = FileStream(args.filename)
    lexer = CSVLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CSVParser(token_stream)
    tree = parser.csvfile()

    table = TableListener()
    walker = ParseTreeWalker()
    walker.walk(table, tree)
    for row in table.result():
        print(row)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    main(args)
