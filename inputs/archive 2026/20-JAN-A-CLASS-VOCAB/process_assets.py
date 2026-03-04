
import os
from PIL import Image
import sys

# Add project root to path to find trim_image if needed, or just run it via subprocess
# But simpler to just use PIL here.

def crop_baker():
    try:
        img_path = "source_page_1.png"
        if not os.path.exists(img_path):
            print(f"Error: {img_path} not found.")
            return

        img = Image.open(img_path)
        w, h = img.size
        
        # Estimate Baker is in top-left, maybe 0 to 40% width, 10% to 50% height (header is at top)
        # Actually in the prompt image 1, the baker is the main visual on the left.
        # Top is "A successful business". Then "Denham Farm Bakery".
        # Baker is left of the text "Denham Farm Bakery is a family business..."
        # So distinct left column.
        # Let's crop x: 0 to 0.35*w, y: 0.15*h to 0.45*h
        
        # Actually I can't see the exact pixels. I'll make a generous crop.
        # Let's try to crop the top-left quadrant but skip the very top header strip.
        left = 0
        top = int(h * 0.15) 
        right = int(w * 0.35)
        bottom = int(h * 0.5)
        
        crop = img.crop((left, top, right, bottom))
        crop.save("baker_raw.png")
        print("Table crop saved to baker_raw.png")
        
    except Exception as e:
        print(f"Error cropping: {e}")

if __name__ == "__main__":
    crop_baker()
