# Generated from LExpr.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LExprParser import LExprParser
else:
    from LExprParser import LExprParser

# This class defines a complete generic visitor for a parse tree produced by LExprParser.

class LExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LExprParser#s.
    def visitS(self, ctx:LExprParser.SContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LExprParser#Add.
    def visitAdd(self, ctx:LExprParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LExprParser#Mult.
    def visitMult(self, ctx:LExprParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LExprParser#Int.
    def visitInt(self, ctx:LExprParser.IntContext):
        return self.visitChildren(ctx)



del LExprParser
