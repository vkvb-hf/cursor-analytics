# Comprehensive QA Review - Post Spider Revamp Notebook

**Review Date**: 2025-01-21  
**Reviewer**: Technical QA Analysis  
**Notebook**: `[PY-3368] post-spider revamp`

---

## 🔴 CRITICAL ISSUES

### 1. **Step Numbering Inconsistency** (Line 677)
**Issue**: Print statement says "Step 4" but it's actually Step 2
```python
print("\n🔄 Step 4: Processing spider data after max CSV date...")
```
**Impact**: Confusing for debugging and execution tracking
**Fix**: Change to `Step 2` or `Step 3` (depending on whether CSV normalization is Step 1 or 2)

### 2. **Date Type Comparison Issue** (Line 689)
**Issue**: Comparing timestamp with string using `>` operator
```python
.filter(F.col("subscribed_at_local") > F.to_timestamp(F.lit(max_csv_date_str)))
```
**Problem**: 
- `max_csv_date_str` is a string from CSV (line 667)
- `subscribed_at_local` is a timestamp column
- String comparison may not work correctly if `max_csv_date_str` format doesn't match

**Impact**: May filter out valid records or include invalid ones
**Fix**: 
```python
max_csv_date_ts = F.to_timestamp(F.lit(max_csv_date_str))
spider_df = (
    spark.table("payments_hf.checkout_customer_details_spider")
    .filter(F.col("subscribed_at_local") > max_csv_date_ts)
    .select(columns)
)
```

### 3. **Missing Variable: `csv_count`** (Line 911)
**Issue**: Variable `csv_count` is referenced but never defined
```python
output_lines.append(f"📅 CSV customers: {csv_count:,}")
```
**Impact**: Will cause `NameError` when writing summary
**Fix**: Add after line 611:
```python
csv_count = csv_customer_identifiers.select("src").distinct().count()
```

### 4. **Duplicate `count_connections` Calculation** (Lines 780-783, 829-830)
**Issue**: `count_connections` is calculated twice
```python
# First calculation (line 780-783)
combined_customer_identifiers = combined_customer_identifiers.withColumn(
    "count_connections",
    F.count("*").over(window_spec_identifier)
)

# Second calculation (line 829-830) - OVERWRITES the first!
.withColumn(
    "count_connections",
    F.count("*").over(Window.partitionBy(*identifier_key_array))
)
```
**Impact**: First calculation is wasted, second overwrites it. Both use same logic but different variable names.
**Fix**: Remove the first calculation (lines 777-783) since the second one is more explicit.

### 5. **Window Function Ordering Mismatch with Original** (Lines 797-807)
**Issue**: Using `created_at_ts` for ordering, but original notebook uses `subscribed_at_local`
**Original Logic**:
```python
window_spec = (
    Window.partitionBy(*identifier_key_array)
    .orderBy("subscribed_at_local")  # <-- Uses subscribed_at_local
    .rowsBetween(Window.unboundedPreceding, -1)
)
```
**Current Logic**:
```python
window_spec = (
    Window.partitionBy(*identifier_key_array)
    .orderBy("created_at_ts")  # <-- Uses created_at_ts
    .rowsBetween(Window.unboundedPreceding, -1)
)
```
**Impact**: 
- Parent relationships may be calculated incorrectly
- CSV data uses `created_at` (from vertices), Spider uses `created_at` (from AttributeProcessor)
- Both should map to `subscribed_at_local` for consistency
- **CRITICAL**: This could cause wrong parent assignments!

**Fix**: Use `subscribed_at_local` for ordering (it's already available in both datasets):
```python
window_spec = (
    Window.partitionBy(*identifier_key_array)
    .orderBy("subscribed_at_local")  # Use subscribed_at_local directly
    .rowsBetween(Window.unboundedPreceding, -1)
)
window_spec_bu = (
    Window.partitionBy(*(["business_unit"] + identifier_key_array))
    .orderBy("subscribed_at_local")  # Use subscribed_at_local directly
    .rowsBetween(Window.unboundedPreceding, -1)
)
# Remove created_at_ts conversion entirely
```

---

## 🟡 HIGH PRIORITY ISSUES

### 6. **Union Column Mismatch Risk** (Line 757)
**Issue**: Using `unionByName` with `allowMissingColumns=True` but columns may have different types
**Risk**: 
- CSV: `created_at` is string, `customer_id` is bigint
- Spider: `created_at` is string, `customer_id` may be different type
- If types don't match exactly, union may fail or coerce incorrectly

**Impact**: Runtime errors or data corruption
**Fix**: Explicitly cast all columns to same types before union:
```python
# Ensure consistent types
csv_customer_identifiers = csv_customer_identifiers.select(
    F.col("business_unit").cast("string"),
    F.col("customer_id").cast("bigint"),
    F.col("customer_uuid").cast("string"),
    F.col("created_at").cast("string"),
    F.col("subscribed_at_local").cast("timestamp"),
    F.col("src").cast("string"),
    F.col("dst").cast("string"),
    F.col("identifier_source").cast("string")
)

spider_customer_identifiers = spider_customer_identifiers.select(
    F.col("business_unit").cast("string"),
    F.col("customer_id").cast("bigint"),
    F.col("customer_uuid").cast("string"),
    F.col("created_at").cast("string"),
    F.col("subscribed_at_local").cast("timestamp"),
    F.col("src").cast("string"),
    F.col("dst").cast("string"),
    F.col("identifier_source").cast("string")
)
```

### 7. **Customer ID Type Inconsistency** (Line 546)
**Issue**: Casting `customer_id` to `bigint` but it may contain non-numeric values
**Risk**: If CSV `customer_id` contains non-numeric strings, cast will fail or produce NULLs
**Impact**: Join with customer table will fail for those records
**Fix**: Add error handling or validation:
```python
csv_customer_identifiers = csv_customer_identifiers.withColumn(
    "customer_id",
    F.when(
        F.col("customer_id").rlike("^[0-9]+$"),  # Only numeric
        F.col("customer_id").cast("bigint")
    ).otherwise(F.lit(None))
)
```

### 8. **Null Handling in `created_at` Coalesce** (Line 791-794)
**Issue**: Coalesce may not handle all null cases correctly
```python
combined_customer_identifiers = combined_customer_identifiers.withColumn(
    "created_at_ts",
    F.coalesce(
        F.to_timestamp(F.col("created_at")),
        F.col("created_at")  # If created_at is already timestamp, this is redundant
    )
)
```
**Problem**: If `created_at` is already a timestamp, `F.to_timestamp()` may fail
**Fix**: Use `subscribed_at_local` directly (it's already a timestamp) or handle nulls properly:
```python
# Since we're removing created_at_ts anyway (per fix #5), this becomes moot
# But if we keep it, use:
combined_customer_identifiers = combined_customer_identifiers.withColumn(
    "created_at_ts",
    F.coalesce(
        F.to_timestamp(F.col("created_at"), "yyyy-MM-dd'T'HH:mm:ss.SSS"),
        F.to_timestamp(F.col("created_at"), "yyyy-MM-dd HH:mm:ss"),
        F.col("subscribed_at_local")  # Fallback to subscribed_at_local
    )
)
```

### 9. **Self-Reference Nullification Logic** (Lines 834-846)
**Issue**: Using `self_id_col` which is `business_unit_customer_id` format, but `src` is `customer:{business_unit}_{customer_uuid}`
**Problem**: 
- `self_id_col = F.concat(F.col("business_unit"), F.lit("_"), F.col("customer_id"))` creates `"US_12345"`
- `direct_parent_in_business_unit` also uses same format: `"US_12345"`
- But `src` is `"customer:US_abc-123-def"` (normalized format)
- **This is CORRECT** - parent IDs use `business_unit_customer_id` format, not `src` format
- **VERIFICATION NEEDED**: Confirm that `direct_parent_in_business_unit` and `direct_parent` use `business_unit_customer_id` format, not `src` format

**Impact**: Self-reference nullification should work correctly IF parent columns use `business_unit_customer_id` format
**Fix**: Verify this is correct by checking original notebook logic

### 10. **Customer Features Extraction** (Lines 1005-1013)
**Issue**: Extracting customer features from `customer_identifiers` table, but this may not have all customer records
**Problem**: 
- `customer_identifiers` only contains customers who have identifiers
- Customers without any identifiers won't appear
- But `graph_customers` needs ALL customers, even those without identifiers

**Impact**: Some customers may be missing from `graph_customers`
**Fix**: Need to get customer features from source tables (CSV vertices + Spider table), not just customer_identifiers:
```python
# Get customer features from CSV vertices
csv_customer_features = (
    vertices_df
    .filter(F.col("~label") == "customer")
    .select(
        F.split(F.col("~id"), "_", 2)[0].alias("business_unit"),
        F.split(F.col("~id"), "_", 2)[1].cast("bigint").alias("customer_id"),
        F.to_timestamp(F.col("created_at")).alias("subscribed_at_local")
    )
    .distinct()
)

# Get customer features from Spider (for dates after max_csv_date)
spider_customer_features = (
    spark.table("payments_hf.checkout_customer_details_spider")
    .filter(F.col("subscribed_at_local") > max_csv_date_ts)
    .select("business_unit", "customer_id", "subscribed_at_local")
    .distinct()
)

# Union both
customer_features_df = csv_customer_features.unionByName(spider_customer_features)
```

---

## 🟠 MEDIUM PRIORITY ISSUES

### 11. **Missing Error Handling for Empty CSV Files** (Lines 491-508)
**Issue**: No check if CSV files are empty
**Impact**: Will fail with unclear error messages
**Fix**: Add validation:
```python
vertices_count = vertices_df.count()
edges_count = csv_edges_df.count()

if vertices_count == 0:
    raise ValueError(f"No vertices found in {save_path}/vertices")
if edges_count == 0:
    raise ValueError(f"No edges found in {save_path}/edges")

print(f"✅ Read {vertices_count:,} vertices and {edges_count:,} edges")
```

### 12. **Missing Validation for Customer UUID Join** (Line 564-568)
**Issue**: No check on join success rate
**Impact**: May silently fail to normalize many records
**Fix**: Already has logging (lines 605-609), but could add warning threshold:
```python
normalized_pct = (normalized_count / total_count) * 100
if normalized_pct < 90:
    print(f"⚠️  WARNING: Only {normalized_pct:.1f}% of records normalized. Expected >90%")
```

### 13. **Date Boundary Condition** (Line 689)
**Issue**: Using `>` instead of `>=` for date filter
**Question**: Should records with `subscribed_at_local == max_csv_date_str` be included in Spider or CSV?
**Impact**: Boundary records may be duplicated or missed
**Fix**: Clarify requirement - typically should use `>` to avoid duplicates, but verify with business logic

### 14. **GraphFrames Dependency** (Line 940)
**Issue**: Installing `graphframes` in notebook cell, but may not be available on cluster
**Impact**: Will fail if cluster doesn't have graphframes
**Fix**: Add to cluster libraries or document requirement

### 15. **Connected Components Filter** (Line 951)
**Issue**: Filtering `count_connections > 1` before creating graph
**Impact**: This is correct - only identifiers with multiple connections form edges
**Verification**: This matches original notebook logic ✅

---

## 🔵 LOW PRIORITY / OPTIMIZATION ISSUES

### 16. **Redundant Table Refresh** (Lines 552, 679-680, 1001)
**Issue**: Multiple `REFRESH TABLE` calls for same tables
**Impact**: Minor performance impact
**Fix**: Refresh once at the beginning

### 17. **Inefficient Customer Features Extraction** (Line 1005-1013)
**Issue**: Using `distinct()` on large dataset
**Impact**: Performance - could use aggregation instead
**Fix**: Use `groupBy().agg(F.min("subscribed_at_local"))` instead of `distinct()`

### 18. **Missing Index on Output Tables**
**Issue**: No optimization hints for downstream queries
**Impact**: Query performance on large tables
**Fix**: Consider partitioning by `business_unit` or `created_at` date

### 19. **DBFS Output Path** (Line 917)
**Issue**: Using timestamp in filename, but may want to keep latest
**Impact**: Multiple output files accumulate
**Fix**: Consider overwriting single file or cleaning up old files

---

## ✅ VERIFICATION CHECKLIST

### Data Flow Verification
- [x] CSV edges → customer_identifiers format conversion
- [x] CSV src normalization (business_unit_customer_id → customer:business_unit_customer_uuid)
- [x] Spider data processing through AttributeProcessor
- [x] Union of CSV and Spider data
- [x] Relationship calculations on combined data
- [x] Connected components creation
- [x] Graph customers creation
- [x] Match reasons calculation

### Schema Verification
- [ ] CSV and Spider have matching column types before union
- [ ] Final table schema matches original `customer_identifiers` table
- [ ] All required columns present in final output

### Logic Verification
- [ ] Parent relationship calculation matches original notebook
- [ ] Self-reference nullification works correctly
- [ ] Count connections calculation is correct
- [ ] Date filtering logic is correct (boundary conditions)

### Downstream Impact
- [ ] `connected_components_20251121` will work with downstream queries
- [ ] `graph_customers_20251121` has all required columns
- [ ] `graph_customers_with_match_reasons_20251121` logic matches original

---

## 📋 RECOMMENDED FIXES (Priority Order)

1. **CRITICAL**: Fix window function ordering to use `subscribed_at_local` (Issue #5)
2. **CRITICAL**: Fix date comparison logic (Issue #2)
3. **CRITICAL**: Fix missing `csv_count` variable (Issue #3)
4. **HIGH**: Add type casting before union (Issue #6)
5. **HIGH**: Fix customer features extraction (Issue #10)
6. **MEDIUM**: Add error handling for empty CSVs (Issue #11)
7. **MEDIUM**: Fix step numbering (Issue #1)
8. **LOW**: Remove duplicate count_connections calculation (Issue #4)

---

## 🎯 TESTING RECOMMENDATIONS

1. **Unit Tests**:
   - Test CSV normalization with sample data
   - Test Spider processing with sample data
   - Test union with mismatched schemas
   - Test window function calculations with known data

2. **Integration Tests**:
   - Run on small date range and verify output
   - Compare output with original notebook for same date range
   - Verify parent relationships are correct
   - Verify count_connections matches expected values

3. **Data Quality Checks**:
   - Verify no duplicate customers in graph_customers
   - Verify all customers from CSV appear in output
   - Verify all customers from Spider (after max date) appear in output
   - Verify parent relationships are valid (parent exists in dataset)

---

## 📝 NOTES

- The refactoring correctly separates raw data extraction from relationship calculations
- The approach of combining CSV and Spider first, then calculating relationships is sound
- The customer_uuid mapping fix (bigint cast) should improve join success rate
- Need to verify that parent relationship format (`business_unit_customer_id`) is consistent throughout






