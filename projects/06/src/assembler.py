from os import path
from sys import argv

from lib.parser import Parser
from lib.symbol_table import SymbolTable
from lib.encoder import Encoder


def main():
    parser = Parser(path=argv[1])
    symbol_table = SymbolTable()
    encoder = Encoder()

    with open("./output.hack", "w") as of:
        # First pass, prepares symbol table
        for inst in parser.get_instruction():
            pass

        # Second pass, generate machine code because address are all ready.
        for inst in parser.get_instruction():
            machine_code = encoder.encode(inst)
            of.write(machine_code)


if __name__ == '__main__':
    main()