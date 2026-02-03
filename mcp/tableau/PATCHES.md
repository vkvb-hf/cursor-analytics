# Tableau MCP Custom Patches

This document describes all modifications made to the official [tableau/tableau-mcp](https://github.com/tableau/tableau-mcp) repository to support HelloFresh Tableau Server 2023.1.5 and add custom features.

## Base Version

- **Source**: https://github.com/tableau/tableau-mcp
- **Cloned**: 2026-02-03
- **Commit**: (latest main at time of clone)

---

## Patch 1: API Version Downgrade

**File**: `src/sdks/tableau/restApi.ts`

**Reason**: HelloFresh Tableau Server is version 2023.1.5, which supports REST API v3.19. The official MCP targets v3.24 (requires Tableau 2023.3+).

**Change**:
```diff
- private static _version = '3.24';
+ private static _version = '3.19';  // Changed for HelloFresh Tableau Server 2023.1.5
```

---

## Patch 2: Add Accept Header for JSON Responses

**File**: `src/sdks/tableau/methods/authenticatedMethods.ts`

**Reason**: Some Tableau API endpoints return XML by default. Adding `Accept: application/json` ensures consistent JSON responses.

**Change**:
```diff
  protected get authHeader(): AuthHeaders {
    if (!this._creds) {
      throw new Error('Authenticate by calling signIn() first');
    }

    return {
      headers: {
        'X-Tableau-Auth': this._creds.token,
+       'Accept': 'application/json',
      },
    };
  }
```

---

## Patch 3: Add Extract Refresh Capability

### New Files Created:

1. **`src/sdks/tableau/types/job.ts`** - TypeScript interfaces and Zod schemas for Job objects
2. **`src/sdks/tableau/apis/jobsApi.ts`** - Zodios endpoint for GET /jobs/{jobId}
3. **`src/sdks/tableau/methods/jobsMethods.ts`** - Method wrapper for job status queries
4. **`src/tools/workbooks/refreshWorkbookExtract.ts`** - MCP tool to trigger extract refresh
5. **`src/tools/jobs/getJobStatus.ts`** - MCP tool to check job status

### Modified Files:

**`src/sdks/tableau/apis/workbooksApi.ts`** - Added refresh endpoint:
```typescript
const refreshWorkbookExtractEndpoint = makeEndpoint({
  method: 'post',
  path: '/sites/:siteId/workbooks/:workbookId/refresh',
  alias: 'refreshWorkbookExtract',
  description: 'Initiates a refresh of the extracts in a workbook.',
  requestFormat: 'json',
  parameters: [
    {
      name: 'body',
      type: 'Body',
      schema: z.object({}).optional(),
    },
  ],
  response: z.object({ job: refreshJobSchema }),
});
```

**`src/sdks/tableau/methods/workbooksMethods.ts`** - Added refresh method:
```typescript
refreshWorkbookExtract = async ({
  workbookId,
  siteId,
}: {
  workbookId: string;
  siteId: string;
}): Promise<RefreshJob> => {
  return (
    await this._apiClient.refreshWorkbookExtract({}, {
      params: { siteId, workbookId },
      ...this.authHeader,
    })
  ).job;
};
```

**`src/sdks/tableau/restApi.ts`** - Added jobsMethods getter (see Patch 1 diff above)

**`src/tools/tools.ts`** - Registered new tools:
```typescript
import { getRefreshWorkbookExtractTool } from './workbooks/refreshWorkbookExtract.js';
import { getGetJobStatusTool } from './jobs/getJobStatus.js';

// Added to toolFactories array:
getRefreshWorkbookExtractTool,
getGetJobStatusTool,
```

**`src/tools/toolName.ts`** - Added tool names:
```typescript
// Added to ToolName type:
'refresh-workbook-extract',
'get-job-status',

// Added to ToolGroupName type:
'job',

// Added to toolGroups:
job: ['get-job-status'],
workbook: [..., 'refresh-workbook-extract'],
```

**`src/restApiInstance.ts`** - Added JWT scopes (for future OAuth support):
```typescript
type JwtScopes = 
  | 'tableau:content:read'
  // ... existing scopes ...
  | 'tableau:tasks:run'
  | 'tableau:tasks:read';
```

**`src/config.test.ts`** - Updated tests to include new tool in workbook group.

---

## Building from Source

```bash
cd mcp/tableau

# Install dependencies
npm install

# Build
npm run build

# Output: build/index.js
```

---

## Testing Changes

After building, test with:

```bash
# Set environment variables
export SERVER="https://tableau.hellofresh.io"
export SITE_NAME=""
export PAT_NAME="Cursor MCP"
export PAT_VALUE="your-token"

# Run the server
node build/index.js
```

Or configure in `~/.cursor/mcp.json` and restart Cursor.

---

## Updating from Upstream

When the official tableau-mcp releases updates:

1. Clone fresh: `git clone https://github.com/tableau/tableau-mcp`
2. Apply patches from this document
3. Build: `npm install && npm run build`
4. Copy `build/index.js` to this folder
5. Test with Cursor

---

## File Inventory

### Custom Files (created by us)
- `src/sdks/tableau/types/job.ts`
- `src/sdks/tableau/apis/jobsApi.ts`
- `src/sdks/tableau/methods/jobsMethods.ts`
- `src/tools/workbooks/refreshWorkbookExtract.ts`
- `src/tools/jobs/getJobStatus.ts`

### Modified Files (patched)
- `src/sdks/tableau/restApi.ts` (API version + jobsMethods)
- `src/sdks/tableau/methods/authenticatedMethods.ts` (Accept header)
- `src/sdks/tableau/apis/workbooksApi.ts` (refresh endpoint)
- `src/sdks/tableau/methods/workbooksMethods.ts` (refresh method)
- `src/tools/tools.ts` (tool registration)
- `src/tools/toolName.ts` (tool names)
- `src/restApiInstance.ts` (JWT scopes)
- `src/config.test.ts` (test updates)
