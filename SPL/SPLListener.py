# Generated from SPL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SPLParser import SPLParser
else:
    from SPLParser import SPLParser

# This class defines a complete listener for a parse tree produced by SPLParser.
class SPLListener(ParseTreeListener):

    # Enter a parse tree produced by SPLParser#pipeline.
    def enterPipeline(self, ctx:SPLParser.PipelineContext):
        pass

    # Exit a parse tree produced by SPLParser#pipeline.
    def exitPipeline(self, ctx:SPLParser.PipelineContext):
        pass


    # Enter a parse tree produced by SPLParser#cmd.
    def enterCmd(self, ctx:SPLParser.CmdContext):
        pass

    # Exit a parse tree produced by SPLParser#cmd.
    def exitCmd(self, ctx:SPLParser.CmdContext):
        pass


    # Enter a parse tree produced by SPLParser#stats.
    def enterStats(self, ctx:SPLParser.StatsContext):
        pass

    # Exit a parse tree produced by SPLParser#stats.
    def exitStats(self, ctx:SPLParser.StatsContext):
        pass


    # Enter a parse tree produced by SPLParser#statsAggTerm.
    def enterStatsAggTerm(self, ctx:SPLParser.StatsAggTermContext):
        pass

    # Exit a parse tree produced by SPLParser#statsAggTerm.
    def exitStatsAggTerm(self, ctx:SPLParser.StatsAggTermContext):
        pass


    # Enter a parse tree produced by SPLParser#statsAggTermList.
    def enterStatsAggTermList(self, ctx:SPLParser.StatsAggTermListContext):
        pass

    # Exit a parse tree produced by SPLParser#statsAggTermList.
    def exitStatsAggTermList(self, ctx:SPLParser.StatsAggTermListContext):
        pass


    # Enter a parse tree produced by SPLParser#statsFunc.
    def enterStatsFunc(self, ctx:SPLParser.StatsFuncContext):
        pass

    # Exit a parse tree produced by SPLParser#statsFunc.
    def exitStatsFunc(self, ctx:SPLParser.StatsFuncContext):
        pass


    # Enter a parse tree produced by SPLParser#replace.
    def enterReplace(self, ctx:SPLParser.ReplaceContext):
        pass

    # Exit a parse tree produced by SPLParser#replace.
    def exitReplace(self, ctx:SPLParser.ReplaceContext):
        pass


    # Enter a parse tree produced by SPLParser#replaceExpr.
    def enterReplaceExpr(self, ctx:SPLParser.ReplaceExprContext):
        pass

    # Exit a parse tree produced by SPLParser#replaceExpr.
    def exitReplaceExpr(self, ctx:SPLParser.ReplaceExprContext):
        pass


    # Enter a parse tree produced by SPLParser#replaceExprList.
    def enterReplaceExprList(self, ctx:SPLParser.ReplaceExprListContext):
        pass

    # Exit a parse tree produced by SPLParser#replaceExprList.
    def exitReplaceExprList(self, ctx:SPLParser.ReplaceExprListContext):
        pass


    # Enter a parse tree produced by SPLParser#headSearch.
    def enterHeadSearch(self, ctx:SPLParser.HeadSearchContext):
        pass

    # Exit a parse tree produced by SPLParser#headSearch.
    def exitHeadSearch(self, ctx:SPLParser.HeadSearchContext):
        pass


    # Enter a parse tree produced by SPLParser#search.
    def enterSearch(self, ctx:SPLParser.SearchContext):
        pass

    # Exit a parse tree produced by SPLParser#search.
    def exitSearch(self, ctx:SPLParser.SearchContext):
        pass


    # Enter a parse tree produced by SPLParser#AndSearch.
    def enterAndSearch(self, ctx:SPLParser.AndSearchContext):
        pass

    # Exit a parse tree produced by SPLParser#AndSearch.
    def exitAndSearch(self, ctx:SPLParser.AndSearchContext):
        pass


    # Enter a parse tree produced by SPLParser#FieldCmpSearch.
    def enterFieldCmpSearch(self, ctx:SPLParser.FieldCmpSearchContext):
        pass

    # Exit a parse tree produced by SPLParser#FieldCmpSearch.
    def exitFieldCmpSearch(self, ctx:SPLParser.FieldCmpSearchContext):
        pass


    # Enter a parse tree produced by SPLParser#NotSearch.
    def enterNotSearch(self, ctx:SPLParser.NotSearchContext):
        pass

    # Exit a parse tree produced by SPLParser#NotSearch.
    def exitNotSearch(self, ctx:SPLParser.NotSearchContext):
        pass


    # Enter a parse tree produced by SPLParser#FullTextSearch.
    def enterFullTextSearch(self, ctx:SPLParser.FullTextSearchContext):
        pass

    # Exit a parse tree produced by SPLParser#FullTextSearch.
    def exitFullTextSearch(self, ctx:SPLParser.FullTextSearchContext):
        pass


    # Enter a parse tree produced by SPLParser#OrSearch.
    def enterOrSearch(self, ctx:SPLParser.OrSearchContext):
        pass

    # Exit a parse tree produced by SPLParser#OrSearch.
    def exitOrSearch(self, ctx:SPLParser.OrSearchContext):
        pass


    # Enter a parse tree produced by SPLParser#ParenSearch.
    def enterParenSearch(self, ctx:SPLParser.ParenSearchContext):
        pass

    # Exit a parse tree produced by SPLParser#ParenSearch.
    def exitParenSearch(self, ctx:SPLParser.ParenSearchContext):
        pass


    # Enter a parse tree produced by SPLParser#wcValue.
    def enterWcValue(self, ctx:SPLParser.WcValueContext):
        pass

    # Exit a parse tree produced by SPLParser#wcValue.
    def exitWcValue(self, ctx:SPLParser.WcValueContext):
        pass


    # Enter a parse tree produced by SPLParser#wcField.
    def enterWcField(self, ctx:SPLParser.WcFieldContext):
        pass

    # Exit a parse tree produced by SPLParser#wcField.
    def exitWcField(self, ctx:SPLParser.WcFieldContext):
        pass


    # Enter a parse tree produced by SPLParser#value.
    def enterValue(self, ctx:SPLParser.ValueContext):
        pass

    # Exit a parse tree produced by SPLParser#value.
    def exitValue(self, ctx:SPLParser.ValueContext):
        pass


    # Enter a parse tree produced by SPLParser#field.
    def enterField(self, ctx:SPLParser.FieldContext):
        pass

    # Exit a parse tree produced by SPLParser#field.
    def exitField(self, ctx:SPLParser.FieldContext):
        pass


    # Enter a parse tree produced by SPLParser#fieldList.
    def enterFieldList(self, ctx:SPLParser.FieldListContext):
        pass

    # Exit a parse tree produced by SPLParser#fieldList.
    def exitFieldList(self, ctx:SPLParser.FieldListContext):
        pass


    # Enter a parse tree produced by SPLParser#cmpOp.
    def enterCmpOp(self, ctx:SPLParser.CmpOpContext):
        pass

    # Exit a parse tree produced by SPLParser#cmpOp.
    def exitCmpOp(self, ctx:SPLParser.CmpOpContext):
        pass



del SPLParser