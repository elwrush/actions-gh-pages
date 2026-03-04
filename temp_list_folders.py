import google.auth
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def list_folders():
    try:
        creds, project = google.auth.default(scopes=SCOPES)
        service = build('drive', 'v3', credentials=creds)
        
        results = service.files().list(
            q="mimeType='application/vnd.google-apps.folder'",
            pageSize=20, 
            fields="nextPageToken, files(id, name)"
        ).execute()
        
        items = results.get('files', [])
        if not items:
            print('No folders found.')
        else:
            print('Folders found:')
            for item in items:
                print(f"{item['name']} ({item['id']})")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_folders()
