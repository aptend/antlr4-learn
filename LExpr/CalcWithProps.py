from LExprListener import LExprListener

from LExprParser import LExprParser


class CalcWithProps(LExprListener):
    def __init__(self):
        self.props = {}

    def result(self, ctx):
        return self.props[ctx]

    def exitS(self, ctx):
        self.props[ctx] = self.props[ctx.e()]

    def exitAdd(self, ctx: LExprParser.AddContext):
        self.props[ctx] = self.props[ctx.e(0)] + self.props[ctx.e(1)]

    def exitMult(self, ctx: LExprParser.MultContext):
        self.props[ctx] = self.props[ctx.e(0)] + self.props[ctx.e(1)]

    def exitInt(self, ctx: LExprParser.IntContext):
        self.props[ctx] = int(ctx.INT().getText())
