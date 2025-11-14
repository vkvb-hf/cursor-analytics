# AI Dataset Exploration Guidelines

This document provides comprehensive guidelines for AI models on how to systematically explore datasets and answer questions from prompts using SQL queries.

## Overview

When answering questions about datasets, follow a structured, iterative approach. **Never assume** - always verify your understanding through careful exploration and validation.

---

## Phase 1: Initial Data Exploration

### Step 1: Check Sample Records

**Objective:** Get a first-hand view of the actual data structure and content.

**Actions:**
1. Retrieve a small sample of records (typically 5-10 rows) from the table
2. Examine the actual data values, not just the schema
3. Identify:
   - Data format and types (dates, strings, numbers)
   - Nullable fields and their patterns
   - Value ranges and realistic examples
   - Relationships between columns

**Example Query:**
```sql
SELECT * FROM schema.table_name LIMIT 10;
```

**Key Questions to Answer:**
- What does a typical record look like?
- Are there any obvious data quality issues?
- What are realistic values for each column?
- How are missing values represented?

### Step 2: Understand the Schema

**Objective:** Comprehensively understand the table structure, data types, and constraints.

**Actions:**
1. Describe the table schema to see column names, types, and comments
2. Check table properties and metadata (location, format, partitioning)
3. Review any available documentation or table comments
4. Identify:
   - Primary keys or unique identifiers
   - Foreign key relationships
   - Partition columns
   - Column data types and constraints

**Example Queries:**
```sql
-- Get column details
DESCRIBE EXTENDED schema.table_name;

-- Alternative: Describe table
DESC schema.table_name;

-- Get table properties
SHOW TABLE EXTENDED IN schema LIKE 'table_name';

-- Check partitions (if applicable)
SHOW PARTITIONS schema.table_name;
```

**Key Questions to Answer:**
- What columns exist and what are their types?
- Are there any constraints or relationships?
- Is the table partitioned? If so, by what columns?
- Are there indexes or special properties?

### Step 3: Understand Data Volume and Distribution

**Objective:** Understand the scale and distribution of data before writing complex queries.

**Actions:**
1. Count total rows to understand data volume
2. Check date ranges if time-series data exists
3. Examine value distributions in key categorical columns
4. Identify any data gaps or anomalies

**Example Queries:**
```sql
-- Row count
SELECT COUNT(*) as total_rows FROM schema.table_name;

-- Date range (if applicable)
SELECT 
    MIN(date_column) as min_date,
    MAX(date_column) as max_date,
    COUNT(DISTINCT date_column) as distinct_dates
FROM schema.table_name;

-- Distribution of categorical values
SELECT 
    category_column,
    COUNT(*) as count,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM schema.table_name) as percentage
FROM schema.table_name
GROUP BY category_column
ORDER BY count DESC
LIMIT 20;
```

**Key Questions to Answer:**
- How many records are in the table?
- What is the time range of the data?
- How is data distributed across categories/values?

---

## Phase 2: Understanding the Question

### Step 1: Parse and Decompose the Question

**Objective:** Break down the user's question into clear, actionable components.

**Actions:**
1. Identify the **core question** - what specifically needs to be answered?
2. Identify **key entities** - what tables, columns, or concepts are mentioned?
3. Identify **time constraints** - are there date ranges or time periods?
4. Identify **filters or conditions** - what subset of data is relevant?
5. Identify **aggregation needs** - does the question require counts, sums, averages, etc.?
6. Identify **expected output format** - single value, list, grouped data, comparison?

**Key Questions to Answer:**
- What is the user really asking for?
- What data is needed to answer this?
- What are the implicit assumptions that need validation?

### Step 2: Identify Required Data Elements

**Objective:** Map the question to specific tables, columns, and relationships.

**Actions:**
1. List all tables needed (can expand later if joins required)
2. List all columns needed for filtering, grouping, and output
3. Identify relationships between tables (if multiple tables)
4. Note any business logic or transformations needed

**Document:**
- Required tables: `[table1, table2, ...]`
- Required columns: `[col1, col2, ...]`
- Filters needed: `[condition1, condition2, ...]`
- Aggregations: `[COUNT, SUM, AVG, ...]`

---

## Phase 3: Step-by-Step Execution Method

### ⚠️ CRITICAL RULE: Do NOT Write Multiple Queries Immediately

**Never assume.** Always build queries incrementally and validate each step before proceeding.

### Step 1: Create Initial Exploration Query

**Objective:** Start with the simplest possible query that addresses part of the question.

**Actions:**
1. Write **ONE simple query** to explore a single aspect
2. Focus on **one table** initially (add joins later if needed)
3. Use **LIMIT** clauses to restrict results during exploration
4. Test filters and conditions one at a time

**Example Workflow:**
```sql
-- Step 1.1: Basic filter test (with LIMIT)
SELECT * 
FROM schema.table_name 
WHERE some_condition = 'value'
LIMIT 10;

-- Step 1.2: Check if filter is working correctly
SELECT COUNT(*) 
FROM schema.table_name 
WHERE some_condition = 'value';

-- Step 1.3: Validate filter logic matches question intent
```

### Step 2: Validate Each Step Before Proceeding

**Objective:** Ensure each query component works correctly before adding complexity.

**Actions:**
1. **Run and review** the query results
2. **Verify** the output matches expectations
3. **Check** for any errors or unexpected NULL values
4. **Confirm** row counts are reasonable
5. **Document** findings before moving to next step

**Validation Checklist:**
- [ ] Query executes without errors
- [ ] Row counts are reasonable (not 0, not unexpectedly large)
- [ ] Results match the logical intent
- [ ] No unexpected NULL values in key columns
- [ ] Data types are handled correctly

### Step 3: Iteratively Add Complexity

**Objective:** Build up the query step by step, validating at each stage.

**Methodology:**
1. **Start simple** - Basic SELECT with minimal filters
2. **Add one filter at a time** - Test each filter independently
3. **Add aggregations gradually** - Test GROUP BY, then aggregations
4. **Add joins later** - Only after understanding individual tables
5. **Refine and optimize** - Remove unnecessary complexity

**Example Progression:**
```sql
-- Stage 1: Basic exploration
SELECT column1, column2 
FROM table1 
LIMIT 10;

-- Stage 2: Add filter (test separately)
SELECT COUNT(*) 
FROM table1 
WHERE date_column >= '2024-01-01';

-- Stage 3: Add grouping (test separately)
SELECT category, COUNT(*) 
FROM table1 
WHERE date_column >= '2024-01-01'
GROUP BY category;

-- Stage 4: Add joins only if needed (understand each table first)
SELECT t1.column1, t2.column2 
FROM table1 t1
JOIN table2 t2 ON t1.id = t2.id
WHERE t1.date_column >= '2024-01-01'
LIMIT 10;

-- Stage 5: Final aggregation
SELECT category, COUNT(*) as count, SUM(amount) as total
FROM table1 t1
JOIN table2 t2 ON t1.id = t2.id
WHERE t1.date_column >= '2024-01-01'
GROUP BY category;
```

### Step 4: Handle Edge Cases and Data Quality

**Objective:** Ensure the query handles real-world data issues correctly.

**Actions:**
1. Check for NULL values in key columns
2. Verify date/time handling (timezones, formats)
3. Check for duplicate records if uniqueness matters
4. Validate filter conditions handle NULLs appropriately
5. Test boundary conditions

**Example Checks:**
```sql
-- Check for NULLs in critical columns
SELECT COUNT(*) as null_count
FROM table_name
WHERE critical_column IS NULL;

-- Verify date format consistency
SELECT DISTINCT date_format(date_column, 'yyyy-MM-dd') as date_str
FROM table_name
LIMIT 20;

-- Check for duplicates (if relevant)
SELECT 
    key_column, 
    COUNT(*) as count
FROM table_name
GROUP BY key_column
HAVING COUNT(*) > 1;
```

---

## Phase 4: Iterative Refinement

### Step 1: Run Initial Query

**Objective:** Get first results and assess if they answer the question.

**Actions:**
1. Execute the query with reasonable limits
2. Review the output format and values
3. Assess if the results look correct logically
4. Note any surprises or unexpected results

### Step 2: Refine Based on Results

**Objective:** Adjust the query based on what the data reveals.

**Actions:**
1. If results are empty → Check filters, might be too restrictive
2. If results are too large → Add appropriate filters
3. If values seem wrong → Verify filters and joins
4. If structure is wrong → Review GROUP BY, aggregations

**Common Refinements:**
- Adjusting date ranges
- Adding or removing filters
- Correcting join conditions
- Fixing aggregation logic
- Handling NULL values appropriately

### Step 3: Validate Against Business Logic

**Objective:** Ensure results make sense from a business perspective.

**Actions:**
1. Compare results to known benchmarks or expectations
2. Check for reasonable value ranges
3. Verify calculated metrics (percentages, averages) are logical
4. Validate relationships between aggregated values

---

## Phase 5: Validation and Verification

### Step 1: Revisit the Original Question

**Objective:** Confirm the query truly answers what was asked.

**Actions:**
1. **Read the original question again** carefully
2. **Map each part of the question** to query components:
   - Does the SELECT match what was asked?
   - Do the filters match the conditions?
   - Does the aggregation match the metric requested?
   - Does the output format match expectations?

**Validation Checklist:**
- [ ] Question: `[restate the question]`
- [ ] Query addresses: `[list what the query addresses]`
- [ ] Gaps identified: `[list any gaps if present]`
- [ ] Matches question intent: `[Yes/No with explanation]`

### Step 2: Test Query Output

**Objective:** Verify the SQL query produces valid, meaningful results.

**Actions:**
1. **Run the full query** (remove LIMIT if needed for final answer)
2. **Review output structure** - columns, rows, format
3. **Spot-check values** - manually verify a few rows
4. **Check for errors** - NULLs, type mismatches, calculation errors

**Example Validation Queries:**
```sql
-- Final query (with appropriate LIMIT for exploration)
SELECT ...
FROM ...
WHERE ...
GROUP BY ...
ORDER BY ...
LIMIT 100;

-- Validation: Check summary statistics
SELECT 
    COUNT(*) as total_rows,
    COUNT(DISTINCT key_column) as distinct_keys,
    MIN(numeric_column) as min_val,
    MAX(numeric_column) as max_val,
    AVG(numeric_column) as avg_val
FROM (final_query) subquery;
```

### Step 3: Answer Validation

**Objective:** Confirm the results directly answer the question.

**Actions:**
1. **Extract the specific answer** from results
2. **Format appropriately** (number, list, table, etc.)
3. **Provide context** if needed (time period, filters applied)
4. **Highlight any caveats** or limitations

**Answer Format:**
- Direct answer to the question
- Relevant context (date range, filters, etc.)
- Any assumptions made
- Any data quality issues encountered
- Confidence level in the answer

---

## Phase 6: Documentation and Communication

### Step 1: Document Your Approach

**Objective:** Leave a clear trail of how the answer was derived.

**Actions:**
1. Document the exploration steps taken
2. Record key findings from each phase
3. Note any assumptions or limitations
4. Save the final query for reference

### Step 2: Present the Answer

**Objective:** Clearly communicate the answer with appropriate context.

**Format:**
1. **Direct Answer** - The specific answer to the question
2. **Methodology** - Brief summary of approach
3. **Key Findings** - Important discoveries during exploration
4. **SQL Query** - The final query used
5. **Limitations** - Any data quality issues or assumptions

---

## Common Pitfalls to Avoid

### ❌ DON'T:
1. **Assume without verifying** - Always check sample data first
2. **Write complex queries immediately** - Build incrementally
3. **Skip validation steps** - Each step needs verification
4. **Ignore NULL values** - They can significantly impact results
5. **Use wrong data types** - Date/time handling is critical
6. **Forget to check data volume** - Large tables need careful filtering
7. **Ignore business context** - Results must make logical sense

### ✅ DO:
1. **Start with samples** - Always look at actual data first
2. **Understand schema thoroughly** - Know columns, types, constraints
3. **Build queries incrementally** - One step at a time
4. **Validate at each stage** - Verify before adding complexity
5. **Check edge cases** - NULLs, boundaries, duplicates
6. **Revisit the question** - Ensure you're answering what was asked
7. **Test final results** - Spot-check and logical validation

---

## Example Workflow: Complete Scenario

**Question:** "How many chargebacks occurred in the last 30 days for US customers?"

### Phase 1: Initial Exploration
```sql
-- Step 1: Sample records
SELECT * FROM chargebacks_table LIMIT 10;

-- Step 2: Schema understanding
DESCRIBE EXTENDED chargebacks_table;

-- Step 3: Data volume and range
SELECT COUNT(*) FROM chargebacks_table;
SELECT MIN(chargeback_date), MAX(chargeback_date) FROM chargebacks_table;
SELECT DISTINCT country FROM chargebacks_table LIMIT 20;
```

### Phase 2: Understanding the Question
- **Core question:** Count of chargebacks
- **Time constraint:** Last 30 days
- **Filter:** US customers only
- **Entities:** chargebacks_table, date column, country column

### Phase 3: Step-by-Step Execution
```sql
-- Step 1: Test date filter (last 30 days)
SELECT COUNT(*) 
FROM chargebacks_table 
WHERE chargeback_date >= CURRENT_DATE - INTERVAL 30 DAYS;

-- Step 2: Test country filter separately
SELECT COUNT(*) 
FROM chargebacks_table 
WHERE country = 'US';

-- Step 3: Combine filters
SELECT COUNT(*) 
FROM chargebacks_table 
WHERE chargeback_date >= CURRENT_DATE - INTERVAL 30 DAYS
  AND country = 'US';

-- Step 4: Verify with sample
SELECT * 
FROM chargebacks_table 
WHERE chargeback_date >= CURRENT_DATE - INTERVAL 30 DAYS
  AND country = 'US'
LIMIT 10;

-- Step 5: Final query with validation
SELECT 
    COUNT(*) as chargeback_count,
    MIN(chargeback_date) as earliest_date,
    MAX(chargeback_date) as latest_date
FROM chargebacks_table 
WHERE chargeback_date >= CURRENT_DATE - INTERVAL 30 DAYS
  AND country = 'US';
```

### Phase 4: Iterative Refinement
- Check if date column format is correct
- Verify country values are stored as 'US' (not 'USA', 'United States', etc.)
- Validate date range covers exactly 30 days

### Phase 5: Validation
- Re-read question: ✓ Count chargebacks ✓ Last 30 days ✓ US customers
- Test output: ✓ Returns a count ✓ Date range verified ✓ Country filter correct
- Business logic check: ✓ Count seems reasonable ✓ Dates are recent

### Phase 6: Present Answer
**Answer:** "There were X chargebacks in the last 30 days for US customers (from [date] to [date])."

---

## Summary Checklist

Before providing an answer, ensure you have:

- [ ] ✅ Checked sample records from the table
- [ ] ✅ Understood the schema (columns, types, constraints)
- [ ] ✅ Understood the question thoroughly (all components parsed)
- [ ] ✅ Created a step-by-step execution plan
- [ ] ✅ Built queries incrementally (not all at once)
- [ ] ✅ Validated each step before proceeding
- [ ] ✅ Iterated and refined based on results
- [ ] ✅ Revisited the original question
- [ ] ✅ Validated the SQL query gives the correct answer
- [ ] ✅ Checked for edge cases and data quality issues
- [ ] ✅ Verified results make business sense

---

**Remember:** Quality over speed. Taking time to explore systematically will lead to accurate, reliable answers.

