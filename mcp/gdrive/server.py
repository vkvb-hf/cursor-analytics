#!/usr/bin/env python3
"""
Google Drive MCP Server

A Model Context Protocol server for reading Google Drive files (Docs, Sheets, etc.)
Uses OAuth2 for authentication (user credentials, not service account).

Tools:
- gdrive_read: Read content of any file by ID or URL
- gdrive_read_url: Read content directly from a Google Drive URL
- gdrive_list: List files in Drive or a specific folder
- gdrive_search: Search for files by name or query

Configuration:
- Place credentials.json in this directory (OAuth2 client credentials)
- On first run, will open browser for authentication and save token.json

Usage:
    python server.py

Configure in ~/.cursor/mcp.json to use with Cursor.
"""

import os
import re
import io
from typing import Any, Optional

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

from mcp.server.fastmcp import FastMCP

# =============================================================================
# CONFIGURATION
# =============================================================================

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.path.join(BASE_DIR, 'credentials.json')
TOKEN_FILE = os.path.join(BASE_DIR, 'token.json')

# Initialize FastMCP
mcp = FastMCP("Google Drive MCP")

# =============================================================================
# AUTHENTICATION
# =============================================================================

def get_drive_service():
    """Get authenticated Google Drive service."""
    creds = None
    
    if os.path.exists(TOKEN_FILE):
        try:
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        except Exception:
            pass

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception:
                if os.path.exists(TOKEN_FILE):
                    os.remove(TOKEN_FILE)
                return get_drive_service()
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    return build('drive', 'v3', credentials=creds)

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def extract_file_id(url_or_id: str) -> str:
    """
    Extract file ID from a Google Drive/Docs/Sheets URL or return as-is if already an ID.
    
    Supports:
    - https://docs.google.com/document/d/FILE_ID/edit
    - https://docs.google.com/spreadsheets/d/FILE_ID/edit
    - https://drive.google.com/file/d/FILE_ID/view
    - https://drive.google.com/open?id=FILE_ID
    - Raw file ID
    """
    if not url_or_id:
        return url_or_id
    
    # Pattern for /d/FILE_ID/ format (Docs, Sheets, Drive)
    match = re.search(r'/d/([a-zA-Z0-9_-]+)', url_or_id)
    if match:
        return match.group(1)
    
    # Pattern for ?id=FILE_ID format
    match = re.search(r'[?&]id=([a-zA-Z0-9_-]+)', url_or_id)
    if match:
        return match.group(1)
    
    # Assume it's already a file ID
    return url_or_id


def read_file_content(service, file_id: str) -> dict[str, Any]:
    """Read content of a file, handling different MIME types."""
    try:
        # Get file metadata
        file_metadata = service.files().get(
            fileId=file_id,
            fields='id, name, mimeType, webViewLink, modifiedTime'
        ).execute()
        
        mime_type = file_metadata.get('mimeType')
        name = file_metadata.get('name')
        
        # Determine export format based on MIME type
        if mime_type == 'application/vnd.google-apps.document':
            # Google Doc -> Plain text
            request = service.files().export_media(fileId=file_id, mimeType='text/plain')
            export_type = 'Google Doc'
        elif mime_type == 'application/vnd.google-apps.spreadsheet':
            # Google Sheet -> CSV
            request = service.files().export_media(fileId=file_id, mimeType='text/csv')
            export_type = 'Google Sheet'
        elif mime_type == 'application/vnd.google-apps.presentation':
            # Google Slides -> Plain text
            request = service.files().export_media(fileId=file_id, mimeType='text/plain')
            export_type = 'Google Slides'
        else:
            # Regular file -> Download directly
            request = service.files().get_media(fileId=file_id)
            export_type = 'File'
        
        # Download content
        file_content = io.BytesIO()
        downloader = MediaIoBaseDownload(file_content, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()
        
        content_bytes = file_content.getvalue()
        
        # Try to decode as text
        try:
            text = content_bytes.decode('utf-8')
            return {
                "success": True,
                "file_id": file_id,
                "name": name,
                "mime_type": mime_type,
                "export_type": export_type,
                "link": file_metadata.get('webViewLink'),
                "modified_time": file_metadata.get('modifiedTime'),
                "content": text,
                "size_kb": round(len(content_bytes) / 1024, 2)
            }
        except UnicodeDecodeError:
            return {
                "success": False,
                "file_id": file_id,
                "name": name,
                "mime_type": mime_type,
                "error": "File is binary and cannot be read as text"
            }
            
    except Exception as e:
        return {
            "success": False,
            "file_id": file_id,
            "error": str(e)
        }

# =============================================================================
# MCP TOOLS
# =============================================================================

@mcp.tool()
def gdrive_read(file_id_or_url: str) -> dict[str, Any]:
    """
    Read the content of a Google Drive file (Doc, Sheet, or regular file).
    
    Accepts either a file ID or a full Google Drive/Docs/Sheets URL.
    
    Examples:
    - gdrive_read("1xTymhg4_zU4XPDy9XJYXCsaeZmKVCkFUJRr5bvzFNf0")
    - gdrive_read("https://docs.google.com/document/d/1xTymhg4_zU4XPDy9XJYXCsaeZmKVCkFUJRr5bvzFNf0/edit")
    
    Args:
        file_id_or_url: The file ID or full URL of the Google Drive file
    
    Returns:
        JSON with: success, file_id, name, mime_type, content, size_kb
    """
    try:
        file_id = extract_file_id(file_id_or_url)
        service = get_drive_service()
        return read_file_content(service, file_id)
    except Exception as e:
        return {
            "success": False,
            "input": file_id_or_url,
            "error": str(e)
        }


@mcp.tool()
def gdrive_list(
    page_size: int = 20,
    folder_id: Optional[str] = None,
    file_type: Optional[str] = None
) -> dict[str, Any]:
    """
    List files in Google Drive.
    
    Args:
        page_size: Number of files to return (default: 20, max: 100)
        folder_id: Optional folder ID to list files from (can be URL or ID)
        file_type: Optional filter: 'doc', 'sheet', 'slide', 'folder', or 'all' (default)
    
    Returns:
        JSON with: success, count, files[] (each with id, name, mimeType, link)
    """
    try:
        service = get_drive_service()
        
        # Build query
        query_parts = ["trashed = false"]
        
        if folder_id:
            folder_id = extract_file_id(folder_id)
            query_parts.append(f"'{folder_id}' in parents")
        
        # File type filter
        mime_type_map = {
            'doc': 'application/vnd.google-apps.document',
            'sheet': 'application/vnd.google-apps.spreadsheet',
            'slide': 'application/vnd.google-apps.presentation',
            'folder': 'application/vnd.google-apps.folder',
        }
        
        if file_type and file_type in mime_type_map:
            query_parts.append(f"mimeType = '{mime_type_map[file_type]}'")
        
        query = " and ".join(query_parts)
        
        results = service.files().list(
            pageSize=min(page_size, 100),
            fields="nextPageToken, files(id, name, mimeType, webViewLink, modifiedTime, owners)",
            q=query,
            orderBy="modifiedTime desc"
        ).execute()
        
        items = results.get('files', [])
        
        files = []
        for item in items:
            owners = item.get('owners', [{}])
            owner_name = owners[0].get('displayName', 'Unknown') if owners else 'Unknown'
            
            files.append({
                "id": item['id'],
                "name": item['name'],
                "mime_type": item['mimeType'],
                "link": item.get('webViewLink'),
                "modified_time": item.get('modifiedTime', '')[:10],
                "owner": owner_name
            })
        
        return {
            "success": True,
            "count": len(files),
            "files": files
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


@mcp.tool()
def gdrive_search(
    query: str,
    page_size: int = 20
) -> dict[str, Any]:
    """
    Search for files in Google Drive by name.
    
    Args:
        query: Search term (searches in file names)
        page_size: Number of results to return (default: 20)
    
    Returns:
        JSON with: success, count, files[] (each with id, name, mimeType, link)
    
    Examples:
    - gdrive_search("project plan")
    - gdrive_search("Q4 report")
    """
    try:
        service = get_drive_service()
        
        # Build search query
        full_query = f"trashed = false and name contains '{query}'"
        
        results = service.files().list(
            pageSize=min(page_size, 100),
            fields="nextPageToken, files(id, name, mimeType, webViewLink, modifiedTime, owners)",
            q=full_query,
            orderBy="modifiedTime desc"
        ).execute()
        
        items = results.get('files', [])
        
        files = []
        for item in items:
            owners = item.get('owners', [{}])
            owner_name = owners[0].get('displayName', 'Unknown') if owners else 'Unknown'
            
            files.append({
                "id": item['id'],
                "name": item['name'],
                "mime_type": item['mimeType'],
                "link": item.get('webViewLink'),
                "modified_time": item.get('modifiedTime', '')[:10],
                "owner": owner_name
            })
        
        return {
            "success": True,
            "query": query,
            "count": len(files),
            "files": files
        }
        
    except Exception as e:
        return {
            "success": False,
            "query": query,
            "error": str(e)
        }


@mcp.tool()
def gdrive_get_info(file_id_or_url: str) -> dict[str, Any]:
    """
    Get metadata about a Google Drive file without reading its content.
    
    Args:
        file_id_or_url: The file ID or full URL
    
    Returns:
        JSON with: success, file_id, name, mime_type, size, link, modified_time, owner
    """
    try:
        file_id = extract_file_id(file_id_or_url)
        service = get_drive_service()
        
        file_metadata = service.files().get(
            fileId=file_id,
            fields='id, name, mimeType, size, webViewLink, modifiedTime, owners, createdTime'
        ).execute()
        
        owners = file_metadata.get('owners', [{}])
        owner_name = owners[0].get('displayName', 'Unknown') if owners else 'Unknown'
        owner_email = owners[0].get('emailAddress', 'Unknown') if owners else 'Unknown'
        
        return {
            "success": True,
            "file_id": file_metadata['id'],
            "name": file_metadata['name'],
            "mime_type": file_metadata['mimeType'],
            "size_bytes": file_metadata.get('size'),
            "link": file_metadata.get('webViewLink'),
            "created_time": file_metadata.get('createdTime'),
            "modified_time": file_metadata.get('modifiedTime'),
            "owner": owner_name,
            "owner_email": owner_email
        }
        
    except Exception as e:
        return {
            "success": False,
            "input": file_id_or_url,
            "error": str(e)
        }


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    mcp.run()
