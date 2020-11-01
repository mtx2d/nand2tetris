import argparse
import sys
from typing import List

from lib.parser import Parser
from lib.code_writer import CodeWriter


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", help="input_path file")
    parser.add_argument("output", help="output file")
    return parser.parse_args(argv[1:])


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    parser = Parser(args.input_path)
    code_writer = CodeWriter(
        args.input_path
    )  # need input filename for static variables
    with open(args.output, "w") as of:
        for inst in parser.parse():
            print(code_writer.write(inst), file=of)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
