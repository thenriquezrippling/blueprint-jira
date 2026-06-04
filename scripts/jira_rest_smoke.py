#!/usr/bin/env python3
"""
Verify Jira Cloud API token (Basic auth: email + API token).

Environment:
  JIRA_SITE         e.g. https://rippling.atlassian.net
  JIRA_EMAIL        Atlassian account email
  JIRA_API_TOKEN    API token from id.atlassian.com

Usage:
  python scripts/jira_rest_smoke.py
  python scripts/jira_rest_smoke.py --path /rest/api/3/field/search?startAt=0&maxResults=1

Do not commit tokens. Do not paste tokens into chat.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from typing import Any


def basic_auth_header(email: str, token: str) -> str:
    raw = f"{email}:{token}".encode("utf-8")
    return "Basic " + base64.b64encode(raw).decode("ascii")


def request_json(site: str, path: str, email: str, token: str) -> tuple[int, Any]:
    site = site.rstrip("/")
    if not path.startswith("/"):
        path = "/" + path
    url = site + path
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": basic_auth_header(email, token),
            "Accept": "application/json",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8")
            code = resp.getcode() or 200
            if not body:
                return code, None
            return code, json.loads(body)
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(err_body)
        except json.JSONDecodeError:
            parsed = err_body
        return e.code, {"_http_error": True, "body": parsed}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--path",
        default="/rest/api/3/myself",
        help="API path under JIRA_SITE (default: /rest/api/3/myself)",
    )
    args = parser.parse_args()

    site = os.environ.get("JIRA_SITE", "").strip()
    email = os.environ.get("JIRA_EMAIL", "").strip()
    token = os.environ.get("JIRA_API_TOKEN", "").strip()

    missing = [k for k, v in [("JIRA_SITE", site), ("JIRA_EMAIL", email), ("JIRA_API_TOKEN", token)] if not v]
    if missing:
        print("Missing environment variables:", ", ".join(missing), file=sys.stderr)
        print("See docs/jira-api-token.md", file=sys.stderr)
        return 1

    code, data = request_json(site, args.path, email, token)
    print(json.dumps({"status": code, "data": data}, indent=2))

    if isinstance(data, dict) and data.get("_http_error"):
        return 1
    if code >= 400:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
