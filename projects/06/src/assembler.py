from os import path
from sys import argv

from lib.encoder import Encoder
from lib.instruction import Instruction, AInstruction, CInstruction, LInstruction
from lib.parser import Parser
from lib.symbol_table import SymbolTable


def add_labels_to_symbol_table(parser: Parser, symbol_table: SymbolTable):
    line_count = 0
    for inst in parser.get_instruction():
        if isinstance(inst, LInstruction):
            symbol_table.add_label(inst.name, line_count)
            continue
        line_count += 1


def generate_machine_code(parser: Parser, symbol_table: SymbolTable, encoder: Encoder):
    for inst in parser.get_instruction():
        if isinstance(inst, LInstruction):
            continue
        machine_code = encoder.encode(inst, symbol_table.get_or_add)
        yield machine_code


def main():
    parser = Parser(path=argv[1])
    symbol_table = SymbolTable()
    encoder = Encoder()

    with open(argv[2] if len(argv) > 2 else "./output.hack", "w") as of:
        # First pass
        add_labels_to_symbol_table(parser, symbol_table)

        # Second pass
        machine_code_gnerator = generate_machine_code(parser, symbol_table, encoder)

        # Write to file
        for machine_code in machine_code_gnerator:
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
