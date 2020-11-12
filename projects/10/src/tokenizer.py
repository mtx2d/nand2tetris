import re
import string
import sys
from jack_token import Token


class Tokenizer:
    @staticmethod
    def strip_comments(line):
        return re.sub(
            "//.*?$|/\*.*?\*/|'(?:\\.|[^\\'])*'",
            "",
            line,
            flags=re.S,
        ).strip()

    @staticmethod
    def parse(input_file) -> Token:
        with open(input_file, "r") as f:
            for line in f:
                line = line.strip()
                line = Tokenizer.strip_comments(line)
                if not line:
                    continue
                print(line)

                token = ""
                i = 0
                is_parsing_quoted_string = False
                while i < len(line):
                    if is_parsing_quoted_string:
                        while i < len(line) and line[i] != '"':
                            token += line[i]
                            i += 1
                        yield Token.create(f'"{token}"')
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