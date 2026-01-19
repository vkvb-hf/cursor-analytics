# Agent Usage - Non-Blocking Query Execution

## The Problem

When agents run queries via terminal commands, the chat interface locks because:
- Terminal commands block until completion
- Even if queries run in background, the terminal command itself blocks
- Chat interface shows "running" and prompts queue

## The Solution

Use the **Agent Background API** directly in Python code - no terminal commands!

## How Agents Should Use It

### Direct Python API (Recommended)

```python
# In agent code - import and use directly
import sys
import os
sys.path.insert(0, '/Users/visal.kumar/Documents/databricks/cursor_databricks')
from parallel.agent_background_api import submit_and_continue, get_api

# Submit queries - returns in <0.1s, chat stays responsive
query_ids = submit_and_continue([
    "SELECT COUNT(*) FROM table1",
    "SELECT COUNT(*) FROM table2"
], query_ids=["query1", "query2"])

# Continue with other work immediately
# Chat interface is NOT locked!

# Later, check results (non-blocking)
api = get_api()
status = api.get_status()
if status['completed'] > 0:
    results = api.get_results(query_ids, wait=False)
```

### Key Points

1. **Import directly** - Don't use `run_terminal_cmd`
2. **Returns immediately** - `submit_and_continue()` returns in <0.1s
3. **Chat stays responsive** - No blocking, prompts process immediately
4. **Check results later** - Use `get_results()` when needed

## Example: Agent Workflow

```python
# Step 1: Submit queries (non-blocking)
from parallel.agent_background_api import submit_and_continue, get_api

query1 = "SELECT ..."  # Long running query
query2 = "SELECT ..."  # Another query

query_ids = submit_and_continue(
    queries=[query1, query2],
    query_ids=["analysis_1", "analysis_2"]
)

# Step 2: Agent continues immediately
# Can process other requests, analyze data, etc.
# Chat interface is responsive!

# Step 3: Check status (non-blocking)
api = get_api()
status = api.get_status()
print(f"Running: {status['running']}, Completed: {status['completed']}")

# Step 4: Get results when ready
# Option A: Non-blocking check
results = api.get_results(query_ids, wait=False)
if results:
    # Process results
    pass

# Option B: Wait for specific query (only if needed)
result = api.executor.get_result(query_ids[0], wait=True, timeout=60)
```

## Why This Works

1. **No terminal commands** - Direct Python calls
2. **Thread-based execution** - Queries run in background threads
3. **Immediate return** - API calls return in milliseconds
4. **Persistent executor** - Global executor persists across calls

## Comparison

### ❌ Wrong: Using Terminal Commands
```python
# This blocks the chat interface!
run_terminal_cmd("python parallel/submit_and_continue.py")
# Chat locked until script exits
```

### ✅ Correct: Direct API Calls
```python
# This returns immediately!
from parallel.agent_background_api import submit_and_continue
query_ids = submit_and_continue([query1, query2])
# Chat stays responsive!
```

## Status Checking

```python
from parallel.agent_background_api import get_api

api = get_api()

# Non-blocking status check
status = api.get_status()
print(f"Total: {status['total']}")
print(f"Running: {status['running']}")
print(f"Completed: {status['completed']}")

# Check specific queries
completed = api.check_completed(["query1", "query2"])
# Returns: {"query1": True, "query2": False}

# Get results (non-blocking)
results = api.get_results(["query1"], wait=False)
# Returns immediately with available results
```

## Best Practices for Agents

1. **Always use direct API** - Never use terminal commands for background queries
2. **Submit and continue** - Don't wait unless you need results immediately
3. **Check status periodically** - Use non-blocking status checks
4. **Get results when needed** - Use `wait=False` for non-blocking, `wait=True` only when necessary

## Complete Example

```python
import sys
import os
sys.path.insert(0, '/Users/visal.kumar/Documents/databricks/cursor_databricks')

from parallel.agent_background_api import submit_and_continue, get_api
from core.query_util import print_table

# Submit queries - returns immediately
query_ids = submit_and_continue([
    "SELECT dd.iso_year_week, COUNT(DISTINCT a.customer_id) as total_customers...",
    "SELECT * FROM payments_hf.checkout_funnel_backend LIMIT 5"
], query_ids=["checkout_analysis", "sample_data"])

# Agent can do other work here
# Chat interface stays responsive!

# Later, check if queries completed
api = get_api()
status = api.get_status()

if status['completed'] > 0:
    # Get results
    results = api.get_results(query_ids, wait=False)
    
    for query_id, result in results.items():
        if result:
            print_table(result, limit=20, title=f"Results from {query_id}")
```

