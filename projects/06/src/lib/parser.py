import os
import re
import sys

from lib.instruction import Instruction, AInstruction, CInstruction, LInstruction
from typing import Generator, Tuple


class Parser:
    """
    Parse the Xxx.asm into stream of instructions.
    - read source file
    - understand the format of input file
    - break each into different components
        - C: dest, comp, jump
        - A: value
    """

    def __init__(self, path: str):
        self._path = path

    def _get_clean_line(self, line):
        return self.strip_comments(line.strip())

    def _parse_c_instruction(self, line):
        if line.count(";") > 1:
            raise ValueError('line format error, should not have more than one ";" ')

        if line.count("=") > 1:
            raise ValueError('line format error, should not have more than one "="')

        if "=" in line and ";" in line:
            # D=M; JMP
            dest, tail = line.split("=")
            comp, jump = tail.split(";")
            return CInstruction(dest=dest.strip(), comp=comp.strip(), jump=jump.strip())
        elif ";" in line:
            # M; JMP
            comp, jump = line.split(";")
            return CInstruction(dest=None, comp=comp.strip(), jump=jump.strip())
        elif "=" in line:
            # M=D
            dest, comp = line.split("=")
            return CInstruction(dest=dest.strip(), comp=comp.strip(), jump=None)
        else:
            # D
            return CInstruction(dest=None, comp=line.strip(), jump=None)

        raise ValueError("line format invalid: ", line)

    def _parse(self, line) -> Instruction:
        if line.startswith("("):
            inst = LInstruction(name=line[1:-1].strip())
        elif line.startswith("@"):
            inst = AInstruction(value=line[1:])
        else:
            inst = self._parse_c_instruction(line)

        return inst

    def get_instruction(self) -> Generator[Tuple[int, Instruction], None, None]:
        with open(self._path, "r") as f:
            for line in f:
                line = self._get_clean_line(line)
                if not line:
                    continue
                instruction = self._parse(line)
                yield instruction

    def strip_comments(self, text):
        return re.sub(
            "//.*?$|/\*.*?\*/|'(?:\\.|[^\\'])*'|\"(?:\\.|[^\\\"])*\"",
            "",
            text,
            flags=re.S,
        ).strip()
