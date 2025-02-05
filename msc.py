def tokenize(src: str):
    toks = []

    pos = 0
    while pos < len(src):
        c = src[pos]

        if c in ["\n", " ", "\r", "\t"]:
            pos += 1
        elif c in "+-*%":
            pos += 1
            toks.append((c, "op"))
        elif c == "=":
            pos += 1
            toks.append((c, "eq"))
        elif c.isalpha():
            start = pos
            while pos < len(src) and src[pos].isalpha():
                pos += 1

            toks.append((src[start:pos], "id"))
        elif c.isdigit():
            start = pos
            while pos < len(src) and src[pos].isdigit():
                pos += 1

            toks.append((src[start:pos], "num"))
        else:
            pos += 1

    toks.append(("", "eof"))

    return toks


class Parser:
    def __init__(self, toks):
        self.toks = toks
        self.pos = 0
        self.cur = toks[self.pos]

    def consume(self):
        if self.cur[1] == "eof":
            return None

        prev = self.cur
        self.pos += 1
        self.cur = self.toks[self.pos]
        return prev

    def expect(self, typ, msg=None):
        if self.cur[1] != typ:
            raise SyntaxError(msg if msg else "Syntax Error Unspecified.")

        return self.consume()

    def peek(self):
        if self.toks[self.pos + 1][1] == "eof":
            return None

        return self.toks[self.pos + 1]

    def parse(self):
        program = {"kind": "Program", "body": []}

        while self.cur[1] != "eof":
            program.get("body").append(self.parse_stmt())

        return program

    def parse_stmt(self):
        typ = self.cur[1]

        print(typ)

        if typ == "id":
            # var dec or ref
            if self.peek()[1] == "eq":
                return self.parse_var_dec()

            return {
                "kind": "Identifier",
                "symbol": self.consume()[0]
            }
        elif typ == "num":
            # just make literal
            return {
                "kind": "NumericLiteral",
                "value": int(self.consume()[0])
            }
        else:
            raise SyntaxError(f"Unknown token: {self.cur[1]}")

    def parse_var_dec(self):
        var_name = self.consume()
        # we already checked for an eq
        self.consume()

        # just parse a statement
        init = self.parse_stmt()

        return {
            "kind": "VarDecl",
            "name": var_name,
            "init": init
        }


toks = tokenize("hello = 1")
print(toks)
parser = Parser(toks)
ast = parser.parse()
print(ast)
