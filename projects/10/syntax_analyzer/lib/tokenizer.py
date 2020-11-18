import re
import string
import sys
from .jack_token import Token


class Tokenizer:
    @staticmethod
    def strip_comments(line):
        return re.sub(
            r"//.*?$|/\*\*.*?\*/|'(?:\\.|[^\\'])*'",
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
                is_parsing_quoted_string = False
                while i < len(line):
                    if is_parsing_quoted_string:
                        while i < len(line) and line[i] != '"':
                            token += line[i]
                            i += 1
                        if token:
                            yield Token.create(f'"{token}"')
                            token = ""
                        is_parsing_quoted_string = not is_parsing_quoted_string
                    else:
                        if line[i] == '"':
                            is_parsing_quoted_string = not is_parsing_quoted_string
                        elif line[i] in string.ascii_letters + string.digits + "_":
                            token += line[i]
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
