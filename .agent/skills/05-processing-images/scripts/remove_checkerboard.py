
import sys
from PIL import Image

def remove_checkerboard(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        # If it looks like gray or white (common checkerboard colors)
        # Gray is typically (204, 204, 204) or similar
        # White is (255, 255, 255)
        # We want to keep anything that is clearly NOT a light gray or white
        r, g, b, a = item
        
        # In black and white line art, the lines are dark.
        # Anything light (sum of RGB > some threshold) should be white/transparent.
        if r > 180 and g > 180 and b > 180:
            new_data.append((255, 255, 255, 0)) # Make it fully transparent
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path, "PNG")

if __name__ == "__main__":
    remove_checkerboard(sys.argv[1], sys.argv[2])
