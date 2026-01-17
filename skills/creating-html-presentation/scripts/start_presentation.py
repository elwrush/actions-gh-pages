import argparse
import json
import os
import sys

PALETTES = {
    "1": "Cyber-Gamer",
    "2": "Indigo Nightfall",
    "3": "Teal Horizon",
    "4": "Deep Purple",
    "5": "Blue Grey Steel",
    "6": "Amber Sunrise",
    "7": "Green Forest",
    "8": "Red Alert",
    "9": "Light Blue Ocean",
    "10": "Pink Blossom"
}

def clean_path(path):
    return path.strip().strip("'").strip('"')

def validate_folder(folder):
    if not os.path.exists(folder):
        print(f"Error: Target folder '{folder}' does not exist.")
        sys.exit(1)
    
    # Check for minimal expected files (Handout or LP)
    has_content = False
    for f in os.listdir(folder):
        if f.endswith('.pdf') or f.endswith('.typ') or f.endswith('.md'):
            has_content = True
            break
            
    if not has_content:
        print(f"Warning: No obvious source content (PDF/TYP/MD) found in '{folder}'. proceeding cautiously.")

def main():
    parser = argparse.ArgumentParser(description="Deterministic Gatekeeper for Presentation Creation")
    parser.add_argument("--folder", required=True, help="Target folder for the presentation (inputs/...)")
    parser.add_argument("--audience", required=True, choices=["Middle School", "High School"], help="Target Audience")
    parser.add_argument("--mode", required=True, choices=["Bell", "Intensive"], help="Branding Mode")
    parser.add_argument("--palette", required=True, choices=[str(i) for i in range(1, 11)], help="Palette ID (1-10)")
    parser.add_argument("--assets", required=True, choices=["image", "sound", "video", "all"], help="Asset Mix")
    parser.add_argument("--imgstyle", choices=["photo", "illustration", "vector"], help="Image Style (Required if assets includes images)")
    
    args = parser.parse_args()

    # Logic Checks
    folder = clean_path(args.folder)
    validate_folder(folder)

    # Tone Derivation
    tone = "Pop & Verve" if args.audience == "Middle School" else "Expert/Academic"
    palette_name = PALETTES[args.palette]

    config = {
        "status": "APPROVED",
        "gates": {
            "audience": args.audience,
            "tone": tone,
            "branding": args.mode,
            "palette_id": args.palette,
            "palette_name": palette_name,
            "asset_strategy": {
                "mix": args.assets,
                "image_style": args.imgstyle
            }
        },
        "folder": folder
    }

    config_path = os.path.join(folder, "presentation_config.json")
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

    print(f"\n✅ GATE CLEARED. Config written to {config_path}")
    print(f"==================================================")
    print(f"Audience:   {args.audience} ({tone})")
    print(f"Palette:    #{args.palette} {palette_name}")
    print(f"Strategy:   {args.assets} / {args.imgstyle}")
    print(f"==================================================")
    print(f"Current State: STEP 0 & 1 COMPLETE.")
    print(f"NEXT ACTION: Proceed to Step 2 (Visual Plan Markdown).")

if __name__ == "__main__":
    main()
