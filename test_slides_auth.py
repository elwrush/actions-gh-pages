"""
Test script to verify Google Slides API authentication.

This script:
1. Authenticates using OAuth 2.0 credentials
2. Creates a simple test presentation
3. Verifies the Slides API is working correctly
"""

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Scopes required for Google Slides API
SCOPES = [
    'https://www.googleapis.com/auth/presentations',
    'https://www.googleapis.com/auth/drive.file'
]


def authenticate():
    """Authenticate and return the Slides API service."""
    creds = None
    token_path = '.credentials/token.json'
    credentials_path = '.credentials/credentials.json'
    
    # Strategy 1: Try Application Default Credentials (ADC)
    import os
    from pathlib import Path
    adc_path = Path(os.environ.get('APPDATA', '')) / 'gcloud' / 'application_default_credentials.json'
    
    if adc_path.exists():
        try:
            creds = Credentials.from_authorized_user_file(str(adc_path), SCOPES)
            if creds and creds.valid:
                print("✓ Using Application Default Credentials (ADC)")
                return build('slides', 'v1', credentials=creds)
            elif creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
                print("✓ Using Application Default Credentials (ADC) [refreshed]")
                return build('slides', 'v1', credentials=creds)
        except Exception as e:
            print(f"⚠ ADC found but failed to load: {e}")

    # Strategy 2: Legacy OAuth flow (fallback)
    print("⚠ ADC not configured, falling back to legacy OAuth...")
    
    # Check if we have valid credentials saved
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    # If no valid credentials, authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing expired credentials...")
            creds.refresh(Request())
        else:
            print("Starting OAuth flow...")
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save credentials for next time
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
        print(f"Credentials saved to {token_path}")
    
    print("✓ Using legacy OAuth credentials")
    return build('slides', 'v1', credentials=creds)

def create_test_presentation(service):
    """Create a simple test presentation."""
    try:
        # Create a new presentation
        presentation = {
            'title': 'Google Slides API Test - ' + 
                     __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        presentation = service.presentations().create(body=presentation).execute()
        
        print(f"✅ SUCCESS!")
        print(f"Presentation created: {presentation.get('title')}")
        print(f"Presentation ID: {presentation.get('presentationId')}")
        print(f"View it: https://docs.google.com/presentation/d/{presentation.get('presentationId')}/edit")
        
        return presentation.get('presentationId')
    
    except HttpError as error:
        print(f"❌ ERROR: {error}")
        return None

def main():
    """Main function."""
    print("=" * 60)
    print("Google Slides API Authentication Test")
    print("=" * 60)
    
    # Authenticate
    service = authenticate()
    print("✅ Authentication successful!")
    
    # Create test presentation
    print("\nCreating test presentation...")
    presentation_id = create_test_presentation(service)
    
    if presentation_id:
        print("\n" + "=" * 60)
        print("🎉 Google Slides API is working correctly!")
        print("=" * 60)

if __name__ == '__main__':
    main()
