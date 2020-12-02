import os
import sys
import argparse
from pathlib import Path
from more_itertools import peekable
from lib.compilation_engine import CompilationEngine
from lib.symbol_table import SymbolTable
from lib.tokenizer import Tokenizer


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-path",
        required=True,
        help="source file or directory, can be relative or absolute",
    )

    return parser.parse_args(argv[1:])


def get_files(path):
    # return a list of .jack files
    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist.")
    if path.is_file():
        if not path.suffix == ".jack":
            raise Exception(f"{path} is not a jack file.")
        return [path.absolute()]
    elif path.is_dir():
        return [p for p in path.iterdir() if p.suffix == ".jack"]
    else:
        raise Exception(f"{path} is neither a dir or a file.")


def main(argv):
    args = parse_args(argv)

    source_path = Path(args.source_path).absolute()
    for file in get_files(source_path):
        tokens = peekable(Tokenizer.parse(file))
        symbol_table = SymbolTable(file)
        vm_instructions = CompilationEngine(file).parse(tokens, symbol_table)

        output_vm = file.parent.joinpath(f"{file.stem}.vm")
        if output_vm.exists():
            print(f"{output_vm} already exists, skipping.")
            continue

        with open(output_vm, "w") as of:
            for instruction in vm_instructions:
                print(instruction, file=of)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
