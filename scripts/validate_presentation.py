#!/usr/bin/env python3
"""
Presentation JSON Validator

Validates presentation.json files against the schema to ensure
template adherence. Provides both strict and warning modes.

Usage:
    python scripts/validate_presentation.py [path] [--strict]
    
Examples:
    python scripts/validate_presentation.py                                    # Validate all
    python scripts/validate_presentation.py inputs/28-01-2026-B1-Match-Girl-E/  # Validate one
    python scripts/validate_presentation.py --strict                           # Strict mode
"""

import json
import sys
import glob
import os
import argparse
from pathlib import Path

# ANSI color codes (with ASCII-safe symbols for Windows)
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

# ASCII-safe symbols for Windows compatibility
CHECK = "[OK]"
CROSS = "[FAIL]"
WARN = "[WARN]"
INFO = "[INFO]"
BULLET = "-"

# Allowed layouts (from schema)
ALLOWED_LAYOUTS = {
    "title", "segue", "split_task", "strategy", 
    "matching", "answer", "video", "impact", "vocab",
    "mission", "split_table", "video_answer", "checklist", 
    "table", "match_reorder", "answer_list", "answer_detail", "image"
}

# Required fields per layout (answer slides may not require some fields)
LAYOUT_REQUIREMENTS = {
    "matching": ["pairs", "shuffled"],
    "vocab": ["word", "phoneme", "context_sentence"],
    "split_task": ["content"],
    "answer": ["answer"],
    "impact": ["main_text", "points"],
    "title": [],
    "segue": ["phase"],
    "strategy": ["content"],
    "video": ["video_url"],
    "mission": [],
    "split_table": [],
    "video_answer": [],
    "checklist": [],
    "table": [],
    "match_reorder": [],
    "answer_list": [],
    "answer_detail": [],
    "image": []
}

# Layout-specific field requirements
LAYOUT_SPECIFIC_FIELDS = {
    "matching": {
        "pairs": lambda v: isinstance(v, list) and len(v) > 0,
        "shuffled": lambda v: isinstance(v, list) and len(v) > 0
    },
    "vocab": {
        "word": lambda v: isinstance(v, str) and len(v) > 0,
        "phoneme": lambda v: isinstance(v, str) and "/" in v,
        "context_sentence": lambda v: isinstance(v, str) and len(v) > 0
    },
    "split_task": {
        "content": lambda v: isinstance(v, str) and len(v) > 0,
        "timer": lambda v: isinstance(v, (int, float)) and 0 < v <= 60
    },
    "answer": {
        "answer": lambda v: isinstance(v, str) and len(v) > 0,
        "explanation": lambda v: isinstance(v, str) and len(v) > 0
    },
    "impact": {
        "main_text": lambda v: isinstance(v, str) and len(v) > 0,
        "points": lambda v: isinstance(v, list) and len(v) > 0
    },
    "video": {
        "video_url": lambda v: isinstance(v, str) and len(v) > 0
    }
}


def print_header(text):
    """Print a section header."""
    print(f"\n{BOLD}{BLUE}{'=' * 60}{RESET}")
    print(f"{BOLD}{BLUE}{text}{RESET}")
    print(f"{BOLD}{BLUE}{'=' * 60}{RESET}\n")


def print_success(text):
    """Print a success message."""
    print(f"{GREEN}{CHECK} {text}{RESET}")


def print_error(text):
    """Print an error message."""
    print(f"{RED}{CROSS} {text}{RESET}")


def print_warning(text):
    """Print a warning message."""
    print(f"{YELLOW}{WARN} {text}{RESET}")


def print_info(text):
    """Print an info message."""
    print(f"{BLUE}{INFO} {text}{RESET}")


def load_schema():
    """Load the JSON schema from file."""
    schema_path = Path(__file__).parent.parent / "schemas" / "presentation.schema.json"
    try:
        with open(schema_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print_error(f"Schema file not found: {schema_path}")
        return None
    except json.JSONDecodeError as e:
        print_error(f"Invalid JSON in schema file: {e}")
        return None


def validate_file(filepath, schema, strict=False):
    """
    Validate a single presentation JSON file.
    
    Args:
        filepath: Path to the presentation.json file
        schema: The JSON schema to validate against
        strict: If True, fail on warnings too
    
    Returns:
        tuple: (success: bool, errors: list, warnings: list)
    """
    errors = []
    warnings = []
    
    # Load the presentation file
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        errors.append(f"File not found: {filepath}")
        return False, errors, warnings
    except json.JSONDecodeError as e:
        errors.append(f"Invalid JSON: {e}")
        return False, errors, warnings
    
    # Normalize field names (handle data-id -> data_id)
    def normalize_slide(slide):
        if 'data-id' in slide and 'data_id' not in slide:
            slide['data_id'] = slide['data-id']
        return slide
    
    # Validate meta section
    if "meta" not in data:
        errors.append("Missing required 'meta' section")
    else:
        if "title" not in data["meta"]:
            errors.append("Missing required 'meta.title'")
        if "theme" in data["meta"] and data["meta"]["theme"] not in ["noir", "thai-heritage", "indonesia", "amazon"]:
            warnings.append(f"Unknown theme: {data['meta'].get('theme')}")
    
    # Validate slides
    if "slides" not in data:
        errors.append("Missing required 'slides' section")
    else:
        # Banned Teacher-Facing Words (for student-centric voice check)
        BANNED_WORDS = ["lead-in", "warmer", "gist", "detail", "rationale", "the tools", "the crime", "objective", "procedure"]
        
        for i, slide in enumerate(data["slides"]):
            slide = normalize_slide(slide)
            slide_path = f"slides[{i}]"
            layout = slide.get("layout", "")
            title = slide.get("title", "").lower()
            
            # Check for Banned Words in Title
            for word in BANNED_WORDS:
                if word in title:
                    errors.append(f"{slide_path}: Banned teacher-facing word '{word}' found in title '{slide.get('title')}'. Use student-centric action titles instead.")
            
            # Check required fields
            if not layout:
                errors.append(f"{slide_path}: Missing required 'layout'")
            elif layout not in ALLOWED_LAYOUTS:
                errors.append(f"{slide_path}: Invalid layout '{layout}'. Allowed: {', '.join(sorted(ALLOWED_LAYOUTS))}")
            
            # Check title requirement (vocab layout uses 'word' as title)
            if layout == "vocab":
                if "word" not in slide:
                    errors.append(f"{slide_path}: Missing required 'word' for vocab layout")
            else:
                if "title" not in slide:
                    errors.append(f"{slide_path}: Missing required 'title'")
            
            # Check layout-specific requirements
            # Answer slides don't require pairs/shuffled
            if layout in LAYOUT_REQUIREMENTS and not slide.get("is_answer"):
                for field in LAYOUT_REQUIREMENTS[layout]:
                    if field not in slide:
                        errors.append(f"{slide_path}: Missing required field '{field}' for {layout} layout (unless is_answer=true)")
            
            # Validate layout-specific field values
            if layout in LAYOUT_SPECIFIC_FIELDS:
                validators = LAYOUT_SPECIFIC_FIELDS[layout]
                for field, validator in validators.items():
                    if field in slide and not validator(slide[field]):
                        warnings.append(f"{slide_path}: Field '{field}' may have invalid value")
            
            # Check timer values
            if "timer" in slide:
                if not isinstance(slide["timer"], (int, float)):
                    errors.append(f"{slide_path}: 'timer' must be a number")
                elif slide["timer"] > 60:
                    warnings.append(f"{slide_path}: Timer value {slide['timer']} exceeds recommended max (60)")
            
            # Check image paths
            if "image" in slide:
                img_path = slide["image"]
                if not img_path.startswith(("images/", "published/images/")):
                    warnings.append(f"{slide_path}: Image path '{img_path}' should start with 'images/' or 'published/images/'")
            
            # Check matching slides have corresponding answer slides
            if layout == "matching" and not slide.get("is_answer"):
                data_id = slide.get("data_id", "")
                has_answer = any(
                    s.get("layout") == "matching" and 
                    s.get("is_answer") and 
                    normalize_slide(s).get("data_id") == data_id
                    for s in data["slides"]
                )
                if not has_answer:
                    warnings.append(f"{slide_path}: Matching slide has no corresponding answer slide (data_id='{data_id}')")
    
    # Strict mode: warnings become errors
    if strict and warnings:
        errors.extend(warnings)
        warnings = []
    
    return len(errors) == 0, errors, warnings


def find_presentation_files(path=None):
    """Find all presentation.json files."""
    if path is None:
        # Default to inputs directory
        base_path = Path(__file__).parent.parent / "inputs"
    elif Path(path).is_file():
        return [Path(path)]
    else:
        base_path = Path(path)
    
    # Find all presentation.json files
    patterns = [
        base_path / "**" / "presentation.json",
    ]
    
    if base_path.is_file() and base_path.name == "presentation.json":
        return [base_path]
    
    files = []
    for pattern in patterns:
        files.extend(glob.glob(str(pattern), recursive=True))
    
    return [Path(f) for f in files]


def validate_directory(path=None, strict=False):
    """Validate all presentation files in a directory."""
    files = find_presentation_files(path)
    
    if not files:
        print_warning(f"No presentation.json files found")
        return False
    
    print_header(f"Validating {len(files)} Presentation File(s)")
    
    all_success = True
    validated = 0
    
    for filepath in sorted(files):
        # Resolve to absolute path to avoid subpath errors
        filepath = filepath.resolve()
        project_root = Path(__file__).parent.parent.resolve()
        
        try:
            relative_path = filepath.relative_to(project_root)
        except ValueError:
            relative_path = filepath
            
        print(f"\n{ BOLD }Checking: {relative_path}{RESET}")
        
        success, errors, warnings = validate_file(filepath, None, strict)
        
        if warnings:
            print_info("Warnings:")
            for w in warnings:
                print_warning(f"  {w}")
        
        if errors:
            print_error("Errors:")
            for e in errors:
                print_error(f"  {e}")
            all_success = False
        elif success:
            print_success("Valid")
            validated += 1
    
    # Summary
    print_header("Validation Summary")
    print(f"Total files: {len(files)}")
    print(f"Validated: {validated}")
    print(f"Failed: {len(files) - validated}")
    
    if all_success:
        print_success("All " + str(len(files)) + " presentations are valid!")
    else:
        print_error("" + str(len(files) - validated) + " presentation(s) have errors")
        sys.exit(1)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Validate presentation.json files against the template schema."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=None,
        help="Path to a specific presentation.json file or directory"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results in JSON format"
    )
    
    args = parser.parse_args()
    
    # Load schema (optional - we can validate without it using our custom logic)
    schema = load_schema()
    
    # Find and validate files
    files = find_presentation_files(args.path)
    
    if not files:
        print_warning("No presentation.json files found")
        sys.exit(1)
    
    if args.json:
        results = []
        for filepath in files:
            success, errors, warnings = validate_file(filepath, schema, args.strict)
            results.append({
                "file": str(filepath),
                "valid": success,
                "errors": errors,
                "warnings": warnings
            })
        print(json.dumps(results, indent=2))
        sys.exit(0 if all(r["valid"] for r in results) else 1)
    
    validate_directory(args.path, args.strict)


if __name__ == "__main__":
    main()
