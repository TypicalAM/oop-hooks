import argparse
import subprocess
from typing import Sequence, Tuple


def check_file(filename: str) -> Tuple[str, ...]:
    # Run ctags on the file
    ctags_output = subprocess.run(
        ["ctags", "-x", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        encoding="utf-8",
        check=False,
    )

    # Filter out non-classes
    ctags_content = []
    for line in ctags_output.stdout.splitlines():
        split_line = line.split()
        if len(split_line) <= 2 or split_line[1] != "class":
            continue

        ctags_content.append(split_line[0])

    # Filter names that end with "er"
    return tuple(filter(lambda x: x.endswith("er"), ctags_content))


def check_er_suffix(filenames: Sequence[str]) -> int:
    retv = 0

    filenames_filtered = set(filenames)

    for argument in filenames_filtered:
        if (
            argument.endswith(".cpp")
            or argument.endswith(".hpp")
            or argument.endswith(".h")
            or argument.endswith(".java")
        ):
            classes = check_file(argument)
            if classes:
                for class_name in classes:
                    print(f"Found a class that ends with 'er': {class_name}")
                retv = 1

    return retv


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filenames",
        nargs="*",
        help="Filenames pre-commit believes are changed",
    )
    args = parser.parse_args(argv)

    return check_er_suffix(args.filenames)


if __name__ == "__main__":
    main()
