"""
Convert JSON to XML

from
{
    "description" : "An imaginary server config file",
    "logs" : {"level":"verbose", "dir":"/var/log"},
    "host" : "antlr.org",
    "admin": ["parrt", "tombu"],
    "aliases": []
}

to

<description>An imaginary server config file</description>
<logs>
    <level>verbose</level>
    <dir>/var/log</dir>
</logs>
<host>antlr.org</host>
<admin>
    <element>parrt</element>
    <element>tombu</element>
</admin>
<aliases></aliases>
"""


from JSONParser import JSONParser
from JSONListener import JSONListener


class MyXmlEmitter(JSONListener):
    NONE = 0
    ARRAY = 1
    OBJ = 2

    def __init__(self):
        self.indent_lv = 0
        self.modes = [0]
        self.buf = []

    @property
    def indent(self):
        return '  ' * self.indent_lv

    @property
    def mode(self):
        return self.modes[-1]

    def mode_push(self, m):
        self.modes.append(m)

    def mode_pop(self):
        if len(self.modes) > 1:
            self.modes.pop()

    def append(self, content):
        self.buf.append(self.indent+content)

    def appendln(self, content):
        self.buf.append(self.indent+content+'\n')

    def result(self):
        return ''.join(self.buf)

    # Enter a parse tree produced by JSONParser#AnObj.
    def enterAnObj(self, ctx: JSONParser.AnObjContext):
        self.mode_push(self.OBJ)

    # Exit a parse tree produced by JSONParser#AnObj.
    def exitAnObj(self, ctx: JSONParser.AnObjContext):
        self.mode_pop()

    # Enter a parse tree produced by JSONParser#AnArray.
    def enterAnArray(self, ctx: JSONParser.AnArrayContext):
        if self.mode == self.ARRAY:
            self.appendln('<element>')
        self.modes.append(self.ARRAY)
        self.indent_lv += 1

    # Exit a parse tree produced by JSONParser#AnArray.
    def exitAnArray(self, ctx: JSONParser.AnArrayContext):
        self.indent_lv -= 1
        if self.mode == self.ARRAY:
            self.appendln('</element>')
        self.mode_pop()

    def enterEmptyArray(self, ctx: JSONParser.EmptyArrayContext):
        if self.mode == self.ARRAY:
            self.appendln('<element></element>')

    # Enter a parse tree produced by JSONParser#pair.
    def enterPair(self, ctx: JSONParser.PairContext):
        self.appendln("<{}>".format(ctx.STRING().getText()[1:-1]))
        self.indent_lv += 1

    # Exit a parse tree produced by JSONParser#pair.
    def exitPair(self, ctx: JSONParser.PairContext):
        self.indent_lv -= 1
        self.appendln("<{}/>".format(ctx.STRING().getText()[1:-1]))

    # Exit a parse tree produced by JSONParser#String.
    def exitString(self, ctx: JSONParser.StringContext):
        text = ctx.getText()[1:-1]
        if self.mode == self.ARRAY:
            self.appendln("<element>{}</element>".format(text))
        else:
            self.appendln(text)

    # Exit a parse tree produced by JSONParser#Atom.
    def exitAtom(self, ctx: JSONParser.AtomContext):
        text = ctx.getText()
        if self.mode == self.ARRAY:
            self.appendln("<element>{}</element>".format(text))
        else:
            self.appendln(text)
