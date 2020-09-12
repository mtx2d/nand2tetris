from os import path

from parser import Parser
from lib.symbol_table import SymbolTable
from lib.encoder import Encoder


def main():
    parser = Parser(file_path="some path here")
    symbol_table = SymbolTable()
    encoder = Encoder()

    with open("/output.hack", "w") as of:
        # First pass, prepares symbol table
        for inst in parser.get_instruction():
            symbol_table
            pass

        # Second pass, generate machine code because address are all ready.
        for inst in parser.get_instruction():
            machine_code = encoder.encode(inst)
            of.write(machine_code)
            pass
