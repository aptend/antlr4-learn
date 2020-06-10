"use strict"

// 只能模拟predicates，形如{predicate}?，没办法执行action
// 所以只有手动设置1、0
// 1 嵌套，全部换行符会忽略
// 0 无嵌套，除了\转义，全部换行符都保留
var self = { nesting : 0 };

module.exports.evaluateLexerPredicate = function (lexer, ruleIndex, actionIndex, predicate) {
    return eval(predicate);
}

module.exports.evaluateParserPredicate = function (parser, ruleIndex, actionIndex, predicate) {
    return eval(predicate);
}
