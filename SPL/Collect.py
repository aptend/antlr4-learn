import sys
from antlr4 import CommonTokenStream, ParseTreeWalker, FileStream, InputStream
from SPLListener import SPLListener
from SPLLexer import SPLLexer
from SPLParser import SPLParser

from enum import Enum, auto


class CMD(Enum):
    SEARCH = auto()
    REPLACE = auto()
    STATS = auto()


class SEARCH_KIND(Enum):
    FULLTEXT = auto()
    CMP_EXPR = auto()
    IN_EXPR = auto()


class CMP_OP(Enum):
    EQ = auto()
    NEQ = auto()
    LE = auto()
    LT = auto()
    GE = auto()
    GT = auto()


class LOGICAL_OP(Enum):
    AND = auto()
    OR = auto()
    NOT = auto()


class Search:
    cid = CMD.SEARCH

    def __init__(self):
        pass


class Replace:
    cid = CMD.REPLACE

    def __init__(self):
        pass


class Stats:
    cid = CMD.STATS

    def __init__(self):
        pass


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
