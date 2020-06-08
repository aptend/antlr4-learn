import sys
from antlr4 import (BufferedTokenStream, TokenStreamRewriter,
                    CommonTokenStream, ParseTreeWalker, FileStream, InputStream)
from CymbolListener import CymbolListener
from CymbolLexer import CymbolLexer
from Cymbol import Cymbol

class CommentShifter(CymbolListener):
    def __init__(self, tokens: BufferedTokenStream):
        self.tokens = tokens
        self.rewriter = TokenStreamRewriter.TokenStreamRewriter(tokens)
    
    def exitVarDecl(self, ctx: Cymbol.VarDeclContext):
        semi_idx = ctx.stop.tokenIndex  # ctx停止时的Token， ;号，在字符流中的索引
        # 收集出现在;之后，可见channle中下一个token或EOF之前，在指定隐藏channel中的tokens
        if (tokens := self.tokens.getHiddenTokensToRight(semi_idx, CymbolLexer.COMMENTS_CHAN)):
            if (comment := tokens[0]):
                cmt = comment.text[2:].strip()
                self.rewriter.insertBeforeToken(ctx.start, f'/* {cmt} */\n')
                self.rewriter.replaceSingleToken(comment, '\n')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = CymbolLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Cymbol(token_stream)
    tree = parser.src()

    walker = ParseTreeWalker()
    shifter = CommentShifter(token_stream)
    walker.walk(shifter, tree)
    print(shifter.rewriter.getDefaultText())




