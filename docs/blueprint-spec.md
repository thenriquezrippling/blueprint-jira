# Blueprint system specification (repo copy)

## Canonical product spec

- **Authoritative source (live):** [Tax Ops Universal Workflow Blueprint](https://docs.google.com/document/d/1keyqyWl2dotMuRJUN7Gv7YpvoGRTFEkt2QfYnJjh1JI/edit) — Google Doc id `1keyqyWl2dotMuRJUN7Gv7YpvoGRTFEkt2QfYnJjh1JI` (v4.0, May 2026).
- **Full text in repo:** [`tax-ops-universal-blueprint-v4.txt`](./tax-ops-universal-blueprint-v4.txt) — last synced from that Google Doc via MCP `fetch` (re-run fetch and overwrite this file when the Doc changes).
- **Jira gap analysis:** [`blueprint-v4-jira-alignment.md`](./blueprint-v4-jira-alignment.md) — maps v4 §04 field schema to project **BLUEPRINT** and flags missing fields.

### Executive summary (from v4)

Tax Ops ingests work from **six channels** (email, Slack, voicemail, agency portals, VP assignment, system alerts). The blueprint defines a **universal Jira-based workflow**: zero dark work, auto-routing (work type → pillar → jurisdiction/DRI), SLA enforcement, leadership visibility, cross-ticket tracing (mandatory link taxonomy), and **18** Jira/automation rules phased over Foundation → Automation → AI expansion.

**Hierarchy:** Epic → Story → Task → Subtask with explicit “when to use” rules; standalone intake items should become **Stories** first to avoid orphaned Tasks.

**Routing:** Two-step pillar then DRI; client segment can upgrade priority (Enterprise); unclassified items go to an **Unassigned** path with timeboxed SLA to clear.

This markdown file stays the **integration anchor** for this repository (cloud ids, issue types, repo tooling). Narrative, examples, automations list, and governance live in the v4 text file above.

## Jira initiative (live backlog)

Program epic for rolling out the blueprint inside **BLUEPRINT**:

- **Epic:** [BLUEPRINT-117](https://rippling.atlassian.net/browse/BLUEPRINT-117) — *Tax Ops Universal Blueprint v4 — Jira rollout & enablement*
- **Child stories:** `BLUEPRINT-118` … `BLUEPRINT-125` (see epic comment for the index table).
- **Filter (JQL):** `project = BLUEPRINT AND labels = blueprint-framework ORDER BY rank`

Created via Atlassian MCP; **Specialization** set to *Systems & Product* on stories. Reassign **Assignee** / **Manager** as needed for real owners.

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

- Full v4 spec (plain text): [`tax-ops-universal-blueprint-v4.txt`](./tax-ops-universal-blueprint-v4.txt)
- v4 ↔ Jira alignment: [`blueprint-v4-jira-alignment.md`](./blueprint-v4-jira-alignment.md)
- Field inventory: [`jira-field-inventory.json`](./jira-field-inventory.json) (generated).
- Field map for tools: [`../config/blueprint-field-map.json`](../config/blueprint-field-map.json).
- Mapping notes: [`field-mapping.md`](./field-mapping.md).
- Jira API token + GitHub Actions: [`jira-api-token.md`](./jira-api-token.md).
