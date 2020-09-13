import argparse
import sys
from typing import List

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


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Assembly file for assembly commands: *.asm")
    parser.add_argument(
        "output",
        help="Binary file for machine code: *.hack",
        default="./output.hack",
    )
    return parser.parse_args(argv[1:])


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    parser = Parser(path=args.input)
    symbol_table = SymbolTable()
    encoder = Encoder()

    with open(args.output, "w") as of:
        # First pass
        add_labels_to_symbol_table(parser, symbol_table)

        # Second pass
        machine_code_gnerator = generate_machine_code(parser, symbol_table, encoder)

        # Write to file
        for machine_code in machine_code_gnerator:
            of.write(machine_code + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
