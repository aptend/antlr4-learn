# Generated from JSON.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3\25\n\3\3\4\3\4\3\4\3\4\7\4\33")
        buf.write("\n\4\f\4\16\4\36\13\4\3\4\3\4\3\4\3\4\5\4$\n\4\3\5\3\5")
        buf.write("\3\5\3\5\7\5*\n\5\f\5\16\5-\13\5\3\5\3\5\3\5\3\5\5\5\63")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\6\2\2\7\2\4\6\b\n\2\2\2<\2\f\3")
        buf.write("\2\2\2\4\24\3\2\2\2\6#\3\2\2\2\b\62\3\2\2\2\n\64\3\2\2")
        buf.write("\2\f\r\5\4\3\2\r\3\3\2\2\2\16\25\7\13\2\2\17\25\7\f\2")
        buf.write("\2\20\25\5\b\5\2\21\25\5\6\4\2\22\25\7\t\2\2\23\25\7\n")
        buf.write("\2\2\24\16\3\2\2\2\24\17\3\2\2\2\24\20\3\2\2\2\24\21\3")
        buf.write("\2\2\2\24\22\3\2\2\2\24\23\3\2\2\2\25\5\3\2\2\2\26\27")
        buf.write("\7\3\2\2\27\34\5\n\6\2\30\31\7\4\2\2\31\33\5\n\6\2\32")
        buf.write("\30\3\2\2\2\33\36\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2")
        buf.write("\35\37\3\2\2\2\36\34\3\2\2\2\37 \7\5\2\2 $\3\2\2\2!\"")
        buf.write("\7\3\2\2\"$\7\5\2\2#\26\3\2\2\2#!\3\2\2\2$\7\3\2\2\2%")
        buf.write("&\7\6\2\2&+\5\4\3\2\'(\7\4\2\2(*\5\4\3\2)\'\3\2\2\2*-")
        buf.write("\3\2\2\2+)\3\2\2\2+,\3\2\2\2,.\3\2\2\2-+\3\2\2\2./\7\7")
        buf.write("\2\2/\63\3\2\2\2\60\61\7\6\2\2\61\63\7\7\2\2\62%\3\2\2")
        buf.write("\2\62\60\3\2\2\2\63\t\3\2\2\2\64\65\7\13\2\2\65\66\7\b")
        buf.write("\2\2\66\67\5\4\3\2\67\13\3\2\2\2\7\24\34#+\62")
        return buf.getvalue()


class JSONParser ( Parser ):

    grammarFileName = "JSON.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "','", "'}'", "'['", "']'", "':'", 
                     "<INVALID>", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "BOOLEAN", 
                      "NULL", "STRING", "NUMBER", "WS" ]

    RULE_json = 0
    RULE_value = 1
    RULE_obj = 2
    RULE_array = 3
    RULE_pair = 4

    ruleNames =  [ "json", "value", "obj", "array", "pair" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    BOOLEAN=7
    NULL=8
    STRING=9
    NUMBER=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class JsonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(JSONParser.ValueContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_json

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson" ):
                listener.enterJson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson" ):
                listener.exitJson(self)




    def json(self):

        localctx = JSONParser.JsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_json)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JSONParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ObjValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def obj(self):
            return self.getTypedRuleContext(JSONParser.ObjContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjValue" ):
                listener.enterObjValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjValue" ):
                listener.exitObjValue(self)


    class StringContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(JSONParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class ArrayValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(JSONParser.ArrayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayValue" ):
                listener.enterArrayValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayValue" ):
                listener.exitArrayValue(self)


    class AtomContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(JSONParser.NUMBER, 0)
        def BOOLEAN(self):
            return self.getToken(JSONParser.BOOLEAN, 0)
        def NULL(self):
            return self.getToken(JSONParser.NULL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)



    def value(self):

        localctx = JSONParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_value)
        try:
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONParser.STRING]:
                localctx = JSONParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(JSONParser.STRING)
                pass
            elif token in [JSONParser.NUMBER]:
                localctx = JSONParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.match(JSONParser.NUMBER)
                pass
            elif token in [JSONParser.T__3]:
                localctx = JSONParser.ArrayValueContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.array()
                pass
            elif token in [JSONParser.T__0]:
                localctx = JSONParser.ObjValueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 15
                self.obj()
                pass
            elif token in [JSONParser.BOOLEAN]:
                localctx = JSONParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 16
                self.match(JSONParser.BOOLEAN)
                pass
            elif token in [JSONParser.NULL]:
                localctx = JSONParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 17
                self.match(JSONParser.NULL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JSONParser.RULE_obj

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EmptyObjContext(ObjContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ObjContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyObj" ):
                listener.enterEmptyObj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyObj" ):
                listener.exitEmptyObj(self)


    class AnObjContext(ObjContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ObjContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONParser.PairContext)
            else:
                return self.getTypedRuleContext(JSONParser.PairContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnObj" ):
                listener.enterAnObj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnObj" ):
                listener.exitAnObj(self)



    def obj(self):

        localctx = JSONParser.ObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = JSONParser.AnObjContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.match(JSONParser.T__0)
                self.state = 21
                self.pair()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONParser.T__1:
                    self.state = 22
                    self.match(JSONParser.T__1)
                    self.state = 23
                    self.pair()
                    self.state = 28
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 29
                self.match(JSONParser.T__2)
                pass

            elif la_ == 2:
                localctx = JSONParser.EmptyObjContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.match(JSONParser.T__0)
                self.state = 32
                self.match(JSONParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JSONParser.RULE_array

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EmptyArrayContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyArray" ):
                listener.enterEmptyArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyArray" ):
                listener.exitEmptyArray(self)


    class AnArrayContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONParser.ValueContext)
            else:
                return self.getTypedRuleContext(JSONParser.ValueContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnArray" ):
                listener.enterAnArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnArray" ):
                listener.exitAnArray(self)



    def array(self):

        localctx = JSONParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = JSONParser.AnArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(JSONParser.T__3)
                self.state = 36
                self.value()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONParser.T__1:
                    self.state = 37
                    self.match(JSONParser.T__1)
                    self.state = 38
                    self.value()
                    self.state = 43
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 44
                self.match(JSONParser.T__4)
                pass

            elif la_ == 2:
                localctx = JSONParser.EmptyArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(JSONParser.T__3)
                self.state = 47
                self.match(JSONParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSONParser.STRING, 0)

        def value(self):
            return self.getTypedRuleContext(JSONParser.ValueContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self):

        localctx = JSONParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(JSONParser.STRING)
            self.state = 51
            self.match(JSONParser.T__5)
            self.state = 52
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





