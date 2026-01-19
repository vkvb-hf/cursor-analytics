# Background Query Execution - Non-Blocking Usage

## The Problem

When you run queries sequentially, the agent/script **blocks** waiting for each query to complete. This means:
- You can't do other work while queries run
- Your prompts appear to "queue" because the system is waiting
- Total time = sum of all query times

## The Solution: Background Execution

The background executor runs queries **asynchronously** - you submit them and continue working immediately.

## How It Works

1. **Submit queries** → Returns immediately (non-blocking)
2. **Queries run in background** → Using thread pool executor
3. **Check status anytime** → Without waiting
4. **Get results when ready** → Queries continue running independently

## Usage Examples

### Example 1: Submit and Continue (Non-Blocking)

```python
from parallel.background_executor import get_background_executor

executor = get_background_executor()

# Submit queries - returns immediately!
query_ids = executor.submit_queries([
    "SELECT COUNT(*) FROM table1",
    "SELECT COUNT(*) FROM table2"
])

# Continue working here - queries run in background
print("Queries submitted, continuing with other work...")

# Later, check results
results = executor.get_result(query_ids[0], wait=True)
```

### Example 2: Command Line (Non-Blocking)

```bash
# Submit queries - script exits immediately
python parallel/submit_and_continue.py

# Check status later
python parallel/run_background_queries.py --status

# Get results when ready
python parallel/run_background_queries.py --results checkout_analysis sample_data
```

### Example 3: In Agent Workflow

```python
# Agent can submit queries and continue
executor = get_background_executor()
query_ids = executor.submit_queries([query1, query2])

# Agent can do other work here
# ... analyze other data ...
# ... process files ...
# ... run other queries ...

# Check if queries are done
status = executor.get_tracker().get_status_summary()
if status['completed'] > 0:
    # Get results
    results = executor.get_result(query_ids[0])
```

## Key Differences

### Sequential (Blocking)
```python
# Blocks here - can't do anything else
result1 = run_query(query1)  # Waits 10s
result2 = run_query(query2)   # Waits 10s
# Total: 20s, agent blocked for 20s
```

### Background (Non-Blocking)
```python
# Returns immediately - agent can continue
executor.submit_queries([query1, query2])  # Returns in <0.1s
# Agent can do other work immediately
# Queries run in background
# Total: ~10s (both run concurrently), agent blocked for <0.1s
```

## Why Prompts Appear to Queue

When you run a **blocking** script:
1. Script starts executing
2. Script waits for queries to complete
3. During this wait, your prompts are queued
4. Once queries finish, script returns and prompts are processed

With **background** execution:
1. Script submits queries
2. Script returns immediately (<0.1s)
3. Your prompts are processed immediately
4. Queries continue running independently

## Best Practices

1. **Use background executor for long queries** - Don't block the agent
2. **Check status periodically** - See progress without waiting
3. **Get results when needed** - Use `wait=True` only when you actually need results
4. **Use callbacks for notifications** - Get notified when queries complete

## Example: Agent Workflow

```python
# Step 1: Submit queries (non-blocking)
executor = get_background_executor()
query_ids = executor.submit_queries([long_query1, long_query2])

# Step 2: Agent continues with other work
# ... do analysis ...
# ... process other data ...

# Step 3: Check if queries are done (non-blocking check)
status = executor.get_tracker().get_status_summary()
print(f"Completed: {status['completed']}, Running: {status['running']}")

# Step 4: Get results when ready (only blocks if wait=True)
if status['completed'] > 0:
    result = executor.get_result(query_ids[0], wait=False)  # Non-blocking
    if result:
        # Process results
        pass
    else:
        # Query still running, check later
        pass
```

## Command Line Workflow

```bash
# Terminal 1: Submit queries
python parallel/submit_and_continue.py
# Exits immediately, queries run in background

# Terminal 2: Continue working, check status anytime
python parallel/run_background_queries.py --status

# When ready, get results
python parallel/run_background_queries.py --results query_1 query_2
```

## Summary

- **Background executor** = Non-blocking, returns immediately
- **Sequential execution** = Blocking, waits for completion
- **Use background** when you want to continue working
- **Use sequential** only when you immediately need results

