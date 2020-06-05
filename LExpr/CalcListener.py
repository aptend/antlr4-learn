from LExprListener import LExprListener

from LExprParser import LExprParser


class CalcListener(LExprListener):
    def __init__(self):
        self.stack = []

    def result(self):
        assert len(self.stack) == 1
        return self.stack[0]

    def exitAdd(self, ctx: LExprParser.AddContext):
        self.stack.append(self.stack.pop() + self.stack.pop())

    def exitMult(self, ctx: LExprParser.MultContext):
        self.stack.append(self.stack.pop() * self.stack.pop())

    def exitInt(self, ctx: LExprParser.IntContext):
        self.stack.append(int(ctx.INT().getText()))
