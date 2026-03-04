Read a file from Google Drive: $ARGUMENTS

## Step 1 — Extract File ID and Detect Type

Parse `$ARGUMENTS` for a Google Drive URL or file ID:
- **Google Docs**: `https://docs.google.com/document/d/<ID>/...`
- **Google Sheets**: `https://docs.google.com/spreadsheets/d/<ID>/...`
- **Google Slides**: `https://docs.google.com/presentation/d/<ID>/...`
- **Other Drive files**: `https://drive.google.com/file/d/<ID>/...`
- **Bare ID**: a long alphanumeric string with hyphens/underscores

Extract the `<ID>` between `/d/` and the next `/`.

If no valid ID can be extracted, ask the user for the URL.

## Step 2 — Fetch Content

Run the appropriate Python command based on file type. All use auth from `daily_context_updater`.

### Google Docs → plain text
```bash
cd scripts/gdrive && python3 -c "
import warnings; warnings.filterwarnings('ignore')
from daily_context_updater import get_credentials, get_drive_service, read_doc_content
service = get_drive_service(get_credentials())
print(read_doc_content(service, '$FILE_ID', 'doc'))
" 2>/dev/null
```

### Google Sheets → CSV
```bash
cd scripts/gdrive && python3 -c "
import warnings, io; warnings.filterwarnings('ignore')
from daily_context_updater import get_credentials, get_drive_service
from googleapiclient.http import MediaIoBaseDownload
service = get_drive_service(get_credentials())
req = service.files().export_media(fileId='$FILE_ID', mimeType='text/csv')
buf = io.BytesIO()
dl = MediaIoBaseDownload(buf, req)
done = False
while not done: _, done = dl.next_chunk()
print(buf.getvalue().decode('utf-8'))
" 2>/dev/null
```
Note: This exports the **first sheet only**. For multi-sheet spreadsheets, prefer the Google Sheets MCP (`read_sheet`) which supports range selection.

### Google Slides → plain text
```bash
cd scripts/gdrive && python3 -c "
import warnings, io; warnings.filterwarnings('ignore')
from daily_context_updater import get_credentials, get_drive_service
from googleapiclient.http import MediaIoBaseDownload
service = get_drive_service(get_credentials())
req = service.files().export_media(fileId='$FILE_ID', mimeType='text/plain')
buf = io.BytesIO()
dl = MediaIoBaseDownload(buf, req)
done = False
while not done: _, done = dl.next_chunk()
print(buf.getvalue().decode('utf-8'))
" 2>/dev/null
```

### Other files (PDF, CSV, images, etc.) → download raw
```bash
cd scripts/gdrive && python3 -c "
import warnings, io; warnings.filterwarnings('ignore')
from daily_context_updater import get_credentials, get_drive_service
from googleapiclient.http import MediaIoBaseDownload
service = get_drive_service(get_credentials())
# Get file metadata to determine name and type
meta = service.files().get(fileId='$FILE_ID', fields='name,mimeType').execute()
print(f\"File: {meta['name']}\nType: {meta['mimeType']}\n\")
req = service.files().get_media(fileId='$FILE_ID')
buf = io.BytesIO()
dl = MediaIoBaseDownload(buf, req)
done = False
while not done: _, done = dl.next_chunk()
content = buf.getvalue()
try:
    print(content.decode('utf-8'))
except UnicodeDecodeError:
    path = '/tmp/' + meta['name']
    with open(path, 'wb') as f: f.write(content)
    print(f'Binary file saved to: {path}')
" 2>/dev/null
```

Replace `$FILE_ID` with the extracted ID. Suppress stderr warnings.

## Step 3 — Display

- **Text content** (Docs, Slides, CSV): Present as markdown
- **Binary files** (PDF, images): Report the saved path so the user can open it
- **Large Sheets**: Suggest using Google Sheets MCP for range queries instead

If the fetch fails, check:
1. Is `scripts/gdrive/token.json` present? If not, run `python3 scripts/gdrive/daily_context_updater.py --dry-run` once to authenticate.
2. Does the user have access to the file?
