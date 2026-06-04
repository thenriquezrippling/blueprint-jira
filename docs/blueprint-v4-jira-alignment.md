# Tax Ops Universal Blueprint v4 ↔ BLUEPRINT Jira alignment

**Source:** *Tax Ops Universal Workflow Blueprint* v4.0 (May 2026) — [canonical Google Doc](https://docs.google.com/document/d/1keyqyWl2dotMuRJUN7Gv7YpvoGRTFEkt2QfYnJjh1JI/edit); plain-text mirror in [`tax-ops-universal-blueprint-v4.txt`](./tax-ops-universal-blueprint-v4.txt) (synced from Docs MCP).

This table compares **Section 04 — Universal Jira Field Schema** (and closely related concepts) to fields captured in [`jira-field-inventory.json`](./jira-field-inventory.json) for project **BLUEPRINT** as of the last inventory refresh.

| v4 field (concept) | In BLUEPRINT today? | Current / proposed mapping |
|--------------------|---------------------|----------------------------|
| Issue Type | Yes | Native types: Epic, Story, Task, Subtask, Filings, Amendments, Audits, Systems, Leadership — use types + hierarchy per v4 §01. |
| Summary / title | Yes | `summary` — apply v4 title pattern in automation (`[Work Type] · [Employer] · [State] · [Action]`). |
| Work Stream | Partial | v8 streams include Refiles, New Hire, Agency Notice, Escalation, Internal Ops. **Map:** issue type + `labels` until a dedicated select exists. |
| Pillar | Partial | `customfield_26133` **Specialization** overlaps (e.g. Filings & Payments, Amendments, Audits). **Gap:** v4 also lists *New Hire Reporting*, *E2E PEO*, *Rippling Direct* — not all appear as Specialization options; use **labels** or extend field options in Jira admin. |
| Assignee / DRI | Yes | `assignee` |
| Priority | Yes | `priority` — Jira uses Rippling’s priority scheme (incl. *Parker*) + standard levels; v4 uses **P1–P4** labels. **Reconcile** naming and automation thresholds in Jira admin + automations. |
| Client Segment | **Gap** | v4: Enterprise / Mid-Market / SMB / Internal with upgrade rules. **Not** in current inventory — add custom field or encode via `labels`. |
| SLA Bucket | **Gap / partial** | v4 defines buckets derived from priority × segment. Jira has `customfield_26130` **SLA** with **P0–P3** options — different scale than v4 **P1–P4**. Align semantics or rename options with Tax Ops. |
| Queue Status | **Gap** | v4: Active / Aging / Escalated / Parked / Unassigned — not in inventory. |
| Operational Readiness | **Gap** | v4 §05 + readiness framework — critical; not in inventory. |
| Operational Risk Status | **Gap** | v4: On Track / At Risk / Critical Risk / Dependency Risk / Penalty Risk — not in inventory. |
| Jurisdiction / State | **Gap** | v4 required text — use new custom field or structured label convention (e.g. `jurisdiction/OH`). |
| Employer / Client ID | **Gap** | v4 required — new field or link to external system of record. |
| Regulatory Deadline | **Gap** | v4 §06 — distinct from SLA due date; not separate in inventory. **Optional:** map to `duedate` only if team accepts single date (doc discourages conflating). |
| Operational Deadline | **Gap** | v4 §06 — internal cutoff; not in inventory. |
| Due Date (SLA target) | Yes | `duedate` — matches v4 “SLA Deadline / Due Date” if automations maintain it. |
| Source Channel | **Gap** | v4: Email / Voicemail / Slack / Agency Notice / Leadership / System-Generated — not in inventory. |
| Parent goal / initiative | Yes | `parent`; Epics for initiatives per v4 hierarchy. |
| Filing frequency | Partial | `customfield_26129` **Cadence** (Semi-Monthly, Monthly, …) — close to v4 “Filing Frequency”; confirm option set with Tax Ops. |
| Labels | Yes | `labels` — use for enterprise flags, `escalated`, `client-visible`, etc., per v4. |
| Story Points | Yes | `customfield_10016` — v4 defers mandatory points; optional is consistent. |
| Team | Yes | `customfield_10001` |
| Manager (pillar) | Partial | `customfield_26132` **Manager** — aligns with “manager DRI” naming in routing tables, not identical to “Pillar” column in doc. |
| MMDD | Present | `customfield_26131` — not called out in v4 schema table; may map to internal milestone / month-day tracking if Tax Ops agrees. |
| Atlas “Project” | Yes | `customfield_27433` — optional cross-link to Atlas. |
| Blocker Type (11 categories) | **Gap** | v4 §05 taxonomy — needs select + transition gates; not in inventory. |
| Issue links (refile of, corrects, …) | Native | Use Jira issue links; align **link type** names with v4 §03B (may require admin configuration of link types). |

## Decisions called out in v4 that affect Jira

The document lists **7 decisions** (owners, SLA defaults, Kitty intake path, Audits workflow, Salesforce vs Jira SoR, routing agent scope, story points). Those should be resolved before expanding the Jira schema to match every v4 field.

## Suggested next engineering steps

1. **Freeze a target schema** — Export v4 Section 04 + §05 into a checklist; for each **Gap**, ticket Jira admin work (new custom field + screens + automations) or an explicit **labels convention** where fields are intentionally deferred.
2. **Refresh inventory** after each Jira change — Re-run MCP `getJiraIssueTypeMetaWithFields` and update `docs/jira-field-inventory.json` and `BlueprintMapper`.
3. **Routing agent** — v4 Phase 2: extend agent to populate the unified fields at creation; jurisdiction→DRI table is a documented prerequisite.

## Doc scope boundary (v4)

Intake, coordination, governance, escalation, and visibility only — **not** filings execution, ACH orchestration, Salesforce SoR, etc. Keep automation bounded accordingly.
