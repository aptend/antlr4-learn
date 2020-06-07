from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

import argparse
from JSONLexer import JSONLexer
from JSONParser import JSONParser
from J2XListener import MyXmlEmitter, XmlEmitter


def main(args):
    input_stream = FileStream(args.filename)
    lexer = JSONLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = JSONParser(token_stream)
    tree = parser.json()

    emiter = XmlEmitter
    if args.iterative:
        emiter = MyXmlEmitter

    xml = emiter()
    walker = ParseTreeWalker()
    walker.walk(xml, tree)
    print(xml.result())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('-i', dest='iterative', action='store_true')
    args = parser.parse_args()
    main(args)
