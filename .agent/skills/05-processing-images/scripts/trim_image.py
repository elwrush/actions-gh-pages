#!/usr/bin/env python
"""
trim_image.py - Trims whitespace from images

Usage:
    python trim_image.py <input_image> [output_image] [--padding 10] [--threshold 250]

Arguments:
    input_image     Path to the source image
    output_image    Optional output path (defaults to input with _trimmed suffix)
    --padding       Pixels of padding to add around content (default: 0)
    --threshold     Brightness threshold for "white" detection (0-255, default: 250)

Example:
    python trim_image.py images/title_graphic.jpg images/title_graphic_trimmed.jpg --padding 5
"""

import sys
import argparse
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow is required. Install with: pip install Pillow")
    sys.exit(1)


def get_content_bbox(image, threshold=250):
    """
    Find the bounding box of non-white content in an image.
    
    Args:
        image: PIL Image object
        threshold: Brightness level above which a pixel is considered "white"
        
    Returns:
        (left, top, right, bottom) tuple, or None if image is entirely white
    """
    # Convert to grayscale for simpler analysis
    gray = image.convert('L')
    pixels = gray.load()
    width, height = gray.size
    
    # Find bounds
    left = width
    top = height
    right = 0
    bottom = 0
    
    for y in range(height):
        for x in range(width):
            if pixels[x, y] < threshold:
                left = min(left, x)
                top = min(top, y)
                right = max(right, x)
                bottom = max(bottom, y)
    
    if right <= left or bottom <= top:
        return None  # No content found
    
    return (left, top, right + 1, bottom + 1)


def trim_image(input_path, output_path=None, padding=0, threshold=250):
    """
    Trim whitespace from an image and save the result.
    
    Args:
        input_path: Path to source image
        output_path: Path for output (defaults to input_trimmed.ext)
        padding: Pixels of padding to add around content
        threshold: Brightness threshold for white detection
        
    Returns:
        Path to the output file
    """
    input_path = Path(input_path)
    
    if output_path is None:
        output_path = input_path.parent / f"{input_path.stem}_trimmed{input_path.suffix}"
    else:
        output_path = Path(output_path)
    
    # Load image
    img = Image.open(input_path)
    original_size = img.size
    
    # Find content bounding box
    bbox = get_content_bbox(img, threshold)
    
    if bbox is None:
        print(f"Warning: No content detected in {input_path}. Saving copy as-is.")
        img.save(output_path)
        return output_path
    
    # Apply padding (bounded by image edges)
    left = max(0, bbox[0] - padding)
    top = max(0, bbox[1] - padding)
    right = min(img.width, bbox[2] + padding)
    bottom = min(img.height, bbox[3] + padding)
    
    # Crop
    cropped = img.crop((left, top, right, bottom))
    new_size = cropped.size
    
    # Save
    cropped.save(output_path)
    
    print(f"Trimmed: {input_path}")
    print(f"  Original: {original_size[0]}x{original_size[1]}")
    print(f"  Trimmed:  {new_size[0]}x{new_size[1]}")
    print(f"  Saved to: {output_path}")
    
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Trim whitespace from images",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("input", help="Path to input image")
    parser.add_argument("output", nargs="?", help="Path to output image (optional)")
    parser.add_argument("--padding", type=int, default=0, help="Padding in pixels (default: 0)")
    parser.add_argument("--threshold", type=int, default=250, help="White threshold 0-255 (default: 250)")
    parser.add_argument("--transparent", action="store_true", help="Make near-white background transparent (outputs PNG)")
    
    args = parser.parse_args()
    
    if not Path(args.input).exists():
        print(f"Error: Input file not found: {args.input}")
        sys.exit(1)
    
    output_path = trim_image(args.input, args.output, args.padding, args.threshold)
    
    # Make background transparent if requested
    if args.transparent:
        make_transparent(output_path, args.threshold)


def make_transparent(image_path, threshold=250):
    """
    Replace near-white pixels with transparency and save as PNG.
    """
    image_path = Path(image_path)
    img = Image.open(image_path).convert("RGBA")
    pixels = img.load()
    
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            # If pixel is near-white, make transparent
            if r > threshold and g > threshold and b > threshold:
                pixels[x, y] = (255, 255, 255, 0)
    
    # Save as PNG (required for transparency)
    png_path = image_path.with_suffix('.png')
    img.save(png_path)
    print(f"  Transparent: {png_path}")
    
    # Remove original if it was a different format
    if image_path.suffix.lower() != '.png' and image_path.exists():
        image_path.unlink()
    
    return png_path


if __name__ == "__main__":
    main()
