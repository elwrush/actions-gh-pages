import argparse
import os
import sys
import requests
import shutil

# Pixabay API Endpoint
API_URL = "https://pixabay.com/api/"

def download_image(query, output_path, image_type="photo", orientation="horizontal"):
    api_key = os.environ.get("PIXABAY_API_KEY")
    if not api_key:
        print("[ERROR] PIXABAY_API_KEY environment variable is not set.")
        sys.exit(1)

    params = {
        "key": api_key,
        "q": query,
        "image_type": image_type,
        "orientation": orientation,
        "per_page": 3,  # Fetch top 3 to pick best
        "safesearch": "true"
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        if int(data["totalHits"]) > 0:
            # Pick the first result (most relevant)
            image_url = data["hits"][0]["largeImageURL"] # Use largeImageURL for better quality
            
            print(f"[INFO] Found image: {image_url}")
            
            # Download
            img_response = requests.get(image_url, stream=True)
            img_response.raise_for_status()

            # Create directory if missing
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            with open(output_path, 'wb') as f:
                img_response.raw.decode_content = True
                shutil.copyfileobj(img_response.raw, f)
            
            print(f"[SUCCESS] Saved to: {output_path}")
            return True
        else:
            print(f"[WARN] No images found for query: '{query}'")
            return False

    except Exception as e:
        print(f"[ERROR] Failed to download image: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download images from Pixabay.")
    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--type", default="photo", choices=["all", "photo", "illustration", "vector"], help="Image type")
    parser.add_argument("--orientation", default="horizontal", choices=["all", "horizontal", "vertical"], help="Orientation")

    args = parser.parse_args()

    success = download_image(args.query, args.output, args.type, args.orientation)
    if not success:
        sys.exit(1)
