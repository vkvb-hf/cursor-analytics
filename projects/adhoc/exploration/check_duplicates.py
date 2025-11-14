#!/usr/bin/env python3
"""Check for duplicates in the table and investigate why."""

import sys
from databricks import sql
from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN

def check_duplicates():
    """Check for duplicates in the table."""
    table_name = "payments_hf.adyen_ml_test_data"
    
    print("=" * 80)
    print("Checking for Duplicates")
    print("=" * 80)
    
    try:
        with sql.connect(
            server_hostname=SERVER_HOSTNAME,
            http_path=HTTP_PATH,
            access_token=TOKEN,
            timeout_seconds=600
        ) as connection:
            
            with connection.cursor() as cursor:
                # Step 1: Check total rows vs unique rows
                cursor.execute(f"SELECT COUNT(*) as total_rows FROM {table_name}")
                total_rows = cursor.fetchone()[0]
                
                # Check for exact duplicates (all columns)
                cursor.execute(f"""
                    SELECT 
                        COUNT(*) as total_rows,
                        COUNT(DISTINCT *) as unique_rows
                    FROM {table_name}
                """)
                
                # Since COUNT(DISTINCT *) might not work, let's check differently
                print(f"\n📊 Total rows: {total_rows:,}")
                
                # Step 2: Check for duplicates by Merchant_Reference
                print(f"\n🔍 Checking duplicates by Merchant_Reference...")
                cursor.execute(f"""
                    SELECT 
                        Merchant_Reference,
                        COUNT(*) as duplicate_count,
                        COUNT(DISTINCT PSP_Reference) as unique_psp_refs,
                        COUNT(DISTINCT source_filename) as unique_files
                    FROM {table_name}
                    GROUP BY Merchant_Reference
                    HAVING COUNT(*) > 1
                    ORDER BY duplicate_count DESC
                    LIMIT 20
                """)
                
                merchant_duplicates = cursor.fetchall()
                
                if merchant_duplicates:
                    print(f"\n⚠️  Found {len(merchant_duplicates)} Merchant_References with duplicates")
                    print(f"\nTop 20 Merchant_References with duplicates:")
                    print("-" * 80)
                    print(f"{'Merchant_Reference':<50} {'Count':>10} {'Unique PSP_Refs':>15} {'Unique Files':>15}")
                    print("-" * 80)
                    
                    for row in merchant_duplicates:
                        merchant_ref = (row[0] or 'NULL')[:48]
                        count = row[1]
                        unique_psp = row[2]
                        unique_files = row[3]
                        print(f"{merchant_ref:<50} {count:>10,} {unique_psp:>15,} {unique_files:>15,}")
                    
                    # Investigate a specific example
                    example_merchant = merchant_duplicates[0][0]
                    print(f"\n📋 Investigating example: {example_merchant}")
                    print("-" * 80)
                    
                    cursor.execute(f"""
                        SELECT 
                            PSP_Reference,
                            source_filename,
                            Creation_Date,
                            Status,
                            Value,
                            Currency,
                            COUNT(*) as occurrence_count
                        FROM {table_name}
                        WHERE Merchant_Reference = '{example_merchant.replace("'", "''")}'
                        GROUP BY 
                            PSP_Reference,
                            source_filename,
                            Creation_Date,
                            Status,
                            Value,
                            Currency
                        ORDER BY occurrence_count DESC
                        LIMIT 10
                    """)
                    
                    print(f"\nSample records for {example_merchant}:")
                    print("-" * 80)
                    print(f"{'PSP_Reference':<20} {'File':<30} {'Date':<20} {'Status':<15} {'Count':>6}")
                    print("-" * 80)
                    
                    for row in cursor.fetchall():
                        psp_ref = (row[0] or 'NULL')[:18]
                        filename = (row[1] or 'NULL')[:28]
                        date = (row[2] or 'NULL')[:18]
                        status = (row[3] or 'NULL')[:13]
                        count = row[6]
                        print(f"{psp_ref:<20} {filename:<30} {date:<20} {status:<15} {count:>6}")
                
                else:
                    print(f"\n✅ No duplicates found by Merchant_Reference")
                
                # Step 3: Check for duplicates by PSP_Reference (should be unique)
                print(f"\n🔍 Checking duplicates by PSP_Reference (should be unique)...")
                cursor.execute(f"""
                    SELECT 
                        PSP_Reference,
                        COUNT(*) as duplicate_count,
                        COUNT(DISTINCT Merchant_Reference) as unique_merchant_refs,
                        COUNT(DISTINCT source_filename) as unique_files
                    FROM {table_name}
                    GROUP BY PSP_Reference
                    HAVING COUNT(*) > 1
                    ORDER BY duplicate_count DESC
                    LIMIT 20
                """)
                
                psp_duplicates = cursor.fetchall()
                
                if psp_duplicates:
                    print(f"\n⚠️  Found {len(psp_duplicates)} PSP_References with duplicates")
                    print(f"\nTop 20 PSP_References with duplicates:")
                    print("-" * 80)
                    print(f"{'PSP_Reference':<25} {'Count':>10} {'Unique Merchants':>18} {'Unique Files':>15}")
                    print("-" * 80)
                    
                    for row in psp_duplicates:
                        psp_ref = (row[0] or 'NULL')[:23]
                        count = row[1]
                        unique_merchants = row[2]
                        unique_files = row[3]
                        print(f"{psp_ref:<25} {count:>10,} {unique_merchants:>18,} {unique_files:>15,}")
                else:
                    print(f"\n✅ No duplicates found by PSP_Reference")
                
                # Step 4: Check for exact duplicate rows (all columns)
                print(f"\n🔍 Checking for exact duplicate rows (all columns identical)...")
                cursor.execute(f"""
                    SELECT 
                        PSP_Reference,
                        Merchant_Reference,
                        source_filename,
                        COUNT(*) as duplicate_count
                    FROM {table_name}
                    GROUP BY PSP_Reference, Merchant_Reference, source_filename
                    HAVING COUNT(*) > 1
                    ORDER BY duplicate_count DESC
                    LIMIT 10
                """)
                
                exact_duplicates = cursor.fetchall()
                
                if exact_duplicates:
                    print(f"\n⚠️  Found {len(exact_duplicates)} sets of exact duplicate rows")
                    print(f"\nSample exact duplicates:")
                    print("-" * 80)
                    for row in exact_duplicates:
                        psp_ref = (row[0] or 'NULL')[:18]
                        merch_ref = (row[1] or 'NULL')[:30]
                        filename = (row[2] or 'NULL')[:25]
                        count = row[3]
                        print(f"PSP: {psp_ref:<18} Merchant: {merch_ref:<30} File: {filename:<25} Count: {count:,}")
                else:
                    print(f"\n✅ No exact duplicate rows found")
                
                # Step 5: Summary statistics
                print(f"\n📊 Summary Statistics:")
                print("-" * 80)
                
                cursor.execute(f"""
                    SELECT 
                        COUNT(DISTINCT PSP_Reference) as unique_psp_refs,
                        COUNT(DISTINCT Merchant_Reference) as unique_merchant_refs,
                        COUNT(DISTINCT source_filename) as unique_files
                    FROM {table_name}
                """)
                
                stats = cursor.fetchone()
                print(f"Unique PSP_References: {stats[0]:,}")
                print(f"Unique Merchant_References: {stats[1]:,}")
                print(f"Unique source files: {stats[2]:,}")
                print(f"Total rows: {total_rows:,}")
                print(f"\nRows per unique Merchant_Reference: {total_rows / stats[1]:.2f}")
                print(f"Rows per unique PSP_Reference: {total_rows / stats[0]:.2f}")
                
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    check_duplicates()


