import os
import re


class Parser:
    """
    Parse the Xxx.asm into stream of instructions.
    """

    def __init__(self, path: str):
        self._path = path
        self._count = 0

    def get_instruction(self):
        with open(self._path, "r") as f:
            count = self._count
            line = f.readline().strip()
            # skip empty lines
            while line.isspace() or not line:
                line = f.readline().strip()
            # strip comments
            line = self.strip_comments(line)
            self._count += 1
            yield count, line

    def strip_comments(self, text):
        return re.sub(
            "//.*?$|/\*.*?\*/|'(?:\\.|[^\\'])*'|\"(?:\\.|[^\\\"])*\"",
            "",
            text,
            flags=re.S,
        ).strip()
