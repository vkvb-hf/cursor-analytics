# Universal Notebook Output Solution

**Goal**: See notebook output in terminal for ANY notebook, universally.

## Analysis of Approaches

### Current Approach (Print Interception)
**Status**: ❌ Not working reliably
- Complex setup with multiple fallback methods
- Scope issues across cells
- Output variable not always available
- Requires code injection

### Option 1: Databricks Jobs API Output (RECOMMENDED) ✅
**How it works**: Use Databricks' native `/api/2.1/jobs/runs/get-output` endpoint
- **Pros**:
  - ✅ Works for ANY notebook without modification
  - ✅ Captures all cell outputs (print, query results, errors)
  - ✅ Native Databricks feature - reliable
  - ✅ No code injection needed
  - ✅ No scope issues
- **Cons**:
  - ⚠️ Limited to what Databricks captures (but captures most things)
  - ⚠️ Need to parse the response structure

### Option 2: DBFS File Writing
**How it works**: Notebook writes output to DBFS file
- **Pros**:
  - ✅ Full control over output format
  - ✅ Can capture everything
- **Cons**:
  - ❌ Requires code changes in notebook
  - ❌ Not universal

### Option 3: stdout/stderr Interception
**How it works**: Intercept Python stdout/stderr
- **Pros**:
  - ✅ Catches everything
- **Cons**:
  - ❌ Complex
  - ❌ May not work in Databricks environment
  - ❌ Requires code injection

## Recommended Solution: Databricks Jobs API Output

### Implementation Strategy

1. **Use Databricks Jobs API** to get notebook cell outputs
2. **Parse the response** to extract:
   - Print statements (`text/plain`)
   - Query results (DataFrames)
   - Errors
   - All cell outputs
3. **Display in terminal** in a readable format
4. **Works universally** - no notebook modification needed

### API Endpoint

```
GET /api/2.1/jobs/runs/get-output?run_id={run_id}
```

### Response Structure

```json
{
  "notebook_output": {
    "result": {
      "data": [
        {
          "text/plain": "print statement output"
        },
        {
          "text/html": "<html>...</html>"
        }
      ],
      "errorSummary": "...",
      "cause": "..."
    }
  },
  "error": "...",
  "error_trace": "..."
}
```

### Implementation Plan

1. **Enhance `get_task_output()` method** to better parse notebook outputs
2. **Extract all cell outputs** from the response
3. **Format and display** in terminal
4. **Handle different output types** (text, HTML, errors)
5. **Make it the default** output method

### Benefits

- ✅ **Universal**: Works for any notebook
- ✅ **No code changes**: Notebooks work as-is
- ✅ **Reliable**: Uses native Databricks API
- ✅ **Complete**: Captures print, queries, errors
- ✅ **Simple**: No complex injection logic

### Next Steps

1. Enhance the output parsing in `get_task_output()`
2. Improve display formatting
3. Make it the primary output method
4. Keep DBFS method as fallback/optional

