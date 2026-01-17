from PIL import Image
import os
import glob
import numpy as np

IMAGE_DIR = r"c:\PROJECTS\LESSONS AND SLIDESHOWS 2\18-01-26_Fight-or-Flight\images"

def remove_checkerboard(image_path):
    print(f"Aggressive cleaning: {os.path.basename(image_path)}")
    img = Image.open(image_path).convert("RGBA")
    data = np.array(img)

    r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
    
    # Heuristic for "Neutral Pixel" (Checkerboard squares are always neutral gray/white/black)
    # The brain content is VIBRANT (High saturation).
    # Background is DESATURATED (Low saturation).
    
    # Calculate saturation-like metric
    max_val = np.maximum(np.maximum(r, g), b)
    min_val = np.minimum(np.minimum(r, g), b)
    delta = max_val - min_val # High delta = Vibrant color
    
    # Mask 1: Pixels with very low saturation (Gray/White/Black)
    is_desaturated = delta < 30 
    
    # Combine: If it's desaturated, make it transparent.
    # Exception: Keep very bright whites if they are inside the image? 
    # For these assets, the background is 100% checkerboard.
    
    mask = is_desaturated
    
    # Apply transparency
    data[mask] = [0, 0, 0, 0]
    
    # Create new image
    new_img = Image.fromarray(data)
    new_img.save(image_path)
    print(f"✅ Aggressively Cleaned {os.path.basename(image_path)}")

if __name__ == "__main__":
    png_files = glob.glob(os.path.join(IMAGE_DIR, "*.png"))
    for f in png_files:
        try:
            remove_checkerboard(f)
        except Exception as e:
            print(f"❌ Error: {e}")
