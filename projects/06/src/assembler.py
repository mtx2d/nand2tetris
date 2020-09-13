from os import path
from sys import argv

from lib.encoder import Encoder
from lib.instruction import Instruction, AInstruction, CInstruction, LInstruction
from lib.parser import Parser
from lib.symbol_table import SymbolTable


def main():
    parser = Parser(path=argv[1])
    symbol_table = SymbolTable()
    encoder = Encoder()

    with open(argv[2] or "./output.hack", "w") as of:
        # First pass, prepares symbol table
        for (num, inst) in parser.get_instruction():
            if isinstance(inst, LInstruction):
                if not symbol_table.has_symbol(inst.name):
                    symbol_table.add(inst.name, num + 1)

        # Second pass, generate machine code because address are all ready.
        for (num, inst) in parser.get_instruction():
            machine_code = encoder.encode(inst)
            of.write(machine_code + "\n")


if __name__ == "__main__":
    main()
