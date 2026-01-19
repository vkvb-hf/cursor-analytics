#!/usr/bin/env python3
"""Check if same PSP_Reference or Merchant_Reference have conflicting attributes."""

import sys
from databricks import sql
from config import SERVER_HOSTNAME, HTTP_PATH, TOKEN

def check_conflicting_attributes():
    """Check for conflicting attributes."""
    table_name = "payments_hf.adyen_ml_test_data"
    
    print("=" * 80)
    print("Checking for Conflicting Attributes")
    print("=" * 80)
    
    try:
        with sql.connect(
            server_hostname=SERVER_HOSTNAME,
            http_path=HTTP_PATH,
            access_token=TOKEN,
            timeout_seconds=600
        ) as connection:
            
            with connection.cursor() as cursor:
                
                # Check 1: PSP_Reference with multiple Status values
                print("\n🔍 Check 1: PSP_Reference with multiple Status values")
                print("-" * 80)
                cursor.execute(f"""
                    SELECT 
                        PSP_Reference,
                        COUNT(DISTINCT Status) as unique_statuses,
                        COUNT(*) as total_rows,
                        COUNT(DISTINCT source_filename) as unique_files
                    FROM {table_name}
                    GROUP BY PSP_Reference
                    HAVING COUNT(DISTINCT Status) > 1
                    ORDER BY unique_statuses DESC, total_rows DESC
                    LIMIT 20
                """)
                
                psp_multiple_status = cursor.fetchall()
                if psp_multiple_status:
                    print(f"\n⚠️  Found {len(psp_multiple_status)} PSP_References with multiple Status values")
                    print(f"\nTop 20 examples:")
                    print(f"{'PSP_Reference':<25} {'Unique Statuses':>18} {'Total Rows':>12} {'Unique Files':>15}")
                    print("-" * 80)
                    
                    for row in psp_multiple_status:
                        psp_ref = (row[0] or 'NULL')[:23]
                        unique_statuses = row[1]
                        total_rows = row[2]
                        unique_files = row[3]
                        print(f"{psp_ref:<25} {unique_statuses:>18} {total_rows:>12,} {unique_files:>15,}")
                    
                    # Show example with details
                    example_psp = psp_multiple_status[0][0]
                    print(f"\n📋 Example: {example_psp}")
                    print("-" * 80)
                    cursor.execute(f"""
                        SELECT 
                            Status,
                            source_filename,
                            Creation_Date,
                            COUNT(*) as count
                        FROM {table_name}
                        WHERE PSP_Reference = '{example_psp.replace("'", "''")}'
                        GROUP BY Status, source_filename, Creation_Date
                        ORDER BY Status, source_filename
                    """)
                    
                    print(f"{'Status':<15} {'File':<40} {'Date':<20} {'Count':>6}")
                    print("-" * 80)
                    for row in cursor.fetchall():
                        status = (row[0] or 'NULL')[:13]
                        filename = (row[1] or 'NULL')[:38]
                        date = (row[2] or 'NULL')[:18]
                        count = row[3]
                        print(f"{status:<15} {filename:<40} {date:<20} {count:>6}")
                else:
                    print(f"\n✅ No PSP_References found with multiple Status values")
                
                # Check 2: PSP_Reference with multiple risk_profile values
                print("\n🔍 Check 2: PSP_Reference with multiple risk_profile values")
                print("-" * 80)
                cursor.execute(f"""
                    SELECT 
                        PSP_Reference,
                        COUNT(DISTINCT risk_profile) as unique_risk_profiles,
                        COUNT(*) as total_rows,
                        COUNT(DISTINCT source_filename) as unique_files
                    FROM {table_name}
                    GROUP BY PSP_Reference
                    HAVING COUNT(DISTINCT risk_profile) > 1
                    ORDER BY unique_risk_profiles DESC, total_rows DESC
                    LIMIT 20
                """)
                
                psp_multiple_risk = cursor.fetchall()
                if psp_multiple_risk:
                    print(f"\n⚠️  Found {len(psp_multiple_risk)} PSP_References with multiple risk_profile values")
                    print(f"\nTop 20 examples:")
                    print(f"{'PSP_Reference':<25} {'Unique Risk Profiles':>22} {'Total Rows':>12} {'Unique Files':>15}")
                    print("-" * 80)
                    
                    for row in psp_multiple_risk:
                        psp_ref = (row[0] or 'NULL')[:23]
                        unique_risk = row[1]
                        total_rows = row[2]
                        unique_files = row[3]
                        print(f"{psp_ref:<25} {unique_risk:>22} {total_rows:>12,} {unique_files:>15,}")
                else:
                    print(f"\n✅ No PSP_References found with multiple risk_profile values")
                
                # Check 3: PSP_Reference with multiple profile_reference values
                print("\n🔍 Check 3: PSP_Reference with multiple profile_reference values")
                print("-" * 80)
                cursor.execute(f"""
                    SELECT 
                        PSP_Reference,
                        COUNT(DISTINCT profile_reference) as unique_profile_refs,
                        COUNT(*) as total_rows,
                        COUNT(DISTINCT source_filename) as unique_files
                    FROM {table_name}
                    WHERE profile_reference IS NOT NULL
                    GROUP BY PSP_Reference
                    HAVING COUNT(DISTINCT profile_reference) > 1
                    ORDER BY unique_profile_refs DESC, total_rows DESC
                    LIMIT 20
                """)
                
                psp_multiple_prof_ref = cursor.fetchall()
                if psp_multiple_prof_ref:
                    print(f"\n⚠️  Found {len(psp_multiple_prof_ref)} PSP_References with multiple profile_reference values")
                    print(f"\nTop 20 examples:")
                    print(f"{'PSP_Reference':<25} {'Unique Profile Refs':>22} {'Total Rows':>12} {'Unique Files':>15}")
                    print("-" * 80)
                    
                    for row in psp_multiple_prof_ref:
                        psp_ref = (row[0] or 'NULL')[:23]
                        unique_prof_ref = row[1]
                        total_rows = row[2]
                        unique_files = row[3]
                        print(f"{psp_ref:<25} {unique_prof_ref:>22} {total_rows:>12,} {unique_files:>15,}")
                    
                    # Show example
                    example_psp = psp_multiple_prof_ref[0][0]
                    print(f"\n📋 Example: {example_psp}")
                    print("-" * 80)
                    cursor.execute(f"""
                        SELECT 
                            profile_reference,
                            risk_profile,
                            source_filename,
                            COUNT(*) as count
                        FROM {table_name}
                        WHERE PSP_Reference = '{example_psp.replace("'", "''")}'
                        GROUP BY profile_reference, risk_profile, source_filename
                        ORDER BY profile_reference, source_filename
                    """)
                    
                    print(f"{'Profile Ref':<20} {'Risk Profile':<30} {'File':<40} {'Count':>6}")
                    print("-" * 80)
                    for row in cursor.fetchall():
                        prof_ref = (row[0] or 'NULL')[:18]
                        risk_prof = (row[1] or 'NULL')[:28]
                        filename = (row[2] or 'NULL')[:38]
                        count = row[3]
                        print(f"{prof_ref:<20} {risk_prof:<30} {filename:<40} {count:>6}")
                else:
                    print(f"\n✅ No PSP_References found with multiple profile_reference values")
                
                # Check 4: Merchant_Reference with multiple Status values
                print("\n🔍 Check 4: Merchant_Reference with multiple Status values")
                print("-" * 80)
                cursor.execute(f"""
                    SELECT 
                        Merchant_Reference,
                        COUNT(DISTINCT Status) as unique_statuses,
                        COUNT(*) as total_rows,
                        COUNT(DISTINCT PSP_Reference) as unique_psp_refs,
                        COUNT(DISTINCT source_filename) as unique_files
                    FROM {table_name}
                    GROUP BY Merchant_Reference
                    HAVING COUNT(DISTINCT Status) > 1
                    ORDER BY unique_statuses DESC, total_rows DESC
                    LIMIT 20
                """)
                
                merch_multiple_status = cursor.fetchall()
                if merch_multiple_status:
                    print(f"\n⚠️  Found {len(merch_multiple_status)} Merchant_References with multiple Status values")
                    print(f"\nTop 20 examples:")
                    print(f"{'Merchant_Reference':<50} {'Unique Statuses':>18} {'Total Rows':>12} {'Unique PSPs':>12} {'Unique Files':>15}")
                    print("-" * 80)
                    
                    for row in merch_multiple_status:
                        merch_ref = (row[0] or 'NULL')[:48]
                        unique_statuses = row[1]
                        total_rows = row[2]
                        unique_psp = row[3]
                        unique_files = row[4]
                        print(f"{merch_ref:<50} {unique_statuses:>18} {total_rows:>12,} {unique_psp:>12,} {unique_files:>15,}")
                else:
                    print(f"\n✅ No Merchant_References found with multiple Status values")
                
                # Check 5: Merchant_Reference with multiple risk_profile values
                print("\n🔍 Check 5: Merchant_Reference with multiple risk_profile values")
                print("-" * 80)
                cursor.execute(f"""
                    SELECT 
                        Merchant_Reference,
                        COUNT(DISTINCT risk_profile) as unique_risk_profiles,
                        COUNT(*) as total_rows,
                        COUNT(DISTINCT PSP_Reference) as unique_psp_refs,
                        COUNT(DISTINCT source_filename) as unique_files
                    FROM {table_name}
                    GROUP BY Merchant_Reference
                    HAVING COUNT(DISTINCT risk_profile) > 1
                    ORDER BY unique_risk_profiles DESC, total_rows DESC
                    LIMIT 20
                """)
                
                merch_multiple_risk = cursor.fetchall()
                if merch_multiple_risk:
                    print(f"\n⚠️  Found {len(merch_multiple_risk)} Merchant_References with multiple risk_profile values")
                    print(f"\nTop 20 examples:")
                    print(f"{'Merchant_Reference':<50} {'Unique Risk Profiles':>22} {'Total Rows':>12} {'Unique PSPs':>12} {'Unique Files':>15}")
                    print("-" * 80)
                    
                    for row in merch_multiple_risk:
                        merch_ref = (row[0] or 'NULL')[:48]
                        unique_risk = row[1]
                        total_rows = row[2]
                        unique_psp = row[3]
                        unique_files = row[4]
                        print(f"{merch_ref:<50} {unique_risk:>22} {total_rows:>12,} {unique_psp:>12,} {unique_files:>15,}")
                else:
                    print(f"\n✅ No Merchant_References found with multiple risk_profile values")
                
                # Check 6: Merchant_Reference with multiple profile_reference values
                print("\n🔍 Check 6: Merchant_Reference with multiple profile_reference values")
                print("-" * 80)
                cursor.execute(f"""
                    SELECT 
                        Merchant_Reference,
                        COUNT(DISTINCT profile_reference) as unique_profile_refs,
                        COUNT(*) as total_rows,
                        COUNT(DISTINCT PSP_Reference) as unique_psp_refs,
                        COUNT(DISTINCT source_filename) as unique_files
                    FROM {table_name}
                    WHERE profile_reference IS NOT NULL
                    GROUP BY Merchant_Reference
                    HAVING COUNT(DISTINCT profile_reference) > 1
                    ORDER BY unique_profile_refs DESC, total_rows DESC
                    LIMIT 20
                """)
                
                merch_multiple_prof_ref = cursor.fetchall()
                if merch_multiple_prof_ref:
                    print(f"\n⚠️  Found {len(merch_multiple_prof_ref)} Merchant_References with multiple profile_reference values")
                    print(f"\nTop 20 examples:")
                    print(f"{'Merchant_Reference':<50} {'Unique Profile Refs':>22} {'Total Rows':>12} {'Unique PSPs':>12} {'Unique Files':>15}")
                    print("-" * 80)
                    
                    for row in merch_multiple_prof_ref:
                        merch_ref = (row[0] or 'NULL')[:48]
                        unique_prof_ref = row[1]
                        total_rows = row[2]
                        unique_psp = row[3]
                        unique_files = row[4]
                        print(f"{merch_ref:<50} {unique_prof_ref:>22} {total_rows:>12,} {unique_psp:>12,} {unique_files:>15,}")
                else:
                    print(f"\n✅ No Merchant_References found with multiple profile_reference values")
                
                # Summary
                print("\n" + "=" * 80)
                print("Summary")
                print("=" * 80)
                
                summary_data = [
                    ("PSP_Reference with multiple Status", len(psp_multiple_status) if psp_multiple_status else 0),
                    ("PSP_Reference with multiple risk_profile", len(psp_multiple_risk) if psp_multiple_risk else 0),
                    ("PSP_Reference with multiple profile_reference", len(psp_multiple_prof_ref) if psp_multiple_prof_ref else 0),
                    ("Merchant_Reference with multiple Status", len(merch_multiple_status) if merch_multiple_status else 0),
                    ("Merchant_Reference with multiple risk_profile", len(merch_multiple_risk) if merch_multiple_risk else 0),
                    ("Merchant_Reference with multiple profile_reference", len(merch_multiple_prof_ref) if merch_multiple_prof_ref else 0),
                ]
                
                for check_name, count in summary_data:
                    status = "⚠️" if count > 0 else "✅"
                    print(f"{status} {check_name:<50} {count:>6,}")
                
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    check_conflicting_attributes()


