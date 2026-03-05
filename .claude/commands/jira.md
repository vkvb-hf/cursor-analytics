Manage Jira tickets: $ARGUMENTS

## Detect Intent

Parse `$ARGUMENTS` to determine the mode:

- **SHOW mode** — JUST a ticket ID with no action, or "show" + ticket ID (e.g., `GA-142`, `show GA-142`)
- **UPDATE mode** — A ticket ID with an action (e.g., `GA-142 add comment ...`, `GA-142 rewrite`, `rewrite GA-142`)
- **CREATE mode** — No ticket ID detected

---

## Hardcoded Defaults

| Field | Value |
|-------|-------|
| Cloud ID | `c563471e-8682-4abc-8fa9-5465b05abad5` |
| Project Key | `GA` |
| Sprint | None (goes to backlog) |

### Assignee
Do NOT hardcode. Fetch the current user via `getJiraCurrentUser` (cloudId: `c563471e-8682-4abc-8fa9-5465b05abad5`) at the start of CREATE mode to get their `accountId` and display name. Use this as the default assignee.

### Components
Do NOT hardcode. Infer the component from the ticket content:

| Content signals | Component |
|----------------|-----------|
| payments, billing, invoicing, charges, refunds, PSP, checkout | `Payments` |
| conversions, attribution, funnel, signup, activation, onboarding | `Conversions` |
| ads, advertising, campaigns, impressions, clicks, ad spend, tracking | `Ad Tech` |
| email, push, notifications, messaging, SMS, comms | `Communications` |

If the component cannot be confidently inferred, ask the user during the draft review step (Step 4).

## Field Selection (CRITICAL — always pass `fields` to reduce response size)

Only request the fields needed for each mode. The Jira API returns ~66KB without filtering vs ~3KB with.

| Mode | `fields` array |
|------|---------------|
| **SHOW** | `["summary","status","issuetype","assignee","reporter","priority","created","updated","parent","description","issuelinks","comment","customfield_10007"]` |
| **UPDATE** (default) | `["summary","status","assignee"]` |
| **UPDATE** (rewrite) | `["summary","status","issuetype","description","issuelinks","parent","comment"]` |
| **CREATE** (context fetch) | `["summary","status","description"]` |

---

## Ticket Template

All tickets MUST follow this format:

```
**User Story:**
As a [role], I want to [action], so that I can [goal/benefit].

**Why are we doing this?**
[Business context explaining the motivation, background, and impact. Include relevant metrics, test results, or business drivers.]

**Acceptance Criteria:**
- [Specific, measurable condition 1]
- [Specific, measurable condition 2]
- [Specific, measurable condition 3]

**Additional Details:**
- [Links to documentation]
- [Related tickets]
- [Technical context or constraints]

**Dependencies:** (if applicable)
- [TICKET-123](link) - Description of dependency
```

### Section Guidelines
- **User Story:** Be specific with the role (Analyst, Finance Team Member, Product Manager). State the action and the business outcome.
- **Why:** Most important section. Include business context, what led to this work, quantitative metrics if available, and stakeholder needs.
- **Acceptance Criteria:** Specific and measurable. Focus on outcomes, not tasks. Include validation requirements.
- **Additional Details:** Documentation links, related tickets with brief descriptions, data sources, constraints.
- **Dependencies:** Only include if work is blocked by other tickets. Link with context.

---

## SHOW Mode

### Step 1 — Fetch Ticket
Extract the ticket ID from `$ARGUMENTS`. Call `getJiraIssue` with:
- `cloudId`: `c563471e-8682-4abc-8fa9-5465b05abad5`
- `issueIdOrKey`: the extracted ticket ID
- `fields`: `["summary","status","issuetype","assignee","reporter","priority","created","updated","parent","description","issuelinks","comment","customfield_10007"]`

### Step 2 — Display
Present a clean, readable summary:

```
### <TICKET-ID>: <summary>

| Field | Value |
|-------|-------|
| Status | <status> |
| Type | <issue type> |
| Assignee | <assignee name> |
| Reporter | <reporter name> |
| Priority | <priority> |
| Sprint | <sprint name or "Backlog"> |
| Created | <date> |
| Updated | <date> |
| Parent/Epic | <parent key + title, if any> |

---

<description — render as markdown, preserving the original formatting>

---

**Linked Issues:**
- <type>: <TICKET-KEY> — <summary> (<status>)

**Comments** (<count>):
> **<author>** — <date>
> <comment body, truncated to ~200 chars if long>
```

- If there are more than 5 comments, show the 5 most recent and note "... and N earlier comments"
- If there are linked issues, list them grouped by link type (blocks, is blocked by, relates to, etc.)
- If the description is empty, note "[No description]"

---

## CREATE Mode

### Step 1 — Infer Issue Type
From the topic in `$ARGUMENTS`, determine the issue type:

| Keywords | Issue Type | Type Name |
|----------|-----------|-----------|
| analysis, investigate, understand, explore, retention, funnel, metrics | Story | `Story` |
| pipeline, ETL, table, data feed, sync, migrate, build | Task | `Task` |
| bug, fix, broken, error, wrong, incorrect, missing data | Bug | `Bug` |
| epic, initiative, program, workstream | Epic | `Epic` |
| _(default)_ | Task | `Task` |

### Step 2 — Gather Context
Ask the user ONE focused question:

> What's the business context for this ticket? You can share:
> - Related ticket IDs (I'll fetch them)
> - Doc links
> - A quick text summary
>
> Or say "skip" if the topic is self-explanatory.

Then:
- If user provides **ticket IDs** → fetch each via `getJiraIssue` (cloudId: `c563471e-8682-4abc-8fa9-5465b05abad5`, fields: `["summary","status","description"]`) and extract relevant context
- If user provides **URLs** → fetch content and extract relevant context
- If user provides **text** → use it directly as context
- If user says **"skip"** → infer context from the topic in `$ARGUMENTS`

**Wait for user response before proceeding.**

### Step 3 — Draft Ticket
Using the template above, draft a complete ticket:
- Write a concise **summary** (ticket title) — action-oriented, under 80 chars
- Fill in every section of the template using gathered context
- For analysis tickets, use role "Stakeholder" or "PM" (the person requesting the analysis, not the analyst)
- For pipeline/ETL tickets, use role "Data Consumer" or the specific stakeholder
- Make acceptance criteria specific to the deliverable (e.g., "Analysis completed for DE market", "Table refreshes daily")

### Step 4 — Show Draft
Present the full ticket to the user:

```
**Summary:** <title>
**Type:** <Story/Task/Bug/Epic>
**Project:** GA
**Assignee:** <current user display name>
**Component:** <inferred component, or "None — please specify">

---

<full description using the template>
```

If the component could not be inferred, ask along with: "Ready to create this ticket? Or would you like to edit anything?"

**Wait for user response before proceeding.**

### Step 5 — Create Ticket
Call `createJiraIssue` with:
- `cloudId`: `c563471e-8682-4abc-8fa9-5465b05abad5`
- `projectKey`: `GA`
- `issueTypeName`: the inferred type from Step 1
- `summary`: the title
- `description`: the formatted description (use ADF format as required by the API)
- `additionalFields`: `{"assignee": {"accountId": "<accountId from getJiraCurrentUser>"}, "components": [{"name": "<inferred or user-specified component>"}]}`

### Step 6 — Return Result
Share the created ticket key and URL with the user.

---

## UPDATE Mode

### Step 1 — Fetch Current Ticket
Extract the ticket ID from `$ARGUMENTS`. Call `getJiraIssue` with:
- `cloudId`: `c563471e-8682-4abc-8fa9-5465b05abad5`
- `issueIdOrKey`: the extracted ticket ID
- `fields`: `["summary","status","assignee"]` (default) — or `["summary","status","issuetype","description","issuelinks","parent","comment"]` if the action is "rewrite"/"reformat"

Show a brief summary of the current ticket (title, status, assignee).

### Step 2 — Parse Update Action
From the remaining text in `$ARGUMENTS` (after the ticket ID), determine what to do:

| Pattern | Action | Tool |
|---------|--------|------|
| "rewrite" or "reformat" | Reformat description to template (see Rewrite sub-flow below) | `editJiraIssue` |
| "add comment ..." or "comment ..." | Add a comment | `addCommentToJiraIssue` |
| "add dependency on X" or "link to X" or "depends on X" | Add issue link | `editJiraIssue` |
| "assign to [name]" | Change assignee | Look up via `lookupJiraAccountId`, then `editJiraIssue` |
| "move to [status]" or "transition to [status]" | Transition ticket | Fetch transitions via `getTransitionsForJiraIssue`, then `transitionJiraIssue` |
| "log [time]" or "add worklog [time]" | Log work | `addWorklogToJiraIssue` |
| Any other change request | Edit fields | `editJiraIssue` with appropriate fields |

### Step 3 — Execute
Call the appropriate MCP tool(s). Always use `cloudId`: `c563471e-8682-4abc-8fa9-5465b05abad5`.

### Step 4 — Confirm
Show what was changed (field, old value → new value where applicable).

### Rewrite Sub-flow (triggered by "rewrite" or "reformat" action)

1. **Extract context** from the fetched ticket:
   - Current description (however minimal or unstructured)
   - Issue type, linked issues, parent epic (fetch linked tickets for additional context)
   - Comments (scan for useful context)

2. **Reformat description** using the ticket template:
   - Preserve all existing information — do not discard anything meaningful
   - Restructure into the proper sections (User Story, Why, Acceptance Criteria, etc.)
   - Flag missing context with `[TODO: ...]`
   - Keep the same issue type and summary unless clearly wrong

3. **Show draft** — Present before/after to the user.
   Ask: "Ready to apply this rewrite? Or would you like to adjust anything?"
   **Wait for user response before proceeding.**

4. **Apply** — Call `editJiraIssue` with the reformatted description (ADF format).
