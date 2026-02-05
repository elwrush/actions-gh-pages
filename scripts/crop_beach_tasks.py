from PIL import Image
import os

def crop_images():
    img = Image.open('inputs/b1-beach-vocab/images/page2.png')
    w, h = img.size
    
    # Coordinates estimated for (637, 849) image
    # The 5 images are between y=260 and y=400 roughly
    # x ranges:
    # 1: 50-160
    # 2: 170-280
    # 3: 290-400
    # 4: 410-520
    # 5: 530-630
    
    y_top = 260
    y_bottom = 390
    
    crops = [
        (60, y_top, 160, y_bottom),  # Volleyball
        (170, y_top, 280, y_bottom), # Sunbathing
        (290, y_top, 400, y_bottom), # Surfing
        (410, y_top, 520, y_bottom), # Diving
        (530, y_top, 630, y_bottom)  # Windsurfing
    ]
    
    names = ["volleyball", "sunbathing", "surfing", "diving", "windsurfing"]
    
    for i, box in enumerate(crops):
        cropped = img.crop(box)
        # Trim whitespace
        # (Assuming the background is white-ish)
        cropped.save(f'inputs/b1-beach-vocab/images/task3_{names[i]}.png')
        print(f"Saved {names[i]}")

if __name__ == "__main__":
    crop_images()
