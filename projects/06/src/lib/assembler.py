from os import path

from parser import Parser
from symbol_table import SymbolTable
from encoder import Encoder


def main():
    parser = Parser(file_path="some path here")
    symbol_table = SymbolTable()
    encoder = Encoder()

    # First pass, prepares symbol table
    for inst in parser.get_instruction():
        symbol_table
        pass

    # Second pass, generate machine code because address are all ready.
    for inst in parser.get_instruction():
        machine_code = encoder.encode(inst)
        pass
