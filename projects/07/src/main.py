import argparse
import sys
from typing import List

from lib import translator


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    parser.add_argument("output", help="output file")
    return parser.parse_args(argv[1:])


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    with open(args.output, "w") as of:
        for line in translator(args.intput).translate():
            print(line, file=of)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
