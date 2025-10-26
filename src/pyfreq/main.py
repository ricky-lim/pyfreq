import argparse
import sys

from importlib.metadata import version
from dataclasses import dataclass
from pathlib import Path

from pyfreq.lib import count


def main() -> None:
    args = collect_args()
    config = Config.build(args)
    run(config)


def collect_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version", "-v", action="version", version=f"{version('pyfreq')}"
    )
    parser.add_argument("word", type=str, help="Word to count")
    parser.add_argument("file_path", type=Path, help="Text file to search")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    return parser.parse_args()


@dataclass
class Config:
    word: str
    file_path: Path

    @classmethod
    def build(cls, args: argparse.Namespace) -> "Config":
        if args.word is None:
            raise ValueError("Word is not provided")
        if args.file_path is None:
            raise ValueError("A file path is not provided")

        return cls(word=args.word, file_path=args.file_path)


def run(config: Config):
    with open(config.file_path, "r") as f:
        content = f.read()

    result = count(config.word, content)
    print(result)
