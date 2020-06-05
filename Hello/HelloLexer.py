# Generated from Hello.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("\"\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\6\3\23\n\3\r\3\16\3\24\3\4\6\4\30\n\4\r\4")
        buf.write("\16\4\31\3\5\6\5\35\n\5\r\5\16\5\36\3\5\3\5\2\2\6\3\3")
        buf.write("\5\4\7\5\t\6\3\2\5\3\2c|\3\2\62;\5\2\13\f\17\17\"\"\2")
        buf.write("$\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\3\13")
        buf.write("\3\2\2\2\5\22\3\2\2\2\7\27\3\2\2\2\t\34\3\2\2\2\13\f\7")
        buf.write("j\2\2\f\r\7g\2\2\r\16\7n\2\2\16\17\7n\2\2\17\20\7q\2\2")
        buf.write("\20\4\3\2\2\2\21\23\t\2\2\2\22\21\3\2\2\2\23\24\3\2\2")
        buf.write("\2\24\22\3\2\2\2\24\25\3\2\2\2\25\6\3\2\2\2\26\30\t\3")
        buf.write("\2\2\27\26\3\2\2\2\30\31\3\2\2\2\31\27\3\2\2\2\31\32\3")
        buf.write("\2\2\2\32\b\3\2\2\2\33\35\t\4\2\2\34\33\3\2\2\2\35\36")
        buf.write("\3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37 \3\2\2\2 !\b\5")
        buf.write("\2\2!\n\3\2\2\2\6\2\24\31\36\3\b\2\2")
        return buf.getvalue()


class HelloLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    ID = 2
    NUM = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'hello'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUM", "WS" ]

    ruleNames = [ "T__0", "ID", "NUM", "WS" ]

    grammarFileName = "Hello.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


