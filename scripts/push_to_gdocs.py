"""
Push to Google Docs Script

Uploads an HTML file to Google Drive and converts it to a Google Doc.
Embeds local images as base64 data URIs for proper rendering.
"""

import argparse
import base64
import io
import os
import re
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

# Get the project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Credentials paths
CREDENTIALS_PATH = os.path.join(PROJECT_ROOT, '.credentials', 'GDocs-credentials.json')
TOKEN_PATH = os.path.join(PROJECT_ROOT, '.credentials', 'gdocs-token.json')

# Scopes needed for Drive upload and Docs formatting
SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/documents'
]

# Default target folder
DEFAULT_FOLDER_ID = '1_n11w9BRN6sd0uaXlqEXjqZuZ74zFiOl'

# A4 page size in points (1 inch = 72 points, A4 = 210mm x 297mm)
A4_WIDTH_PT = 595.276  # 210mm
A4_HEIGHT_PT = 841.89  # 297mm

# 2cm margins in points (1cm = 28.35 points)
MARGIN_2CM_PT = 56.7  # 2cm



def get_credentials():
    """Authenticates and returns Google API credentials."""
    creds = None
    
    # Strategy 1: Try Application Default Credentials (ADC)
    # Windows-specific path as per user OS settings
    # Note: We import Path inside function or at top level if already imported. 
    # Based on file imports, we need to ensure Path is imported or use os.path
    # The file currently uses os, let's stick to os logic or add pathlib
    from pathlib import Path
    adc_path = Path(os.environ.get('APPDATA', '')) / 'gcloud' / 'application_default_credentials.json'
    
    if adc_path.exists():
        try:
            creds = Credentials.from_authorized_user_file(str(adc_path), SCOPES)
            if creds and creds.valid:
                print("✓ Using Application Default Credentials (ADC)")
                return creds
            elif creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
                print("✓ Using Application Default Credentials (ADC) [refreshed]")
                return creds
        except Exception as e:
            print(f"⚠ ADC found but failed to load: {e}")
            
    # Strategy 2: Legacy OAuth flow (fallback)
    print("⚠ ADC not configured, falling back to legacy OAuth...")
    
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
    
    print("✓ Using legacy OAuth credentials")
    return creds


def get_drive_service(creds=None):
    """Returns Google Drive API service."""
    if creds is None:
        creds = get_credentials()
    return build('drive', 'v3', credentials=creds)


def get_docs_service(creds=None):
    """Returns Google Docs API service."""
    if creds is None:
        creds = get_credentials()
    return build('docs', 'v1', credentials=creds)


def set_page_format(doc_id, creds):
    """
    Sets A4 page size and 2cm margins on the document.
    
    Args:
        doc_id: Google Doc ID
        creds: Google API credentials
    """
    docs_service = get_docs_service(creds)
    
    requests = [
        {
            'updateDocumentStyle': {
                'documentStyle': {
                    'pageSize': {
                        'width': {'magnitude': A4_WIDTH_PT, 'unit': 'PT'},
                        'height': {'magnitude': A4_HEIGHT_PT, 'unit': 'PT'}
                    },
                    'marginTop': {'magnitude': MARGIN_2CM_PT, 'unit': 'PT'},
                    'marginBottom': {'magnitude': MARGIN_2CM_PT, 'unit': 'PT'},
                    'marginLeft': {'magnitude': MARGIN_2CM_PT, 'unit': 'PT'},
                    'marginRight': {'magnitude': MARGIN_2CM_PT, 'unit': 'PT'}
                },
                'fields': 'pageSize,marginTop,marginBottom,marginLeft,marginRight'
            }
        }
    ]
    
    docs_service.documents().batchUpdate(
        documentId=doc_id,
        body={'requests': requests}
    ).execute()
    
    print("📐 Set page format: A4 with 2cm margins")


def get_mime_type(file_path):
    """Returns the MIME type based on file extension."""
    ext = os.path.splitext(file_path)[1].lower()
    mime_types = {
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.gif': 'image/gif',
        '.webp': 'image/webp',
    }
    return mime_types.get(ext, 'image/png')


def embed_images_as_base64(html_content, html_file_path):
    """
    Finds all local image references in HTML and converts them to base64 data URIs.
    
    Args:
        html_content: The HTML string
        html_file_path: Path to the HTML file (for resolving relative paths)
    
    Returns:
        Modified HTML with embedded base64 images
    """
    html_dir = os.path.dirname(os.path.abspath(html_file_path))
    
    # Pattern to match src attributes with local paths (not http/https/data)
    img_pattern = re.compile(r'(<img[^>]+src=["\'])([^"\']+)(["\'][^>]*>)', re.IGNORECASE)
    
    def replace_with_base64(match):
        prefix = match.group(1)
        src = match.group(2)
        suffix = match.group(3)
        
        # Skip if already a data URI or external URL
        if src.startswith('data:') or src.startswith('http://') or src.startswith('https://'):
            return match.group(0)
        
        # Resolve relative path
        if src.startswith('../'):
            # Handle relative paths like "../images/file.jpg"
            img_path = os.path.normpath(os.path.join(html_dir, src))
        elif src.startswith('/'):
            img_path = src
        else:
            img_path = os.path.join(html_dir, src)
        
        # Check if file exists
        if not os.path.exists(img_path):
            print(f"⚠️  Image not found: {img_path}")
            return match.group(0)
        
        # Read and encode image
        try:
            with open(img_path, 'rb') as img_file:
                encoded = base64.b64encode(img_file.read()).decode('utf-8')
            
            mime_type = get_mime_type(img_path)
            data_uri = f"data:{mime_type};base64,{encoded}"
            
            print(f"✅ Embedded: {os.path.basename(img_path)}")
            return f"{prefix}{data_uri}{suffix}"
        
        except Exception as e:
            print(f"⚠️  Failed to embed {img_path}: {e}")
            return match.group(0)
    
    return img_pattern.sub(replace_with_base64, html_content)


def push_to_gdocs(file_path: str, doc_name: str, folder_id: str = None) -> str:
    """
    Upload an HTML file to Google Drive and convert to Google Doc.
    
    Args:
        file_path: Path to the HTML file
        doc_name: Name for the Google Doc
        folder_id: Target folder ID (uses default if not specified)
    
    Returns:
        URL of the created Google Doc
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if folder_id is None:
        folder_id = DEFAULT_FOLDER_ID
    
    # Read HTML content
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    print(f"📄 Processing: {file_path}")
    
    # Embed local images as base64
    html_content = embed_images_as_base64(html_content, file_path)
    
    # Authenticate
    print("🔑 Authenticating...")
    creds = get_credentials()
    service = get_drive_service(creds)
    
    # Prepare upload
    file_metadata = {
        'name': doc_name,
        'mimeType': 'application/vnd.google-apps.document',
        'parents': [folder_id]
    }
    
    # Use MediaIoBaseUpload with BytesIO (the working pattern)
    media = MediaIoBaseUpload(
        io.BytesIO(html_content.encode('utf-8')),
        mimetype='text/html',
        resumable=True
    )
    
    print("📤 Uploading...")
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id, webViewLink'
    ).execute()
    
    doc_url = file.get('webViewLink')
    doc_id = file.get('id')
    
    # Set A4 page format with 2cm margins
    set_page_format(doc_id, creds)
    
    print(f"✅ Created Google Doc: {doc_name}")
    print(f"   ID: {doc_id}")
    print(f"   URL: {doc_url}")
    
    return doc_url


def main():
    parser = argparse.ArgumentParser(
        description='Upload HTML to Google Docs with embedded images'
    )
    parser.add_argument(
        '--file', '-f',
        required=True,
        help='Path to HTML file to upload'
    )
    parser.add_argument(
        '--name', '-n',
        required=True,
        help='Name for the Google Doc'
    )
    parser.add_argument(
        '--folder', '-d',
        default=None,
        help=f'Target folder ID (default: {DEFAULT_FOLDER_ID})'
    )
    
    args = parser.parse_args()
    
    try:
        url = push_to_gdocs(args.file, args.name, args.folder)
        print(f"\n🔗 Open: {url}")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
