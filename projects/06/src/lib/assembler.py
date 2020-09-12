from os import path

from parser import Parser
from symbol_table import SymbolTable
from encoder import Encoder


def main():
    parser = Parser(file_path="some path here")
    symbol_table = SymbolTable()
    encoder = Encoder()

    while parser.has_next_instruction():
        inst = parser.get_instruction()
        encoder
