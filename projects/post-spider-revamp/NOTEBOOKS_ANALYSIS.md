# Notebooks Analysis: Neptune Backfill & Graph Duplicate Detection

## Overview

This document explains the two notebooks that form the basis for the post-spider-revamp project:
1. **(Clone:20251121) Neptune Backfill Data** - Writes graph data to S3 for Neptune bulk load
2. **(Clone:20251121) Graph Duplicate Detection Notebook** - Processes checkout data to create customer identifier graph

## Notebook 1: Neptune Backfill Data

### Purpose
Converts the `payments_hf.customer_identifiers` table into Neptune graph format (edges and vertices) and writes to S3 for bulk loading into Neptune database.

### Data Flow
```
payments_hf.customer_identifiers (table)
  ↓
Transform to Neptune format
  ↓
Write to S3: s3://hf-payments-data-lake-live-main/voucher_abuse/neptune_backfill/20250305/
  ├── edges/ (CSV files)
  └── vertices/ (CSV files)
```

### Input Schema (customer_identifiers table)
- `src`: Customer node ID (e.g., "US_12345")
- `dst`: Identifier node ID (e.g., "email:john@example.com")
- `identifier_source`: Source of identifier (e.g., "email", "phone", "card")
- `created_at`: Timestamp

### Output Schema

#### Edges CSV (`edges/`)
- `~id`: Unique edge ID (concatenation of label, from, to)
- `~from`: Source node (customer)
- `~to`: Target node (identifier)
- `~label`: Edge label (identifier_source)

#### Vertices CSV (`vertices/`)
- `~id`: Vertex ID
- `~label`: Vertex type ("customer" or "identifier")
- `created_at`: Creation timestamp (only for customer vertices)
- `checkout_success`: Boolean flag (only for customer vertices)

### Key Operations
1. **Read from table**: `spark.table("payments_hf.customer_identifiers")`
2. **Rename columns** to Neptune format (`src` → `~from`, `dst` → `~to`, etc.)
3. **Create edge IDs**: Concatenate label, from, to
4. **Filter invalid data**: Remove rows containing quotes
5. **Create vertices**: Extract unique customer and identifier nodes
6. **Write to S3**: Partitioned CSV files for bulk load

### Sample Data Structure
```python
# Edges example
~id,~from,~to,~label
email_123_email:john@example.com,US_12345,email:john@example.com,email

# Vertices example
~id,~label,created_at,checkout_success
US_12345,customer,2025-02-05T12:51:03.000+00:00,True
email:john@example.com,identifier,,
```

---

## Notebook 2: Graph Duplicate Detection Notebook

### Purpose
Processes raw checkout customer details to create a graph-based duplicate detection system. Extracts identifiers from customer data, builds edges between customers and identifiers, and identifies duplicate customers through graph analysis.

### Data Flow
```
payments_hf.checkout_customer_details_bob (table)
  ↓
Pre-process with AttributeProcessor (clean & normalize)
  ↓
Extract identifiers (email, phone, card, etc.)
  ↓
Create edges: customer → identifier
  ↓
payments_hf.customer_identifiers (table)
  ↓
Build graph & find connected components
  ↓
payments_hf.graph_customers (table)
```

### Input Schema (checkout_customer_details_bob)
- `customer_uuid`: Unique customer UUID
- `business_unit`: Business unit code (US, DE, etc.)
- `customer_id`: Customer ID
- `subscribed_at_local`: Subscription timestamp
- `first_name`, `last_name`: Name fields
- `phone`: Phone number
- `postcode`: Postal code
- `address`: Address
- `account_email`, `shopper_email`: Email addresses
- `card_first_6`, `card_last_2`: Card information
- `ip`: IP address

### Processing Steps

#### Step 1: Raw Data to Identifiers (`raw_to_identifiers()`)
1. **Read checkout data**: From `checkout_customer_details_bob` and `checkout_customer_details_spider` (split by date: 2025-05-25)
2. **Join with business_units**: Get country, language info
3. **Pre-process with AttributeProcessor**: 
   - Clean and normalize all fields
   - Extract identifiers (email, phone, card, address, etc.)
   - Generate customer node ID
4. **Create attribute nodes**: Explode identifiers array
5. **Calculate parent relationships**: Using window functions to find direct parents
6. **Create edges**: customer_node (src) → identifier (dst)
7. **Save to table**: `payments_hf.customer_identifiers`

#### Step 2: Identifiers to Connected Components (`identifiers_to_components()`)
1. **Filter edges**: Only keep identifiers with `count_connections > 1`
2. **Create graph**: Using GraphFrames library
3. **Find connected components**: Groups of connected customers/identifiers
4. **Save**: `payments_hf.connected_components`

#### Step 3: Connected Components to Customers (`components_to_customers()`)
1. **Join components with customer identifiers**
2. **Aggregate by customer**: Get component, parent relationships
3. **Calculate cluster metrics**: 
   - `nth_in_cluster`: Order within cluster
   - `cluster_size`: Total customers in cluster
   - `root_in_cluster`: First customer in cluster
   - `is_duplicate_in_business_unit`: Flag for duplicates
4. **Save**: `payments_hf.graph_customers`

#### Step 4: Components to Clusters (`components_to_clusters()`)
1. **Generate digraph strings**: For visualization
2. **Save**: `payments_hf.graph_clusters`

### Output Schema (customer_identifiers table)
- `src`: Customer node (e.g., "US_12345")
- `dst`: Identifier node (e.g., "email:john@example.com")
- `identifier_source`: Source type (e.g., "email", "phone", "card")
- `business_unit`: Business unit code
- `customer_id`: Customer ID
- `customer_uuid`: Customer UUID
- `created_at`: Creation timestamp
- `subscribed_at_local`: Subscription timestamp
- `has_direct_parent_in_business_unit`: Boolean
- `direct_parent_in_business_unit`: Parent customer ID
- `has_direct_parent`: Boolean
- `direct_parent`: Parent customer ID
- `count_connections`: Number of customers sharing this identifier

### Key Dependencies
- `voucher_fraud.preprocessor.preprocessor.AttributeProcessor`: Pre-processing library
- `graphframes`: Graph analysis library
- `payments_hf.business_units`: Business unit metadata

---

## Relationship Between Notebooks

```
Graph Duplicate Detection Notebook
  ↓ (creates)
payments_hf.customer_identifiers (table)
  ↓ (reads from)
Neptune Backfill Data Notebook
  ↓ (writes to)
S3 CSV files (edges/vertices)
  ↓ (bulk loads to)
Neptune Database
```

## Key Differences

| Aspect | Graph Duplicate Detection | Neptune Backfill |
|--------|---------------------------|------------------|
| **Input** | Raw checkout data (tables) | Processed customer_identifiers table |
| **Output** | customer_identifiers table | S3 CSV files (Neptune format) |
| **Purpose** | Create graph from raw data | Export graph to Neptune |
| **Format** | Spark DataFrame/Delta table | CSV files with Neptune format |
| **Columns** | Standard column names | Neptune format (~from, ~to, ~label) |

---

## Post-Spider-Revamp Requirements

The new notebook should:
1. **Read from S3 CSV files** instead of `checkout_customer_details_bob`
2. **Convert Neptune format back** to customer_identifiers format
3. **Create table**: `payments_hf.customer_identifiers_20251121`

### Data Transformation Needed

From Neptune edges CSV:
- `~from` → `src`
- `~to` → `dst`  
- `~label` → `identifier_source`

Additional columns needed (from vertices or derived):
- `business_unit`: Extract from customer node (e.g., "US_12345" → "US")
- `customer_id`: Extract from customer node (e.g., "US_12345" → "12345")
- `created_at`: From vertices CSV
- `subscribed_at_local`: May need to derive or join with other data
- `customer_uuid`: May need to join with original data
- `count_connections`: Calculate from edges
- Parent relationship fields: Calculate using window functions

### Challenges
1. **Missing metadata**: CSV files may not have all columns from original table
2. **Customer node parsing**: Need to extract business_unit and customer_id from node ID
3. **Timestamp handling**: May need to join with original checkout data for full timestamps
4. **Parent relationships**: Need to recalculate using window functions






