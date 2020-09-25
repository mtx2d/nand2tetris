from typing import Generator

from .parser import Parser
from .code_writer import CodeWriter


class Translator:
    def __init__(self, input_file: str):
        self.parser = Parser(input_file)
        self.code_writer = CodeWriter()

    def translate(self) -> Generator[str, None, None]:
        for inst in self.parser.parse():
            yield self.code_writer.write(inst)
