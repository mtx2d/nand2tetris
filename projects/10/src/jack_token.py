import string


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
            return IntegerConstant(int(token_str))
        elif token_str[0] == '"' and token_str[-1] == '"':
            return StringConstant(token_str)
        else:
            return Identifier(token_str)

    def __repr__(self):
        return f"{self.name}({self.val})"


class Keyword(Token):
    def __init__(self, val):
        self.name = "Keyword"
        self.val = val

    def __eq__(self, other) -> bool:
        if isinstance(other, Keyword):
            return self.val == other.val


class Symbol(Token):
    def __init__(self, val):
        self.name = "Symbol"
        self.val = val

    def __eq__(self, other) -> bool:
        if isinstance(other, Symbol):
            return self.val == other.val


class IntegerConstant(Token):
    def __init__(self, val):
        self.name = "IntegerConstant"
        self.val = val

    def __eq__(self, other) -> bool:
        if isinstance(other, IntegerConstant):
            return self.val == other.val


class StringConstant(Token):
    def __init__(self, val):
        self.name = "StringConstant"
        self.val = val

    def __eq__(self, other) -> bool:
        if isinstance(other, StringConstant):
            return self.val == other.val


class Identifier(Token):
    def __init__(self, val):
        self.name = "Identifier"
        self.val = val

    def __eq__(self, other) -> bool:
        if isinstance(other, Identifier):
            return self.val == other.val