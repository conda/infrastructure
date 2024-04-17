#!/usr/bin/env python3
"""Sort specified keys in JSON files."""

from __future__ import annotations

import json
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    """Sort specified keys in JSON files."""
    parser = ArgumentParser()
    parser.add_argument(
        "--sort-keys",
        type=lambda keys: keys.split(","),
        default=[],
        help="Keys to sort",
    )
    parser.add_argument("filenames", nargs="*", type=Path, help="Filenames to fix")
    args = parser.parse_args(argv)

    def object_pairs_hook(pairs):
        return {
            name: sorted(set(value), key=str.lower) if name in args.sort_keys else value
            for name, value in pairs
        }

    status = 0
    for path in args.filenames:
        original = path.read_text()
        try:
            content = json.loads(original, object_pairs_hook=object_pairs_hook)
        except ValueError:
            status = 2  # invalid json format
        else:
            pretty = f"{json.dumps(content, indent=2)}\n"  # include trailing newline
            path.write_text(pretty)
            status = status or original != pretty  # record whether modified
    return status


if __name__ == "__main__":
    sys.exit(main())
