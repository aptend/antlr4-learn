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
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\7")
        buf.write("\2\17\n\2\f\2\16\2\22\13\2\3\2\3\2\3\2\3\2\5\2\30\n\2")
        buf.write("\3\3\3\3\3\3\3\3\7\3\36\n\3\f\3\16\3!\13\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3\'\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\5\5\63\n\5\3\5\2\2\6\2\4\6\b\2\2\29\2\27\3\2\2\2\4&\3")
        buf.write("\2\2\2\6(\3\2\2\2\b\62\3\2\2\2\n\13\7\3\2\2\13\20\5\6")
        buf.write("\4\2\f\r\7\4\2\2\r\17\5\6\4\2\16\f\3\2\2\2\17\22\3\2\2")
        buf.write("\2\20\16\3\2\2\2\20\21\3\2\2\2\21\23\3\2\2\2\22\20\3\2")
        buf.write("\2\2\23\24\7\5\2\2\24\30\3\2\2\2\25\26\7\3\2\2\26\30\7")
        buf.write("\5\2\2\27\n\3\2\2\2\27\25\3\2\2\2\30\3\3\2\2\2\31\32\7")
        buf.write("\6\2\2\32\37\5\b\5\2\33\34\7\4\2\2\34\36\5\b\5\2\35\33")
        buf.write("\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 \"\3\2")
        buf.write("\2\2!\37\3\2\2\2\"#\7\7\2\2#\'\3\2\2\2$%\7\6\2\2%\'\7")
        buf.write("\7\2\2&\31\3\2\2\2&$\3\2\2\2\'\5\3\2\2\2()\7\13\2\2)*")
        buf.write("\7\b\2\2*+\5\b\5\2+\7\3\2\2\2,\63\7\13\2\2-\63\7\f\2\2")
        buf.write(".\63\5\4\3\2/\63\5\2\2\2\60\63\7\t\2\2\61\63\7\n\2\2\62")
        buf.write(",\3\2\2\2\62-\3\2\2\2\62.\3\2\2\2\62/\3\2\2\2\62\60\3")
        buf.write("\2\2\2\62\61\3\2\2\2\63\t\3\2\2\2\7\20\27\37&\62")
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

    RULE_obj = 0
    RULE_array = 1
    RULE_pair = 2
    RULE_value = 3

    ruleNames =  [ "obj", "array", "pair", "value" ]

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
        self.enterRule(localctx, 0, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = JSONParser.AnObjContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(JSONParser.T__0)
                self.state = 9
                self.pair()
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONParser.T__1:
                    self.state = 10
                    self.match(JSONParser.T__1)
                    self.state = 11
                    self.pair()
                    self.state = 16
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 17
                self.match(JSONParser.T__2)
                pass

            elif la_ == 2:
                localctx = JSONParser.EmptyObjContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(JSONParser.T__0)
                self.state = 20
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
        self.enterRule(localctx, 2, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = JSONParser.AnArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(JSONParser.T__3)
                self.state = 24
                self.value()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONParser.T__1:
                    self.state = 25
                    self.match(JSONParser.T__1)
                    self.state = 26
                    self.value()
                    self.state = 31
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 32
                self.match(JSONParser.T__4)
                pass

            elif la_ == 2:
                localctx = JSONParser.EmptyArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(JSONParser.T__3)
                self.state = 35
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
        self.enterRule(localctx, 4, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(JSONParser.STRING)
            self.state = 39
            self.match(JSONParser.T__5)
            self.state = 40
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



    class SkipContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(JSONParser.ArrayContext,0)

        def obj(self):
            return self.getTypedRuleContext(JSONParser.ObjContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSkip" ):
                listener.enterSkip(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSkip" ):
                listener.exitSkip(self)


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
        self.enterRule(localctx, 6, self.RULE_value)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONParser.STRING]:
                localctx = JSONParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(JSONParser.STRING)
                pass
            elif token in [JSONParser.NUMBER]:
                localctx = JSONParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(JSONParser.NUMBER)
                pass
            elif token in [JSONParser.T__3]:
                localctx = JSONParser.SkipContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.array()
                pass
            elif token in [JSONParser.T__0]:
                localctx = JSONParser.SkipContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.obj()
                pass
            elif token in [JSONParser.BOOLEAN]:
                localctx = JSONParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 46
                self.match(JSONParser.BOOLEAN)
                pass
            elif token in [JSONParser.NULL]:
                localctx = JSONParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 47
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





