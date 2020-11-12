import os
import sys
import argparse
from pathlib import Path
from tokenizer import Tokenizer


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-path",
        required=True,
        help="source file or directory, can be relative or absolute",
    )

    return parser.parse_args(argv[1:])


def get_output_path(source_path):
    path = Path(source_path)
    if not path.exists():
        raise FileNotFoundError(f"{source_path} does not exist.")
    return os.path.join(path.stem, ".xml")


def parse(tokenizer, output_file):
    pass


def main(argv):
    args = parse_args(argv)
    output_path = get_output_path(args.source_path)
    if Path(output_path).exists():
        raise FileExistsError(f"{output_path} already exists")

    tokens = Tokenizer.parse(Path(args.source_path).absolute())
    with open(output_path, "w") as of:
        for token in tokens:
            print(token, file=of)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))