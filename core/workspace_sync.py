#!/usr/bin/env python3
"""
Workspace Sync Utility

Bidirectional sync between local filesystem and Databricks workspace.
Supports:
- Upload local files to Databricks workspace
- Download workspace files to local
- Watch mode for automatic sync
- Notebook-specific handling
"""

import os
import sys
import base64
import requests
from pathlib import Path
from typing import Dict, List, Optional, Set
from datetime import datetime

# Add parent directory to path for config import
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATABRICKS_HOST, TOKEN


class WorkspaceSync:
    """
    Bidirectional sync between local directory and Databricks workspace.
    
    Usage:
        sync = WorkspaceSync(
            local_dir="./notebooks",
            workspace_dir="/Workspace/Users/user@example.com/notebooks"
        )
        
        # Upload local files to workspace
        sync.sync_to_workspace()
        
        # Download workspace files to local
        sync.sync_from_workspace()
        
        # Watch for changes and auto-sync
        sync.watch_and_sync()
    """
    
    def __init__(self, local_dir: str, workspace_dir: str, 
                 host: str = None, token: str = None):
        """
        Initialize workspace sync.
        
        Args:
            local_dir: Local directory path
            workspace_dir: Databricks workspace directory path (e.g., /Workspace/Users/...)
            host: Databricks host (defaults to config)
            token: Databricks token (defaults to config)
        """
        self.local_dir = Path(local_dir).expanduser().resolve()
        self.workspace_dir = workspace_dir.rstrip('/')
        self.host = host or DATABRICKS_HOST
        self.token = token or TOKEN
        self.headers = {"Authorization": f"Bearer {self.token}"}
        
        # Ensure local directory exists
        self.local_dir.mkdir(parents=True, exist_ok=True)
    
    def _get_language_from_extension(self, file_path: Path) -> str:
        """Determine Databricks language from file extension."""
        ext = file_path.suffix.lower()
        language_map = {
            '.py': 'PYTHON',
            '.sql': 'SQL',
            '.scala': 'SCALA',
            '.r': 'R'
        }
        return language_map.get(ext, 'PYTHON')
    
    def _create_workspace_dirs(self, workspace_path: str):
        """Create directory structure in workspace if needed."""
        path_parts = workspace_path.strip('/').split('/')
        
        for i in range(1, len(path_parts)):
            parent_path = '/' + '/'.join(path_parts[:i])
            mkdir_url = f"{self.host}/api/2.0/workspace/mkdirs"
            mkdir_payload = {"path": parent_path}
            
            try:
                response = requests.post(mkdir_url, headers=self.headers, json=mkdir_payload)
                if response.status_code not in [200, 400]:
                    response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                if "RESOURCE_ALREADY_EXISTS" not in str(e):
                    print(f"⚠️  Warning creating directory {parent_path}: {e}")
    
    def upload_file(self, local_path: Path, workspace_path: str = None, 
                   overwrite: bool = True) -> Dict[str, any]:
        """
        Upload a single file to Databricks workspace.
        
        Args:
            local_path: Local file path
            workspace_path: Target workspace path (if None, auto-generate)
            overwrite: Whether to overwrite existing file
        
        Returns:
            Dictionary with success status and details
        """
        if not local_path.exists():
            return {'success': False, 'error': f'File not found: {local_path}'}
        
        if workspace_path is None:
            # Auto-generate workspace path
            relative_path = local_path.relative_to(self.local_dir)
            workspace_path = f"{self.workspace_dir}/{relative_path.as_posix()}"
        
        # Create directory structure
        workspace_dir = '/'.join(workspace_path.split('/')[:-1])
        self._create_workspace_dirs(workspace_dir)
        
        # Read file content
        try:
            with open(local_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            return {'success': False, 'error': f'Cannot read file as text: {local_path}'}
        except Exception as e:
            return {'success': False, 'error': f'Error reading file: {e}'}
        
        # Determine language
        language = self._get_language_from_extension(local_path)
        
        # Encode content
        content_b64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')
        
        # Upload file
        try:
            import_url = f"{self.host}/api/2.0/workspace/import"
            payload = {
                "path": workspace_path,
                "content": content_b64,
                "format": "SOURCE",
                "language": language,
                "overwrite": overwrite
            }
            
            response = requests.post(import_url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            return {
                'success': True,
                'local_path': str(local_path),
                'workspace_path': workspace_path,
                'size_kb': len(content.encode('utf-8')) / 1024
            }
        except requests.exceptions.HTTPError as e:
            error_msg = str(e)
            try:
                error_detail = e.response.json()
                error_msg = f"{e}: {error_detail}"
            except:
                if hasattr(e, 'response') and hasattr(e.response, 'text'):
                    error_msg = f"{e}: {e.response.text}"
            
            return {'success': False, 'error': error_msg}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def download_file(self, workspace_path: str, local_path: Path = None,
                     overwrite: bool = True) -> Dict[str, any]:
        """
        Download a file from Databricks workspace.
        
        Args:
            workspace_path: Workspace file path
            local_path: Local file path (if None, auto-generate)
            overwrite: Whether to overwrite existing file
        
        Returns:
            Dictionary with success status and details
        """
        if local_path is None:
            # Auto-generate local path
            relative_path = workspace_path.replace(self.workspace_dir, '').lstrip('/')
            local_path = self.local_dir / relative_path
        
        # Check if local file exists
        if local_path.exists() and not overwrite:
            return {'success': False, 'error': f'File exists and overwrite=False: {local_path}'}
        
        # Create local directory
        local_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Download file
        try:
            export_url = f"{self.host}/api/2.0/workspace/export"
            params = {"path": workspace_path, "format": "SOURCE"}
            
            response = requests.get(export_url, headers=self.headers, params=params)
            response.raise_for_status()
            
            data = response.json()
            content_b64 = data.get('content', '')
            content = base64.b64decode(content_b64).decode('utf-8')
            
            # Write to local file
            with open(local_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return {
                'success': True,
                'workspace_path': workspace_path,
                'local_path': str(local_path),
                'size_kb': len(content.encode('utf-8')) / 1024
            }
        except requests.exceptions.HTTPError as e:
            error_msg = str(e)
            try:
                error_detail = e.response.json()
                error_msg = f"{e}: {error_detail}"
            except:
                if hasattr(e, 'response') and hasattr(e.response, 'text'):
                    error_msg = f"{e}: {e.response.text}"
            
            return {'success': False, 'error': error_msg}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def list_workspace_files(self, workspace_dir: str = None, 
                           recursive: bool = True) -> List[str]:
        """
        List all files in workspace directory.
        
        Args:
            workspace_dir: Directory to list (defaults to self.workspace_dir)
            recursive: Whether to list recursively
        
        Returns:
            List of workspace file paths
        """
        if workspace_dir is None:
            workspace_dir = self.workspace_dir
        
        files = []
        
        try:
            list_url = f"{self.host}/api/2.0/workspace/list"
            params = {"path": workspace_dir}
            
            response = requests.get(list_url, headers=self.headers, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            for item in data.get('objects', []):
                path = item['path']
                object_type = item.get('object_type', '')
                
                if object_type == 'NOTEBOOK' or object_type == 'FILE':
                    files.append(path)
                elif object_type == 'DIRECTORY' and recursive:
                    # Recursively list subdirectories
                    files.extend(self.list_workspace_files(path, recursive=True))
            
            return files
        except Exception as e:
            print(f"⚠️  Error listing workspace files: {e}")
            return []
    
    def sync_to_workspace(self, pattern: str = "**/*.py", 
                         dry_run: bool = False) -> Dict[str, any]:
        """
        Sync local files to Databricks workspace.
        
        Args:
            pattern: Glob pattern for files to sync (default: **/*.py)
            dry_run: If True, only show what would be synced
        
        Returns:
            Dictionary with sync results
        """
        print(f"\n📤 Syncing local files to workspace...")
        print(f"   Local: {self.local_dir}")
        print(f"   Workspace: {self.workspace_dir}")
        print(f"   Pattern: {pattern}")
        
        if dry_run:
            print("   [DRY RUN MODE - No files will be uploaded]")
        
        files = list(self.local_dir.glob(pattern))
        results = {
            'success': [],
            'failed': [],
            'total': len(files)
        }
        
        for file_path in files:
            if file_path.is_file():
                relative_path = file_path.relative_to(self.local_dir)
                workspace_path = f"{self.workspace_dir}/{relative_path.as_posix()}"
                
                if dry_run:
                    print(f"   Would upload: {file_path} -> {workspace_path}")
                    results['success'].append({
                        'local': str(file_path),
                        'workspace': workspace_path,
                        'dry_run': True
                    })
                else:
                    result = self.upload_file(file_path, workspace_path)
                    if result['success']:
                        print(f"   ✅ {file_path.name} -> {workspace_path}")
                        results['success'].append(result)
                    else:
                        print(f"   ❌ {file_path.name}: {result.get('error', 'Unknown error')}")
                        results['failed'].append(result)
        
        print(f"\n📊 Sync complete: {len(results['success'])} succeeded, {len(results['failed'])} failed")
        return results
    
    def sync_from_workspace(self, pattern: str = None,
                           dry_run: bool = False) -> Dict[str, any]:
        """
        Sync workspace files to local directory.
        
        Args:
            pattern: Optional pattern to filter files (not implemented yet)
            dry_run: If True, only show what would be synced
        
        Returns:
            Dictionary with sync results
        """
        print(f"\n📥 Syncing workspace files to local...")
        print(f"   Workspace: {self.workspace_dir}")
        print(f"   Local: {self.local_dir}")
        
        if dry_run:
            print("   [DRY RUN MODE - No files will be downloaded]")
        
        workspace_files = self.list_workspace_files()
        results = {
            'success': [],
            'failed': [],
            'total': len(workspace_files)
        }
        
        for workspace_path in workspace_files:
            if workspace_path.startswith(self.workspace_dir):
                relative_path = workspace_path.replace(self.workspace_dir, '').lstrip('/')
                local_path = self.local_dir / relative_path
                
                if dry_run:
                    print(f"   Would download: {workspace_path} -> {local_path}")
                    results['success'].append({
                        'workspace': workspace_path,
                        'local': str(local_path),
                        'dry_run': True
                    })
                else:
                    result = self.download_file(workspace_path, local_path)
                    if result['success']:
                        print(f"   ✅ {workspace_path} -> {local_path.name}")
                        results['success'].append(result)
                    else:
                        print(f"   ❌ {workspace_path}: {result.get('error', 'Unknown error')}")
                        results['failed'].append(result)
        
        print(f"\n📊 Sync complete: {len(results['success'])} succeeded, {len(results['failed'])} failed")
        return results
    
    def watch_and_sync(self, pattern: str = "**/*.py", 
                      interval: int = 2, 
                      direction: str = "to_workspace"):
        """
        Watch for file changes and automatically sync.
        
        Args:
            pattern: Glob pattern for files to watch
            interval: Check interval in seconds
            direction: 'to_workspace' or 'from_workspace'
        
        Note: This is a basic implementation. For production, consider using
        watchdog library for more efficient file watching.
        """
        print(f"\n👀 Watching for changes...")
        print(f"   Pattern: {pattern}")
        print(f"   Direction: {direction}")
        print(f"   Press Ctrl+C to stop\n")
        
        last_modified = {}
        
        try:
            while True:
                files = list(self.local_dir.glob(pattern))
                
                for file_path in files:
                    if file_path.is_file():
                        mtime = file_path.stat().st_mtime
                        file_key = str(file_path)
                        
                        if file_key not in last_modified or mtime > last_modified[file_key]:
                            if file_key in last_modified:
                                print(f"🔄 Detected change: {file_path.name}")
                                
                                if direction == "to_workspace":
                                    result = self.upload_file(file_path)
                                    if result['success']:
                                        print(f"   ✅ Synced to workspace")
                                    else:
                                        print(f"   ❌ Sync failed: {result.get('error')}")
                            
                            last_modified[file_key] = mtime
                
                import time
                time.sleep(interval)
        
        except KeyboardInterrupt:
            print("\n\n👋 Stopped watching")


def main():
    """CLI entry point for workspace sync."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Sync files between local and Databricks workspace')
    parser.add_argument('--local-dir', required=True, help='Local directory path')
    parser.add_argument('--workspace-dir', required=True, help='Workspace directory path')
    parser.add_argument('--direction', choices=['to_workspace', 'from_workspace', 'both'],
                       default='to_workspace', help='Sync direction')
    parser.add_argument('--pattern', default='**/*.py', help='File pattern to sync')
    parser.add_argument('--watch', action='store_true', help='Watch for changes and auto-sync')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be synced without actually syncing')
    
    args = parser.parse_args()
    
    sync = WorkspaceSync(args.local_dir, args.workspace_dir)
    
    if args.watch:
        direction = 'to_workspace' if args.direction in ['to_workspace', 'both'] else 'from_workspace'
        sync.watch_and_sync(pattern=args.pattern, direction=direction)
    else:
        if args.direction in ['to_workspace', 'both']:
            sync.sync_to_workspace(pattern=args.pattern, dry_run=args.dry_run)
        
        if args.direction in ['from_workspace', 'both']:
            sync.sync_from_workspace(dry_run=args.dry_run)


if __name__ == "__main__":
    main()






