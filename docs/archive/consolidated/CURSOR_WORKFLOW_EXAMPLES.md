# Cursor Workflow Examples: Real-World Scenarios

Practical examples of how to use Cursor effectively with the Databricks toolkit for common tasks.

## 📊 Scenario 1: Daily Data Quality Check

### What You Need
Check data quality for a critical table every morning.

### How to Ask Cursor

```
You: "Create a daily data quality check script for payments_hf.checkout_customer_actuals.
It should:
1. Check row count matches yesterday
2. Find NULL values in key columns (customer_id, business_unit, checkout_date)
3. Detect duplicate customer_ids
4. Validate date ranges
5. Export results to CSV
6. Create a summary report"
```

### What Cursor Will Do

```python
# Cursor generates this automatically:
from databricks_api import DatabricksAPI
from datetime import datetime, timedelta
import csv

db = DatabricksAPI()

# 1. Check row count
today_count = db.run_sql(
    "SELECT COUNT(*) as cnt FROM payments_hf.checkout_customer_actuals",
    display=False
)[0][0]

# 2. Find NULLs
nulls = db.run_sql("""
    SELECT 
        COUNT(*) FILTER (WHERE customer_id IS NULL) as null_customer_id,
        COUNT(*) FILTER (WHERE business_unit IS NULL) as null_business_unit,
        COUNT(*) FILTER (WHERE checkout_date IS NULL) as null_checkout_date
    FROM payments_hf.checkout_customer_actuals
""", display=False)

# 3. Find duplicates
duplicates = db.find_duplicates(
    "payments_hf.checkout_customer_actuals",
    key_column="customer_id",
    limit=100
)

# 4. Validate dates
date_range = db.run_sql("""
    SELECT 
        MIN(checkout_date) as min_date,
        MAX(checkout_date) as max_date,
        COUNT(DISTINCT checkout_date) as distinct_dates
    FROM payments_hf.checkout_customer_actuals
""", display=False)

# 5. Export and report
# ... Cursor generates complete solution
```

### Time Saved
- **Manual**: 45 minutes
- **With Cursor**: 5 minutes
- **Savings**: 89%

---

## 🔍 Scenario 2: Investigate Data Anomaly

### What You Need
Investigate why a metric dropped suddenly.

### How to Ask Cursor

```
You: "Investigate why duplicate customer detection rate dropped 20% yesterday.
Compare yesterday vs. last week:
1. Query duplicate_customers for both periods
2. Break down by business unit and match reason
3. Check if specific match types decreased
4. Identify which business units are affected
5. Create a diagnostic notebook"
```

### What Cursor Will Do

```python
# Cursor creates investigation script:
from databricks_api import DatabricksAPI
from datetime import datetime, timedelta

db = DatabricksAPI()

yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
last_week_start = (datetime.now() - timedelta(days=8)).strftime('%Y-%m-%d')
last_week_end = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')

# Compare periods
yesterday_data = db.run_sql(f"""
    SELECT 
        business_unit,
        match_reasons,
        COUNT(*) as count
    FROM payments_hf.duplicate_customers
    WHERE subscription_date_local = '{yesterday}'
    GROUP BY business_unit, match_reasons
""")

last_week_data = db.run_sql(f"""
    SELECT 
        business_unit,
        match_reasons,
        COUNT(*) as count
    FROM payments_hf.duplicate_customers
    WHERE subscription_date_local BETWEEN '{last_week_start}' AND '{last_week_end}'
    GROUP BY business_unit, match_reasons
""")

# Analysis and comparison
# ... Cursor generates complete analysis
```

### Time Saved
- **Manual**: 2 hours
- **With Cursor**: 15 minutes
- **Savings**: 87%

---

## 📈 Scenario 3: Create Weekly Report

### What You Need
Automated weekly fraud analysis report.

### How to Ask Cursor

```
You: "Create a weekly fraud analysis report that:
1. Queries duplicate_customers for the last 7 days
2. Groups by business unit, match reason, and day
3. Calculates fraud rates and trends
4. Compares with previous week
5. Creates a Databricks notebook with visualizations
6. Schedules it to run every Monday at 8 AM
7. Exports summary to CSV"
```

### What Cursor Will Do

```python
# Cursor creates complete solution:
from databricks_api import DatabricksAPI, notebook

db = DatabricksAPI()

# Generate notebook content
notebook_content = """
# Databricks notebook source
# MAGIC %md
# MAGIC # Weekly Fraud Analysis Report
# MAGIC 
# MAGIC Generated: {date}

# COMMAND ----------

# MAGIC %sql
# MAGIC WITH current_week AS (
# MAGIC   SELECT 
# MAGIC     business_unit,
# MAGIC     match_reasons,
# MAGIC     subscription_date_local,
# MAGIC     COUNT(*) as duplicate_count
# MAGIC   FROM payments_hf.duplicate_customers
# MAGIC   WHERE subscription_date_local >= CURRENT_DATE - INTERVAL 7 DAYS
# MAGIC   GROUP BY business_unit, match_reasons, subscription_date_local
# MAGIC ),
# MAGIC previous_week AS (
# MAGIC   SELECT 
# MAGIC     business_unit,
# MAGIC     match_reasons,
# MAGIC     COUNT(*) as duplicate_count
# MAGIC   FROM payments_hf.duplicate_customers
# MAGIC   WHERE subscription_date_local BETWEEN CURRENT_DATE - INTERVAL 14 DAYS 
# MAGIC     AND CURRENT_DATE - INTERVAL 8 DAYS
# MAGIC   GROUP BY business_unit, match_reasons
# MAGIC )
# MAGIC SELECT 
# MAGIC   cw.business_unit,
# MAGIC   cw.match_reasons,
# MAGIC   SUM(cw.duplicate_count) as current_week_count,
# MAGIC   SUM(pw.duplicate_count) as previous_week_count,
# MAGIC   (SUM(cw.duplicate_count) - SUM(pw.duplicate_count)) / SUM(pw.duplicate_count) * 100 as change_pct
# MAGIC FROM current_week cw
# MAGIC LEFT JOIN previous_week pw ON cw.business_unit = pw.business_unit 
# MAGIC   AND cw.match_reasons = pw.match_reasons
# MAGIC GROUP BY cw.business_unit, cw.match_reasons
# MAGIC ORDER BY current_week_count DESC

# COMMAND ----------

# Visualization code
# ... Cursor generates complete notebook
"""

# Create and schedule job
job = notebook(
    "/Workspace/reports/weekly_fraud_analysis",
    notebook_content,
    "Weekly Fraud Analysis Report",
    schedule="0 8 * * 1"  # Every Monday at 8 AM
)
```

### Time Saved
- **Manual**: 4 hours
- **With Cursor**: 20 minutes
- **Savings**: 92%

---

## 🔧 Scenario 4: Debug Production Issue

### What You Need
Debug why a job is failing.

### How to Ask Cursor

```
You: "Job 12345 is failing. Help me debug:
1. Get the job output and error logs
2. Check what table it's querying
3. Verify the table exists and has data
4. Test the query manually
5. Identify the issue and suggest a fix"
```

### What Cursor Will Do

```python
# Cursor creates debugging script:
from databricks_api import DatabricksAPI

db = DatabricksAPI()

# 1. Get job output
job_output = db.get_job_output(run_id=12345)
print("Job Output:", job_output)

# 2. Check job details
job_details = db.get_job_status(run_id=12345)
print("Job Details:", job_details)

# 3. Analyze error
# Cursor reads the error and suggests fixes

# 4. Test query
# Cursor extracts the query and tests it

# 5. Suggest fix
# Cursor provides solution
```

### Time Saved
- **Manual**: 1 hour
- **With Cursor**: 10 minutes
- **Savings**: 83%

---

## 📋 Scenario 5: Build New Feature

### What You Need
Build a new analysis feature.

### How to Ask Cursor

```
You: "Create a new feature to analyze cross-brand duplicate detection:
1. Query graph_customers_with_match_reasons for cross-brand matches
2. Analyze which attributes match across brands
3. Calculate cross-brand match rates by business unit
4. Create a notebook with the analysis
5. Add it to the projects/adhoc/ directory
6. Document how to use it"
```

### What Cursor Will Do

```python
# Cursor creates complete feature:
# 1. Creates projects/adhoc/analyze_cross_brand_duplicates.py
# 2. Uses existing patterns from repository
# 3. Implements all requested functionality
# 4. Adds documentation
# 5. Follows repository structure rules
```

### Time Saved
- **Manual**: 3 hours
- **With Cursor**: 30 minutes
- **Savings**: 83%

---

## 🎯 Key Takeaways

### Pattern Recognition

Notice the pattern? For every task:

1. **Describe what you want** (not how to do it)
2. **Cursor uses the toolkit** automatically
3. **Cursor generates complete solution**
4. **You review and refine**

### Productivity Multiplier

- **10x faster** for simple tasks
- **5x faster** for complex workflows
- **Better quality** (uses tested utilities)
- **Consistent** (follows repository patterns)

### The Secret

**Stop coding. Start describing.**

Cursor + Your Toolkit = Supercharged Productivity

---

## 🚀 Next Steps

1. **Try one scenario** from above
2. **Adapt it** to your needs
3. **Ask Cursor** to refine it
4. **Save it** as a template
5. **Reuse** for similar tasks

**Remember**: The more you use Cursor with your toolkit, the better it gets at understanding your patterns and preferences!

