import re
import string
import sys
from .jack_token import Token


class Tokenizer:
    @staticmethod
    def strip_comments(line):
        return re.sub(
            r"//.*?$|'(?:\\.|[^\\'])*'",
            "",
            line,
            flags=re.S | re.M,
        ).strip()

    @staticmethod
    def parse(input_file) -> Token:
        # BUG: cannot handle multi-line block comments
        # TODO: update tokenizing to handle multiline case
        with open(input_file, "r") as f:
            for line in f:
                line = line.strip()
                line = Tokenizer.strip_comments(line)
                if not line:
                    continue

                token = ""
                i = 0
                state = 1  # 1 - normal matching; 2 - match string; 4 - match multiline comments
                while i < len(line):
                    if state == 4:
                        if i + 1 >= len(line):
                            continue
                        if line[i] == "*" and line[i + 1] == "/":
                            # end of match
                            state = 1
                    elif state == 1:
                        while i < len(line) and line[i] != '"':
                            token += line[i]
                            i += 1
                        if token:
                            yield Token.create(f'"{token}"')
                            token = ""
                        state = 2
                    elif state == 2:
                        if line[i] == '"':
                            state = 1

                        elif line[i] in string.ascii_letters + string.digits + "_":
                            token += line[i]
                        elif i + 2 < len(line) and line[i : i + 3] == "/**":
                            if token:
                                yield Token.create(token)
                                token = ""
                            state = 4
                        elif line[i] in Token.SYMBOLS:
                            if token:
                                yield Token.create(token)
                                token = ""
                            yield Token.create(line[i])
                        elif line[i] in string.whitespace:
                            if token:
                                yield Token.create(token)
                                token = ""
                    i += 1
