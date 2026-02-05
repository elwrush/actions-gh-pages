from PIL import Image

def crop_coast():
    img = Image.open('inputs/b1-beach-vocab/images/page1.png')
    # Coastline image with labels
    crop = img.crop((165, 10, 715, 340))
    crop.save('inputs/b1-beach-vocab/images/coast_diagram.png')
    print("Saved coast_diagram.png")
    
    # Also crop the "Beach activities" icons if possible
    # They are in a row: surfing, windsurfing, diving, volleyball, sunbathing
    y_top = 490
    y_bottom = 600
    
    activities = [
        (165, y_top, 290, y_bottom),
        (315, y_top, 440, y_bottom),
        (465, y_top, 595, y_bottom),
        (630, y_top, 780, y_bottom), # Volleyball
        (800, y_top, 940, y_bottom)  # Sunbathing
    ]
    # Wait, the width is only 747. My coordinates are too high.
    # Let's re-calculate for 747 width.
    # icons are roughly 1/5 of the width each.
    
    x_starts = [165, 320, 465, 630, 800] # These were guessed for larger image.
    
    # Actually, the image width is 747.
    # Activity row spans most of the width below part A.
    # surfing: ~165 to ~280? No, let's look at the uploaded image.
    # Surfing is 1st.
    
if __name__ == "__main__":
    crop_coast()
