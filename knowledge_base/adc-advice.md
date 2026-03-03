# Engineering Guide: Application Default Credentials (ADC) Implementation

## Overview
This project has transitioned from explicit service account JSON key loading to **Application Default Credentials (ADC)**. This change improves security by removing hardcoded file paths and simplifies environment configuration across local development and production (CI/CD, Cloud) environments.

---

## 1. Why ADC?
*   **Security:** Prevents "secret leakage" by avoiding the need to pass around or hardcode paths to `.json` credential files.
*   **Portability:** The same code works locally (using your user identity or a local key) and in the cloud (using Attached Service Accounts) without modification.
*   **Standardization:** Follows Google's recommended "Best Practice" for library authentication.

---

## 2. Code Implementation (Python)

### The Legacy Way (Deprecated)
Previously, we used `google.oauth2.service_account` which required finding and loading a specific file:
```python
from google.oauth2.service_account import Credentials
# Hardcoded or searched path
cred_file = ".credentials/service-account.json"
creds = Credentials.from_service_account_file(cred_file, scopes=SCOPES)
```

### The ADC Way (Current Standard)
We now use `google.auth` to automatically discover the credentials from the environment:
```python
import google.auth
from googleapiclient.discovery import build

# 1. Automatically find credentials
creds, project = google.auth.default(scopes=SCOPES)

# 2. Use the credentials to build the service
service = build('drive', 'v3', credentials=creds)
```

---

## 3. Environment Setup

To use ADC, the environment must be configured so the library knows which identity to assume.

### Local Development (Using a Key)
If you are working locally and have a JSON key, set the following environment variable in your terminal:
*   **PowerShell:** `$env:GOOGLE_APPLICATION_CREDENTIALS="C:\path	o\your\key.json"`
*   **Command Prompt:** `set GOOGLE_APPLICATION_CREDENTIALS=C:\path	o\your\key.json`

### Local Development (Using User Identity)
Alternatively, you can authenticate as yourself using the Google Cloud CLI:
```bash
gcloud auth application-default login
```
This creates a local "well-known" file that `google.auth.default()` will find automatically without any environment variables.

---

## 4. Best Practices for Agents
1.  **Remove `find_credentials()`:** If you see functions that search the filesystem for `.json` files in `.credentials/`, refactor them to use ADC.
2.  **Scope Management:** Always pass the required `scopes` to `google.auth.default(scopes=...)` to ensure the credentials have the necessary permissions.
3.  **Graceful Errors:** Handle cases where `google.auth.exceptions.DefaultCredentialsError` might be raised if the environment is not configured.

*Last Updated: February 2026*
