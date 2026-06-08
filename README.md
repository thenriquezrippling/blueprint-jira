# Blueprint Jira tooling

Repo-local spec and helpers for the **BLUEPRINT** Jira project (`rippling.atlassian.net`).

## Contents

| Path | Purpose |
|------|---------|
| [docs/blueprint-spec.md](docs/blueprint-spec.md) | Integration anchor: Jira ids, issue types, links to the v4 spec. |
| [docs/tax-ops-universal-blueprint-v4.txt](docs/tax-ops-universal-blueprint-v4.txt) | **Full** Tax Ops Universal Blueprint v4 text (exported from the `.docx`). |
| [docs/blueprint-v4-jira-alignment.md](docs/blueprint-v4-jira-alignment.md) | v4 field schema vs BLUEPRINT Jira — gaps and partial mappings. |
| [docs/jira-field-inventory.json](docs/jira-field-inventory.json) | Issue types + field keys and select options for automation. |
| [docs/field-mapping.md](docs/field-mapping.md) | Human-readable semantic → Jira mapping notes. |
| [config/blueprint-field-map.json](config/blueprint-field-map.json) | Stable aliases used by the Python mapper. |
| [docs/leadership-touchpoints.md](docs/leadership-touchpoints.md) | Who leadership is for (Robin/Kitty/managers), triggers, cadence, metrics. |
| [docs/jira-api-token.md](docs/jira-api-token.md) | Jira API token + REST; GitHub Actions pattern for automation beyond MCP. |
| [.github/workflows/jira-api-smoke.yml](.github/workflows/jira-api-smoke.yml) | `workflow_dispatch` — verifies `JIRA_*` Actions secrets. |
| `src/blueprint_jira/` | `BlueprintMapper` builds `additional_fields` for MCP / REST. |

## Jira API token (REST / GitHub Actions)

```bash
export JIRA_SITE="https://rippling.atlassian.net"
export JIRA_EMAIL="you@rippling.com"
export JIRA_API_TOKEN="..."   # from id.atlassian.com — do not commit

python scripts/jira_rest_smoke.py
```

See [docs/jira-api-token.md](docs/jira-api-token.md) for curl examples, admin limits, and GitHub Actions wiring. After adding secrets, run **Actions → Jira API smoke** (manual workflow).

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
