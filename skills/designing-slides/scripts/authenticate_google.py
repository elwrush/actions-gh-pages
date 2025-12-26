"""
Google API Authentication Module

Handles OAuth 2.0 authentication for Google Slides and Docs APIs.
"""

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes for Google APIs
SLIDES_SCOPES = [
    'https://www.googleapis.com/auth/presentations',
    'https://www.googleapis.com/auth/drive.file'
]

DOCS_SCOPES = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive.file'
]

def _get_credentials(scopes):
    """Internal function to get or refresh credentials."""
    creds = None
    token_path = '.credentials/token.json'
    credentials_path = '.credentials/credentials.json'
    
    # Load existing credentials
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, scopes)
    
    # Refresh or create new credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, scopes)
            creds = flow.run_local_server(port=0)
        
        # Save credentials
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    
    return creds

def authenticate_slides():
    """
    Authenticate and return Google Slides API service.
    
    Returns:
        googleapiclient.discovery.Resource: Slides API service object
    """
    creds = _get_credentials(SLIDES_SCOPES)
    return build('slides', 'v1', credentials=creds)

def authenticate_docs():
    """
    Authenticate and return Google Docs API service.
    
    Returns:
        googleapiclient.discovery.Resource: Docs API service object
    """
    creds = _get_credentials(DOCS_SCOPES)
    return build('docs', 'v1', credentials=creds)

def authenticate_drive():
    """
    Authenticate and return Google Drive API service.
    
    Returns:
        googleapiclient.discovery.Resource: Drive API service object
    """
    creds = _get_credentials(SLIDES_SCOPES + DOCS_SCOPES)
    return build('drive', 'v3', credentials=creds)
