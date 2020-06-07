"""
Visit a CSV parsed tree, and output a list of maps:

[
    {Details=Mid Bonus, Month=June, Amount="$2,000"},
    {Details=, Month=January, Amount=\"""zippo""\"},
    {Details=Total Bonuses, Month="", Amount="$5,000"}
]
"""


from CSVListener import CSVListener
from CSVParser import CSVParser


class TableListener(CSVListener):
    def __init__(self):
        self.hdrs = []
        self.curr_row_fields = []
        self.table = []

    def result(self):
        return self.table

    def exitText(self, ctx: CSVParser.TextContext):
        self.curr_row_fields.append(ctx.TEXT().getText())

    def exitString(self, ctx: CSVParser.StringContext):
        self.curr_row_fields.append(ctx.STRING().getText())

    def exitNone(self, ctx: CSVParser.NoneContext):
        self.curr_row_fields.append(None)

    def exitHdr(self, ctx: CSVParser.HdrContext):
        self.hdrs = self.curr_row_fields[:]

    def enterRow(self, ctx: CSVParser.RowContext):
        self.curr_row_fields = []

    def exitRow(self, ctx: CSVParser.RowContext):
        if ctx.parentCtx.getRuleIndex() == CSVParser.RULE_hdr:
            return
        self.table.append(dict(zip(self.hdrs, self.curr_row_fields)))
