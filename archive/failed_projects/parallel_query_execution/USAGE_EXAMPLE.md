# Usage Example - Background Query Execution

## How to Use (For Agents)

When you want to run queries in the background, use this pattern:

```python
import sys
import os
sys.path.insert(0, '/Users/visal.kumar/Documents/databricks/cursor_databricks')
from parallel.agent_background_api import submit_and_continue, get_api

# Step 1: Submit queries to run in BACKGROUND
# IMPORTANT: Tell the user queries are running in background!
query_ids = submit_and_continue(
    queries=[query1, query2],
    query_ids=["query_1", "query_2"]
)

# Step 2: Inform user
print("✅ Queries submitted to run in BACKGROUND")
print(f"Query IDs: {', '.join(query_ids)}")
print("Queries are executing in the background - you can continue working!")

# Step 3: Later, check status (non-blocking)
api = get_api()
status = api.get_status()
print(f"Status: {status['running']} running, {status['completed']} completed")

# Step 4: Get results when ready
results = api.get_results(query_ids, wait=False)  # Non-blocking
# Or wait if needed:
# results = api.get_results(query_ids, wait=True)  # Blocks until done
```

## Communication Pattern

**Always explicitly state:**
1. "Submitting queries to run in BACKGROUND"
2. "Queries are now running in the background"
3. "You can continue working while they execute"
4. "Check status later with..."

## Example Response

```
I'm submitting your queries to run in the BACKGROUND. This means:
- Queries will execute concurrently
- The chat interface stays responsive
- You can continue working immediately
- I'll track their progress and notify you when complete

Query IDs: checkout_analysis, sample_data
Status: 2 queries running in background

You can check status anytime, and I'll retrieve results when they're ready.
```

