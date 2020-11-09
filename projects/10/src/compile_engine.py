import os
import sys
import argparse
from pathlib import Path
from exception import FileExistsException


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source_path",
        required=True,
        help="source file or directory, can be relative or absolute",
    )

    return parser.parse_args(argv[1:])


def get_output_path(source_path):
    path = Path(source_path)
    if not path.exists():
        raise FileNotFoundError(f"{source_path} does not exist.")
    return os.path.join(path.stem, ".jack")


def main(argv):
    args = parse_args(argv)
    output_path = get_output_path(args.source_path)
    if Path(output_path).exists():
        raise FileExistsException(f"{output_path} already exists")

    analyser = Analyser(output_path)
    with open(output_path, "w") as of:
        for out in analyser.process():
            print(out, file=of)

if __name__ == "__main__":
    sys.exit(main(sys.argv))