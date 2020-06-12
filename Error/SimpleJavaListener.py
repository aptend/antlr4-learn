# Generated from SimpleJava.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleJavaParser import SimpleJavaParser
else:
    from SimpleJavaParser import SimpleJavaParser

# This class defines a complete listener for a parse tree produced by SimpleJavaParser.
class SimpleJavaListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleJavaParser#prog.
    def enterProg(self, ctx:SimpleJavaParser.ProgContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#prog.
    def exitProg(self, ctx:SimpleJavaParser.ProgContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#classDef.
    def enterClassDef(self, ctx:SimpleJavaParser.ClassDefContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#classDef.
    def exitClassDef(self, ctx:SimpleJavaParser.ClassDefContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#member.
    def enterMember(self, ctx:SimpleJavaParser.MemberContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#member.
    def exitMember(self, ctx:SimpleJavaParser.MemberContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#stat.
    def enterStat(self, ctx:SimpleJavaParser.StatContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#stat.
    def exitStat(self, ctx:SimpleJavaParser.StatContext):
        pass


    # Enter a parse tree produced by SimpleJavaParser#expr.
    def enterExpr(self, ctx:SimpleJavaParser.ExprContext):
        pass

    # Exit a parse tree produced by SimpleJavaParser#expr.
    def exitExpr(self, ctx:SimpleJavaParser.ExprContext):
        pass



del SimpleJavaParser