import re
from lib.instruction import Instruction


class Parser:
    @staticmethod
    def strip_comments(text: str) -> str:
        return re.sub(
            "//.*?$|/\*.*?\*/|'(?:\\.|[^\\'])*'|\"(?:\\.|[^\\\"])*\"",
            "",
            text,
            flags=re.S,
        ).strip()

    def __init__(self, input_file: str):
        self.input_file = input_file

    def parse(self) -> Instruction:
        with open(self.input_file, "r") as f:
            for line in f:
                line = line.strip()
                line = self.strip_comments(line)
                if not line:
                    continue
                yield line
