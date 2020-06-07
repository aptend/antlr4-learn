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
    PAIR = 3

    def __init__(self):
        self.indent_lv = 0
        self.modes = [0]
        self.buf = []
        self.inline_close = False

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

    def append_inline(self, content):
        self.buf.append(content)

    def appendln(self, content):
        self.buf.append(self.indent+content)
        self.buf.append('\n')

    def remove_trailing_newline(self):
        if self.buf[-1] == '\n':
            self.buf.pop()

    def result(self):
        return ''.join(self.buf)

    def enterAnObj(self, ctx: JSONParser.AnObjContext):
        if self.mode == self.ARRAY:
            self.appendln('<element>')
            self.indent_lv += 1
        self.mode_push(self.OBJ)

    def exitAnObj(self, ctx: JSONParser.AnObjContext):
        self.mode_pop()
        if self.mode == self.ARRAY:
            self.indent_lv -= 1
            self.appendln('</element>')

    def enterAnArray(self, ctx: JSONParser.AnArrayContext):
        if self.mode == self.ARRAY:
            self.appendln('<element>')
            self.indent_lv += 1
        self.mode_push(self.ARRAY)

    def exitAnArray(self, ctx: JSONParser.AnArrayContext):
        self.mode_pop()
        if self.mode == self.ARRAY:
            self.indent_lv -= 1
            self.appendln('</element>')

    def enterEmptyArray(self, ctx: JSONParser.EmptyArrayContext):
        if self.mode == self.ARRAY:
            self.appendln('<element></element>')
        else:
            self.remove_trailing_newline()
            self.inline_close = True

    def enterPair(self, ctx: JSONParser.PairContext):
        self.appendln("<{}>".format(ctx.STRING().getText()[1:-1]))
        self.indent_lv += 1
        self.mode_push(self.PAIR)

    def exitPair(self, ctx: JSONParser.PairContext):
        close_txt = "</{}>".format(ctx.STRING().getText()[1:-1])
        self.indent_lv -= 1
        if self.inline_close:
            self.append_inline(close_txt+'\n')
            self.inline_close = False
        else:
            self.appendln(close_txt)
        self.mode_pop()

    def exit_with_atom_text(self, text):
        if self.mode == self.ARRAY:
            self.appendln("<element>{}</element>".format(text))
        else:
            self.remove_trailing_newline()
            self.inline_close = True
            self.append_inline(text)

    def exitString(self, ctx: JSONParser.StringContext):
        self.exit_with_atom_text(ctx.getText()[1:-1])

    def exitAtom(self, ctx: JSONParser.AtomContext):
        self.exit_with_atom_text(ctx.getText())
