import pypdf
import sys
import os

def extract_text(pdf_path, output_path):
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n\n"
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"[OK] Extracted text to {output_path}")
    except Exception as e:
        print(f"[ERROR] Extraction failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_pdf.py <pdf_path> <output_path>")
        sys.exit(1)
    extract_text(sys.argv[1], sys.argv[2])
