import re


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
                    if i + 1 == len(line) or line[i + 1] in " \n\t":
                        token += line[i]
                        i += 2
                        yield token
                        token = ""
                    else:
                        token += line[i]
                        i += 1