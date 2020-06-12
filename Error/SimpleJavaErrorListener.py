
from antlr4.error.ErrorListener import ErrorListener


class VerboseListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        stack = recognizer.getRuleInvocationStack()
        stack.reverse()
        print("rule stack: ", str(stack))
        print(f"line {line}:{column} at {offendingSymbol}: {msg}")


class UnderlineDrawer(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"line {line}:{column} {msg}")

        # To be continued
        # _tokens = recognizer.getInputStream()

