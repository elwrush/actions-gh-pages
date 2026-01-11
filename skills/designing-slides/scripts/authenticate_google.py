"""
Google API Authentication Module

Handles OAuth 2.0 authentication for Google Slides and Docs APIs.
Prioritizes Application Default Credentials (ADC) over manual token management.
"""

import os
from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes for Google APIs
# Using broader 'drive' scope instead of 'drive.file' for better compatibility with existing ADC tokens
SLIDES_SCOPES = [
    'https://www.googleapis.com/auth/presentations',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/documents'
]

DOCS_SCOPES = SLIDES_SCOPES

# Legacy paths
CREDENTIALS_DIR = Path(".credentials")
CLIENT_SECRET_FILE = CREDENTIALS_DIR / "credentials.json"
TOKEN_FILE = CREDENTIALS_DIR / "token.json"
GDOCS_TOKEN_FILE = CREDENTIALS_DIR / "gdocs-token.json"

def _get_credentials(scopes):
    """
    Internal function to get or refresh credentials.
    Prioritizes ADC, falls back to gdocs-token.json, then token.json.
    """
    creds = None
    
    # Strategy 1: Try Application Default Credentials (ADC)
    adc_path = Path(os.environ.get('APPDATA', '')) / 'gcloud' / 'application_default_credentials.json'
    
    if adc_path.exists():
        try:
            creds = Credentials.from_authorized_user_file(str(adc_path), scopes)
            if creds and creds.valid:
                print("[OK] Using Application Default Credentials (ADC)")
                return creds
            elif creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
                print("[OK] Using Application Default Credentials (ADC) [refreshed]")
                return creds
        except Exception as e:
            print(f"[WARN] ADC Scope/Refresh Issue: {e}")

    # Strategy 2: Try gdocs-token.json (often more recent)
    if GDOCS_TOKEN_FILE.exists():
        try:
            creds = Credentials.from_authorized_user_file(str(GDOCS_TOKEN_FILE), scopes)
            if creds and creds.valid:
                print("[OK] Using gdocs-token.json")
                return creds
            elif creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
                print("[OK] Using gdocs-token.json [refreshed]")
                return creds
        except Exception as e:
            print(f"[WARN] gdocs-token issue: {e}")

    # Strategy 3: Legacy token.json
    if TOKEN_FILE.exists():
        try:
            creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), scopes)
            if creds and creds.valid:
                print("[OK] Using token.json")
                return creds
            elif creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
                print("[OK] Using token.json [refreshed]")
                return creds
        except Exception as e:
            print(f"[WARN] token.json issue: {e}")

    if not creds or not creds.valid:
        print(f"\n❌ AUTHENTICATION FAILED")
        print("Please refresh your credentials by running:")
        print("gcloud auth application-default login --scopes=\"https://www.googleapis.com/auth/presentations,https://www.googleapis.com/auth/drive,https://www.googleapis.com/auth/documents\"")
        
        # We don't run flow.run_local_server here because it hangs in agent mode
        raise Exception("Authentication required. Please run the gcloud command above.")

    return creds

def authenticate_slides():
    """Authenticate and return Google Slides API service."""
    creds = _get_credentials(SLIDES_SCOPES)
    return build('slides', 'v1', credentials=creds)

def authenticate_docs():
    """Authenticate and return Google Docs API service."""
    creds = _get_credentials(DOCS_SCOPES)
    return build('docs', 'v1', credentials=creds)

def authenticate_drive():
    """Authenticate and return Google Drive API service."""
    creds = _get_credentials(SLIDES_SCOPES)
    return build('drive', 'v3', credentials=creds)
