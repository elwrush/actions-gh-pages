---
name: 11-uploading-to-google-drive
description: Uploads files to a specified Google Drive folder or creates subfolders using Application Default Credentials (ADC).
---

# Uploading to Google Drive (ADC Implementation)

## Purpose
This skill automates the process of uploading local files to Google Drive or creating subfolders. It uses **Application Default Credentials (ADC)** for secure, flexible authentication.

## Workflow
1. **Identify Target Root**: Read `knowledge_base/folder-links.md` and prompt for a choice.
2. **Create Subfolder (Optional)**: If requested, create a subfolder within the root and get the new ID.
3. **Identify File(s)**: Locate the paths of the material to be uploaded.
4. **Execute Operation**: Use the `upload_to_drive.py` script (ADC-powered).

## Commands

### Upload a File
```powershell
python skills/11-uploading-to-google-drive/scripts/upload_to_drive.py upload "[FILE_PATH]" "[FOLDER_ID]"
```

### Create a Folder
```powershell
python skills/11-uploading-to-google-drive/scripts/upload_to_drive.py create-folder "[FOLDER_NAME]" "[PARENT_ID]"
```

## Prerequisites
- The environment must be configured for ADC:
  - **Option A (Recommended)**: Run `gcloud auth application-default login` to authenticate as your user.
  - **Option B**: Set `$env:GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\service-account.json"`.
- Python libraries: `google-auth`, `google-api-python-client`.

## Error Handling
- If `DefaultCredentialsError` occurs, guide the user to the `gcloud` login command or environment variable setup.
- If a `404` error occurs, ensure the authenticated identity (User or Service Account) has "Editor" access to the target folder.
