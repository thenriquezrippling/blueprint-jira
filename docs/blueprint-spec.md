# Blueprint system specification (repo copy)

The original design lived in a Google Doc that is not machine-readable from this workspace. This document is the **working specification** for automation and integrations. Update it when the canonical doc changes.

## Jira anchor

| Property | Value |
|----------|-------|
| Site | `https://rippling.atlassian.net` |
| Cloud ID (API) | `969226a5-2105-49eb-a9f7-e3852660973e` |
| Project key | `BLUEPRINT` |
| Project name | Blueprint — Filings & Payments Systems and Product Pillar |
| Style | Next-gen (simplified) |

## Issue-type model (from Jira)

Blueprint work is organized in **BLUEPRINT** using these issue types:

| Issue type | Jira id | Role in blueprint |
|------------|---------|-------------------|
| Epic | `18241` | Portfolio / initiative container |
| Story | `24284` | User-facing feature slice |
| Task | `18240` | Distinct unit of work |
| Subtask | `18242` | Child work item |
| Amendments | `18570` | Amendment track |
| Filings | `18571` | Filing track |
| Audits | `18572` | Audit track |
| Systems | `18573` | Systems track |
| Leadership | `24285` | Confidential work type |

**Conventions**

- Use **Epic** for cross-cutting blueprint themes; link **Story** / **Task** issues to the epic via parent/epic link fields as supported by the project configuration.
- Domain tracks (**Filings**, **Amendments**, **Audits**, **Systems**) capture pillar-specific work; pick the type that matches the workstream.

## Automation goals

1. **Discover** required fields and allowed values per issue type (see `docs/jira-field-inventory.json`).
2. **Map** local / tool naming to Jira field keys (see `config/blueprint-field-map.json`).
3. **Create and update** issues via Atlassian MCP or REST using those keys.

## Out of scope for MCP-only flows

Creating **new** custom field definitions in Jira requires Jira admin (UI or admin-scoped REST). This repo documents and consumes existing fields only.

## References

- Field inventory: [`jira-field-inventory.json`](./jira-field-inventory.json) (generated).
- Field map for tools: [`../config/blueprint-field-map.json`](../config/blueprint-field-map.json).
- Mapping notes: [`field-mapping.md`](./field-mapping.md).
