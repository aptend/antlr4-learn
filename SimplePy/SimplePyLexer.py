# Generated from e:\repos\antlr-learn\SimplePy/SimplePyLexer.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\7\5(\n")
        buf.write("\5\f\5\16\5+\13\5\3\6\6\6.\n\6\r\6\16\6/\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\5\13?\n\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\5\fG\n\f\3\f\3\f\3\r\6\rL\n\r")
        buf.write("\r\r\16\rM\3\r\3\r\3\16\3\16\5\16T\n\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\7\17\\\n\17\f\17\16\17_\13\17\3\17\3\17")
        buf.write("\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\3\2\7\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\3\2\62;\4\2\13\13\"\"\4\2\f\f\17\17\2h\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\3\37\3\2\2\2\5!\3\2\2\2\7#\3\2\2\2\t%\3\2\2\2\13")
        buf.write("-\3\2\2\2\r\61\3\2\2\2\17\64\3\2\2\2\21\67\3\2\2\2\23")
        buf.write(":\3\2\2\2\25>\3\2\2\2\27F\3\2\2\2\31K\3\2\2\2\33Q\3\2")
        buf.write("\2\2\35Y\3\2\2\2\37 \7?\2\2 \4\3\2\2\2!\"\7-\2\2\"\6\3")
        buf.write("\2\2\2#$\7.\2\2$\b\3\2\2\2%)\t\2\2\2&(\t\3\2\2\'&\3\2")
        buf.write("\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\n\3\2\2\2+)\3\2\2")
        buf.write("\2,.\t\4\2\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2")
        buf.write("\60\f\3\2\2\2\61\62\7*\2\2\62\63\b\7\2\2\63\16\3\2\2\2")
        buf.write("\64\65\7+\2\2\65\66\b\b\3\2\66\20\3\2\2\2\678\7]\2\28")
        buf.write("9\b\t\4\29\22\3\2\2\2:;\7_\2\2;<\b\n\5\2<\24\3\2\2\2=")
        buf.write("?\7\17\2\2>=\3\2\2\2>?\3\2\2\2?@\3\2\2\2@A\7\f\2\2AB\6")
        buf.write("\13\2\2BC\3\2\2\2CD\b\13\6\2D\26\3\2\2\2EG\7\17\2\2FE")
        buf.write("\3\2\2\2FG\3\2\2\2GH\3\2\2\2HI\7\f\2\2I\30\3\2\2\2JL\t")
        buf.write("\5\2\2KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NO\3\2\2")
        buf.write("\2OP\b\r\6\2P\32\3\2\2\2QS\7^\2\2RT\7\17\2\2SR\3\2\2\2")
        buf.write("ST\3\2\2\2TU\3\2\2\2UV\7\f\2\2VW\3\2\2\2WX\b\16\6\2X\34")
        buf.write("\3\2\2\2Y]\7%\2\2Z\\\n\6\2\2[Z\3\2\2\2\\_\3\2\2\2][\3")
        buf.write("\2\2\2]^\3\2\2\2^`\3\2\2\2_]\3\2\2\2`a\b\17\6\2a\36\3")
        buf.write("\2\2\2\n\2)/>FMS]\7\3\7\2\3\b\3\3\t\4\3\n\5\b\2\2")
        return buf.getvalue()


class SimplePyLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EQ = 1
    PLUS = 2
    COMMA = 3
    ID = 4
    INT = 5
    LPAREN = 6
    RPAREN = 7
    LBRACK = 8
    RBRACK = 9
    IGNORE_NEWLINE = 10
    NEWLINE = 11
    WS = 12
    LINE_ESCAPE = 13
    COMMENT = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'+'", "','", "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "EQ", "PLUS", "COMMA", "ID", "INT", "LPAREN", "RPAREN", "LBRACK", 
            "RBRACK", "IGNORE_NEWLINE", "NEWLINE", "WS", "LINE_ESCAPE", 
            "COMMENT" ]

    ruleNames = [ "EQ", "PLUS", "COMMA", "ID", "INT", "LPAREN", "RPAREN", 
                  "LBRACK", "RBRACK", "IGNORE_NEWLINE", "NEWLINE", "WS", 
                  "LINE_ESCAPE", "COMMENT" ]

    grammarFileName = "SimplePyLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


        self.nesting = 0


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[5] = self.LPAREN_action 
            actions[6] = self.RPAREN_action 
            actions[7] = self.LBRACK_action 
            actions[8] = self.RBRACK_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def LPAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.nesting += 1
     

    def RPAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.nesting -= 1
     

    def LBRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.nesting += 1
     

    def RBRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.nesting -= 1
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[9] = self.IGNORE_NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def IGNORE_NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.nesting>0
         


