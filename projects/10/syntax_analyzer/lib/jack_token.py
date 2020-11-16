import string
import abc


class Token:
    KEYWORDS = set(
        [
            "class",
            "constructor",
            "function",
            "method",
            "field",
            "static",
            "var",
            "int",
            "char",
            "boolean",
            "void",
            "true",
            "false",
            "null",
            "this",
            "let",
            "do",
            "if",
            "else",
            "while",
            "return",
        ]
    )

    SYMBOLS = set(
        [
            "{",
            "}",
            "(",
            ")",
            "[",
            "]",
            ".",
            ",",
            ";",
            "+",
            "-",
            "*",
            "/",
            "&",
            "|",
            "<",
            ">",
            "=",
            "~",
        ]
    )

    @staticmethod
    def create(token_str):
        if token_str in Token.KEYWORDS:
            return Keyword(token_str)
        elif token_str in Token.SYMBOLS:
            return Symbol(token_str)
        elif all([d in string.digits for d in token_str]):
            return IntegerConstant(token_str)
        elif token_str[0] == '"' and token_str[-1] == '"':
            return StringConstant(token_str[1:-1])
        else:
            return Identifier(token_str)
    
    def __init__(self):
        self.name = "Token"
        self.val = "TokenValue"
        self.tab_size = 4

    @abc.abstractmethod
    def __repr__(self):
        return f"{self.name}({self.val})"


class Keyword(Token):
    def __init__(self, val):
        super(Keyword, self).__init__()
        self.name = "Keyword"
        self.val = val

    def __eq__(self, other) -> bool:
        if isinstance(other, Keyword):
            return self.val == other.val

    def to_xml(self, lvl=0):
        return f"{' ' * self.tab_size * lvl}<keyword> {self.val} </keyword>"


class Symbol(Token):
    def __init__(self, val):
        super(Symbol, self).__init__()
        self.name = "Symbol"
        self.val = val

    def __eq__(self, other) -> bool:
        if isinstance(other, Symbol):
            return self.val == other.val

    def to_xml(self, lvl=0):
        if self.val == "<":
            return f"{' ' * self.tab_size * lvl}<symbol> &lt; </symbol>"
        elif self.val == ">":
            return f"{' ' * self.tab_size * lvl}<symbol> &gt; </symbol>"
        elif self.val == "&":
            return f"{' ' * self.tab_size * lvl}<symbol> &amp; </symbol>"
        else:
            return f"{' ' * self.tab_size * lvl}<symbol> {self.val} </symbol>"


class IntegerConstant(Token):
    def __init__(self, val: str):
        super(IntegerConstant, self).__init__()
        self.name = "IntegerConstant"
        self.val = val

    def __eq__(self, other) -> bool:
        if isinstance(other, IntegerConstant):
            return self.val == other.val

    def to_xml(self, lvl=0):
        return f"{' ' * self.tab_size * lvl}<integerConstant> {self.val} </integerConstant>"


class StringConstant(Token):
    def __init__(self, val):
        super(StringConstant, self).__init__()
        self.name = "StringConstant"
        self.val = val

    def __eq__(self, other) -> bool:
        if isinstance(other, StringConstant):
            return self.val == other.val

    def to_xml(self, lvl=0):
        return f"{' ' * self.tab_size * lvl}<stringConstant> {self.val} </stringConstant>"


class Identifier(Token):
    def __init__(self, val):
        super(Identifier, self).__init__()
        self.name = "Identifier"
        self.val = val

    def __eq__(self, other) -> bool:
        if isinstance(other, Identifier):
            return self.val == other.val

    def to_xml(self, lvl=0):
        return f"{' ' * self.tab_size * lvl}<identifier> {self.val} </identifier>"
