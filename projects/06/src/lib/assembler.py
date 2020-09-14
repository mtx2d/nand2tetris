from .encoder import Encoder
from .instruction import Instruction, AInstruction, CInstruction, LInstruction
from .parser import Parser
from .symbol_table import SymbolTable

from typing import Generator


class Assembler:
    def __init__(self, path):
        self.parser = Parser(path)
        self.symbol_table = SymbolTable()
        self.encoder = Encoder()

    def assemble(self) -> Generator[str, None, None]:

        # First pass, add labels to symbol_table.
        line_count = 0
        for inst in self.parser.get_instruction():
            if isinstance(inst, LInstruction):
                if inst.name == "INFINITE_LOOP":
                    print(
                        "DEBUG, line_count", line_count, "self path", self.parser._path
                    )
                self.symbol_table.add_entry(inst.name, line_count)  # ROM addr
                continue
            line_count += 1

        print("DEBUG: ", self.symbol_table.table)

        # Second pass, look up symbols in the symbol_table.
        for inst in self.parser.get_instruction():
            if isinstance(inst, LInstruction):
                continue
            if isinstance(inst, AInstruction):
                if not all([v.isdigit() for v in inst.value]):
                    self.symbol_table.get_address(inst.value)  # RAM addr
            machine_code = self.encoder.encode(inst, self.symbol_table)
            yield machine_code
