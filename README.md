# Blueprint Jira tooling

Repo-local spec and helpers for the **BLUEPRINT** Jira project (`rippling.atlassian.net`).

## Contents

| Path | Purpose |
|------|---------|
| [docs/blueprint-spec.md](docs/blueprint-spec.md) | Working blueprint spec (Google Doc was not importable). |
| [docs/jira-field-inventory.json](docs/jira-field-inventory.json) | Issue types + field keys and select options for automation. |
| [docs/field-mapping.md](docs/field-mapping.md) | Human-readable semantic → Jira mapping notes. |
| [config/blueprint-field-map.json](config/blueprint-field-map.json) | Stable aliases used by the Python mapper. |
| `src/blueprint_jira/` | `BlueprintMapper` builds `additional_fields` for MCP / REST. |

## Python mapper

From the repository root, with Python 3.10+:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
blueprint-issue-payload < examples/sample-blueprint-input.json
```

Or without install:

```bash
PYTHONPATH=src python -c "import json; from blueprint_jira import BlueprintMapper; print(json.dumps(BlueprintMapper().additional_fields(json.load(open('examples/sample-blueprint-input.json'))), indent=2))"
```

Use the printed JSON as `additional_fields` when calling Atlassian MCP `createJiraIssue` together with `projectKey: "BLUEPRINT"`, `cloudId` from the spec, and the desired `issueTypeName`.

## Creating issues via MCP

1. Resolve `cloudId` with MCP `getAccessibleAtlassianResources`.
2. Choose `issueTypeName` (e.g. `Systems`, `Epic`, `Task`).
3. Run `blueprint-issue-payload` on your JSON to obtain custom field payloads.
4. Call `createJiraIssue` with `summary` (and optional `description`) plus merged `additional_fields`.

## Regenerating field metadata

Jira admin can add fields or options. Refresh [docs/jira-field-inventory.json](docs/jira-field-inventory.json) using MCP `getJiraIssueTypeMetaWithFields` per issue type and merge changes.
