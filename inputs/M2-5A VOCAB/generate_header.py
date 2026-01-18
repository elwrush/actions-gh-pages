import os
import requests
import shutil
import json
import base64

# Configuration
API_KEY = os.environ.get("GEMINI_API_KEY")
OUTPUT_PATH = r"C:\PROJECTS\LESSONS AND SLIDESHOWS 2\inputs\M2-5A VOCAB\generated_header.png"
FALLBACK_PATH = r"C:\PROJECTS\LESSONS AND SLIDESHOWS 2\inputs\M2-5A VOCAB\header_banner.jpg"

PROMPT = "Cinematic 8k resolution wide banner image for broadsheet business header 'From Local to Global'. Abstract transition from rustic bakery to modern glass skyline. Dark maroon and teal styling. No text."

def generate_header():
    if not API_KEY:
        print("Error: GEMINI_API_KEY not found in environment.")
        use_fallback()
        return

    url = "https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-001:generateImages"
    
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": API_KEY
    }
    
    data = {
        "prompt": PROMPT,
        "sampleCount": 1,
        "aspectRatio": "16:9" # Attempting wide format
    }

    print(f"Requesting image generation from {url}...")
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            result = response.json()
            # Handle response structure (it varies, usually 'images': [{'image64': ...}])
            # Or 'predictions' in older endpoints. Assuming new generateImages format:
            if "images" in result and len(result["images"]) > 0:
                img_data = result["images"][0].get("image64", result["images"][0].get("bytesBase64Encoded"))
                if img_data:
                    with open(OUTPUT_PATH, "wb") as f:
                        f.write(base64.b64decode(img_data))
                    print(f"Success! Image saved to {OUTPUT_PATH}")
                    return
        
        print(f"Generation failed. Status: {response.status_code}, Response: {response.text}")
        use_fallback()

    except Exception as e:
        print(f"Exception during generation: {e}")
        use_fallback()

def use_fallback():
    print("Using fallback image...")
    if os.path.exists(FALLBACK_PATH):
        shutil.copy(FALLBACK_PATH, OUTPUT_PATH)
        print(f"Copied fallback to {OUTPUT_PATH}")
    else:
        print("Fallback image not found!")

if __name__ == "__main__":
    generate_header()
