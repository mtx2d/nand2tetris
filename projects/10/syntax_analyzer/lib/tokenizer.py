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

                    if i + 2 < len(line) and line[i : i + 3] == "/**":
                        if state == 4:
                            token = "" 
                            i += 3
                        elif state == 2:
                            token += line[i : i + 3]
                            i += 3
                        elif state == 1:
                            if token:
                                yield Token.create(token)
                                token = ""
                            i += 3
                            while i < len(line) and (
                                i + 1 >= len(line) or line[i : i + 2] != "*/"
                            ):
                                i += 1
                            state = 4
                    elif i + 1 < len(line) and line[i : i + 2] == "*/":
                        if state == 4:
                            token = ""
                            i += 2
                            state = 1
                        elif state == 2:
                            token += token[i]
                            i += 1
                        elif state == 1:
                            token += token[i]
                            i += 1
                    elif line[i] == '"':
                        if state == 4:
                            token = ""
                            i += 1
                        elif state == 2:
                            token += line[i]  # include the quotation sign
                            i += 1
                            state = 1  # stop matching quoted string
                        elif state == 1:
                            token += line[i]
                            i += 1
                            state = 2  # start matching quoted string
                    elif line[i] in string.ascii_letters + string.digits + "_":
                        if state == 4:
                            i += 1
                        elif state == 2:
                            token += line[i]
                            i += 1
                        elif state == 1:
                            token += line[i]
                            i += 1
                    elif line[i] in Token.SYMBOLS:
                        if state == 4:
                            i += 1
                        elif state == 2:
                            token += line[i]
                            i += 1
                        elif state == 1:
                            if token:
                                yield Token.create(token)
                                token = ""
                            i += 1
                            yield Token.create(line[i])
                    else:
                        if state == 4:
                            i += 1
                        elif state == 2 or state == 1:
                            token += line[i]
                            i += 1

