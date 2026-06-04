# Blueprint field mapping (BLUEPRINT)

For the **Tax Ops Universal Blueprint v4** universal schema vs current Jira fields, see [`blueprint-v4-jira-alignment.md`](./blueprint-v4-jira-alignment.md).

All pillar custom fields already exist in Jira. No new custom field definitions were created in this implementation (MCP cannot create fields; your site already had them).

## Semantic to Jira

| Blueprint concept | Jira field key | Notes |
|-------------------|----------------|--------|
| Title | `summary` | Required on create |
| Body | `description` | Markdown or ADF per API client |
| Assignee | `assignee` | Account id |
| Priority | `priority` | Use `name` e.g. `Medium` |
| Labels | `labels` | string[] |
| Due date | `duedate` | `YYYY-MM-DD` |
| Start date | `customfield_10015` | date |
| Story points | `customfield_10016` | number |
| Team | `customfield_10001` | team payload per Jira |
| Cadence | `customfield_26129` | option: use `{"id": "<optionId>"}` |
| SLA | `customfield_26130` | option id |
| MMDD | `customfield_26131` | date |
| Manager | `customfield_26132` | option id |
| Specialization | `customfield_26133` | option id — aligns with pillar |
| Atlas project | `customfield_27433` | atlas-project type |
| Parent (hierarchy) | `parent` | Issue key or `{ "key": "BLUEPRINT-1" }` |
| Epic color | `customfield_10017` | Epic only |

## Tracks vs issue types

Use native **issue types** for domain work (`Amendments`, `Filings`, `Audits`, `Systems`, `Leadership`) and set **Specialization** to the matching pillar when you want a consistent secondary filter across types.

## Subtasks

`parent` is **required** for `Subtask`. Provide the parent issue key when creating subtasks.

## Regenerating inventory

Issue metadata can drift. Re-run Atlassian MCP `getJiraIssueTypeMetaWithFields` for each `issueTypeId` and update [`jira-field-inventory.json`](./jira-field-inventory.json), or run `python scripts/dump_field_map.py` after editing that script to point at your REST client if you add one later.
