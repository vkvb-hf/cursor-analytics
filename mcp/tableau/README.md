# Tableau MCP

Pre-built Tableau MCP server for HelloFresh Tableau Server (2023.1.5).

## Why Custom Build?

- **Official `@tableau/mcp-server`** uses REST API v3.24 (requires Tableau 2023.3+)
- **HelloFresh Tableau Server** is version 2023.1.5 (supports REST API v3.19)
- **This build** is patched to use API v3.19 + includes custom enhancements

## Quick Setup

### 1. Get a Personal Access Token (PAT)

1. Go to Tableau Server → Settings → Personal Access Tokens
2. Create a new token named `Cursor MCP`
3. Copy the token value (you won't see it again)

### 2. Add to Cursor MCP Config

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "tableau": {
      "command": "node",
      "args": ["/path/to/cursor-analytics/mcp/tableau/index.js"],
      "env": {
        "SERVER": "https://tableau.hellofresh.io",
        "SITE_NAME": "",
        "PAT_NAME": "Cursor MCP",
        "PAT_VALUE": "your-pat-token-here"
      }
    }
  }
}
```

**Path Examples:**
- **macOS:** `"/Users/yourname/Documents/databricks/cursor-analytics/mcp/tableau/index.js"`
- **Windows:** `"C:/Users/YourName/Documents/cursor-analytics/mcp/tableau/index.js"`

### 3. Restart Cursor

Fully quit (Cmd+Q / Alt+F4) and reopen Cursor.

---

## Available Tools (12 tools)

### Workbooks & Views

| Tool | Description |
|------|-------------|
| `list-workbooks` | List workbooks with filtering |
| `get-workbook` | Get workbook details and views |
| `list-views` | List views across workbooks |
| `get-view-image` | Get screenshot of a view |
| `get-view-data` | Get view data as CSV |
| `refresh-workbook-extract` | **Trigger extract refresh** |

### Datasources

| Tool | Description |
|------|-------------|
| `list-datasources` | List published datasources |
| `get-datasource-metadata` | Get field metadata |
| `query-datasource` | Run VizQL queries |

### Jobs

| Tool | Description |
|------|-------------|
| `get-job-status` | Check async job status |

### Search & Content

| Tool | Description |
|------|-------------|
| `search-content` | Search across all content types |

---

## Usage Examples

### List Workbooks
```
"List the first 10 Tableau workbooks"
"Find workbooks with 'Payments' in the name"
```

### Get Dashboard Screenshot
```
"Show me an image of the Payments P0 Metrics dashboard"
```

### Refresh Extract (NEW)
```
"Refresh the [PY-2003] ASCS Experiment Results dashboard"
```

### Check Refresh Status
```
"Check status of job 8cbb024b-b058-42e4-9add-212315a87219"
```

### Query Datasource
```
"Query the Sales datasource for total revenue by region"
```

---

## Custom Enhancements

This build includes functionality **not in the official Tableau MCP**:

### Extract Refresh Capability

Trigger workbook extract refreshes directly from Cursor - equivalent to clicking "Refresh Extracts" in Tableau Server UI.

**How it works:**
1. Call `refresh-workbook-extract` with workbook ID
2. Returns a job ID immediately (async operation)
3. Call `get-job-status` to check progress
4. Job completes with `finishCode: 0` on success

**Example flow:**
```
User: "Refresh the ASCS Experiment Results dashboard"

AI: Found workbook c295f65a-d8d4-43fe-85ce-210ba4a96da7
    Triggering refresh...
    Job ID: 8cbb024b-b058-42e4-9add-212315a87219
    Status: In Progress (0%)

User: "Check status"

AI: Job 8cbb024b-b058-42e4-9add-212315a87219
    Status: Completed ✓
    Progress: 100%
    Duration: 1 minute 20 seconds
```

---

## Limitations

### What You CANNOT Do:
- View custom SQL embedded in workbooks
- See calculated field formulas
- View parameter logic
- Access workbook XML structure
- Modify dashboards (create/update/delete)

### To Access These:
Download the `.twbx` file from Tableau Server UI and extract it.

---

## Troubleshooting

### 404 Errors
- Verify `SERVER` URL is correct (no trailing slash)
- Confirm `SITE_NAME` is correct (empty string `""` for default site)

### 401 Errors
- PAT token may be invalid or expired
- Generate new token in Tableau → Settings → Personal Access Tokens

### "Tool not found"
- Restart Cursor (full quit, not just close window)
- Check MCP status in Cursor Settings → MCP

### Refresh Returns 400
- Workbook may not have extracts to refresh
- Check workbook has embedded data sources with extracts

---

## Build Information

| Property | Value |
|----------|-------|
| Source | https://github.com/tableau/tableau-mcp |
| API Version | 3.19 (patched from 3.24) |
| Target Server | HelloFresh Tableau Server 2023.1.5 |
| Build Date | 2026-02-03 |
| Custom Features | Extract refresh, job status |

---

## Updating the Build

When updates are needed:

1. Clone official repo: `git clone https://github.com/tableau/tableau-mcp`
2. Apply patches (see below)
3. Build: `npm install && npm run build`
4. Copy `build/index.js` to this folder
5. Test with Cursor

### Required Patches

**File: `src/sdks/tableau/restApi.ts`**
```typescript
// Line ~49: Change API version
private static _version = '3.19';  // Changed from '3.24'
```

**Additional files for refresh capability:**
- `src/sdks/tableau/types/job.ts` (new)
- `src/sdks/tableau/apis/jobsApi.ts` (new)
- `src/sdks/tableau/apis/workbooksApi.ts` (modified)
- `src/sdks/tableau/methods/jobsMethods.ts` (new)
- `src/sdks/tableau/methods/workbooksMethods.ts` (modified)
- `src/tools/workbooks/refreshWorkbookExtract.ts` (new)
- `src/tools/jobs/getJobStatus.ts` (new)
- Plus tool registration in `tools.ts` and `toolName.ts`

Full source with patches: `/Users/visal.kumar/Documents/tableau-mcp/`
