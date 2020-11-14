import os
import sys
import argparse
from pathlib import Path
from lib.tokenizer import Tokenizer
from lib.compilation_engine import CompilationEngine


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-path",
        required=True,
        help="source file or directory, can be relative or absolute",
    )

    return parser.parse_args(argv[1:])


def get_files(path):
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
        tokens = Tokenizer.parse(file)
        output_xml = file.parent.joinpath(f"{file.stem}.xml")

        if output_xml.exists():
            print(f"{output_xml} already exists, skipping.")
            continue

        with open(output_xml, "w") as of:
            for token in tokens:
                print(token)

            CompilationEngine.parse(tokens, of) 

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
