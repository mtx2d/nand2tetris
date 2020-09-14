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
        for inst in parser.get_instruction():
            if isinstance(inst, LInstruction):
                symbol_table.add_entry(inst.name, line_count)  # ROM addr
                continue
            line_count += 1

            if isinstance(inst, AInstruction):
                if all([v.isdigit() for v in inst.value]):
                    continue
                addr = symbol_table.get_address(inst.value)
                symbol_table.add_entry(inst.value, addr)  # RAM addr

        # Second pass, look up symbols in the symbol_table.
        for inst in parser.get_instruction():
            if isinstance(inst, LInstruction):
                continue
            machine_code = encoder.encode(inst, symbol_table)
            yield machine_code
