#!/usr/bin/env python3
"""
Notebook Output Reader

Read and display notebook output from DBFS files.
"""

import requests
import base64
from typing import Optional, Dict, List
from pathlib import Path


class NotebookOutputReader:
    """
    Read and display notebook output from DBFS.
    
    Usage:
        from core.notebook_output_reader import NotebookOutputReader
        
        reader = NotebookOutputReader()
        reader.display_output("/tmp/notebook_outputs/my_job_20240101_120000.txt")
    """
    
    def __init__(self, databricks_host: str = None, token: str = None):
        """
        Initialize output reader.
        
        Args:
            databricks_host: Databricks workspace host (from config if not provided)
            token: Databricks token (from config if not provided)
        """
        if databricks_host is None or token is None:
            try:
                from config import DATABRICKS_HOST, TOKEN
                self.host = databricks_host or DATABRICKS_HOST
                self.token = token or TOKEN
            except ImportError:
                raise ValueError("Must provide databricks_host and token, or have config.py")
        else:
            self.host = databricks_host
            self.token = token
        
        self.headers = {"Authorization": f"Bearer {self.token}"}
    
    def read_output(self, output_path: str) -> Optional[str]:
        """
        Read output file from DBFS.
        
        Args:
            output_path: DBFS path to output file
        
        Returns:
            File content as string, or None if error
        """
        read_url = f"{self.host}/api/2.0/dbfs/read"
        payload = {"path": output_path}
        
        try:
            response = requests.get(read_url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            file_data = response.json()
            if 'data' in file_data:
                content = base64.b64decode(file_data['data']).decode('utf-8')
                return content
            else:
                print(f"⚠️  No data in file: {output_path}")
                return None
                
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"❌ File not found: {output_path}")
            else:
                print(f"❌ Error reading file: {e}")
                if hasattr(e, 'response') and hasattr(e.response, 'text'):
                    print(f"   Response: {e.response.text}")
            return None
        except Exception as e:
            print(f"❌ Error reading output: {e}")
            return None
    
    def display_output(self, output_path: str, show_header: bool = True) -> bool:
        """
        Read and display formatted output.
        
        Args:
            output_path: DBFS path to output file
            show_header: If True, show header before output
        
        Returns:
            True if successful, False otherwise
        """
        content = self.read_output(output_path)
        
        if content:
            if show_header:
                print("\n" + "=" * 100)
                print("NOTEBOOK OUTPUT")
                print("=" * 100)
                print(f"File: {output_path}")
                print("=" * 100)
            
            print(content)
            return True
        else:
            return False
    
    def list_output_files(self, directory: str = "/tmp/notebook_outputs", pattern: str = "*.txt") -> List[str]:
        """
        List output files in a directory.
        
        Args:
            directory: DBFS directory path
            pattern: File pattern to match
        
        Returns:
            List of file paths
        """
        list_url = f"{self.host}/api/2.0/dbfs/list"
        payload = {"path": directory}
        
        try:
            response = requests.get(list_url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            data = response.json()
            files = []
            
            for item in data.get('files', []):
                if item['is_dir'] == False:
                    file_path = item['path']
                    if pattern == "*" or file_path.endswith(pattern.replace("*", "")):
                        files.append(file_path)
            
            return sorted(files, reverse=True)  # Most recent first
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"⚠️  Directory not found: {directory}")
            else:
                print(f"❌ Error listing files: {e}")
            return []
        except Exception as e:
            print(f"❌ Error listing output files: {e}")
            return []
    
    def get_latest_output(self, directory: str = "/tmp/notebook_outputs", job_name: str = None) -> Optional[str]:
        """
        Get the latest output file.
        
        Args:
            directory: DBFS directory path
            job_name: Optional job name to filter by
        
        Returns:
            Path to latest output file, or None
        """
        files = self.list_output_files(directory)
        
        if not files:
            return None
        
        if job_name:
            # Filter by job name
            safe_job_name = job_name.replace(" ", "_").replace("/", "_")
            filtered = [f for f in files if safe_job_name in f]
            if filtered:
                return filtered[0]
        
        # Return most recent
        return files[0]
    
    def display_latest_output(self, directory: str = "/tmp/notebook_outputs", job_name: str = None) -> bool:
        """
        Display the latest output file.
        
        Args:
            directory: DBFS directory path
            job_name: Optional job name to filter by
        
        Returns:
            True if successful, False otherwise
        """
        latest_file = self.get_latest_output(directory, job_name)
        
        if latest_file:
            return self.display_output(latest_file)
        else:
            print(f"❌ No output files found in {directory}")
            return False

