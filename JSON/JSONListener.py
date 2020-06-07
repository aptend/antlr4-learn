# Generated from JSON.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JSONParser import JSONParser
else:
    from JSONParser import JSONParser

# This class defines a complete listener for a parse tree produced by JSONParser.
class JSONListener(ParseTreeListener):

    # Enter a parse tree produced by JSONParser#AnObj.
    def enterAnObj(self, ctx:JSONParser.AnObjContext):
        pass

    # Exit a parse tree produced by JSONParser#AnObj.
    def exitAnObj(self, ctx:JSONParser.AnObjContext):
        pass


    # Enter a parse tree produced by JSONParser#EmptyObj.
    def enterEmptyObj(self, ctx:JSONParser.EmptyObjContext):
        pass

    # Exit a parse tree produced by JSONParser#EmptyObj.
    def exitEmptyObj(self, ctx:JSONParser.EmptyObjContext):
        pass


    # Enter a parse tree produced by JSONParser#AnArray.
    def enterAnArray(self, ctx:JSONParser.AnArrayContext):
        pass

    # Exit a parse tree produced by JSONParser#AnArray.
    def exitAnArray(self, ctx:JSONParser.AnArrayContext):
        pass


    # Enter a parse tree produced by JSONParser#EmptyArray.
    def enterEmptyArray(self, ctx:JSONParser.EmptyArrayContext):
        pass

    # Exit a parse tree produced by JSONParser#EmptyArray.
    def exitEmptyArray(self, ctx:JSONParser.EmptyArrayContext):
        pass


    # Enter a parse tree produced by JSONParser#pair.
    def enterPair(self, ctx:JSONParser.PairContext):
        pass

    # Exit a parse tree produced by JSONParser#pair.
    def exitPair(self, ctx:JSONParser.PairContext):
        pass


    # Enter a parse tree produced by JSONParser#String.
    def enterString(self, ctx:JSONParser.StringContext):
        pass

    # Exit a parse tree produced by JSONParser#String.
    def exitString(self, ctx:JSONParser.StringContext):
        pass


    # Enter a parse tree produced by JSONParser#Atom.
    def enterAtom(self, ctx:JSONParser.AtomContext):
        pass

    # Exit a parse tree produced by JSONParser#Atom.
    def exitAtom(self, ctx:JSONParser.AtomContext):
        pass


    # Enter a parse tree produced by JSONParser#Skip.
    def enterSkip(self, ctx:JSONParser.SkipContext):
        pass

    # Exit a parse tree produced by JSONParser#Skip.
    def exitSkip(self, ctx:JSONParser.SkipContext):
        pass



del JSONParser