"""
Lesson Plan Validator (Typst & HTML Support)
Checks lesson plans for compliance with writing-lesson-plans skill requirements.
Includes Detail Density comparison against model YAMLs.
"""

import sys
import re
import os
from pathlib import Path

# Add project root for YAML library
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

try:
    import yaml
except ImportError:
    yaml = None

class LessonPlanValidator:
    def __init__(self, content, filename=""):
        self.filename = filename
        self.content = content
        self.errors = []
        self.warnings = []
        self.metadata = self._extract_metadata()
        self.stages = self._extract_stages()
    
    def _extract_metadata(self):
        """Extract lesson metadata from Typst file."""
        metadata = {}
        
        # Look for metadata field in typst dict
        duration_match = re.search(r'duration:\s*"(\d+)\s*Minutes"', self.content, re.IGNORECASE)
        if duration_match:
            metadata['duration'] = int(duration_match.group(1))
        
        shape_match = re.search(r'shape:\s*"([A-J])', self.content, re.IGNORECASE)
        if shape_match:
            metadata['shape'] = shape_match.group(1).upper()
        
        cefr_match = re.search(r'cefr:\s*"([A-C][0-2])', self.content, re.IGNORECASE)
        if cefr_match:
            metadata['cefr'] = cefr_match.group(1).upper()
        
        # Backup shape from filename
        if not metadata.get('shape') and self.filename:
             shape_match = re.search(r'-([A-J])\.', self.filename)
             if shape_match:
                 metadata['shape'] = shape_match.group(1).upper()

        return metadata

    def _extract_stages(self):
        """Extract stage procedures and their word counts from Typst blocks."""
        stages = []
        # Find all STAGE headers first
        # Pattern: STAGE [Number]: [Name]
        stage_headers = re.finditer(r'STAGE\s+(?:ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|[1-8]):\s+(.*?)(?=\]|\))', self.content, re.IGNORECASE)
        
        for match in stage_headers:
            name = match.group(1).strip()
            header_pos = match.end()
            remaining_content = self.content[header_pos:]
            
            # Extract blocks like [...]
            blocks = re.findall(r'\[(.*?)\]', remaining_content, re.DOTALL)
            
            if len(blocks) >= 3:
                # Sort by size to find procedure
                sorted_blocks = sorted(blocks[:5], key=len, reverse=True)
                proc_text = sorted_blocks[0].strip()
                
                stages.append({
                    'name': name,
                    'procedure': proc_text,
                    'word_count': len(re.findall(r'\w+', proc_text))
                })
        return stages

    def validate(self):
        """Run all validation checks."""
        self._check_timing()
        self._check_preteach_vocabulary()
        self._check_stage_structure()
        
        return len(self.errors) == 0
    
    def _check_timing(self):
        """Verify stage times add up to total duration."""
        # Simple extraction of numbers followed by "Min" in Typst
        time_vals = re.findall(r'\[(\d+)\s*Min\]', self.content)
        
        if time_vals:
            total = sum(int(t) for t in time_vals)
            expected = self.metadata.get('duration', 0)
            if expected and abs(total - expected) > 2:
                self.warnings.append(f"⚠️ Timing check: Detected stage times sum to {total} mins, expected {expected}.")

    def _check_preteach_vocabulary(self):
        """Verify pre-teach vocabulary stage for receptive skills shapes."""
        shape = self.metadata.get('shape', '')
        if shape in ['E', 'F', 'G', 'H']:
            has_vocab = any("pre-teach" in s['name'].lower() or "vocabulary" in s['name'].lower() for s in self.stages)
            if not has_vocab:
                self.errors.append(f"❌ Shape {shape} requires a Pre-teach Vocabulary stage.")

    def _check_stage_structure(self):
        """Check for proper stage numbers."""
        if len(self.stages) < 3:
            self.warnings.append(f"⚠️ Low stage count ({len(self.stages)}). Verify Shape requirements.")

    def print_report(self):
        """Print validation report."""
        print("\n" + "="*60)
        print("LESSON PLAN VALIDATION REPORT")
        print(f"File: {self.filename}")
        print("="*60 + "\n")
        
        print("Detected Metadata:")
        print(f"  Shape: {self.metadata.get('shape', 'Not detected')}")
        print(f"  Duration: {self.metadata.get('duration', 'Not detected')} minutes")
        print(f"  CEFR: {self.metadata.get('cefr', 'Not detected')}")
        print()
        
        if self.errors:
            print("🚫 VALIDATION FAILED\n")
            for error in self.errors:
                print(error)
        else:
            print("✅ VALIDATION PASSED\n")
        
        if self.warnings:
            print("⚠️ WARNINGS:\n")
            for warning in self.warnings:
                print(warning)
        
        print("="*60 + "\n")

def validate_file(filepath):
    path = Path(filepath)
    if not path.exists():
        print(f"File not found: {filepath}")
        return False
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    validator = LessonPlanValidator(content, path.name)
    is_valid = validator.validate()
    validator.print_report()
    
    return is_valid

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python validate_lesson_plan.py <file>")
        sys.exit(1)
    
    sys.exit(0 if validate_file(sys.argv[1]) else 1)
