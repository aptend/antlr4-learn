# Generated from SimpleJava.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("R\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\6\n\63\n\n\r\n\16\n")
        buf.write("\64\3\13\6\138\n\13\r\13\16\139\3\f\6\f=\n\f\r\f\16\f")
        buf.write(">\3\f\3\f\3\r\3\r\3\r\3\r\7\rG\n\r\f\r\16\rJ\13\r\3\r")
        buf.write("\5\rM\n\r\3\r\3\r\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\3\2\6\3\2\62;\4\2")
        buf.write("C\\c|\5\2\13\f\17\17\"\"\4\2\f\f\17\17\2V\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5!\3\2\2")
        buf.write("\2\7#\3\2\2\2\t%\3\2\2\2\13)\3\2\2\2\r+\3\2\2\2\17-\3")
        buf.write("\2\2\2\21/\3\2\2\2\23\62\3\2\2\2\25\67\3\2\2\2\27<\3\2")
        buf.write("\2\2\31B\3\2\2\2\33\34\7e\2\2\34\35\7n\2\2\35\36\7c\2")
        buf.write("\2\36\37\7u\2\2\37 \7u\2\2 \4\3\2\2\2!\"\7}\2\2\"\6\3")
        buf.write("\2\2\2#$\7\177\2\2$\b\3\2\2\2%&\7k\2\2&\'\7p\2\2\'(\7")
        buf.write("v\2\2(\n\3\2\2\2)*\7=\2\2*\f\3\2\2\2+,\7*\2\2,\16\3\2")
        buf.write("\2\2-.\7+\2\2.\20\3\2\2\2/\60\7?\2\2\60\22\3\2\2\2\61")
        buf.write("\63\t\2\2\2\62\61\3\2\2\2\63\64\3\2\2\2\64\62\3\2\2\2")
        buf.write("\64\65\3\2\2\2\65\24\3\2\2\2\668\t\3\2\2\67\66\3\2\2\2")
        buf.write("89\3\2\2\29\67\3\2\2\29:\3\2\2\2:\26\3\2\2\2;=\t\4\2\2")
        buf.write("<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?@\3\2\2\2@A\b")
        buf.write("\f\2\2A\30\3\2\2\2BC\7\61\2\2CD\7\61\2\2DH\3\2\2\2EG\n")
        buf.write("\5\2\2FE\3\2\2\2GJ\3\2\2\2HF\3\2\2\2HI\3\2\2\2IL\3\2\2")
        buf.write("\2JH\3\2\2\2KM\7\17\2\2LK\3\2\2\2LM\3\2\2\2MN\3\2\2\2")
        buf.write("NO\7\f\2\2OP\3\2\2\2PQ\b\r\2\2Q\32\3\2\2\2\b\2\649>HL")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class SimpleJavaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    INT = 9
    ID = 10
    WS = 11
    COM = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'class'", "'{'", "'}'", "'int'", "';'", "'('", "')'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "INT", "ID", "WS", "COM" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "INT", "ID", "WS", "COM" ]

    grammarFileName = "SimpleJava.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


