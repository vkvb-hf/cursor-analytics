#!/usr/bin/env python3
"""
Full Workspace Sync Script

Syncs entire Databricks workspace to local directory:
/Workspace/Users/visal.kumar@hellofresh.com/ 
  → /Users/visal.kumar/Documents/databricks/visal.kumar@hellofresh.com/
"""

import os
import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.workspace_sync import WorkspaceSync


def main():
    """Sync entire workspace."""
    
    # Configuration
    local_dir = "/Users/visal.kumar/Documents/databricks/visal.kumar@hellofresh.com"
    workspace_dir = "/Workspace/Users/visal.kumar@hellofresh.com"
    
    print("=" * 80)
    print("Full Workspace Sync")
    print("=" * 80)
    print(f"\nLocal Directory:  {local_dir}")
    print(f"Workspace Directory: {workspace_dir}")
    print("\n📥 Downloading all files from workspace to local...")
    
    # Create sync instance
    sync = WorkspaceSync(
        local_dir=local_dir,
        workspace_dir=workspace_dir
    )
    
    # Sync from workspace (download everything)
    print("\n📥 Downloading all files from workspace...")
    result = sync.sync_from_workspace()
    
    # Summary
    print("\n" + "=" * 80)
    print("Sync Complete!")
    print("=" * 80)
    print(f"✅ Successfully synced: {len(result['success'])} files")
    if result['failed']:
        print(f"❌ Failed: {len(result['failed'])} files")
        for failed in result['failed'][:5]:  # Show first 5 failures
            print(f"   - {failed.get('workspace', 'unknown')}: {failed.get('error', 'Unknown error')}")
        if len(result['failed']) > 5:
            print(f"   ... and {len(result['failed']) - 5} more")
    
    print(f"\n📁 Local files are now at: {local_dir}")
    print(f"🌐 View in Databricks: {workspace_dir}")


if __name__ == "__main__":
    main()

