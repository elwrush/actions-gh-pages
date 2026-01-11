---
name: publishing-worksheets
description: >
  Uploads PDF worksheets to a specific Google Drive folder for distribution.
  Use when the user wants to publish, upload, or share worksheets to Google Drive.
---

# Publishing Worksheets Skill

## Description
Uploads PDF worksheets to a specific Google Drive folder for distribution.

## Authentication (ADC)
This skill uses **Application Default Credentials (ADC)** as the primary authentication method. 
- Ensure you have run `gcloud auth application-default login` on your system.
- The script will automatically detect these credentials.
- Fallback to legacy OAuth (`token.json`) is supported but discouraged.

## Setup
Ensure dependencies are installed:
```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## Usage
Use the python script to upload a file.

### Command Line
```bash
python skills/publishing-worksheets/scripts/publish_to_drive.py --file <path_to_pdf>
```

### Workflow
1.  **Generate** the worksheet PDF using the `generating-worksheets` skill.
2.  **Validate** the PDF locally (open file to check branding/layout before upload).
3.  **Publish** using this skill - the Google Drive link will appear in task artifacts.

### Arguments
- `--file`: Path to the local file to upload.
- `--folder`: (Optional) Drive Folder ID. Defaults to `1_n11w9BRN6sd0uaXlqEXjqZuZ74zFiOl`.
- `--name`: (Optional) Custom filename on Drive.
- `--title`: (Optional) Lesson Title. If provided, renames file to `DD-MM-YY-Worksheet-[Title].pdf` (e.g. `12-05-25-Worksheet-Politeness.pdf`).

### Example
```bash
python skills/publishing-worksheets/scripts/publish_to_drive.py --file inputs/Lesson1/worksheet.pdf --title "Politeness"
```
