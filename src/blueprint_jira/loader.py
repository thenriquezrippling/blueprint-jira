from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_json(relative: str) -> Any:
    path = _repo_root() / relative
    with path.open(encoding="utf-8") as f:
        return json.load(f)
