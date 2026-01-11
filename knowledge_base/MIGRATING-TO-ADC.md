\# Migrating to Application Default Credentials (ADC)



> \*\*Purpose\*\*: This guide helps agents migrate Python scripts from manual OAuth token management to Google's Application Default Credentials (ADC) system.



---



\## Why Migrate to ADC?



| Manual OAuth | ADC |

|--------------|-----|

| Each script manages its own `token.json` | Centralized credentials managed by gcloud |

| Token refresh logic in every script | Automatic token refresh by Google libraries |

| Credentials tied to project folders | Works across all projects on the machine |

| Requires client secret files | No client secrets needed after setup |

| Browser auth flow per-project | One-time browser auth covers everything |



---



\## Prerequisites



1\. \*\*Google Cloud SDK\*\* installed and in PATH

&nbsp;  ```powershell

&nbsp;  gcloud --version

&nbsp;  ```



2\. \*\*Python packages\*\* installed:

&nbsp;  ```powershell

&nbsp;  pip install google-auth google-auth-oauthlib google-api-python-client

&nbsp;  ```



---



\## Step 1: Set Up ADC (One-Time)



Run this command to authenticate with the required scopes:



```powershell

\# Clear any conflicting environment variable first

$env:GOOGLE\_APPLICATION\_CREDENTIALS = ""



\# Authenticate with required scopes

gcloud auth application-default login --scopes="openid,https://www.googleapis.com/auth/userinfo.email,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/drive.file"

```



> \*\*Note\*\*: Add additional scopes as needed (e.g., `https://www.googleapis.com/auth/spreadsheets` for Sheets API).



A browser window will open. Complete the Google login and grant permissions.



\### Verify ADC Setup



```powershell

\# Check if credentials file exists

Test-Path "$env:APPDATA\\gcloud\\application\_default\_credentials.json"

\# Should return: True

```



---



\## Step 2: Migrate Your Python Code



\### Before (Manual OAuth)



```python

from google.auth.transport.requests import Request

from google.oauth2.credentials import Credentials

from google\_auth\_oauthlib.flow import InstalledAppFlow



SCOPES = \['https://www.googleapis.com/auth/drive.file']

TOKEN\_FILE = ".credentials/token.json"

CLIENT\_SECRET\_FILE = ".credentials/client\_secret.json"



def authenticate():

&nbsp;   creds = None

&nbsp;   if os.path.exists(TOKEN\_FILE):

&nbsp;       creds = Credentials.from\_authorized\_user\_file(TOKEN\_FILE, SCOPES)

&nbsp;   

&nbsp;   if not creds or not creds.valid:

&nbsp;       if creds and creds.expired and creds.refresh\_token:

&nbsp;           creds.refresh(Request())

&nbsp;       else:

&nbsp;           flow = InstalledAppFlow.from\_client\_secrets\_file(

&nbsp;               CLIENT\_SECRET\_FILE, SCOPES)

&nbsp;           creds = flow.run\_local\_server(port=0)

&nbsp;       

&nbsp;       with open(TOKEN\_FILE, 'w') as token:

&nbsp;           token.write(creds.to\_json())

&nbsp;   

&nbsp;   return creds

```



\### After (ADC with Fallback)



```python

import os

from pathlib import Path

from google.auth.transport.requests import Request

from google.oauth2.credentials import Credentials

from google\_auth\_oauthlib.flow import InstalledAppFlow



SCOPES = \['https://www.googleapis.com/auth/drive.file']



\# Legacy paths (for fallback only)

CREDENTIALS\_DIR = Path(".credentials")

CLIENT\_SECRET\_FILE = CREDENTIALS\_DIR / "client\_secret.json"

TOKEN\_FILE = CREDENTIALS\_DIR / "token.json"



def authenticate():

&nbsp;   """

&nbsp;   Authenticate using ADC first, falling back to legacy OAuth if ADC fails.

&nbsp;   

&nbsp;   ADC Setup:

&nbsp;   1. Run: gcloud auth application-default login --scopes="openid,..."

&nbsp;   2. Or set GOOGLE\_APPLICATION\_CREDENTIALS env var to a service account JSON

&nbsp;   """

&nbsp;   creds = None

&nbsp;   

&nbsp;   # Strategy 1: Try Application Default Credentials (ADC)

&nbsp;   adc\_path = Path(os.environ.get('APPDATA', '')) / 'gcloud' / 'application\_default\_credentials.json'

&nbsp;   

&nbsp;   if adc\_path.exists():

&nbsp;       try:

&nbsp;           creds = Credentials.from\_authorized\_user\_file(str(adc\_path), SCOPES)

&nbsp;           if creds and creds.valid:

&nbsp;               print("✓ Using Application Default Credentials (ADC)")

&nbsp;               return creds

&nbsp;           elif creds and creds.expired and creds.refresh\_token:

&nbsp;               creds.refresh(Request())

&nbsp;               print("✓ Using Application Default Credentials (ADC) \[refreshed]")

&nbsp;               return creds

&nbsp;       except Exception as e:

&nbsp;           print(f"⚠ ADC found but failed to load: {e}")

&nbsp;   

&nbsp;   # Strategy 2: Legacy OAuth flow (fallback)

&nbsp;   print("⚠ ADC not configured, falling back to legacy OAuth...")

&nbsp;   

&nbsp;   if TOKEN\_FILE.exists():

&nbsp;       creds = Credentials.from\_authorized\_user\_file(str(TOKEN\_FILE), SCOPES)

&nbsp;   

&nbsp;   if not creds or not creds.valid:

&nbsp;       if creds and creds.expired and creds.refresh\_token:

&nbsp;           creds.refresh(Request())

&nbsp;       else:

&nbsp;           if not CLIENT\_SECRET\_FILE.exists():

&nbsp;               print(f"ERROR: No credentials available.")

&nbsp;               print("\\nTo fix this, either:")

&nbsp;               print("  1. Run: gcloud auth application-default login --scopes=...")

&nbsp;               print(f"  2. Place OAuth client secrets at: {CLIENT\_SECRET\_FILE}")

&nbsp;               raise FileNotFoundError("No credentials available")

&nbsp;               

&nbsp;           flow = InstalledAppFlow.from\_client\_secrets\_file(

&nbsp;               str(CLIENT\_SECRET\_FILE), SCOPES)

&nbsp;           creds = flow.run\_local\_server(port=0)

&nbsp;       

&nbsp;       with open(TOKEN\_FILE, 'w') as token:

&nbsp;           token.write(creds.to\_json())

&nbsp;   

&nbsp;   print("✓ Using legacy OAuth credentials")

&nbsp;   return creds

```



---



\## Step 3: Cross-Platform Considerations



The ADC path varies by operating system:



```python

import os

from pathlib import Path



def get\_adc\_path():

&nbsp;   """Get the ADC credentials path for the current OS."""

&nbsp;   if os.name == 'nt':  # Windows

&nbsp;       return Path(os.environ.get('APPDATA', '')) / 'gcloud' / 'application\_default\_credentials.json'

&nbsp;   else:  # Linux/macOS

&nbsp;       return Path.home() / '.config' / 'gcloud' / 'application\_default\_credentials.json'

```



---



\## Common Scopes Reference



| Service | Scope |

|---------|-------|

| Google Drive (files) | `https://www.googleapis.com/auth/drive.file` |

| Google Drive (full) | `https://www.googleapis.com/auth/drive` |

| Google Sheets | `https://www.googleapis.com/auth/spreadsheets` |

| Google Docs | `https://www.googleapis.com/auth/documents` |

| Google Slides | `https://www.googleapis.com/auth/presentations` |

| Gmail | `https://www.googleapis.com/auth/gmail.modify` |



To add multiple scopes during ADC setup:



```powershell

gcloud auth application-default login --scopes="openid,https://www.googleapis.com/auth/userinfo.email,https://www.googleapis.com/auth/drive.file,https://www.googleapis.com/auth/spreadsheets"

```



---



\## Troubleshooting



\### "ADC not configured" but file exists



\*\*Cause\*\*: The scopes in the ADC file don't match what your script requests.



\*\*Fix\*\*: Re-run the gcloud auth command with all required scopes:

```powershell

gcloud auth application-default login --scopes="openid,https://www.googleapis.com/auth/userinfo.email,<YOUR\_SCOPES>"

```



\### "GOOGLE\_APPLICATION\_CREDENTIALS is set" warning



\*\*Cause\*\*: An environment variable is pointing to a different credentials file.



\*\*Fix\*\*: Clear it before running gcloud auth:

```powershell

$env:GOOGLE\_APPLICATION\_CREDENTIALS = ""

```



\### "Invalid grant" or "Token expired" errors



\*\*Cause\*\*: The ADC token has expired and can't be refreshed.



\*\*Fix\*\*: Re-authenticate:

```powershell

gcloud auth application-default revoke

gcloud auth application-default login --scopes="..."

```



---



\## Service Account Alternative



For server/CI environments without interactive login, use a service account:



1\. Create a service account in Google Cloud Console

2\. Download the JSON key file

3\. Set the environment variable:

&nbsp;  ```powershell

&nbsp;  $env:GOOGLE\_APPLICATION\_CREDENTIALS = "C:\\path\\to\\service-account.json"

&nbsp;  ```



The `google.auth.default()` function will automatically use it.



---



\## Migration Checklist



\- \[ ] Verify gcloud CLI is installed

\- \[ ] Run `gcloud auth application-default login` with required scopes

\- \[ ] Update `authenticate()` function to try ADC first

\- \[ ] Keep legacy OAuth as fallback for backwards compatibility

\- \[ ] Test upload/API call shows "✓ Using Application Default Credentials (ADC)"

\- \[ ] (Optional) Remove old `token.json` files after confirming ADC works



