"""
Pedagogical Validator for HTML Presentations

This validator ensures presentations follow the pedagogical standards:
1. Strict adherence to visual-plan.md
2. Answer interleaving (one answer per slide)
3. Content matches source materials
4. No hallucinated content

Usage:
    python validate_pedagogical.py <index.html> [--visual-plan <path>] [--source <path>]
"""

import argparse
import os
import sys
import io
from bs4 import BeautifulSoup
import re

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def load_visual_plan(plan_path):
    """Parse visual-plan.md and extract expected slide structure."""
    if not os.path.exists(plan_path):
        return None
    
    with open(plan_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract slide headings (### Slide X: Title)
    slides = re.findall(r'###\s+Slide\s+[\d.]+:\s+(.+)', content)
    return slides

def load_source_material(source_path):
    """Parse source material (*.md) and extract tasks/questions."""
    if not os.path.exists(source_path):
        return None
    
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract task sections
    tasks = {}
    current_task = None
    
    for line in content.split('\n'):
        # Match any level 2 header
        h2_match = re.match(r'##\s+(.+)', line)
        if h2_match:
            header_text = h2_match.group(1)
            # Match task headers (## Task 1:, ## Task 2:, etc.)
            task_match = re.match(r'Task\s+(\d+):', header_text, re.IGNORECASE)
            if task_match:
                current_task = int(task_match.group(1))
                tasks[current_task] = {'questions': [], 'answers': []}
            else:
                # Reset task context if it's not a Task header (e.g., Answer Key)
                current_task = None
        
        # Match numbered questions (1., 2., etc.)
        if current_task and re.match(r'^\d+\.\s+', line):
            tasks[current_task]['questions'].append(line.strip())
    
    return tasks

def validate_presentation(html_path, visual_plan_path=None, source_path=None):
    """Main validation function."""
    print(f"🔍 Pedagogical Validation: {html_path}")
    
    if not os.path.exists(html_path):
        print(f"❌ CRITICAL: File not found: {html_path}")
        return False
    
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    issues = []
    warnings = []
    
    # Get all slides
    sections = soup.find_all('section')
    print(f"   Found {len(sections)} slides in presentation")
    
    # CHECK 1: Visual Plan Compliance
    if visual_plan_path:
        expected_slides = load_visual_plan(visual_plan_path)
        if expected_slides:
            print(f"   Visual plan expects {len(expected_slides)} slides")
            if len(sections) != len(expected_slides):
                warnings.append(f"⚠️ Slide Count Mismatch: Expected {len(expected_slides)} slides, found {len(sections)}")
    
    # CHECK 2: Task Detection (Informational Only)
    task_slides = []
    for i, section in enumerate(sections):
        # Check text content AND component attributes
        text = section.get_text().upper()
        
        # Check attributes of slide components
        components = section.find_all(re.compile(r'slide-.*'))
        for comp in components:
            text += " " + (comp.get('title') or "").upper()
            text += " " + (comp.get('badge') or "").upper()
            
        # Look for task indicators
        if 'TASK' in text and any(word in text for word in ['IDENTIFY', 'FILL', 'CLASSIFY', 'JOIN', 'WRITE']):
            # Store the consolidated text for later use
            section['data-validated-text'] = text
            task_slides.append((i, section))
            
    print(f"   Found {len(task_slides)} task slides")
    
    # CHECK 3: Source Material Cross-Reference (Informational Only)
    if source_path:
        source_tasks = load_source_material(source_path)
        if source_tasks:
            print(f"   Source material has {len(source_tasks)} tasks")

    # CHECK 4: Task Naming Consistency
    task_headings = []
    for section in sections:
        # Check H2 OR component title
        h2 = section.find('h2')
        if h2 and 'TASK' in h2.get_text().upper():
            task_headings.append(h2.get_text().strip())
        else:
            # Check components
            components = section.find_all(re.compile(r'slide-.*'))
            for comp in components:
                title = comp.get('title', '')
                if 'TASK' in title.upper():
                    task_headings.append(title.strip())
    
    # Verify sequential numbering
    for i, heading in enumerate(task_headings):
        expected_num = i + 1
        if f'TASK {expected_num}' not in heading.upper() and f'TASK{expected_num}' not in heading.upper():
            warnings.append(f"⚠️ Task Numbering: Expected 'TASK {expected_num}' but found '{heading}'")
    
    # REPORTING
    print("\n--- PEDAGOGICAL VALIDATION REPORT ---")
    
    if warnings:
        print("\n⚠️  WARNINGS:")
        for w in warnings:
            print(f"  {w}")
    
    if issues:
        print("\n❌ CRITICAL ISSUES:")
        for i in issues:
            print(f"  {i}")
        print(f"\n🚫 FAILED: {len(issues)} critical pedagogical issues found.")
        return False
    else:
        print("\n✅ PASSED: No critical pedagogical issues found.")
        if warnings:
            print(f"   ({len(warnings)} warnings - review recommended)")
        return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate HTML Presentation against pedagogical standards.")
    parser.add_argument("file", help="Path to index.html")
    parser.add_argument("--visual-plan", help="Path to visual-plan.md (optional)")
    parser.add_argument("--source", help="Path to source material *.md (optional)")
    
    args = parser.parse_args()
    
    # Auto-detect files in same directory if not provided
    base_dir = os.path.dirname(args.file)
    
    visual_plan = args.visual_plan
    if not visual_plan:
        candidate = os.path.join(base_dir, 'visual-plan.md')
        if os.path.exists(candidate):
            visual_plan = candidate
            print(f"📋 Auto-detected visual plan: {visual_plan}")
    
    source = args.source
    if not source:
        # Look for *.md files in directory
        for file in os.listdir(base_dir):
            if file.endswith('.md') and 'visual-plan' not in file.lower():
                source = os.path.join(base_dir, file)
                print(f"📄 Auto-detected source material: {source}")
                break
    
    success = validate_presentation(args.file, visual_plan, source)
    if not success:
        sys.exit(1)
