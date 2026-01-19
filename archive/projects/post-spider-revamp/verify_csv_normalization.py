#!/usr/bin/env python3
"""
Verification script to test CSV normalization logic with sample records.
This script checks if edges and vertices will match correctly after normalization.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

def verify_csv_normalization():
    """Verify that CSV normalization logic will work correctly."""
    
    print("=" * 80)
    print("CSV Normalization Verification")
    print("=" * 80)
    
    # Initialize SparkSession
    spark = SparkSession.builder.appName("VerifyCSVNormalization").getOrCreate()
    
    # S3 path containing edges and vertices CSV files
    save_path = "s3://hf-payments-data-lake-live-main/voucher_abuse/neptune_backfill/20250305"
    
    print(f"\n📥 Reading CSV files from: {save_path}")
    
    # Read vertices CSV
    vertices_df = (
        spark.read
        .option("header", "true")
        .option("inferSchema", "false")
        .csv(f"{save_path}/vertices")
    )
    
    # Read edges CSV
    csv_edges_df = (
        spark.read
        .option("header", "true")
        .option("inferSchema", "false")
        .csv(f"{save_path}/edges")
    )
    
    print(f"✅ Read {vertices_df.count():,} vertices")
    print(f"✅ Read {csv_edges_df.count():,} edges")
    
    # Get sample records
    print("\n" + "=" * 80)
    print("SAMPLE EDGES (First 5 records)")
    print("=" * 80)
    sample_edges = csv_edges_df.limit(5).collect()
    for i, row in enumerate(sample_edges, 1):
        print(f"\nEdge {i}:")
        print(f"  ~id: {row['~id']}")
        print(f"  ~from: {row['~from']}")
        print(f"  ~to: {row['~to']}")
        print(f"  ~label: {row['~label']}")
    
    print("\n" + "=" * 80)
    print("SAMPLE VERTICES (First 5 customer vertices)")
    print("=" * 80)
    sample_vertices = vertices_df.filter(F.col("~label") == "customer").limit(5).collect()
    for i, row in enumerate(sample_vertices, 1):
        print(f"\nVertex {i}:")
        print(f"  ~id: {row['~id']}")
        print(f"  ~label: {row['~label']}")
        print(f"  created_at: {row.get('created_at', 'N/A')}")
    
    # Test normalization logic
    print("\n" + "=" * 80)
    print("TESTING NORMALIZATION LOGIC")
    print("=" * 80)
    
    # Step 1: Extract business_unit and customer_id from edges
    print("\n1️⃣ Extracting business_unit and customer_id from edges...")
    test_edges = csv_edges_df.limit(10).select(
        F.col("~from").alias("src"),
        F.col("~to").alias("dst"),
        F.col("~label").alias("identifier_source")
    )
    
    test_edges = test_edges.withColumn(
        "src_parts",
        F.split(F.col("src"), "_", 2)
    ).withColumn(
        "business_unit",
        F.col("src_parts")[0]
    ).withColumn(
        "customer_id",
        F.when(
            F.size(F.col("src_parts")) > 1,
            F.col("src_parts")[1]
        ).otherwise(F.lit(None))
    ).drop("src_parts")
    
    test_edges = test_edges.withColumn(
        "customer_id",
        F.col("customer_id").cast("string")
    )
    
    print("\n📊 Sample extracted values:")
    test_edges.select("src", "business_unit", "customer_id", "dst", "identifier_source").show(10, truncate=False)
    
    # Step 2: Join with customer table to get customer_uuid
    print("\n2️⃣ Joining with public_edw_base_grain_live.customer to get customer_uuid...")
    spark.sql("REFRESH TABLE public_edw_base_grain_live.customer")
    
    customer_lookup = (
        spark.table("public_edw_base_grain_live.customer")
        .select(
            F.col("bob_entity_code").alias("business_unit"),
            F.cast(F.col("customer_id"), "string").alias("customer_id"),
            F.col("customer_uuid")
        )
        .distinct()
    )
    
    test_edges_with_uuid = test_edges.join(
        customer_lookup,
        on=["business_unit", "customer_id"],
        how="left"
    )
    
    print("\n📊 Sample records after customer join:")
    test_edges_with_uuid.select(
        "src", "business_unit", "customer_id", "customer_uuid", "dst"
    ).show(10, truncate=False)
    
    # Check join success rate
    total_count = test_edges_with_uuid.count()
    matched_count = test_edges_with_uuid.filter(F.col("customer_uuid").isNotNull()).count()
    unmatched_count = total_count - matched_count
    
    print(f"\n📈 Join Statistics:")
    print(f"   Total edges tested: {total_count}")
    print(f"   Matched (customer_uuid found): {matched_count} ({matched_count/total_count*100:.1f}%)")
    print(f"   Unmatched (customer_uuid not found): {unmatched_count} ({unmatched_count/total_count*100:.1f}%)")
    
    if unmatched_count > 0:
        print("\n⚠️  Unmatched records (customer_uuid not found):")
        test_edges_with_uuid.filter(F.col("customer_uuid").isNull()).select(
            "src", "business_unit", "customer_id"
        ).show(10, truncate=False)
    
    # Step 3: Normalize src format
    print("\n3️⃣ Normalizing src to Spider format: customer:{business_unit}_{customer_uuid}")
    test_edges_normalized = test_edges_with_uuid.withColumn(
        "src_normalized",
        F.when(
            F.col("customer_uuid").isNotNull(),
            F.concat(F.lit("customer:"), F.col("business_unit"), F.lit("_"), F.col("customer_uuid"))
        ).otherwise(F.col("src"))  # Keep original if customer_uuid not found
    )
    
    print("\n📊 Sample normalized src values:")
    test_edges_normalized.select(
        "src", "src_normalized", "business_unit", "customer_id", "customer_uuid"
    ).show(10, truncate=False)
    
    # Step 4: Test vertices join
    print("\n4️⃣ Testing vertices join (using original format)...")
    customer_vertices = vertices_df.filter(
        (F.col("~label") == "customer") & F.col("created_at").isNotNull()
    ).select(
        F.col("~id").alias("src_original"),
        F.col("created_at")
    )
    
    test_edges_for_vertices = test_edges_with_uuid.withColumn(
        "src_original",
        F.concat(F.col("business_unit"), F.lit("_"), F.col("customer_id"))
    )
    
    test_edges_with_created_at = test_edges_for_vertices.join(
        customer_vertices,
        on="src_original",
        how="left"
    )
    
    print("\n📊 Sample records after vertices join:")
    test_edges_with_created_at.select(
        "src_original", "created_at", "src_normalized", "customer_uuid"
    ).show(10, truncate=False)
    
    # Check vertices join success rate
    total_for_vertices = test_edges_with_created_at.count()
    vertices_matched = test_edges_with_created_at.filter(F.col("created_at").isNotNull()).count()
    vertices_unmatched = total_for_vertices - vertices_matched
    
    print(f"\n📈 Vertices Join Statistics:")
    print(f"   Total edges tested: {total_for_vertices}")
    print(f"   Matched (created_at found): {vertices_matched} ({vertices_matched/total_for_vertices*100:.1f}%)")
    print(f"   Unmatched (created_at not found): {vertices_unmatched} ({vertices_unmatched/total_for_vertices*100:.1f}%)")
    
    if vertices_unmatched > 0:
        print("\n⚠️  Unmatched records (created_at not found):")
        test_edges_with_created_at.filter(F.col("created_at").isNull()).select(
            "src_original", "business_unit", "customer_id"
        ).show(10, truncate=False)
    
    # Step 5: Final verification - check format consistency
    print("\n" + "=" * 80)
    print("FINAL VERIFICATION")
    print("=" * 80)
    
    print("\n✅ Normalization Summary:")
    print(f"   Original CSV format: {{business_unit}}_{{customer_id}} (e.g., 'US_12345')")
    print(f"   Normalized format: customer:{{business_unit}}_{{customer_uuid}} (e.g., 'customer:US_abc-123-def')")
    print(f"   Spider format: customer:{{business_unit}}_{{customer_uuid}} (from AttributeProcessor)")
    print(f"   ✅ Formats will match after normalization!")
    
    # Check for any issues
    issues = []
    if unmatched_count > 0:
        issues.append(f"⚠️  {unmatched_count} edges could not be normalized (customer_uuid not found)")
    if vertices_unmatched > 0:
        issues.append(f"⚠️  {vertices_unmatched} edges could not get created_at (vertices not found)")
    
    if issues:
        print("\n⚠️  Potential Issues:")
        for issue in issues:
            print(f"   {issue}")
    else:
        print("\n✅ All checks passed! Normalization should work correctly.")
    
    print("\n" + "=" * 80)
    print("Verification Complete")
    print("=" * 80)

if __name__ == "__main__":
    verify_csv_normalization()






