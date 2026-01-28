import argparse
import os
import sys
import requests
import shutil

# Pixabay Video API Endpoint
API_URL = "https://pixabay.com/api/videos/"

def download_video(query, output_path, video_type="film"):
    api_key = os.environ.get("PIXABAY_API_KEY")
    if not api_key:
        print("[ERROR] PIXABAY_API_KEY environment variable is not set.")
        sys.exit(1)

    params = {
        "key": api_key,
        "q": query,
        "video_type": video_type,
        "per_page": 3,
        "safesearch": "true"
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        if int(data["totalHits"]) > 0:
            # Pick the first result
            video_hit = data["hits"][0]
            
            # Prefer 'medium' (approx 720p/1080p) or 'large' -> fallback to 'small'
            # The API structure usually has a 'videos' dict with keys 'large', 'medium', 'small', 'tiny'
            videos = video_hit.get("videos", {})
            
            if "medium" in videos and videos["medium"]["url"]:
                video_url = videos["medium"]["url"]
                print(f"[INFO] Selected resolution: medium ({videos['medium']['width']}x{videos['medium']['height']})")
            elif "large" in videos and videos["large"]["url"]:
                video_url = videos["large"]["url"]
                print(f"[INFO] Selected resolution: large ({videos['large']['width']}x{videos['large']['height']})")
            else:
                # Fallback
                video_url = videos.get("small", {}).get("url") or videos.get("tiny", {}).get("url")
                print("[WARN] Fallback to low resolution.")

            if not video_url:
                print("[ERROR] No valid video URL found in hit.")
                return False

            print(f"[INFO] Found video: {video_url}")
            
            # Download
            # Videos can be large, so stream it
            vid_response = requests.get(video_url, stream=True)
            vid_response.raise_for_status()

            # Create directory if missing
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            with open(output_path, 'wb') as f:
                shutil.copyfileobj(vid_response.raw, f)
            
            print(f"[SUCCESS] Saved to: {output_path}")
            return True
        else:
            print(f"[WARN] No videos found for query: '{query}'")
            return False

    except Exception as e:
        print(f"[ERROR] Failed to download video: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download videos from Pixabay.")
    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--type", default="film", choices=["all", "film", "animation"], help="Video type")

    args = parser.parse_args()

    success = download_video(args.query, args.output, args.type)
    if not success:
        sys.exit(1)
