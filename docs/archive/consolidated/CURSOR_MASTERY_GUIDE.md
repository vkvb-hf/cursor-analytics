# Cursor Mastery Guide: Maximizing Your Databricks Workflow

**Purpose**: Learn how to use Cursor IDE's AI capabilities to dramatically improve your Databricks workflow and productivity.

## 🎯 Core Philosophy

**Cursor + Databricks Toolkit = Supercharged Productivity**

Instead of writing everything yourself, **ask Cursor to do it** using the toolkit we've built. The AI understands your repository structure and can use all the utilities automatically.

---

## 🚀 Quick Start: The Cursor Way

### Instead of Writing Code, Ask Cursor

**❌ Old Way** (Manual):
```python
# You write everything yourself
from databricks import sql
# ... lots of code ...
```

**✅ Cursor Way** (AI-Assisted):
```
You: "Run a SQL query to get the last 7 days of payment data from payments_hf.f_pvs_replica"
Cursor: [Uses databricks_api automatically]
```

---

## 💡 How to Use Cursor Effectively

### 1. **Use Cursor Chat for Everything**

Cursor Chat understands your repository. You can ask it to:

#### Run SQL Queries
```
You: "Query the payments_hf.f_pvs_replica table for transactions from the last week"

Cursor will:
1. Use databricks_api.sql()
2. Write the query
3. Execute it
4. Show you results
```

#### Inspect Tables
```
You: "Show me the schema and sample data from payments_hf.duplicate_customers"

Cursor will:
1. Use databricks_api.inspect()
2. Get schema, stats, and samples
3. Display formatted results
```

#### Create Notebooks
```
You: "Create a Databricks notebook that analyzes payment fraud trends and run it as a job"

Cursor will:
1. Generate notebook content
2. Use databricks_api.notebook()
3. Create and run the job
4. Show you the job ID
```

### 2. **Leverage Cursor's Code Completion**

When you type in Cursor, it suggests code using your toolkit:

```python
# Start typing:
from databricks_api import 
# Cursor suggests: sql, inspect, notebook, DatabricksAPI

db = DatabricksAPI()
db.
# Cursor suggests: run_sql, inspect_table, find_duplicates, etc.
```

### 3. **Use Cursor's Multi-File Editing**

Ask Cursor to work across multiple files:

```
You: "Create a new analysis script that:
1. Queries the duplicate_customers table
2. Finds large clusters (>100 customers)
3. Exports results to CSV
4. Creates a notebook with the analysis"

Cursor will:
- Create the script in projects/adhoc/
- Use multiple utilities from the toolkit
- Generate complete working code
```

---

## 🎓 Common Workflows: Cursor-Powered

### Workflow 1: Data Exploration

**Traditional Way** (30+ minutes):
1. Write SQL query
2. Test in Databricks UI
3. Copy results
4. Analyze in Python
5. Create visualizations

**Cursor Way** (5 minutes):
```
You: "Explore the duplicate_customers table. Show me:
- Schema and row count
- Sample of 20 rows
- Distribution of cluster sizes
- Top 10 largest clusters"

Cursor will:
1. Use inspect_table() for schema
2. Use run_sql() for analysis queries
3. Format and display results
4. Create a summary
```

### Workflow 2: Creating Analysis Notebooks

**Traditional Way** (1+ hour):
1. Write notebook code manually
2. Test in Databricks UI
3. Debug issues
4. Schedule as job

**Cursor Way** (10 minutes):
```
You: "Create a Databricks notebook that:
- Analyzes payment fraud patterns
- Groups by business unit and date
- Shows trends over time
- Exports results to a table
Then run it as a job called 'Fraud Analysis Daily'"

Cursor will:
1. Generate complete notebook code
2. Use databricks_api.notebook()
3. Create and run the job
4. Provide job status
```

### Workflow 3: Data Quality Checks

**Traditional Way** (Manual):
```python
# You write all the checks yourself
```

**Cursor Way**:
```
You: "Check data quality for payments_hf.checkout_customer_actuals:
- Find duplicate customer_ids
- Check for NULL values in key columns
- Verify date ranges
- Compare row counts with source table"

Cursor will:
1. Use find_duplicates()
2. Use run_sql() for NULL checks
3. Use inspect_table() for stats
4. Generate a quality report
```

---

## 🧠 Advanced Cursor Techniques

### 1. **Context-Aware Requests**

Cursor understands your repository. Reference existing code:

```
You: "Use the same pattern as investigate_large_clusters.py but analyze 
payment fraud instead of cluster sizes"

Cursor will:
- Read the existing file
- Understand the pattern
- Adapt it for your new use case
- Place it in the correct directory (projects/adhoc/)
```

### 2. **Iterative Refinement**

Start simple, then refine:

```
You: "Query the duplicate_customers table"
→ Cursor runs query

You: "Now filter for only US business unit"
→ Cursor modifies and re-runs

You: "Add a breakdown by match reason"
→ Cursor adds GROUP BY and re-runs

You: "Export this to CSV"
→ Cursor uses the toolkit to export
```

### 3. **Multi-Step Workflows**

Ask Cursor to do complex workflows:

```
You: "Create a complete analysis workflow:
1. Query duplicate_customers for clusters > 100
2. For each cluster, get customer details
3. Analyze matching attributes
4. Create a summary notebook
5. Run it as a scheduled job"

Cursor will:
- Break it into steps
- Use appropriate utilities
- Create all necessary files
- Execute the workflow
```

### 4. **Error Handling and Debugging**

When something fails, ask Cursor:

```
You: "This query failed with error X. Fix it and explain what was wrong"

Cursor will:
- Analyze the error
- Fix the issue
- Explain the problem
- Re-run the query
```

---

## 📋 Cursor Commands Cheat Sheet

### Quick SQL Operations

```
"Run this SQL query: [paste query]"
"Query [table] for [condition]"
"Show me [columns] from [table] where [condition]"
"Count rows in [table]"
"Get sample data from [table]"
```

### Table Inspection

```
"Inspect [table]"
"Show schema for [table]"
"Get stats for [table]"
"Find duplicates in [table] by [column]"
"Check data quality for [table]"
```

### Notebook Operations

```
"Create a notebook that [does X]"
"Run [notebook] as a job"
"Check status of job [job_id]"
"Get output from job [run_id]"
```

### Analysis Tasks

```
"Analyze [table] for [pattern]"
"Compare [table1] with [table2]"
"Find [anomalies/trends/patterns] in [table]"
"Create a report for [metric]"
```

---

## 🎯 Real-World Examples

### Example 1: Daily Fraud Analysis

**What you want**: Daily analysis of payment fraud patterns

**Ask Cursor**:
```
"Create a daily fraud analysis workflow:
1. Query payments_hf.duplicate_customers for today's duplicates
2. Group by business unit and match reason
3. Calculate fraud rates
4. Compare with yesterday's rates
5. Create a notebook with visualizations
6. Schedule it to run daily at 9 AM"
```

**Cursor will**:
- Generate SQL queries
- Create the notebook
- Set up the job schedule
- Provide monitoring instructions

### Example 2: Data Quality Monitoring

**What you want**: Monitor data quality for critical tables

**Ask Cursor**:
```
"Create a data quality monitoring script that:
1. Checks payments_hf.checkout_customer_actuals daily
2. Validates row counts match source
3. Checks for NULL values in key columns
4. Finds duplicate customer_ids
5. Sends alerts if quality drops below threshold
6. Creates a dashboard notebook"
```

**Cursor will**:
- Use TableInspector utilities
- Create validation logic
- Set up alerting
- Generate dashboard

### Example 3: Ad-Hoc Investigation

**What you want**: Investigate a specific issue

**Ask Cursor**:
```
"I need to investigate why cluster US_548 has 67,000 customers.
Create a script that:
1. Gets all customers in that cluster
2. Analyzes matching attributes
3. Checks for shared phone numbers or emails
4. Exports detailed analysis to CSV
5. Creates a summary report"
```

**Cursor will**:
- Use existing investigation scripts as reference
- Create new analysis script
- Place it in projects/adhoc/
- Generate complete solution

---

## 🔥 Pro Tips for Maximum Productivity

### 1. **Use Cursor's Composer**

For complex multi-file tasks:
- Open Cursor Composer
- Describe your complete workflow
- Cursor will create all necessary files
- Uses the toolkit automatically

### 2. **Leverage Cursor's Context**

Cursor sees:
- Your open files
- Your repository structure
- Your recent work
- Your coding patterns

**Use this**:
```
"Use the same pattern as [file you have open]"
"Follow the structure from [existing project]"
"Match the style of [reference file]"
```

### 3. **Ask for Explanations**

When Cursor generates code, ask:
```
"Explain how this works"
"Why did you use this approach?"
"What would happen if [scenario]?"
"How can I optimize this?"
```

### 4. **Iterate with Cursor**

Don't try to get it perfect the first time:
```
1. Ask for basic version
2. Test it
3. Ask for improvements
4. Refine based on results
5. Ask for optimization
```

### 5. **Use Cursor for Documentation**

```
"Document this function"
"Create a README for this project"
"Add docstrings to this file"
"Generate usage examples"
```

---

## 🛠️ Cursor + Toolkit Integration Patterns

### Pattern 1: Quick Query → Analysis → Action

```
Step 1: "Query [table] for [condition]"
Step 2: "Analyze these results for [pattern]"
Step 3: "Create a notebook with this analysis"
Step 4: "Run it as a job"
```

### Pattern 2: Exploration → Validation → Production

```
Step 1: "Explore [table] structure and data"
Step 2: "Validate data quality"
Step 3: "Create production notebook"
Step 4: "Schedule as daily job"
```

### Pattern 3: Investigation → Documentation → Automation

```
Step 1: "Investigate [issue]"
Step 2: "Document findings"
Step 3: "Create automated check"
Step 4: "Add to monitoring"
```

---

## 📚 Learning Path

### Beginner: Start Simple
1. Ask Cursor to run simple SQL queries
2. Use `sql()` function for quick queries
3. Ask Cursor to explain results

### Intermediate: Use the API
1. Ask Cursor to use `DatabricksAPI` class
2. Request table inspections
3. Create simple notebooks

### Advanced: Complex Workflows
1. Ask Cursor to create complete workflows
2. Use multiple utilities together
3. Build production-ready solutions

### Expert: Custom Solutions
1. Ask Cursor to extend the toolkit
2. Create new utilities
3. Build reusable patterns

---

## 🎨 Best Practices

### ✅ DO

- **Ask Cursor first** before writing code manually
- **Use natural language** - describe what you want, not how to do it
- **Iterate** - start simple, then refine
- **Reference existing code** - "use the same pattern as X"
- **Ask for explanations** - understand what Cursor creates
- **Use Cursor's suggestions** - accept helpful completions

### ❌ DON'T

- Don't write code manually if Cursor can do it
- Don't ignore Cursor's suggestions without considering them
- Don't ask for everything at once - break it into steps
- Don't forget to validate - test what Cursor creates
- Don't skip documentation - ask Cursor to document

---

## 🚀 Quick Reference: What to Ask Cursor

### For SQL Queries
- "Query [table] for [condition]"
- "Show me [columns] from [table]"
- "Analyze [metric] by [dimension]"
- "Compare [table1] with [table2]"

### For Table Operations
- "Inspect [table]"
- "Find duplicates in [table]"
- "Check data quality for [table]"
- "Get schema for [table]"

### For Notebooks
- "Create a notebook that [does X]"
- "Run [notebook] as a job"
- "Schedule [notebook] to run daily"

### For Analysis
- "Analyze [pattern] in [table]"
- "Investigate [issue]"
- "Create a report for [metric]"
- "Build a dashboard for [data]"

### For Workflows
- "Create a workflow that [does X, Y, Z]"
- "Automate [process]"
- "Set up monitoring for [metric]"

---

## 💼 Real Productivity Gains

### Time Savings

| Task | Manual | With Cursor | Savings |
|------|--------|-------------|---------|
| Write SQL query | 10 min | 2 min | 80% |
| Create notebook | 30 min | 5 min | 83% |
| Data quality check | 20 min | 3 min | 85% |
| Complete analysis | 2 hours | 15 min | 87% |

### Quality Improvements

- ✅ **Fewer bugs**: Cursor uses tested utilities
- ✅ **Better structure**: Cursor follows repository patterns
- ✅ **Consistent style**: Cursor matches your codebase
- ✅ **Documentation**: Cursor adds docstrings and comments

---

## 🎯 Your Action Plan

### Week 1: Learn the Basics
1. Ask Cursor to run 5 SQL queries
2. Use `sql()` function for quick queries
3. Ask Cursor to inspect 3 tables

### Week 2: Use the API
1. Create 2 notebooks using Cursor
2. Run them as jobs
3. Check job status

### Week 3: Build Workflows
1. Ask Cursor to create a complete analysis workflow
2. Automate a daily task
3. Create a monitoring script

### Week 4: Master Advanced Features
1. Use Cursor Composer for complex tasks
2. Create reusable patterns
3. Extend the toolkit with Cursor's help

---

## 🔗 Integration Points

### Cursor Chat
- Ask questions about your data
- Request code generation
- Get explanations
- Debug issues

### Cursor Composer
- Create multi-file projects
- Build complete workflows
- Generate documentation
- Refactor code

### Cursor Autocomplete
- Get suggestions as you type
- See available functions
- Discover utilities
- Learn patterns

### Cursor Terminal
- Run scripts directly
- Execute commands
- Check results
- Monitor jobs

---

## 📖 Example Conversations with Cursor

### Conversation 1: Quick Analysis

```
You: "I need to analyze payment fraud trends for the last month"

Cursor: "I'll query the duplicate_customers table for the last 30 days and analyze fraud patterns."

[Creates and runs query]

Cursor: "Found 15,234 duplicate customers in the last month. Top match reasons:
1. shopper_email: 45%
2. phone: 30%
3. address_name: 25%

Would you like me to:
- Create a detailed breakdown by business unit?
- Generate a visualization notebook?
- Export results to CSV?"
```

### Conversation 2: Complex Workflow

```
You: "Set up daily monitoring for large customer clusters"

Cursor: "I'll create a monitoring workflow that:
1. Queries for clusters > 100 customers daily
2. Tracks growth trends
3. Alerts if new large clusters appear
4. Generates a weekly report

Creating files:
- projects/adhoc/monitor_large_clusters.py
- projects/adhoc/large_clusters_report.py
- Scheduling as daily job

Done! Job ID: 12345, runs daily at 9 AM."
```

---

## 🎓 Conclusion

**The key to using Cursor effectively**: 

**Stop writing code manually. Start describing what you want.**

Cursor + Your Databricks Toolkit = 10x Productivity

The toolkit provides the building blocks. Cursor assembles them into solutions. You just describe what you need.

---

**Remember**: Cursor understands your repository structure, knows your utilities, and can use them automatically. Trust it to do the heavy lifting!

