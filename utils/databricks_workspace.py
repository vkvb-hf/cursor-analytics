#!/usr/bin/env python3
"""
Shared utilities for Databricks Workspace operations.
"""

import os
import base64
import requests
from typing import Dict, Optional


def create_workspace_directory(
    databricks_path: str,
    workspace_host: str,
    token: str
) -> None:
    """
    Create directory structure in Databricks workspace if it doesn't exist.
    
    Args:
        databricks_path: Full workspace path (e.g., /Workspace/Users/...)
        workspace_host: Databricks workspace hostname
        token: Databricks personal access token
    """
    headers = {"Authorization": f"Bearer {token}"}
    path_parts = databricks_path.strip('/').split('/')
    
    for i in range(1, len(path_parts)):
        parent_path = '/' + '/'.join(path_parts[:i])
        mkdir_url = f"{workspace_host}/api/2.0/workspace/mkdirs"
        mkdir_payload = {"path": parent_path}
        
        try:
            mkdir_response = requests.post(mkdir_url, headers=headers, json=mkdir_payload)
            if mkdir_response.status_code not in [200, 400]:
                mkdir_response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if "RESOURCE_ALREADY_EXISTS" not in str(e):
                print(f"⚠️  Warning creating directory {parent_path}: {e}")


def upload_csv_to_workspace(
    csv_file_path: str,
    csv_filename: str,
    databricks_path: str,
    workspace_host: str,
    token: str
) -> Dict[str, any]:
    """
    Upload a CSV file to Databricks workspace.
    
    Args:
        csv_file_path: Local path to CSV file
        csv_filename: Filename for the uploaded file
        databricks_path: Target workspace directory path
        workspace_host: Databricks workspace hostname
        token: Databricks personal access token
    
    Returns:
        Dictionary with 'success' (bool) and either 'workspace_path'/'size_mb' or 'error'
    """
    workspace_file_path = f"{databricks_path.rstrip('/')}/{csv_filename}"
    headers = {"Authorization": f"Bearer {token}"}
    
    # Read file content as text
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as f:
            file_content_text = f.read()
    except UnicodeDecodeError:
        try:
            with open(csv_file_path, 'r', encoding='latin-1') as f:
                file_content_text = f.read()
        except Exception as e:
            return {'success': False, 'error': f"Error reading file: {e}"}
    except Exception as e:
        return {'success': False, 'error': f"Error reading file: {e}"}
    
    # Delete existing file if it exists
    try:
        delete_url = f"{workspace_host}/api/2.0/workspace/delete"
        delete_payload = {"path": workspace_file_path}
        requests.post(delete_url, headers=headers, json=delete_payload)
    except:
        pass  # Non-critical if file doesn't exist
    
    # Upload using Workspace API
    try:
        file_content_b64 = base64.b64encode(file_content_text.encode('utf-8')).decode('utf-8')
        
        import_url = f"{workspace_host}/api/2.0/workspace/import"
        import_payload = {
            "path": workspace_file_path,
            "content": file_content_b64,
            "format": "SOURCE",
            "language": "PYTHON"
        }
        
        response = requests.post(import_url, headers=headers, json=import_payload)
        response.raise_for_status()
        
        return {
            'success': True,
            'workspace_path': workspace_file_path,
            'size_mb': len(file_content_text.encode('utf-8')) / (1024 * 1024)
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

