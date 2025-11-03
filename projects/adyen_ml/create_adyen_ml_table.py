#!/usr/bin/env python3
"""
Create payments_hf.adyen_ml_transactions table with risk profile mapping.

This script uses the generic csv_to_table.py utility for the specific
Adyen ML use case with risk profile mapping.
"""

import sys
from csv_to_table import create_table_from_csvs


# Risk profile mapping (removed duplicates)
RISK_PROFILE_MAPPING = {
    'THLH73H2VSWDN842': 'Jade1314 CANADA ML',
    'QNN7MK9V6T5T87F3': 'Very_High_ecomm',
    'TBDLJCJZX8LLWWF3': 'Medium_ecomm',
    'J2M3VKGZMHZNZ4Q9': 'Medium',
    'DXPLDK9V6T5T87F3': 'High_ecomm',
    'QLKKNG4S2Q9428Q9': 'Very_High',
    'ZDGX3H4S2Q9428Q9': 'High'
}


def extract_profile_reference(filename: str) -> str:
    """
    Extract profile reference from filename.
    Format: {COUNTRY}_{PROFILE_REF}_{REST}
    Example: CA_THLH73H2VSWDN842_Jade1314 2025-08-15T10_13_55Z.csv
    Returns: THLH73H2VSWDN842
    """
    parts = filename.split('_')
    if len(parts) >= 2:
        return parts[1]
    return 'Unknown'


def get_risk_profile(filename: str) -> str:
    """Get risk profile from filename."""
    profile_ref = extract_profile_reference(filename)
    return RISK_PROFILE_MAPPING.get(profile_ref, 'Unknown')


def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Create Adyen ML Transactions table')
    parser.add_argument(
        '--test',
        action='store_true',
        help='Test mode: process only the first CSV file'
    )
    parser.add_argument(
        '--drop-if-exists',
        action='store_true',
        help='Drop table if it exists before creating'
    )
    
    args = parser.parse_args()
    
    workspace_path = "/Workspace/Users/visal.kumar@hellofresh.com/adyen-ml-test"
    table_name = "payments_hf.adyen_ml_test_transactions"
    
    print("=" * 80)
    print("Create Adyen ML Test Transactions Table")
    print("=" * 80)
    print(f"\n📁 Workspace path: {workspace_path}")
    print(f"🎯 Table name: {table_name}")
    if args.test:
        print("🧪 TEST MODE: Processing only first CSV file")
    print("=" * 80)
    
    # Define custom columns for this use case
    custom_columns = {
        'source_filename': lambda f: f,
        'profile_reference': extract_profile_reference,
        'risk_profile': get_risk_profile
    }
    
    print("\n📋 Custom columns:")
    print("   - source_filename: Original CSV filename")
    print("   - profile_reference: Extracted profile reference code")
    print("   - risk_profile: Mapped risk profile based on reference")
    print("=" * 80)
    
    # Use generic utility to create table
    success = create_table_from_csvs(
        workspace_path=workspace_path,
        table_name=table_name,
        custom_columns=custom_columns,
        drop_if_exists=args.drop_if_exists,
        verify=True,
        test_mode=args.test
    )
    
    if success:
        print("\n✅ Table created successfully!")
        print(f"\n📊 You can now query: SELECT * FROM {table_name}")
        print("=" * 80)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
