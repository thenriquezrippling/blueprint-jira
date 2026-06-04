from __future__ import annotations

from typing import Any

from blueprint_jira.loader import load_json


class MapperError(ValueError):
    pass


def _option_id_for(field_key: str, label: str, inventory: dict[str, Any]) -> str:
    label_norm = label.strip().casefold()
    for field in inventory.get("fields", []):
        if field.get("key") != field_key:
            continue
        for opt in field.get("allowedValues") or []:
            if str(opt.get("value", "")).strip().casefold() == label_norm:
                return str(opt["id"])
    raise MapperError(f"No option id for {field_key}={label!r}")


class BlueprintMapper:
    """Turn human-readable blueprint attributes into Jira create/edit field payloads."""

    def __init__(self) -> None:
        self._inventory = load_json("docs/jira-field-inventory.json")
        self._map = load_json("config/blueprint-field-map.json")
        self._jira_keys: dict[str, str] = dict(self._map["jiraKeys"])

    def additional_fields(self, data: dict[str, Any]) -> dict[str, Any]:
        """Build a dict suitable for Atlassian MCP createJiraIssue `additional_fields`.

        Supported keys in ``data`` (all optional except where Jira requires them):
        - title -> summary (if you pass title, it maps to summary; prefer summary)
        - summary, description, labels, duedate, priority (name string), assignee (account id)
        - startDate -> customfield_10015 (YYYY-MM-DD)
        - storyPoints -> customfield_10016
        - cadence, sla, manager, specialization (option labels, case-insensitive)
        - parent (issue key string or dict with key)
        """
        out: dict[str, Any] = {}

        if "title" in data and "summary" not in data:
            out["summary"] = data["title"]
        if "summary" in data:
            out["summary"] = data["summary"]
        if "description" in data:
            out["description"] = data["description"]
        if "labels" in data:
            out["labels"] = data["labels"]
        if "duedate" in data:
            out["duedate"] = data["duedate"]
        if "priority" in data:
            out["priority"] = {"name": data["priority"]}
        if "assignee" in data:
            out["assignee"] = {"id": data["assignee"]}

        if "startDate" in data:
            out[self._jira_keys["startDate"]] = data["startDate"]
        if "storyPoints" in data:
            out[self._jira_keys["storyPoints"]] = data["storyPoints"]

        select_aliases = {
            "cadence": self._jira_keys["cadence"],
            "sla": self._jira_keys["sla"],
            "manager": self._jira_keys["manager"],
            "specialization": self._jira_keys["specialization"],
        }
        for friendly, jira_key in select_aliases.items():
            if friendly not in data:
                continue
            oid = _option_id_for(jira_key, str(data[friendly]), self._inventory)
            out[jira_key] = {"id": oid}

        if "parent" in data:
            p = data["parent"]
            out["parent"] = p if isinstance(p, dict) else {"key": p}

        return out
