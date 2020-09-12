import os
import re
import sys

class Parser:
    """
    Parse the Xxx.asm into stream of instructions.
    """

    def __init__(self, path: str):
        self._path = path
        self._count = 0

    def get_instruction(self, f):
        for line in f:
            line = line.strip()
            # skip empty lines
            if line.isspace() or len(line) == 0:
                continue
            # strip comments
            line = self.strip_comments(line)
            self._count += 1
            yield self._count, line

    def strip_comments(self, text):
        return re.sub(
            "//.*?$|/\*.*?\*/|'(?:\\.|[^\\'])*'|\"(?:\\.|[^\\\"])*\"",
            "",
            text,
            flags=re.S,
        ).strip()
