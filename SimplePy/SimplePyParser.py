# Generated from e:\repos\antlr-learn\SimplePy\SimplePy.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("O\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\6\2\20\n\2\r\2\16\2\21\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\33\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\5\5*\n\5\3\5\3\5\3\5\7\5/\n\5\f\5\16\5\62\13")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\7\69\n\6\f\6\16\6<\13\6\5\6>\n")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7F\n\7\f\7\16\7I\13\7\5\7")
        buf.write("K\n\7\3\7\3\7\3\7\2\3\b\b\2\4\6\b\n\f\2\2\2T\2\17\3\2")
        buf.write("\2\2\4\32\3\2\2\2\6\34\3\2\2\2\b)\3\2\2\2\n\63\3\2\2\2")
        buf.write("\fA\3\2\2\2\16\20\5\4\3\2\17\16\3\2\2\2\20\21\3\2\2\2")
        buf.write("\21\17\3\2\2\2\21\22\3\2\2\2\22\3\3\2\2\2\23\24\5\6\4")
        buf.write("\2\24\25\7\r\2\2\25\33\3\2\2\2\26\27\5\b\5\2\27\30\7\r")
        buf.write("\2\2\30\33\3\2\2\2\31\33\7\r\2\2\32\23\3\2\2\2\32\26\3")
        buf.write("\2\2\2\32\31\3\2\2\2\33\5\3\2\2\2\34\35\7\6\2\2\35\36")
        buf.write("\7\3\2\2\36\37\5\b\5\2\37\7\3\2\2\2 !\b\5\1\2!\"\7\b\2")
        buf.write("\2\"#\5\b\5\2#$\7\t\2\2$*\3\2\2\2%*\5\n\6\2&*\5\f\7\2")
        buf.write("\'*\7\6\2\2(*\7\7\2\2) \3\2\2\2)%\3\2\2\2)&\3\2\2\2)\'")
        buf.write("\3\2\2\2)(\3\2\2\2*\60\3\2\2\2+,\f\b\2\2,-\7\4\2\2-/\5")
        buf.write("\b\5\t.+\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2")
        buf.write("\61\t\3\2\2\2\62\60\3\2\2\2\63\64\7\6\2\2\64=\7\b\2\2")
        buf.write("\65:\5\b\5\2\66\67\7\5\2\2\679\5\b\5\28\66\3\2\2\29<\3")
        buf.write("\2\2\2:8\3\2\2\2:;\3\2\2\2;>\3\2\2\2<:\3\2\2\2=\65\3\2")
        buf.write("\2\2=>\3\2\2\2>?\3\2\2\2?@\7\t\2\2@\13\3\2\2\2AJ\7\n\2")
        buf.write("\2BG\5\b\5\2CD\7\5\2\2DF\5\b\5\2EC\3\2\2\2FI\3\2\2\2G")
        buf.write("E\3\2\2\2GH\3\2\2\2HK\3\2\2\2IG\3\2\2\2JB\3\2\2\2JK\3")
        buf.write("\2\2\2KL\3\2\2\2LM\7\13\2\2M\r\3\2\2\2\n\21\32)\60:=G")
        buf.write("J")
        return buf.getvalue()


class SimplePyParser ( Parser ):

    grammarFileName = "SimplePy.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+'", "','", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "EQ", "PLUS", "COMMA", "ID", "INT", "LPAREN", 
                      "RPAREN", "LBRACK", "RBRACK", "IGNORE_NEWLINE", "NEWLINE", 
                      "WS", "LINE_ESCAPE", "COMMENT" ]

    RULE_file = 0
    RULE_stat = 1
    RULE_assign = 2
    RULE_expr = 3
    RULE_call = 4
    RULE_list = 5

    ruleNames =  [ "file", "stat", "assign", "expr", "call", "list" ]

    EOF = Token.EOF
    EQ=1
    PLUS=2
    COMMA=3
    ID=4
    INT=5
    LPAREN=6
    RPAREN=7
    LBRACK=8
    RBRACK=9
    IGNORE_NEWLINE=10
    NEWLINE=11
    WS=12
    LINE_ESCAPE=13
    COMMENT=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class FileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePyParser.StatContext)
            else:
                return self.getTypedRuleContext(SimplePyParser.StatContext,i)


        def getRuleIndex(self):
            return SimplePyParser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)




    def file(self):

        localctx = SimplePyParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.stat()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePyParser.ID) | (1 << SimplePyParser.INT) | (1 << SimplePyParser.LPAREN) | (1 << SimplePyParser.LBRACK) | (1 << SimplePyParser.NEWLINE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(SimplePyParser.AssignContext,0)


        def NEWLINE(self):
            return self.getToken(SimplePyParser.NEWLINE, 0)

        def expr(self):
            return self.getTypedRuleContext(SimplePyParser.ExprContext,0)


        def getRuleIndex(self):
            return SimplePyParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = SimplePyParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.assign()
                self.state = 18
                self.match(SimplePyParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.expr(0)
                self.state = 21
                self.match(SimplePyParser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.match(SimplePyParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimplePyParser.ID, 0)

        def EQ(self):
            return self.getToken(SimplePyParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(SimplePyParser.ExprContext,0)


        def getRuleIndex(self):
            return SimplePyParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = SimplePyParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(SimplePyParser.ID)
            self.state = 27
            self.match(SimplePyParser.EQ)
            self.state = 28
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(SimplePyParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePyParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimplePyParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(SimplePyParser.RPAREN, 0)

        def call(self):
            return self.getTypedRuleContext(SimplePyParser.CallContext,0)


        def list(self):
            return self.getTypedRuleContext(SimplePyParser.ListContext,0)


        def ID(self):
            return self.getToken(SimplePyParser.ID, 0)

        def INT(self):
            return self.getToken(SimplePyParser.INT, 0)

        def PLUS(self):
            return self.getToken(SimplePyParser.PLUS, 0)

        def getRuleIndex(self):
            return SimplePyParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimplePyParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 31
                self.match(SimplePyParser.LPAREN)
                self.state = 32
                self.expr(0)
                self.state = 33
                self.match(SimplePyParser.RPAREN)
                pass

            elif la_ == 2:
                self.state = 35
                self.call()
                pass

            elif la_ == 3:
                self.state = 36
                self.list()
                pass

            elif la_ == 4:
                self.state = 37
                self.match(SimplePyParser.ID)
                pass

            elif la_ == 5:
                self.state = 38
                self.match(SimplePyParser.INT)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimplePyParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 41
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 42
                    self.match(SimplePyParser.PLUS)
                    self.state = 43
                    self.expr(7) 
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimplePyParser.ID, 0)

        def LPAREN(self):
            return self.getToken(SimplePyParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SimplePyParser.RPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePyParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimplePyParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePyParser.COMMA)
            else:
                return self.getToken(SimplePyParser.COMMA, i)

        def getRuleIndex(self):
            return SimplePyParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = SimplePyParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(SimplePyParser.ID)
            self.state = 50
            self.match(SimplePyParser.LPAREN)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePyParser.ID) | (1 << SimplePyParser.INT) | (1 << SimplePyParser.LPAREN) | (1 << SimplePyParser.LBRACK))) != 0):
                self.state = 51
                self.expr(0)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SimplePyParser.COMMA:
                    self.state = 52
                    self.match(SimplePyParser.COMMA)
                    self.state = 53
                    self.expr(0)
                    self.state = 58
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 61
            self.match(SimplePyParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(SimplePyParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(SimplePyParser.RBRACK, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePyParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimplePyParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePyParser.COMMA)
            else:
                return self.getToken(SimplePyParser.COMMA, i)

        def getRuleIndex(self):
            return SimplePyParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)




    def list(self):

        localctx = SimplePyParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(SimplePyParser.LBRACK)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePyParser.ID) | (1 << SimplePyParser.INT) | (1 << SimplePyParser.LPAREN) | (1 << SimplePyParser.LBRACK))) != 0):
                self.state = 64
                self.expr(0)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SimplePyParser.COMMA:
                    self.state = 65
                    self.match(SimplePyParser.COMMA)
                    self.state = 66
                    self.expr(0)
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 74
            self.match(SimplePyParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         




