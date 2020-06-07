from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

import argparse
from JSONLexer import JSONLexer
from JSONParser import JSONParser
from J2XListener import MyXmlEmitter

XmlEmitter = MyXmlEmitter

def main(args):
    input_stream = FileStream(args.filename)
    lexer = JSONLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = JSONParser(token_stream)
    tree = parser.value()

    xml = XmlEmitter()
    walker = ParseTreeWalker()
    walker.walk(xml, tree)
    print(xml.result())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    main(args)
