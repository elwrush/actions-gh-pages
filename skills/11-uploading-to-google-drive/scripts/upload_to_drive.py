import os
import sys
import argparse
import google.auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.exceptions import DefaultCredentialsError

# Scopes required by the API
SCOPES = ['https://www.googleapis.com/auth/drive']

def get_adc_credentials():
    """
    Automatically finds credentials using Application Default Credentials (ADC).
    Follows the priority:
    1. GOOGLE_APPLICATION_CREDENTIALS env var
    2. GCloud CLI default credentials
    3. Attached service accounts (Cloud)
    """
    try:
        creds, project = google.auth.default(scopes=SCOPES)
        return creds
    except DefaultCredentialsError as e:
        print(f"Error: Application Default Credentials (ADC) not found. {e}")
        print("To fix this locally, run: gcloud auth application-default login")
        print("Or set the GOOGLE_APPLICATION_CREDENTIALS environment variable to your service account JSON key.")
        return None

def create_folder(folder_name, parent_id):
    """Creates a folder in Google Drive using ADC."""
    creds = get_adc_credentials()
    if not creds:
        return None

    try:
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [parent_id]
        }
        
        folder = service.files().create(
            body=file_metadata,
            fields='id, webViewLink'
        ).execute()
        
        return folder
    except Exception as e:
        print(f"Error during folder creation: {e}")
        return None

def upload_file(file_path, folder_id):
    """Uploads a file to Google Drive using ADC."""
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return None

    creds = get_adc_credentials()
    if not creds:
        return None

    try:
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {
            'name': os.path.basename(file_path),
            'parents': [folder_id]
        }
        
        media = MediaFileUpload(file_path, resumable=True)
        
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, webViewLink'
        ).execute()
        
        return file
    except Exception as e:
        print(f"Error during upload: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Interact with Google Drive using ADC.')
    subparsers = parser.add_subparsers(dest='command', help='Sub-commands')

    # Upload command
    upload_parser = subparsers.add_parser('upload', help='Upload a file')
    upload_parser.add_argument('file_path', help='Path to the file to upload')
    upload_parser.add_argument('folder_id', help='Google Drive Folder ID')

    # Create Folder command
    folder_parser = subparsers.add_parser('create-folder', help='Create a folder')
    folder_parser.add_argument('folder_name', help='Name of the folder to create')
    folder_parser.add_argument('parent_id', help='Parent Folder ID')

    args = parser.parse_args()

    if args.command == 'upload':
        result = upload_file(args.file_path, args.folder_id)
        if result:
            print(f"SUCCESS: File uploaded.")
            print(f"File ID: {result.get('id')}")
            print(f"Link: {result.get('webViewLink')}")
        else:
            sys.exit(1)
    elif args.command == 'create-folder':
        result = create_folder(args.folder_name, args.parent_id)
        if result:
            print(f"SUCCESS: Folder created.")
            print(f"Folder ID: {result.get('id')}")
            print(f"Link: {result.get('webViewLink')}")
        else:
            sys.exit(1)
    else:
        parser.print_help()
