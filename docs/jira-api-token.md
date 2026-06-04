# Jira REST API with an API token (and GitHub)

The Cursor **Atlassian MCP** uses OAuth and a fixed tool surface (issues, comments, search, etc.). A **Jira Cloud API token** lets you call **any** REST endpoint your Atlassian account is allowed to use—often including admin operations the MCP does not expose.

## Authentication (Cloud)

Use **HTTP Basic**: username = your **Atlassian email**, password = the **API token** (not your login password).

- Create / revoke tokens: [Atlassian account → Security → API tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
- Base URL: `https://<site>.atlassian.net` (e.g. `https://rippling.atlassian.net`)

```bash
export JIRA_SITE="https://rippling.atlassian.net"
export JIRA_EMAIL="you@company.com"
export JIRA_API_TOKEN="your-token"   # never commit this

curl -sS -u "$JIRA_EMAIL:$JIRA_API_TOKEN" \
  -H "Accept: application/json" \
  "$JIRA_SITE/rest/api/3/myself" | jq .
```

## What a token can do (depends on your role)

| Capability | Typical requirement |
|------------|---------------------|
| Create/edit/search issues | Jira user with project permissions |
| Read field metadata | Usually yes |
| **Create custom fields** (`POST /rest/api/3/field`) | **Jira administrator** (or equivalent product admin) |
| Configure workflows / screens / automations | Admin + often **UI-first**; Automation has its own APIs and limits |
| Team-managed (next-gen) project schema | Some changes are more restricted than **company-managed** projects |

If `POST /rest/api/3/field` returns **401/403**, the token is valid but the account lacks admin (or the operation is disallowed for that project type).

## GitHub Actions

This repo includes [`.github/workflows/jira-api-smoke.yml`](../.github/workflows/jira-api-smoke.yml) (`workflow_dispatch`). Add the same **repository secrets** you use elsewhere:

| Secret | Example |
|--------|---------|
| `JIRA_SITE` | `https://rippling.atlassian.net` |
| `JIRA_EMAIL` | Your Atlassian email |
| `JIRA_API_TOKEN` | API token from id.atlassian.com |

Then: **Actions → Jira API smoke → Run workflow**. A green run confirms Basic auth works from GitHub’s runners.

Fork PRs do not receive these secrets; the workflow is **manual-only** on purpose.

## Official references

- [Jira Cloud platform REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
- [Create custom field](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/#api-rest-api-3-field-post) (`POST /rest/api/3/field`)

## Repo helper

[`scripts/jira_rest_smoke.py`](../scripts/jira_rest_smoke.py) — verifies env vars and calls `/myself` (no extra dependencies). Run locally before wiring GitHub Actions.
