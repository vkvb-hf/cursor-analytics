import os
import json
from typing import Any
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("Google Sheets MCP")

# Google Sheets API setup
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = os.getenv('GOOGLE_SERVICE_ACCOUNT_FILE', 'service-account.json')

def get_sheets_service():
    """Create and return Google Sheets API service"""
    try:
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )
        service = build('sheets', 'v4', credentials=credentials)
        return service
    except Exception as e:
        raise Exception(f"Failed to create Sheets service: {str(e)}")

@mcp.tool()
def read_sheet(spreadsheet_id: str, range_name: str = "Sheet1") -> dict[str, Any]:
    """
    Read data from a Google Sheet.
    
    Args:
        spreadsheet_id: The ID of the spreadsheet (from the URL)
        range_name: The A1 notation of the range to retrieve (default: "Sheet1")
    
    Returns:
        Dictionary containing the sheet data
    """
    try:
        service = get_sheets_service()
        sheet = service.spreadsheets()
        result = sheet.values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name
        ).execute()
        
        values = result.get('values', [])
        
        if not values:
            return {
                "success": True,
                "message": "No data found in the sheet",
                "data": []
            }
        
        # Convert to list of dictionaries using first row as headers
        if len(values) > 1:
            headers = values[0]
            data = []
            for row in values[1:]:
                # Pad row with empty strings if it's shorter than headers
                padded_row = row + [''] * (len(headers) - len(row))
                row_dict = dict(zip(headers, padded_row))
                data.append(row_dict)
            
            return {
                "success": True,
                "headers": headers,
                "row_count": len(data),
                "data": data
            }
        else:
            return {
                "success": True,
                "message": "Only headers found",
                "headers": values[0],
                "data": []
            }
            
    except HttpError as error:
        return {
            "success": False,
            "error": f"Google Sheets API error: {str(error)}"
        }
    except Exception as error:
        return {
            "success": False,
            "error": f"Error reading sheet: {str(error)}"
        }

@mcp.tool()
def get_sheet_info(spreadsheet_id: str) -> dict[str, Any]:
    """
    Get information about a Google Sheet (sheet names, properties, etc.)
    
    Args:
        spreadsheet_id: The ID of the spreadsheet
    
    Returns:
        Dictionary containing spreadsheet metadata
    """
    try:
        service = get_sheets_service()
        sheet = service.spreadsheets()
        result = sheet.get(spreadsheetId=spreadsheet_id).execute()
        
        sheets_info = []
        for sheet_data in result.get('sheets', []):
            properties = sheet_data.get('properties', {})
            sheets_info.append({
                'title': properties.get('title'),
                'sheetId': properties.get('sheetId'),
                'index': properties.get('index'),
                'rowCount': properties.get('gridProperties', {}).get('rowCount'),
                'columnCount': properties.get('gridProperties', {}).get('columnCount')
            })
        
        return {
            "success": True,
            "spreadsheet_title": result.get('properties', {}).get('title'),
            "spreadsheet_id": spreadsheet_id,
            "sheets": sheets_info
        }
        
    except HttpError as error:
        return {
            "success": False,
            "error": f"Google Sheets API error: {str(error)}"
        }
    except Exception as error:
        return {
            "success": False,
            "error": f"Error getting sheet info: {str(error)}"
        }

@mcp.tool()
def read_multiple_ranges(spreadsheet_id: str, ranges: list[str]) -> dict[str, Any]:
    """
    Read multiple ranges from a Google Sheet at once.
    
    Args:
        spreadsheet_id: The ID of the spreadsheet
        ranges: List of A1 notation ranges (e.g., ["Sheet1!A1:B10", "Sheet2!C1:D5"])
    
    Returns:
        Dictionary containing data from all requested ranges
    """
    try:
        service = get_sheets_service()
        sheet = service.spreadsheets()
        result = sheet.values().batchGet(
            spreadsheetId=spreadsheet_id,
            ranges=ranges
        ).execute()
        
        value_ranges = result.get('valueRanges', [])
        
        data = {}
        for i, value_range in enumerate(value_ranges):
            range_name = ranges[i]
            values = value_range.get('values', [])
            data[range_name] = values
        
        return {
            "success": True,
            "ranges": data
        }
        
    except HttpError as error:
        return {
            "success": False,
            "error": f"Google Sheets API error: {str(error)}"
        }
    except Exception as error:
        return {
            "success": False,
            "error": f"Error reading ranges: {str(error)}"
        }

@mcp.tool()
def read_comments(spreadsheet_id: str, sheet_name: str = None, range_name: str = None) -> dict[str, Any]:
    """
    Read comments from a Google Sheet. Can retrieve all comments or filter by sheet/range.
    
    Args:
        spreadsheet_id: The ID of the spreadsheet
        sheet_name: Optional - specific sheet name to get comments from
        range_name: Optional - A1 notation range to get comments from (e.g., "Sheet1!A1:B10")
    
    Returns:
        Dictionary containing comments with their locations and content
    """
    try:
        service = get_sheets_service()
        
        # Get spreadsheet with includeGridData to access comments
        fields = "sheets(properties(title,sheetId),data(rowData(values(note,userEnteredValue))))"
        if range_name:
            result = service.spreadsheets().get(
                spreadsheetId=spreadsheet_id,
                ranges=[range_name],
                fields=fields
            ).execute()
        else:
            result = service.spreadsheets().get(
                spreadsheetId=spreadsheet_id,
                includeGridData=True,
                fields=fields
            ).execute()
        
        all_comments = []
        
        for sheet in result.get('sheets', []):
            sheet_title = sheet.get('properties', {}).get('title')
            sheet_id = sheet.get('properties', {}).get('sheetId')
            
            # Skip if filtering by sheet name and this isn't it
            if sheet_name and sheet_title != sheet_name:
                continue
            
            # Process grid data
            for grid_data in sheet.get('data', []):
                start_row = grid_data.get('startRow', 0)
                start_col = grid_data.get('startColumn', 0)
                
                for row_idx, row_data in enumerate(grid_data.get('rowData', [])):
                    for col_idx, cell in enumerate(row_data.get('values', [])):
                        note = cell.get('note')
                        if note:
                            actual_row = start_row + row_idx + 1  # 1-indexed for A1 notation
                            actual_col = start_col + col_idx
                            col_letter = _column_number_to_letter(actual_col + 1)  # 1-indexed
                            cell_ref = f"{col_letter}{actual_row}"
                            
                            # Get cell value if available
                            cell_value = None
                            user_entered = cell.get('userEnteredValue')
                            if user_entered:
                                if 'stringValue' in user_entered:
                                    cell_value = user_entered['stringValue']
                                elif 'numberValue' in user_entered:
                                    cell_value = user_entered['numberValue']
                                elif 'boolValue' in user_entered:
                                    cell_value = user_entered['boolValue']
                                elif 'formulaValue' in user_entered:
                                    cell_value = user_entered['formulaValue']
                            
                            all_comments.append({
                                'sheet': sheet_title,
                                'sheetId': sheet_id,
                                'cell': cell_ref,
                                'fullReference': f"{sheet_title}!{cell_ref}",
                                'row': actual_row,
                                'column': col_letter,
                                'cellValue': cell_value,
                                'comment': note
                            })
        
        return {
            "success": True,
            "comment_count": len(all_comments),
            "comments": all_comments
        }
        
    except HttpError as error:
        return {
            "success": False,
            "error": f"Google Sheets API error: {str(error)}"
        }
    except Exception as error:
        return {
            "success": False,
            "error": f"Error reading comments: {str(error)}"
        }

def _column_number_to_letter(col_num: int) -> str:
    """Convert column number (1-indexed) to letter (A, B, ..., Z, AA, AB, ...)"""
    result = ""
    while col_num > 0:
        col_num -= 1
        result = chr(col_num % 26 + ord('A')) + result
        col_num //= 26
    return result

if __name__ == "__main__":
    mcp.run()
