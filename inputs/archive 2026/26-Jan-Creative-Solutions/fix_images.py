from PIL import Image
import os

def fix_png(path):
    try:
        img = Image.open(path)
        img.save(path, "PNG")
        print(f"Fixed {path}")
    except Exception as e:
        print(f"Error fixing {path}: {e}")

paths = [
    "inputs/26-Jan-Creative-Solutions/hero.png",
    "inputs/26-Jan-Creative-Solutions/curitiba.png",
    "inputs/26-Jan-Creative-Solutions/murcia.png",
    "inputs/26-Jan-Creative-Solutions/la_paz.png"
]

for p in paths:
    fix_png(p)
