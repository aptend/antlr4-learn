from LExprVisitor import LExprVisitor

from LExprParser import LExprParser


class CalcVisitor(LExprVisitor):
    def visitAdd(self, ctx: LExprParser.AddContext):
        return self.visit(ctx.e(0)) + self.visit(ctx.e(1))

    def visitMult(self, ctx: LExprParser.MultContext):
        return self.visit(ctx.e(0)) * self.visit(ctx.e(1))

    def visitInt(seladdf, ctx: LExprParser.IntContext):
        return int(ctx.INT().getText())
