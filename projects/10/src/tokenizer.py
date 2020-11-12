import re
import string


class Tokenizer:
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

    @staticmethod
    def strip_comments(line):
        return re.sub(
            "//.*?$|/\*.*?\*/|'(?:\\.|[^\\'])*'|\"(?:\\.|[^\\\"])*\"",
            "",
            line,
            flags=re.S,
        ).strip()

    @staticmethod
    def parse(input_file):
        with open(input_file, "r") as f:
            for line in f:
                line = line.strip()
                line = Tokenizer.strip_comments(line)
                line = " ".join(
                    line.split()
                )  # make sure only one space between each word
                if not line:
                    continue

                token = ""
                i = 0
                while i < len(line):
                    if line[i] in string.ascii_letters + string.digits + "_":
                        token += line[i]
                    elif line[i] in Tokenizer.SYMBOLS:
                        if token:
                            yield token
                            token=""
                        yield line[i]
                    elif line[i] in string.whitespace:
                        if token:
                            yield token
                            token = ""
                    i += 1