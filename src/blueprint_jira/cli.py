from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from blueprint_jira.mapper import BlueprintMapper, MapperError


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Convert JSON blueprint attributes to Jira additional_fields JSON.",
    )
    parser.add_argument(
        "input",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="JSON object (default: stdin)",
    )
    args = parser.parse_args(argv)
    try:
        raw: dict[str, Any] = json.load(args.input)
        payload = BlueprintMapper().additional_fields(raw)
        json.dump(payload, sys.stdout, indent=2)
        sys.stdout.write("\n")
    except (json.JSONDecodeError, MapperError, OSError) as e:
        print(e, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
