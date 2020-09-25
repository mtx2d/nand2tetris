import argparse
import sys
from typing import List

from lib.assembler import Assembler


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
    machine_code_generator = Assembler(args.input).assemble()
    with open(args.output, "w") as of:
        for machine_code in machine_code_generator:
            of.write(machine_code + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
