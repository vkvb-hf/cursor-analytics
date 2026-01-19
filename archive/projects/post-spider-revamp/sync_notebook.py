#!/usr/bin/env python3
"""
Sync the post-spider-revamp notebook to Databricks workspace
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.workspace_sync import WorkspaceSync

def main():
    """Sync notebook to workspace."""
    
    # Local file path
    local_file = Path(__file__).parent / "[PY-3368] post-spider revamp"
    workspace_path = "/Workspace/Users/visal.kumar@hellofresh.com/[PY-3368] post-spider revamp"
    
    print("=" * 80)
    print("Sync Notebook to Databricks Workspace")
    print("=" * 80)
    print(f"\n📁 Local file: {local_file}")
    print(f"🌐 Workspace path: {workspace_path}")
    
    if not local_file.exists():
        print(f"\n❌ Error: Local file not found: {local_file}")
        return 1
    
    # Create sync instance (we only need it for upload_file method)
    sync = WorkspaceSync(
        local_dir=str(local_file.parent),
        workspace_dir="/Workspace/Users/visal.kumar@hellofresh.com"
    )
    
    # Upload the file
    print(f"\n📤 Uploading notebook...")
    result = sync.upload_file(local_file, workspace_path, overwrite=True)
    
    if result['success']:
        print(f"\n✅ Successfully uploaded notebook!")
        print(f"   📊 Size: {result.get('size_kb', 0):.2f} KB")
        print(f"   🌐 Workspace: {workspace_path}")
        print(f"\n{'=' * 80}")
        return 0
    else:
        print(f"\n❌ Failed to upload notebook")
        print(f"   Error: {result.get('error', 'Unknown error')}")
        print(f"\n{'=' * 80}")
        return 1

if __name__ == "__main__":
    sys.exit(main())






