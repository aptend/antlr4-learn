import sys
from enum import Enum, auto
from collections import namedtuple
from antlr4 import CommonTokenStream, ParseTreeWalker, FileStream, InputStream

if __name__ is not None and "." in __name__:
    from .SPLListener import SPLListener
    from .SPLParser import SPLParser
    from .SPLLexer import SPLLexer
else:
    from SPLParser import SPLParser
    from SPLLexer import SPLLexer
    from SPLListener import SPLListener


class CMD(Enum):
    SEARCH = auto()
    REPLACE = auto()
    STATS = auto()


class SEARCH_KIND(Enum):
    FULLTEXT = auto()
    CMP = auto()
    IN = auto()


class CMP_OP(Enum):
    EQ = auto()
    NEQ = auto()
    LE = auto()
    LT = auto()
    GE = auto()
    GT = auto()


class LOGICAL_OP(Enum):
    AND = auto()
    OR = auto()
    NOT = auto()


FullTextSearch = namedtuple('FullTextSearch', 'is_leaf kind text')
FieldCmpSearch = namedtuple('FiledCmpSearch', 'is_leaf kind field op value')
FieldInSearch = namedtuple('FieldInSearch', 'is_leaf kind field values')

# And Or Not 的连接
# 其中 Not 为一元操作符，约定 left 参与运算，right 为 None
LogicalJointNode = namedtuple('LogicalJointNode', 'is_leaf op left right')


class Search:
    cid = CMD.SEARCH

    def __init__(self):
        self.logical_tree = None

    def _str_walk(self, node, depth):
        if node is None:
            return
        indent = '  ' * depth
        if node.is_leaf:
            return indent + str(node)
        else:
            left = self._str_walk(node.left, depth+1)
            right = self._str_walk(node.right, depth+1)
            ret = f"{indent}({node.op}\n{left}\n"
            # Not 不存在右分支
            if right is not None:
                ret += right + '\n'
            ret += indent + ')'
            return ret

    def __str__(self):
        ret = self._str_walk(self.logical_tree, 2)
        if ret is None:
            ret = ''
        return f"<{self.__class__.__name__}>\n" + ret


class Replace:
    cid = CMD.REPLACE

    def __init__(self):
        self.in_fields = None
        self.with_ops = None

    def __str__(self):
        return (
            f"<{self.__class__.__name__}>\n"
            f"    with_ops: {self.with_ops}\n"
            f"    in_fields: {self.in_fields}"
        )


StatsAggTerm = namedtuple('StatsAggTerm', 'func func_field as_field')

class Stats:
    cid = CMD.STATS

    def __init__(self):
        self.stats_agg_terms = None
        self.by_fields = None

    def __str__(self):
        padding = '\n' + ' '*8
        return (
            f"<{self.__class__.__name__}>\n"
            f"    agg_terms:{padding}"
            f"{padding.join(str(t) for t in self.stats_agg_terms)}\n"
            f"    by_fields: {self.by_fields}"
        )


class Pipeliner(SPLListener):
    def __init__(self):
        self._cmds = []

    @property
    def cmds(self):
        return self._cmds

    def exitCmd(self, ctx: SPLParser.CmdContext):
        ctx.ret = ctx.getChild(0).ret

    def exitPipeline(self, ctx: SPLParser.PipelineContext):
        self._cmds.append(ctx.headSearch().ret)
        self._cmds.extend(c.ret for c in ctx.cmd())



    # -------------------
    #  基础节点
    # -------------------

    def exitCmpOp(self, ctx: SPLParser.CmpOpContext):
        token_type = ctx.getChild(0).symbol.type
        if token_type == SPLLexer.Eq:
            ctx.ret = CMP_OP.EQ
        elif token_type == SPLLexer.Le:
            ctx.ret = CMP_OP.LE
        elif token_type == SPLLexer.Lt:
            ctx.ret = CMP_OP.LT
        elif token_type == SPLLexer.Gt:
            ctx.ret = CMP_OP.GT
        elif token_type == SPLLexer.Ge:
            ctx.ret = CMP_OP.GE
        else:
            ctx.ret = CMP_OP.NEQ

    # 当前规则中没有wc-field，只用filed
    def exitField(self, ctx: SPLParser.FieldContext):
        # 当前field是 UnquotedValue，没有引号，不用处理
        ctx.ret = ctx.getText()

    def exitFieldList(self, ctx: SPLParser.FieldListContext):
        # 只收集FieldContext，不需要COMMA
        ctx.ret = [child.ret for child in ctx.getChildren(
            lambda x: isinstance(x, SPLParser.FieldContext)
        )]

    def exitValue(self, ctx: SPLParser.ValueContext):
        text = ctx.getText()
        # 去除引号
        if ctx.getChild(0).symbol.type == SPLLexer.QuotedString:
            text = text[1:-1]
        ctx.ret = text

    def exitWcValue(self, ctx: SPLParser.WcValueContext):
        if (child := ctx.value()):
            ctx.ret = child.ret
        elif ctx.getChild(0).symbol.type == SPLLexer.WcQuotedString:
            ctx.ret = ctx.getText()[1:-1]
        else:
            ctx.ret = ctx.getText()

    # -------------------
    #  Search
    # -------------------

    def exitFullTextSearch(self, ctx: SPLParser.FullTextSearchContext):
        ctx.ret = FullTextSearch(is_leaf=True,
                                 kind=SEARCH_KIND.FULLTEXT,
                                 text=ctx.wcValue().ret)

    def exitFieldCmpSearch(self, ctx: SPLParser.FieldCmpSearchContext):
        ctx.ret = FieldCmpSearch(is_leaf=True,
                                 kind=SEARCH_KIND.CMP,
                                 field=ctx.field().ret,
                                 op=ctx.cmpOp().ret,
                                 value=ctx.wcValue().ret)

    def exitParenSearch(self, ctx: SPLParser.ParenSearchContext):
        ctx.ret = ctx.searchExpr().ret

    def exitAndSearch(self, ctx: SPLParser.AndSearchContext):
        ctx.ret = LogicalJointNode(is_leaf=False,
                                   op=LOGICAL_OP.AND,
                                   left=ctx.left.ret,
                                   right=ctx.right.ret)

    def exitOrSearch(self, ctx: SPLParser.OrSearchContext):
        ctx.ret = LogicalJointNode(is_leaf=False,
                                   op=LOGICAL_OP.OR,
                                   left=ctx.left.ret,
                                   right=ctx.right.ret)

    def exitNotSearch(self, ctx: SPLParser.NotSearchContext):
        ctx.ret = LogicalJointNode(is_leaf=False,
                                   op=LOGICAL_OP.NOT,
                                   left=ctx.left.ret,
                                   right=None)

    def exitSearch(self, ctx: SPLParser.SearchContext):
        search = Search()
        if (child := ctx.searchExpr()):
            search.logical_tree = child.ret
        ctx.ret = search

    def exitHeadSearch(self, ctx: SPLParser.HeadSearchContext):
        search = Search()
        if (child := ctx.searchExpr()):
            search.logical_tree = child.ret
        ctx.ret = search

    # -------------------
    #  Replace
    # -------------------

    def exitReplaceExpr(self, ctx: SPLParser.ReplaceExprContext):
        ctx.ret = (ctx.old_val.ret, ctx.new_val.ret)

    def exitReplaceExprList(self, ctx: SPLParser.ReplaceExprListContext):
        # 只收集ReplceExprContext，不需要COMMA
        ctx.ret = [child.ret for child in ctx.getChildren(
            lambda x: isinstance(x, SPLParser.ReplaceExprContext)
        )]

    def exitReplace(self, ctx: SPLParser.ReplaceContext):
        replace = Replace()
        replace.with_ops = ctx.replaceExprList().ret
        if (field_list := ctx.fieldList()):
            replace.in_fields = field_list.ret
        ctx.ret = replace

    # -------------------
    #  Stats
    # -------------------
    def exitStatsFunc(self, ctx: SPLParser.StatsFuncContext):
        ctx.ret = ctx.getText()

    def exitStatsAggTerm(self, ctx: SPLParser.StatsAggTermContext):
        func = ctx.statsFunc().ret
        func_field = ctx.func_field.ret
        as_field = ctx.as_field.ret if ctx.as_field else None
        term = StatsAggTerm(func, func_field, as_field)
        ctx.ret = term

    def exitStatsAggTermList(self, ctx: SPLParser.StatsAggTermListContext):
        ctx.ret = [child.ret for child in ctx.getChildren(
            lambda x: isinstance(x, SPLParser.StatsAggTermContext)
        )]

    def exitStats(self, ctx: SPLParser.StatsContext):
        stats = Stats()
        stats.stats_agg_terms = ctx.statsAggTermList().ret
        if (field_list := ctx.fieldList()):
            stats.by_fields = field_list.ret
        ctx.ret = stats


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1], encoding='utf8')
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = SPLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SPLParser(token_stream)
    tree = parser.pipeline()

    walker = ParseTreeWalker()
    pipeliner = Pipeliner()
    walker.walk(pipeliner, tree)
    for c in pipeliner.cmds:
        print(c)
