import argparse
import subprocess
from typing import Optional, Sequence


def check_file(filename: str) -> Optional[tuple[str]]:
    # Run ctags on the file
    ctags_output = subprocess.run(
        ["ctags", "-x", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        encoding="utf-8",
        check=False,
    )

    # Filter out non-function lines
    ctags_content = []
    for line in ctags_output.stdout.splitlines():
        split_line = line.split()
        if len(split_line) <= 2 or split_line[1] != "function":
            continue

        ctags_content.append(split_line[0])

    # Filter names that start with "get" or "set"
    return tuple(name for name in ctags_content if name.startswith("get") or name.startswith("set"))


def check_getters_setters(filenames: Sequence[str]) -> int:
    retv = 0

    filenames_filtered = set(filenames)

    for argument in filenames_filtered:
        if (
            argument.endswith(".cpp")
            or argument.endswith(".hpp")
            or argument.endswith(".h")
            or argument.endswith(".java")
        ):
            methods = check_file(argument)
            if methods:
                for method_name in methods:
                    print(f"Found a method which looks like a getter or setter: {method_name}")
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

    return check_getters_setters(args.filenames)


if __name__ == "__main__":
    main()
