---
name: processing-images
description: Best practices and tools for processing images for worksheets (trimming, transparency, resizing). Use when the user asks to remove backgrounds, trim margins, fix fake checkerboards, or prepare icons/separators for documents.
---

# Processing Images for Documents

## Purpose
To ensure images used in Typst or other documents are visually clean, print-friendly (grayscale/photocopier safe), and layout-efficient by removing unnecessary whitespace and backgrounds.

## The Constraints
1.  **No Gradients**: Backgrounds must be solid (preferably white/transparent) for clear photocopying.
2.  **Transparent PNGs**: Any non-rectangular graphic (icons, motifs) must have a transparent background.
3.  **No Fake Checkerboards**: **CRITICAL**. Some images have a "fake" gray-and-white checkerboard pattern baked into the pixels. You MUST remove this before placing in Typst.
4.  **Trimmed Whitespace**: Generated images often have huge unnecessary margins. These MUST be trimmed to the content bounding box to avoid destroying document flow.
5.  **Aspect Ratio**: Never distort aspect ratios (squashing) to fit a space. Use specific image dimensions or `width: 100%, height: auto`.

## The Tool: `.agent/skills/processing-images/scripts/trim_image.py`
Use this script to auto-process images.

### Usage
```bash
python .agent/skills/processing-images/scripts/trim_image.py <input> <output> [options]
```

### Options
- `--padding <int>`: Pixels of padding to add (default 0). Use ~10-20px for safety.
- `--threshold <0-255>`: Brightness threshold for "white" (default 250). Lower to ~220-230 if the background is off-white/grayish.
- `--transparent`: **CRITICAL**. Converts the near-white background to alpha transparency and saves as `.png`.

### Common Workflows

#### 1. Processing a Generated Title/Motif
Generated images usually have artifacts or gradients.
```bash
# Trim and make transparent
python .agent/skills/processing-images/scripts/trim_image.py "images/generated_title.jpg" "images/header_final.png" --padding 10 --threshold 230 --transparent
```

#### 2. Preparing a Separator
Separators should be ultra-wide.
1.  Generate/Source an image with a wide aspect ratio (e.g., 20:1).
2.  Trim and transparentize:
    ```bash
    python .agent/skills/processing-images/scripts/trim_image.py "images/separator_raw.jpg" "images/separator.png" --padding 0 --threshold 220 --transparent
    ```
3.  In Typst: `#image("images/separator.png", width: 100%)` (let height flow naturally).

#### 3. Removing Fake Checkerboards
If an image has a "baked-in" checkerboard (gray/white squares):
```bash
python .agent/skills/processing-images/scripts/remove_checkerboard.py "images/fake_png.png" "images/clean_output.png"
```
Then proceed to trim the whitespace if necessary.

## Typst Integration
- **Titles**: Use the trimmed PNG. Limit width to avoid domination (e.g., `width: 8cm`).
- **Separators**: Use `width: 100%` or specific width, never force `height` unless you are sure of the aspect ratio.
- **Insets**: When wrapping text using `meander`, ensure `inset` is sufficient (e.g., `24pt`) so text doesn't crowd transparency edges.
