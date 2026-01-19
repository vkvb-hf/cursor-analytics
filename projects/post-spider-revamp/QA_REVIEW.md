# Critical QA Review: [PY-3368] post-spider revamp Notebook

## Executive Summary

**Status**: ❌ **NOT READY FOR PRODUCTION** - Multiple critical issues identified

This document provides a cell-by-cell technical review with focus on:
1. Correctness of implementation
2. Downstream impacts
3. Data consistency issues
4. Edge cases and error handling

---

## 🔴 CRITICAL ISSUES

### Issue #1: **src Format Mismatch Between CSV and Spider Data**

**Location**: Steps 3-4 (CSV transformation) and Step 2 (Spider processing)

**Problem**:
- **CSV data**: `src` format is `{business_unit}_{customer_id}` (e.g., `"US_12345"`)
  - This comes from the original `customer_identifiers` table where `src` was stored as `{business_unit}_{customer_id}`
- **Spider data**: `src` format is `customer:{business_unit}_{customer_uuid}` (e.g., `"customer:US_abc-123-def"`)
  - This comes from `AttributeProcessor.CUSTOMER_NODE` which formats as `"customer:{business_unit}_{customer_uuid}"`

**Impact**: 
- ❌ **CRITICAL**: When combining CSV and spider data, the `src` values won't match
- ❌ Connected components will fail because nodes with same customer but different formats won't connect
- ❌ Graph analysis will be incorrect - customers will appear as separate nodes
- ❌ Downstream tables (`connected_components`, `graph_customers`) will have incorrect data

**Evidence**:
```python
# CSV: Line 700-712
csv_edges_transformed = base_csv_edges_df.withColumn(
    "src_parts",
    F.split(F.col("src"), "_", 2)  # Expects format: "US_12345"
)

# Spider: Line 663
F.col("customer_node").alias("src")  # Format: "customer:US_abc-123-def"
```

**Fix Required**:
1. Normalize spider `src` to match CSV format: `{business_unit}_{customer_id}`
2. OR normalize CSV `src` to match spider format (but this breaks compatibility with existing data)
3. **Recommended**: Normalize spider data to CSV format since CSV is the historical baseline

---

### Issue #2: **Date Type Mismatch in Comparisons**

**Location**: Step 1 (max_csv_date calculation) and Step 2 (spider filter)

**Problem**:
- `max_csv_date` is extracted as a **string** from CSV (line 512)
- `subscribed_at_local` in spider table is likely a **timestamp/date type**
- Comparison `F.col("subscribed_at_local") > max_csv_date` may fail or give incorrect results

**Impact**:
- ⚠️ **HIGH**: May filter out valid spider records or include invalid ones
- ⚠️ Date boundary logic may be incorrect
- ⚠️ Could cause data loss or duplication

**Evidence**:
```python
# Line 512: max_csv_date is a string
max_csv_date = max_date_result['max_created_at']  # String from CSV

# Line 560: Comparing timestamp with string
.filter(F.col("subscribed_at_local") > max_csv_date)
```

**Fix Required**:
1. Cast `max_csv_date` to timestamp: `F.to_timestamp(F.lit(max_csv_date))`
2. OR cast `subscribed_at_local` to string and compare
3. Ensure consistent timezone handling

---

### Issue #3: **Parent Relationship Recalculation Logic**

**Location**: Step 5 (Recalculate parent relationships)

**Problem**:
1. **CSV data already has parent relationships** from original processing, but we're recalculating
2. **Spider data has parent relationships** calculated during processing (lines 627-653)
3. **We're recalculating on combined data** (lines 790-810), which is correct BUT:
   - We're using `created_at` for ordering, but CSV and spider may have different timestamp formats
   - The window functions may not correctly identify the "first" customer across the combined dataset

**Impact**:
- ⚠️ **MEDIUM**: Parent relationships may be incorrect for customers near the CSV/spider boundary
- ⚠️ Customers who were parents in CSV might not be parents in combined dataset
- ⚠️ Downstream `graph_customers` table will have incorrect parent references

**Evidence**:
```python
# Line 778: Ordering by created_at
.orderBy("created_at")

# But created_at format may differ:
# CSV: String from vertices CSV
# Spider: ISO string from AttributeProcessor
```

**Fix Required**:
1. Ensure `created_at` is consistently formatted (timestamp type)
2. Verify parent relationships are correctly calculated across the boundary
3. Add validation to check parent relationships are logical

---

### Issue #4: **count_connections Double Calculation**

**Location**: Step 2 (Spider processing) and Step 5 (Recalculation)

**Problem**:
1. Spider data calculates `count_connections` during processing (line 649-653)
2. We recalculate `count_connections` on combined data (line 768-771)
3. But the spider `count_connections` is calculated **only on spider data**, not the full combined dataset

**Impact**:
- ⚠️ **MEDIUM**: `count_connections` in spider data is incorrect (only counts spider customers)
- ⚠️ After recalculation, spider edges get correct count, but this is inefficient
- ⚠️ The initial spider `count_connections` is misleading

**Evidence**:
```python
# Line 649-653: Calculate on spider data only
.withColumn(
    "count_connections",
    F.approxCountDistinct("customer_node").over(
        Window.partitionBy(*identifier_key_array)  # Only spider data
    ),
)

# Line 768-771: Recalculate on combined data
combined_df = combined_df.withColumn(
    "count_connections",
    F.count("*").over(window_spec_identifier)  # Combined data
)
```

**Fix Required**:
1. Remove `count_connections` calculation from spider processing (it will be recalculated anyway)
2. OR document that initial calculation is temporary and will be overwritten

---

### Issue #5: **Customer Features Extraction Logic**

**Location**: Step 8 (Create graph_customers)

**Problem**:
1. We extract CSV customer features by filtering `created_at <= max_csv_date` (line 1094)
2. But spider data in `customer_identifiers_20251121` also has `created_at` (from spider processing)
3. The filter `created_at <= max_csv_date` will **exclude spider data** from customer features
4. But then we separately get spider customer features from `checkout_customer_details_spider`

**Impact**:
- ⚠️ **MEDIUM**: Logic is correct but confusing
- ⚠️ We're reading spider customer features from source table instead of using data we already processed
- ⚠️ If spider data processing failed partially, we might miss customer features

**Evidence**:
```python
# Line 1091-1101: Filter CSV data
csv_customer_features = (
    customer_identifiers_df
    .filter(F.col("created_at").isNotNull())
    .filter(F.col("created_at") <= max_csv_date)  # Only CSV
    ...
)

# Line 1108-1117: Get spider from source table
spider_customer_features = (
    spark.table("payments_hf.checkout_customer_details_spider")
    .filter(F.col("subscribed_at_local") > max_csv_date)
    ...
)
```

**Fix Required**:
1. Extract spider customer features from `customer_identifiers_20251121` where `created_at > max_csv_date`
2. This ensures consistency and uses data we already processed
3. Only fall back to source table if needed

---

### Issue #6: **Missing customer_uuid in CSV Data**

**Location**: Step 3 (CSV transformation)

**Problem**:
- CSV data doesn't have `customer_uuid` (line 730: set to `None`)
- Spider data has `customer_uuid` (line 660)
- When combining, we have inconsistent data

**Impact**:
- ⚠️ **LOW**: Schema is consistent (NULL is allowed), but downstream queries expecting `customer_uuid` may fail
- ⚠️ If downstream logic relies on `customer_uuid`, CSV customers will be excluded

**Fix Required**:
1. Document that `customer_uuid` is NULL for CSV data
2. Ensure downstream logic handles NULL `customer_uuid`

---

### Issue #7: **Vertices Join May Fail**

**Location**: Step 3 (CSV transformation, line 722-726)

**Problem**:
- We join CSV edges with vertices to get `created_at` (line 722-726)
- Join key is `src` (customer node)
- But if `src` format in edges doesn't match `~id` format in vertices, join will fail

**Impact**:
- ❌ **HIGH**: If join fails, CSV edges will have NULL `created_at`
- ❌ Parent relationships won't work correctly (ordered by NULL)
- ❌ Date filtering will exclude all CSV data

**Evidence**:
```python
# Line 715-720: Vertices have ~id
customer_vertices_for_join = vertices_df.filter(
    F.col("~label") == "customer"
).select(
    F.col("~id").alias("src"),  # ~id from vertices
    F.col("created_at")
)

# Line 722-726: Join on src
csv_edges_with_timestamp = csv_edges_transformed.join(
    customer_vertices_for_join,
    on="src",  # Must match exactly
    how="left"
)
```

**Fix Required**:
1. Verify `~id` in vertices matches `src` in edges (should be same format: `{business_unit}_{customer_id}`)
2. Add validation to check join success rate
3. Handle NULL `created_at` gracefully

---

## 🟡 MEDIUM PRIORITY ISSUES

### Issue #8: **No Error Handling for Empty CSV Files**

**Location**: Step 1 (Read CSV files)

**Problem**:
- No check if CSV files are empty
- No check if `max_csv_date` is NULL
- Will cause downstream failures

**Fix Required**:
- Add validation for empty dataframes
- Handle NULL `max_csv_date` case

---

### Issue #9: **Inconsistent Column Ordering**

**Location**: Throughout notebook

**Problem**:
- CSV and spider data may have columns in different order
- `unionByName` handles this, but it's inefficient

**Fix Required**:
- Ensure consistent column ordering before union

---

### Issue #10: **Missing Validation Queries**

**Location**: Verification section

**Problem**:
- Verification queries don't check for:
  - NULL `created_at` in final table
  - Mismatched `src` formats
  - Orphaned edges (no matching vertices)
  - Duplicate edges

**Fix Required**:
- Add comprehensive validation queries

---

## 🟢 LOW PRIORITY ISSUES

### Issue #11: **Performance Optimization**

- Reading CSV files multiple times (vertices read twice)
- Could cache intermediate DataFrames
- Window functions could be optimized

---

### Issue #12: **Documentation**

- Missing comments explaining why we recalculate metrics
- Missing explanation of data format differences
- Missing troubleshooting guide

---

## 📋 RECOMMENDED FIXES (Priority Order)

1. **🔴 CRITICAL**: Fix `src` format mismatch (Issue #1)
2. **🔴 CRITICAL**: Fix date type comparison (Issue #2)
3. **🔴 CRITICAL**: Verify vertices join works (Issue #7)
4. **🟡 MEDIUM**: Fix parent relationship recalculation (Issue #3)
5. **🟡 MEDIUM**: Fix customer features extraction (Issue #5)
6. **🟡 MEDIUM**: Remove redundant count_connections calculation (Issue #4)
7. **🟡 MEDIUM**: Add error handling (Issue #8)
8. **🟢 LOW**: Add validation queries (Issue #10)
9. **🟢 LOW**: Performance optimization (Issue #11)

---

## 🧪 TESTING RECOMMENDATIONS

1. **Unit Tests**:
   - Test CSV edge transformation with sample data
   - Test spider data processing with sample data
   - Test date comparison logic
   - Test parent relationship calculation

2. **Integration Tests**:
   - Test full pipeline with small CSV + spider dataset
   - Verify connected components work correctly
   - Verify graph_customers has correct parent relationships
   - Verify match_reasons are correct

3. **Validation Tests**:
   - Compare row counts: CSV edges + spider edges = final table edges
   - Verify no NULL `created_at` in final table
   - Verify `src` format is consistent
   - Verify date ranges are correct
   - Verify parent relationships are logical (parent `created_at` <= child `created_at`)

---

## 📊 DOWNSTREAM IMPACT ANALYSIS

### Tables Created:
1. `customer_identifiers_20251121` - **AFFECTED BY ALL ISSUES**
2. `connected_components_20251121` - **AFFECTED BY Issue #1** (src format mismatch)
3. `graph_customers_20251121` - **AFFECTED BY Issues #1, #3, #5**
4. `graph_customers_with_match_reasons_20251121` - **AFFECTED BY ALL ABOVE**

### Downstream Consumers:
- Any queries using these tables will have incorrect data
- Graph analysis will be wrong
- Duplicate detection will fail
- Match reasons will be incorrect

---

## ✅ CONCLUSION

**The notebook is NOT ready for production** due to critical issues, especially:
1. `src` format mismatch will break graph connectivity
2. Date type mismatch may cause data loss
3. Parent relationships may be incorrect

**Recommendation**: Fix all critical issues before running in production.






