from HelloListener import HelloListener
if __name__ is not None and "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser


class TestListener(HelloListener):

    # Enter a parse tree produced by HelloParser#r.
    def enterR(self, ctx: HelloParser.RContext):
        print("enter, R")
        print('ID', ctx.ID())
        print('NUN', ctx.NUM())

    # Exit a parse tree produced by HelloParser#r.
    def exitR(self, ctx: HelloParser.RContext):
        print("exit, R")
        print('ID', ctx.ID())
        print('NUN', ctx.NUM())


del HelloParser
