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

    with open(argv[2] if len(argv) > 2 else "./output.hack", "w") as of:
        # First pass, prepares symbol table with label address
        for (num, inst) in parser.get_instruction():
            if isinstance(inst, LInstruction):
                if not symbol_table.has_symbol(inst.name):
                    symbol_table.add_label(inst.name, num + 1)

        # Second pass, generate machine code because address are all ready.
        for (_, inst) in parser.get_instruction():
            if isinstance(inst, LInstruction):
                continue
            machine_code = encoder.encode(inst, symbol_table.get_or_add)
            of.write(machine_code + "\n")

        if len(argv) > 3:
            with open(argv[3], "w") as debug_f:
                sorted_st = {
                    k: v
                    for k, v in sorted(
                        symbol_table.table.items(), key=lambda item: item[1]
                    )
                }
                debug_f.write("x = " + str(sorted_st))


if __name__ == "__main__":
    main()
