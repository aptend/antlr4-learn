import sys
from antlr4 import CommonTokenStream, ParseTreeWalker, FileStream, InputStream
from SPLListener import SPLListener
from SPLLexer import SPLLexer
from SPLParser import SPLParser


class Pipeliner(SPLListener):
    def __init__(self):
        self._cmds = []

    def cmds(self):
        return self._cmds


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = SPLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SPLParser(token_stream)
    tree = parser.pipeline()

    walker = ParseTreeWalker()
    pipeliner = Pipeliner()
    walker.walk(pipeliner, tree)
    print(pipeliner.cmds())
