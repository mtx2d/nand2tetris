import argparse
import os
import sys
from typing import List

from lib.parser import Parser
from lib.code_writer import CodeWriter


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", help="input_path file")
    parser.add_argument("output", default="./output.asm", help="output file")
    return parser.parse_args(argv[1:])


def get_files(input_path):
    def is_vm_source_file(file_path):
        return file_path.endswith(".vm") and os.path.isfile(
            os.path.join(input_path, file_path)
        )

    ans = [
        os.path.join(input_path, p)
        for p in os.listdir(input_path)
        if is_vm_source_file(p)
    ]
    return ans


def main(argv: List[str]) -> int:
    args = parse_args(argv)

    for file_path in get_files(args.input_path):
        parser = Parser(file_path)
        code_writer = CodeWriter(file_path)  # need input filename for static variables
        with open(args.output, "a") as of:
            print(code_writer.write_init(), file=of)
            for inst in parser.parse():
                print(code_writer.write(inst), file=of)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))