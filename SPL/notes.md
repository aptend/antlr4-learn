- Generally, you need quotes around phrases and field values that include white spaces, commas, pipes, quotes, brackets or keywords.
    - `... | search "error | stats count"`
    - `error "AND" | dedup`
    - `error "startswith=foo" | dedup`

- The backslash character (\) is used to escape quotes, pipes, and itself.
    - `... | eval myfield="6"`  ->  6
    - `... | eval myfield="\""` ->  "
    - `... | eval myfield="\\"` ->  \
    - `... | eval myfield="\"`  ->  error


- field
    - null field
    - empty field
    - empty value
    - multivalue field


```Python
# ttype是节点类型，叶子节点 TerminalNode 还是非叶子节点 RuleNode，None不做筛选
# i 索引位置，第几个 0-based
def getChild(self, i:int, ttype:type = None):
    if ttype is None:
        return self.children[i] if len(self.children)>i else None
    else:
        for child in self.getChildren():
            if not isinstance(child, ttype):
                continue
            if i==0:
                return child
            i -= 1
        return None

def getChildren(self, predicate = None):
    if self.children is not None:
        for child in self.children:
            if predicate is not None and not predicate(child):
                continue
            yield child

# Token只有叶子节点才有，所以isinstance先筛选
# ttype是Token的类型，是Lexer中的整型
def getToken(self, ttype:int, i:int):
    for child in self.getChildren():
        if not isinstance(child, TerminalNode):
            continue
        if child.symbol.type != ttype:
            continue
        if i==0:
            return child
        i -= 1
    return None
```
