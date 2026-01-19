#!/usr/bin/env python3
"""
Unzip CSV files from zip archives and add zip name prefix to each CSV.

Usage:
    python unzip_csvs.py [--output-dir OUTPUT_DIR]
"""

import os
import sys
import zipfile
import shutil
import argparse
import tempfile
from pathlib import Path

# Import config - works both when installed as package and when run directly
try:
    from core._config import DATABRICKS_HOST, TOKEN
except ImportError:
    # Fallback for direct script execution
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from config import DATABRICKS_HOST, TOKEN


def unzip_and_rename_csvs(source_dir: str, output_dir: str) -> dict:
    """
    Unzip all zip files and add zip name prefix to CSV files.
    
    Args:
        source_dir: Directory containing zip files
        output_dir: Directory to extract CSV files to
    
    Returns:
        Dictionary with extraction results
    """
    results = {
        'csv_files': [],
        'zip_files_processed': [],
        'total_csvs': 0,
        'largest_csv': None,
        'largest_size': 0
    }
    
    os.makedirs(output_dir, exist_ok=True)
    
    zip_files = [f for f in os.listdir(source_dir) if f.lower().endswith('.zip')]
    
    if not zip_files:
        print(f"⚠️  No zip files found in: {source_dir}")
        return results
    
    print(f"📦 Found {len(zip_files)} zip file(s)")
    print("=" * 80)
    
    for zip_file in zip_files:
        zip_path = os.path.join(source_dir, zip_file)
        zip_name_no_ext = os.path.splitext(zip_file)[0]
        
        print(f"\n📂 Processing: {zip_file}")
        
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                file_list = zip_ref.namelist()
                csv_files_in_zip = [f for f in file_list if f.lower().endswith('.csv')]
                
                if not csv_files_in_zip:
                    print(f"   ⚠️  No CSV files found in {zip_file}")
                    continue
                
                print(f"   📄 Found {len(csv_files_in_zip)} CSV file(s)")
                
                for csv_in_zip in csv_files_in_zip:
                    csv_filename = os.path.basename(csv_in_zip)
                    new_csv_filename = f"{zip_name_no_ext}_{csv_filename}"
                    output_path = os.path.join(output_dir, new_csv_filename)
                    
                    # Extract the CSV file
                    zip_ref.extract(csv_in_zip, output_dir)
                    
                    # Handle renaming and subdirectory cleanup
                    extracted_path = os.path.join(output_dir, csv_in_zip)
                    if extracted_path != output_path:
                        if os.path.dirname(csv_in_zip):
                            os.makedirs(os.path.dirname(output_path), exist_ok=True)
                            if os.path.exists(extracted_path):
                                shutil.move(extracted_path, output_path)
                                # Clean up empty subdirectories
                                try:
                                    subdir = os.path.dirname(extracted_path)
                                    if os.path.exists(subdir) and not os.listdir(subdir):
                                        os.rmdir(subdir)
                                except:
                                    pass
                        else:
                            if os.path.exists(extracted_path):
                                os.rename(extracted_path, output_path)
                    
                    if os.path.exists(output_path):
                        file_size = os.path.getsize(output_path)
                        
                        csv_info = {
                            'filename': new_csv_filename,
                            'original_zip': zip_file,
                            'original_csv': csv_filename,
                            'path': output_path,
                            'size': file_size,
                            'size_mb': file_size / (1024 * 1024)
                        }
                        
                        results['csv_files'].append(csv_info)
                        results['total_csvs'] += 1
                        
                        if file_size > results['largest_size']:
                            results['largest_size'] = file_size
                            results['largest_csv'] = csv_info
                        
                        print(f"   ✅ Extracted: {new_csv_filename} ({csv_info['size_mb']:.2f} MB)")
                
                results['zip_files_processed'].append(zip_file)
                
        except zipfile.BadZipFile:
            print(f"   ❌ Error: {zip_file} is not a valid zip file")
        except Exception as e:
            print(f"   ❌ Error processing {zip_file}: {e}")
    
    return results


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Unzip CSV files and add zip name prefix')
    parser.add_argument(
        '--source-dir',
        default=os.path.expanduser("~/Downloads/to_upload"),
        help='Directory containing zip files (default: ~/Downloads/to_upload)'
    )
    parser.add_argument(
        '--output-dir',
        default=os.path.join(tempfile.gettempdir(), "databricks_csv_extract"),
        help='Directory to extract CSV files to'
    )
    
    args = parser.parse_args()
    
    print("=" * 80)
    print("Unzip CSV Files")
    print("=" * 80)
    print(f"\n📂 Source directory: {args.source_dir}")
    print(f"📁 Output directory: {args.output_dir}")
    print("=" * 80)
    
    results = unzip_and_rename_csvs(args.source_dir, args.output_dir)
    
    print("\n" + "=" * 80)
    print("Extraction Summary")
    print("=" * 80)
    print(f"✅ Processed zip files: {len(results['zip_files_processed'])}")
    print(f"✅ Extracted CSV files: {results['total_csvs']}")
    
    if results['largest_csv']:
        largest = results['largest_csv']
        print(f"\n📊 Largest CSV file:")
        print(f"   Filename: {largest['filename']}")
        print(f"   Size: {largest['size_mb']:.2f} MB")
    
    print(f"\n📁 CSV files extracted to: {args.output_dir}")
    print("=" * 80)
    
    sys.exit(0 if results['total_csvs'] > 0 else 1)


if __name__ == "__main__":
    main()


