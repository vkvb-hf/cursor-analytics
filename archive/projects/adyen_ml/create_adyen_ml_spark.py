#!/usr/bin/env python3
"""
Create payments_hf.adyen_ml_test_data table using PySpark.

This script uses PySpark to efficiently read all CSV files in parallel,
create a DataFrame with custom columns, and write to a Delta table.
Much faster than sequential SQL INSERTs!
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, 
    input_file_name, 
    regexp_extract,
    when,
    lit
)
from pyspark.sql.types import StringType
import sys

# Risk profile mapping
RISK_PROFILE_MAPPING = {
    'THLH73H2VSWDN842': 'Jade1314 CANADA ML',
    'QNN7MK9V6T5T87F3': 'Very_High_ecomm',
    'TBDLJCJZX8LLWWF3': 'Medium_ecomm',
    'J2M3VKGZMHZNZ4Q9': 'Medium',
    'DXPLDK9V6T5T87F3': 'High_ecomm',
    'QLKKNG4S2Q9428Q9': 'Very_High',
    'ZDGX3H4S2Q9428Q9': 'High'
}


def get_workspace_file_paths(spark, workspace_path):
    """
    Get all CSV file paths from Databricks workspace.
    Converts workspace paths to file paths that Spark can read.
    """
    from databricks_workspace import get_csv_files_from_workspace
    from config import DATABRICKS_HOST, TOKEN
    
    # Get list of CSV files from workspace
    csv_files = get_csv_files_from_workspace(workspace_path, DATABRICKS_HOST, TOKEN)
    
    if not csv_files:
        return []
    
    # Convert workspace paths to file:// paths or DBFS paths
    # For Databricks, we need to use /Workspace paths or download to DBFS first
    # Actually, Spark can read from workspace if we use the right path format
    
    # Option 1: Use file paths if files are accessible
    # Option 2: Download to DBFS temp location first, then read
    # For now, let's use workspace file paths directly
    
    print(f"📋 Found {len(csv_files)} CSV files")
    return csv_files


def create_table_with_spark(
    workspace_path: str,
    table_name: str,
    drop_if_exists: bool = False
):
    """
    Create Delta table from CSV files using PySpark.
    """
    print("=" * 80)
    print("Create Table using PySpark (Fast Parallel Processing)")
    print("=" * 80)
    print(f"\n📁 Workspace path: {workspace_path}")
    print(f"🎯 Table name: {table_name}")
    print("=" * 80)
    
    try:
        # Initialize Spark session
        print("\n⚡ Step 1: Initializing Spark session...")
        spark = SparkSession.builder \
            .appName("AdyenMLDataLoad") \
            .config("spark.sql.adaptive.enabled", "true") \
            .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
            .getOrCreate()
        
        print("✅ Spark session created")
        
        # Step 2: Use dbutils to get CSV file paths (Databricks way)
        print("\n📋 Step 2: Getting CSV file paths using dbutils...")
        
        try:
            from pyspark.dbutils import DBUtils
            dbutils = DBUtils(spark)
            
            # List all files in workspace path
            print(f"   Listing files in: {workspace_path}")
            files = dbutils.fs.ls(workspace_path)
            csv_paths = [f.path for f in files if f.name.endswith('.csv')]
            
            if not csv_paths:
                print("❌ No CSV files found!")
                return False
            
            print(f"✅ Found {len(csv_paths)} CSV files")
            
            # Show first few files
            print("\n📄 Sample files:")
            for i, csv_path in enumerate(csv_paths[:5], 1):
                filename = csv_path.split('/')[-1]
                print(f"   [{i}] {filename}")
            if len(csv_paths) > 5:
                print(f"   ... and {len(csv_paths) - 5} more files")
            
            # Step 3: Read all CSV files in parallel with Spark
            print(f"\n📥 Step 3: Reading {len(csv_paths)} CSV files in parallel with Spark...")
            print("   ⚡ Spark will automatically parallelize this operation...")
            
            # Read CSV files - Spark reads them in parallel automatically
            df = spark.read \
                .option("header", "true") \
                .option("inferSchema", "false") \
                .option("comment", "#") \
                .option("multiLine", "false") \
                .option("ignoreLeadingWhiteSpace", "true") \
                .option("ignoreTrailingWhiteSpace", "true") \
                .csv(csv_paths)
            
            row_count = df.count()
            print(f"✅ Successfully read DataFrame")
            print(f"   📊 Total rows: {row_count:,}")
            print(f"   📋 Columns: {len(df.columns)}")
            print(f"   📝 Sample columns: {', '.join(df.columns[:5])}...")
            
        except ImportError:
            # Fallback: Use workspace API if dbutils not available (local execution)
            print("   ⚠️  dbutils not available, using workspace API...")
            from databricks_workspace import get_csv_files_from_workspace
            from csv_to_table import DATABRICKS_HOST, TOKEN
            
            csv_files = get_csv_files_from_workspace(workspace_path, DATABRICKS_HOST, TOKEN)
            
            if not csv_files:
                print("❌ No CSV files found!")
                return False
            
            print(f"✅ Found {len(csv_files)} CSV files")
            
            # Convert to Spark-readable paths
            csv_paths = csv_files
            print(f"\n📥 Reading {len(csv_paths)} CSV files...")
            
            df = spark.read \
                .option("header", "true") \
                .option("inferSchema", "false") \
                .option("comment", "#") \
                .option("multiLine", "false") \
                .csv(csv_paths)
            
            row_count = df.count()
            print(f"✅ Read DataFrame with {row_count:,} rows")
        
        # Step 4: Add custom columns
        print("\n🔧 Step 4: Adding custom columns...")
        
        # Get filename from input_file_name() - extract just the filename
        df = df.withColumn(
            "source_filename",
            regexp_extract(input_file_name(), r"([^/]+\.csv)$", 1)
        )
        
        # Extract profile reference from filename
        df = df.withColumn(
            "profile_reference",
            regexp_extract(col("source_filename"), r"_([A-Z0-9]{13})_", 1)
        )
        
        # Map risk profile based on profile_reference
        risk_profile_expr = when(
            col("profile_reference") == "THLH73H2VSWDN842", lit("Jade1314 CANADA ML")
        ).when(
            col("profile_reference") == "QNN7MK9V6T5T87F3", lit("Very_High_ecomm")
        ).when(
            col("profile_reference") == "TBDLJCJZX8LLWWF3", lit("Medium_ecomm")
        ).when(
            col("profile_reference") == "J2M3VKGZMHZNZ4Q9", lit("Medium")
        ).when(
            col("profile_reference") == "DXPLDK9V6T5T87F3", lit("High_ecomm")
        ).when(
            col("profile_reference") == "QLKKNG4S2Q9428Q9", lit("Very_High")
        ).when(
            col("profile_reference") == "ZDGX3H4S2Q9428Q9", lit("High")
        ).otherwise(lit("Unknown"))
        
        df = df.withColumn("risk_profile", risk_profile_expr)
        
        print("✅ Added columns: source_filename, profile_reference, risk_profile")
        
        # Step 5: Sanitize column names (replace spaces with underscores)
        print("\n🧹 Step 5: Sanitizing column names...")
        for col_name in df.columns:
            if ' ' in col_name or any(char in col_name for char in [',', ';', '{', '}', '(', ')']):
                new_name = col_name.replace(' ', '_').replace(',', '_').replace(';', '_') \
                    .replace('{', '_').replace('}', '_').replace('(', '_').replace(')', '_')
                df = df.withColumnRenamed(col_name, new_name)
        
        print("✅ Column names sanitized")
        
        # Step 6: Remove duplicates
        print("\n🔍 Step 6: Removing duplicates...")
        row_count_before = df.count()
        df = df.dropDuplicates()
        row_count_after = df.count()
        duplicates_removed = row_count_before - row_count_after
        print(f"✅ Removed {duplicates_removed:,} duplicate rows")
        print(f"   Remaining rows: {row_count_after:,}")
        
        # Step 7: Create Delta table
        print(f"\n💾 Step 7: Creating Delta table '{table_name}'...")
        
        schema, table = table_name.split('.') if '.' in table_name else ('default', table_name)
        table_location = f"s3://hf-payments-data-lake-live-main/{schema}/{table}_v2"
        
        if drop_if_exists:
            print("   Dropping existing table if it exists...")
            spark.sql(f"DROP TABLE IF EXISTS {table_name}")
        
        # Write to Delta table partitioned by source_filename for better performance
        print(f"   Writing to: {table_location}")
        print(f"   Partitioned by: source_filename")
        
        df.write \
            .format("delta") \
            .mode("overwrite") \
            .option("path", table_location) \
            .option("overwriteSchema", "true") \
            .partitionBy("source_filename") \
            .saveAsTable(table_name)
        
        print("✅ Delta table created successfully!")
        
        # Step 8: Verify
        print("\n📊 Step 8: Verification...")
        result_df = spark.table(table_name)
        total_rows = result_df.count()
        distinct_files = result_df.select("source_filename").distinct().count()
        
        print(f"✅ Table verification:")
        print(f"   Total rows: {total_rows:,}")
        print(f"   Distinct files: {distinct_files}")
        print(f"   Columns: {len(result_df.columns)}")
        
        # Show sample data
        print("\n📋 Sample data:")
        result_df.select("source_filename", "profile_reference", "risk_profile").distinct().show(10)
        
        print("\n" + "=" * 80)
        print("✅ SUCCESS! Table created using PySpark")
        print(f"📊 Query your table: SELECT * FROM {table_name}")
        print("=" * 80)
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    finally:
        try:
            spark.stop()
        except:
            pass


def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Create Adyen ML Test Data table using PySpark')
    parser.add_argument('--drop-if-exists', action='store_true', help='Drop table if it exists')
    
    args = parser.parse_args()
    
    workspace_path = "/Workspace/Users/visal.kumar@hellofresh.com/adyen-ml-test"
    table_name = "payments_hf.adyen_ml_test_data"
    
    success = create_table_with_spark(
        workspace_path=workspace_path,
        table_name=table_name,
        drop_if_exists=args.drop_if_exists
    )
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
