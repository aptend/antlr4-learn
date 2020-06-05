# Generated from Hello.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete generic visitor for a parse tree produced by HelloParser.

class HelloVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HelloParser#r.
    def visitR(self, ctx:HelloParser.RContext):
        return self.visitChildren(ctx)



del HelloParser