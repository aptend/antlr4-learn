# Generated from CSV.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSVParser import CSVParser
else:
    from CSVParser import CSVParser

# This class defines a complete listener for a parse tree produced by CSVParser.
class CSVListener(ParseTreeListener):

    # Enter a parse tree produced by CSVParser#csvfile.
    def enterCsvfile(self, ctx:CSVParser.CsvfileContext):
        pass

    # Exit a parse tree produced by CSVParser#csvfile.
    def exitCsvfile(self, ctx:CSVParser.CsvfileContext):
        pass


    # Enter a parse tree produced by CSVParser#hdr.
    def enterHdr(self, ctx:CSVParser.HdrContext):
        pass

    # Exit a parse tree produced by CSVParser#hdr.
    def exitHdr(self, ctx:CSVParser.HdrContext):
        pass


    # Enter a parse tree produced by CSVParser#row.
    def enterRow(self, ctx:CSVParser.RowContext):
        pass

    # Exit a parse tree produced by CSVParser#row.
    def exitRow(self, ctx:CSVParser.RowContext):
        pass


    # Enter a parse tree produced by CSVParser#string.
    def enterString(self, ctx:CSVParser.StringContext):
        pass

    # Exit a parse tree produced by CSVParser#string.
    def exitString(self, ctx:CSVParser.StringContext):
        pass


    # Enter a parse tree produced by CSVParser#text.
    def enterText(self, ctx:CSVParser.TextContext):
        pass

    # Exit a parse tree produced by CSVParser#text.
    def exitText(self, ctx:CSVParser.TextContext):
        pass


    # Enter a parse tree produced by CSVParser#none.
    def enterNone(self, ctx:CSVParser.NoneContext):
        pass

    # Exit a parse tree produced by CSVParser#none.
    def exitNone(self, ctx:CSVParser.NoneContext):
        pass



del CSVParser