# Leadership touchpoints (Tax Ops Universal Blueprint v4)

This document defines **when leadership engages** versus what **automation + ICs** handle day to day. It matches the blueprint’s intent: **no clerical “project tracking,”** but **clear escalation and visibility** for Robin, Kitty, and pillar managers.

**Canonical spec:** [Tax Ops Universal Workflow Blueprint](https://docs.google.com/document/d/1keyqyWl2dotMuRJUN7Gv7YpvoGRTFEkt2QfYnJjh1JI/edit)  
**Jira rollout epic:** [BLUEPRINT-117](https://rippling.atlassian.net/browse/BLUEPRINT-117)

---

## Roles (who)

| Role | Primary involvement |
|------|------------------------|
| **Kitty (VP, Product Operations)** | Intake convenience, confirmation that work is captured, visibility on her requests, escalation when VIP items drift. |
| **Robin (Director, Tax Operations)** | Cross-pillar health, SLA risk, dependency/blocker patterns, staffing signals, RCA traceability for repeat failures. |
| **Pillar leads / managers** | Jurisdiction→DRI table ownership, clearing unclassified intake, blocker ownership within pillar, approving workflow exceptions when policy requires it. |
| **Systems / engineering (as needed)** | Webhooks, agent extensions, Jira automation limits, integrations—not day-to-day ticket triage. |

---

## Touchpoints by channel (how)

| Channel | What leadership does | What automation does |
|---------|----------------------|-------------------------|
| **Jira dashboards & filters** | Reviews health on a rhythm they choose (daily/weekly); drills into aging, P1, blockers, risk flags. | Keeps issues current; surfaces queues without manual status meetings. |
| **Slack** | Receives **pushes** only on triggers (see below); may use **VP quick-create** / pinned form for intake. | Confirms ticket creation, posts links to threads, sends SLA / escalation alerts. |
| **Email** | Rare for routine ops if blueprint is working; reserved for external/legal escalations as needed. | Routing agent + Jira remain system of record; avoid “status via email.” |

---

## Triggers (when leadership hears from the system)

These are **exception- and summary-driven**, not “every ticket pings Robin.”

### Kitty-oriented triggers (examples from v4)

| Trigger | Typical action |
|---------|----------------|
| **VP quick-create submitted** | Slack confirmation: ticket id, DRI, SLA deadline. |
| **P1 ages past threshold** (e.g. 4h in v4 examples) | Slack alert to DRI + escalation path as policy defines. |
| **Enterprise client + risk** (blocked or SLA halfway) | Additional labels / manager notification per v4 enterprise rules. |
| **Weekly digest** (Phase 2+) | Auto summary: resolved, aging, needs VP attention. |

### Robin-oriented triggers

| Trigger | Typical action |
|---------|----------------|
| **Cross-pillar dashboard thresholds** | e.g. queue depth, SLA compliance, blocker mix—reviewed on a cadence, not per ticket. |
| **Operational Risk Status** = At Risk / Critical Risk | Appears on dashboard; optional Slack route per policy. |
| **Unassigned queue SLA** (v4: clear within 4 business hours for unclassifiable intake) | Pillar lead / Robin path per routing table decision. |
| **RCA / repeat failure pattern** | Uses **issue link taxonomy** (refile of, corrects, caused by, …)—Robin uses links/filters, not ad-hoc email chains. |

### Pillar-manager triggers

| Trigger | Typical action |
|---------|----------------|
| **Jurisdiction missing from DRI table** | Route to pillar lead; table update is the fix (v4 prerequisite). |
| **Blocked with blocker taxonomy set** | Manager monitors aging; automation nudges per v4. |
| **Mandatory link missing on close** | Automation flags; manager remediates within SLA (v4 governance). |

---

## Cadence (how often—not “tracking,” reviewing)

Suggested **defaults** (tune with Robin/Kitty):

| Cadence | Activity |
|---------|----------|
| **Daily (5 min)** | Robin: dashboard—P1, aging, unassigned queue depth. |
| **Weekly (15–30 min)** | Robin + leads: blocker mix, SLA compliance trend, capacity signals. Kitty: digest + any open VP-requested items. |
| **Ad hoc** | Legal/compliance gates, client-visible crises, policy exceptions—routed by automation with full ticket context. |

---

## Success metrics (from v4—what “good” looks like)

Examples already stated in the blueprint (paraphrased):

- **Kitty** can confirm a ticket exists in **under ~2 minutes** after intake (Phase 1).  
- **Robin** has a **real-time cross-pillar** view Day 1 Phase 1.  
- **% of work in Jira** vs shadow channels trends toward **90%+** by Day 30.  
- **SLA compliance** toward **85%+** by Day 60.  
- **No escalation without a prior Jira ticket** by Day 30 (discipline + automation).  

These are **outcomes**, not “leaders updating tickets.”

---

## Implementation mapping (Jira stories)

| Topic | Jira |
|--------|------|
| Dashboards & filters | [BLUEPRINT-123](https://rippling.atlassian.net/browse/BLUEPRINT-123) |
| VP quick-create + Slack | [BLUEPRINT-122](https://rippling.atlassian.net/browse/BLUEPRINT-122) |
| SLA / escalation automations | [BLUEPRINT-121](https://rippling.atlassian.net/browse/BLUEPRINT-121) |
| Field schema (risk, readiness, queue, blockers) | [BLUEPRINT-118](https://rippling.atlassian.net/browse/BLUEPRINT-118) |

---

## Out of scope reminder (v4)

Leadership visibility and governance **do not replace** filings execution, ACH orchestration, Salesforce SoR decisions, etc.—those stay in their systems; Jira tracks and governs the **coordination layer**.
