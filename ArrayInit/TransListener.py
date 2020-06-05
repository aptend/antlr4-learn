from ArrayInitListener import ArrayInitListener
from ArrayInitParser import ArrayInitParser


class TransListener(ArrayInitListener):
    def enterInit(self, ctx: ArrayInitParser.InitContext):
        print('"', end='')

    def exitInit(self, ctx: ArrayInitParser.InitContext):
        print('"', end='')

    def enterValue(self, ctx: ArrayInitParser.ValueContext):
        if ctx.INT():
            print("\\u{:04x}".format(int(ctx.INT().getText())), end='')

    def visitErrorNode(self, err):
        
