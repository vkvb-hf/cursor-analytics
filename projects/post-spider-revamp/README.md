# Post-Spider-Revamp Project

This project creates a customer identifiers graph table from S3 CSV files (Neptune format) instead of processing raw checkout data.

## Overview

The notebook reads edges and vertices CSV files from S3 (created by the Neptune Backfill process) and converts them back to the `customer_identifiers` table format used by the graph duplicate detection system.

## Files

- **`graph_duplicate_detection_from_s3.py`**: Main notebook that reads CSV files from S3 and creates the customer_identifiers table
- **`NOTEBOOKS_ANALYSIS.md`**: Detailed analysis of the source notebooks

## Purpose

This project was created to:
1. Use pre-processed graph data from S3 (Neptune format) instead of raw checkout data
2. Convert Neptune format (edges/vertices CSV) back to customer_identifiers table format
3. Create a new table `payments_hf.customer_identifiers_20251121` with the processed data

## Data Flow

```
S3 CSV Files (Neptune format)
  ├── edges/ (CSV files with ~from, ~to, ~label)
  └── vertices/ (CSV files with ~id, ~label, created_at)
  ↓
Transform to customer_identifiers format
  ↓
payments_hf.customer_identifiers_20251121 (table)
```

## Input Data

### Source S3 Path
```
s3://hf-payments-data-lake-live-main/voucher_abuse/neptune_backfill/20250305
```

### Edges CSV Format
- `~id`: Unique edge ID
- `~from`: Customer node (e.g., "US_12345")
- `~to`: Identifier node (e.g., "email:john@example.com")
- `~label`: Identifier source (e.g., "email", "phone", "card")

### Vertices CSV Format
- `~id`: Vertex ID
- `~label`: Vertex type ("customer" or "identifier")
- `created_at`: Creation timestamp (for customer vertices)
- `checkout_success`: Boolean flag (for customer vertices)

## Output

### Table: `payments_hf.customer_identifiers_20251121`

**Schema:**
- `business_unit`: Business unit code (extracted from customer node)
- `customer_id`: Customer ID (extracted from customer node)
- `customer_uuid`: Customer UUID (NULL, not available in CSV)
- `created_at`: Creation timestamp
- `subscribed_at_local`: Subscription timestamp (uses created_at)
- `src`: Customer node ID
- `dst`: Identifier node ID
- `identifier_source`: Source of identifier
- `has_direct_parent_in_business_unit`: Boolean flag
- `direct_parent_in_business_unit`: Parent customer ID (within business unit)
- `has_direct_parent`: Boolean flag
- `direct_parent`: Parent customer ID (across all business units)
- `count_connections`: Number of customers sharing this identifier

## Usage

### Run in Databricks

1. Upload the notebook to Databricks workspace
2. Set the S3 path if different from default
3. Run all cells

### Configuration

Edit these variables in the notebook:

```python
# S3 path containing edges and vertices CSV files
save_path = "s3://hf-payments-data-lake-live-main/voucher_abuse/neptune_backfill/20250305"

# Output table name
output_table = "payments_hf.customer_identifiers_20251121"
```

## Key Transformations

1. **Column Renaming**: Convert Neptune format to customer_identifiers format
   - `~from` → `src`
   - `~to` → `dst`
   - `~label` → `identifier_source`

2. **Customer Node Parsing**: Extract business_unit and customer_id
   - Format: "business_unit_customer_id" (e.g., "US_12345")
   - Split on underscore to extract components

3. **Timestamp Handling**: Join with vertices to get `created_at`

4. **Parent Relationships**: Calculate using window functions
   - `direct_parent_in_business_unit`: First customer in same business unit
   - `direct_parent`: First customer across all business units

5. **Connection Counting**: Count customers sharing each identifier

## Differences from Original Notebook

| Aspect | Original (Graph Duplicate Detection) | This Project |
|--------|--------------------------------------|--------------|
| **Input** | `payments_hf.checkout_customer_details_bob` | S3 CSV files (edges/vertices) |
| **Processing** | Pre-process with AttributeProcessor | Read pre-processed data |
| **Output Table** | `payments_hf.customer_identifiers` | `payments_hf.customer_identifiers_20251121` |
| **Data Format** | Raw checkout data | Neptune graph format |

## Limitations

1. **Missing customer_uuid**: Not available in CSV files, set to NULL
2. **Limited metadata**: Some columns may not be available from CSV files
3. **Timestamp precision**: Uses `created_at` from vertices, may not match original `subscribed_at_local`

## Verification

The notebook includes verification steps:
- Table schema check
- Row counts by business unit
- Identifier sources distribution
- Connections distribution
- Sample data display

## Related Notebooks

- **(Clone:20251121) Neptune Backfill Data**: Creates the S3 CSV files
- **(Clone:20251121) Graph Duplicate Detection Notebook**: Original notebook that processes raw checkout data

See `NOTEBOOKS_ANALYSIS.md` for detailed analysis of these notebooks.






