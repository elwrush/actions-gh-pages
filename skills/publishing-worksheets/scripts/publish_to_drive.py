import argparse
import os
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

# Scopes
SCOPES = [
    'https://www.googleapis.com/auth/drive'
]

DEFAULT_FOLDER_ID = '1_n11w9BRN6sd0uaXlqEXjqZuZ74zFiOl'


def authenticate():
    """Authenticate and return the Drive API service."""
    creds = None
    # Adjust paths relative to project root or current working dir
    # Ideally script is run from project root
    token_path = '.credentials/token.json'
    credentials_path = '.credentials/credentials.json'

    # Strategy 1: Try Application Default Credentials (ADC)
    from pathlib import Path
    adc_path = Path(os.environ.get('APPDATA', '')) / 'gcloud' / 'application_default_credentials.json'
    
    if adc_path.exists():
        try:
            creds = Credentials.from_authorized_user_file(str(adc_path), SCOPES)
            if creds and creds.valid:
                print("✓ Using Application Default Credentials (ADC)")
                return build('drive', 'v3', credentials=creds)
            elif creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
                print("✓ Using Application Default Credentials (ADC) [refreshed]")
                return build('drive', 'v3', credentials=creds)
        except Exception as e:
            print(f"⚠ ADC found but failed to load: {e}")

    # Strategy 2: Legacy OAuth flow (fallback)
    print("⚠ ADC not configured, falling back to legacy OAuth...")
    
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing expired credentials...")
            creds.refresh(Request())
        else:
            print("Starting OAuth flow...")
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save
        os.makedirs(os.path.dirname(token_path), exist_ok=True)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    
    print("✓ Using legacy OAuth credentials")
    return build('drive', 'v3', credentials=creds)

def main():
    parser = argparse.ArgumentParser(description="Upload file to Google Drive.")
    parser.add_argument("--file", required=True, help="Path to file to upload")
    parser.add_argument("--folder", default=DEFAULT_FOLDER_ID, help="Target Folder ID")
    parser.add_argument("--name", help="Custom filename on Drive (overrides custom logic)")
    parser.add_argument("--title", help="Lesson Title (triggers auto-renaming: DD-MM-YY-Worksheet-[Title].pdf)")
    
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File not found: {args.file}")
        return

    try:
        service = authenticate()
        
        # Determine Filename
        drive_filename = args.name if args.name else os.path.basename(args.file)
        
        # Enforce Convention if Title is provided: DD-MM-YY-Worksheet-[Title].pdf
        if args.title:
            import datetime
            date_str = datetime.datetime.now().strftime("%d-%m-%y")
            # Sanitize title file-system safe just in case, though Drive allows most chars
            safe_title = "".join(c for c in args.title if c.isalnum() or c in (' ', '-', '_')).strip()
            drive_filename = f"{date_str}-Worksheet-{safe_title}.pdf"

        file_metadata = {
            'name': drive_filename,
            'parents': [args.folder]
        }
        
        media = MediaFileUpload(args.file, resumable=True)
        
        print(f"Uploading {args.file} to folder {args.folder}...")
        
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, name, webViewLink'
        ).execute()
        
        print(f"✅ Success! File ID: {file.get('id')}")
        print(f"Link: {file.get('webViewLink')}")

    except HttpError as error:
        print(f"❌ An error occurred: {error}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
