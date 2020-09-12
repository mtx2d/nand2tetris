import os
import re
import sys

from lib.instruction import Instruction

class Parser:
    """
    Parse the Xxx.asm into stream of instructions.
    - read source file
    - understand the format of input file
    - break each into different components
        - C: dest, comp, jump
        - A: value
        - Label: label name
    """

    def __init__(self, path: str):
        self._path = path
        self._count = 0

    def _get_clean_line(self, line):
        return self.strip_comments(line.strip())

    def get_instruction(self):
        with open(self._path, "r") as f:
            for line in f:
                line = self._get_clean_line(line)
                if not line:
                    continue
                self._count += 1
                yield self._count, line

    def strip_comments(self, text):
        return re.sub(
            "//.*?$|/\*.*?\*/|'(?:\\.|[^\\'])*'|\"(?:\\.|[^\\\"])*\"",
            "",
            text,
            flags=re.S,
        ).strip()
