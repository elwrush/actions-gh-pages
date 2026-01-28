
from googleapiclient.discovery import build
import os
from pathlib import Path
from google.oauth2.credentials import Credentials

# Scopes needed
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def get_credentials():
    from pathlib import Path
    adc_path = Path(os.environ.get('APPDATA', '')) / 'gcloud' / 'application_default_credentials.json'
    if adc_path.exists():
        return Credentials.from_authorized_user_file(str(adc_path), SCOPES)
    return None

def check_file(file_id):
    creds = get_credentials()
    if not creds:
        print("No creds found")
        return
    service = build('drive', 'v3', credentials=creds)
    file = service.files().get(fileId=file_id, fields='name, parents').execute()
    print(f"File Name: {file.get('name')}")
    print(f"Parents: {file.get('parents')}")

if __name__ == "__main__":
    check_file('1w4wNCE8Qt8DBX9McfcoR1FGn88l9eW24eFqBtGDqs74')
