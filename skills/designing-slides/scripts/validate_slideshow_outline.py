"""
Slideshow Structure Validator
Checks that answer slides are properly interleaved with question/task slides
per the designing-slides skill requirements.

Usage: python validate_slideshow_outline.py <outline.md>
"""

import sys
import re

class SlideOutlineValidator:
    def __init__(self, outline_text):
        self.outline_text = outline_text
        self.slides = self._parse_slides()
        self.errors = []
        self.warnings = []
    
    def _parse_slides(self):
        """Extract slides from markdown outline."""
        slides = []
        current_slide = None
        
        for line in self.outline_text.split('\n'):
            # Match slide headers: ## Slide N: Title or ## N. Title
            slide_match = re.match(r'^##\s+(?:Slide\s+)?(\d+)[.:]\s+(.+)$', line.strip())
            if slide_match:
                if current_slide:
                    slides.append(current_slide)
                num, title = slide_match.groups()
                current_slide = {
                    'number': int(num),
                    'title': title.strip(),
                    'content': []
                }
            elif current_slide and line.strip().startswith('-'):
                current_slide['content'].append(line.strip()[1:].strip())
        
        if current_slide:
            slides.append(current_slide)
        
        return slides
    
    def _is_question_slide(self, slide):
        """Detect if a slide poses an explicit task requiring student answers."""
        title_lower = slide['title'].lower()
        content_text = ' '.join(slide['content']).lower()
        
        # Exclude transition slides (short slides with 1-2 bullets)
        if len(slide['content']) <= 2 and all(len(b) < 60 for b in slide['content']):
            return False
        
        # Explicit task indicators (requires answer slide)
        task_phrases = [
            'your turn',
            'task:',
            'exercise:',
            'practice:',
            'complete the',
            'fill in the',
            'match the',
            'find the answer'
        ]
        
        for phrase in task_phrases:
            if phrase in title_lower or phrase in content_text:
                return True
        
        return False
    
    def _is_answer_slide(self, slide):
        """Detect if a slide contains an answer."""
        title_lower = slide['title'].lower()
        content_text = ' '.join(slide['content']).lower()
        
        answer_indicators = ['answer', 'key', 'solution', 'correct']
        
        for word in answer_indicators:
            if word in title_lower:
                return True
        
        return False
    
    def _is_transition_slide(self, slide):
        """Detect if a slide is a transition/signpost slide."""
        title_lower = slide['title'].lower()
        
        transition_indicators = [
            'transition',
            "let's",
            "time to",
            "now for",
            "here's your",
            "your turn",
            "before we",
            "let us"
        ]
        
        # Check if title contains transition indicators
        for indicator in transition_indicators:
            if indicator in title_lower:
                return True
        
        # Also check if it's a short slide with just one bullet (likely a transition)
        if len(slide['content']) == 1 and len(slide['content'][0]) < 80:
            return True
        
        return False
    
    def validate(self):
        """Run all validation checks."""
        self._check_interleaving()
        self._check_answer_slides_exist()
        self._check_bullet_limits()
        self._check_vocabulary_format()
        self._check_image_policy()
        self._check_mechanistic_language()
        self._check_transition_slides()
        
        return len(self.errors) == 0
    
    def _check_transition_slides(self):
        """Check for mandatory transition slides at checkpoints."""
        transition_slides = [s for s in self.slides if self._is_transition_slide(s)]
        
        # Should have at least 3 transition slides for a typical lesson
        if len(transition_slides) < 3:
            self.warnings.append(
                f"⚠️ Only {len(transition_slides)} transition slides detected. "
                f"Per skill requirements, insert transitions BEFORE: vocabulary, challenge, "
                f"hero tool, practice, and reflection sections."
            )
    
    def _check_interleaving(self):
        """Verify answer slides immediately follow question slides."""
        for i, slide in enumerate(self.slides):
            if self._is_question_slide(slide):
                if i + 1 < len(self.slides):
                    next_slide = self.slides[i + 1]
                    if not self._is_answer_slide(next_slide):
                        self.errors.append(
                            f"❌ Slide {slide['number']} (\"{slide['title']}\") is a question/task "
                            f"but is NOT followed by an answer slide. "
                            f"Next slide is \"{next_slide['title']}\""
                        )
                else:
                    self.errors.append(
                        f"❌ Slide {slide['number']} (\"{slide['title']}\") is a question/task "
                        f"but has no following slide (should have answer key)."
                    )
    
    def _check_answer_slides_exist(self):
        """Check if there are any answer slides at all."""
        has_questions = any(self._is_question_slide(s) for s in self.slides)
        has_answers = any(self._is_answer_slide(s) for s in self.slides)
        
        if has_questions and not has_answers:
            self.errors.append(
                "❌ CRITICAL: Slideshow contains question/task slides but NO answer slides detected."
            )
    
    def _check_bullet_limits(self):
        """Enforce 5-7 bullet point maximum per slide."""
        for slide in self.slides:
            bullet_count = len(slide['content'])
            if bullet_count > 7:
                self.errors.append(
                    f"❌ Slide {slide['number']} (\"{slide['title']}\") has {bullet_count} bullet points. "
                    f"Maximum is 7 per skill requirements."
                )
            elif bullet_count > 6:
                self.warnings.append(
                    f"⚠️ Slide {slide['number']} (\"{slide['title']}\") has {bullet_count} bullets. "
                    f"Consider reducing to 5-6 for better readability."
                )
    
    def _check_vocabulary_format(self):
        """Check vocabulary slides follow the required format with actual Thai script."""
        for slide in self.slides:
            title_lower = slide['title'].lower()
            if 'vocab' in title_lower or 'vocabulary' in title_lower:
                content_text = ' '.join(slide['content'])
                
                # Check for required pattern: word /phonemic/: Thai translation
                if not re.search(r'/[^/]+/:', content_text):
                    self.errors.append(
                        f"❌ Slide {slide['number']} (\"{slide['title']}\") is marked as vocabulary "
                        f"but doesn't follow required format: word /phonemic/: Thai translation"
                    )
                
                # Check for actual Thai script (Unicode range for Thai: \u0E00-\u0E7F)
                if not re.search(r'[\u0E00-\u0E7F]', content_text):
                    self.errors.append(
                        f"❌ Slide {slide['number']} (\"{slide['title']}\") vocabulary slide "
                        f"must contain actual Thai script, not English transliteration."
                    )
                
                # Check context sentence length (short sentences often don't contextualize well)
                # Find sentences with the bolded word
                context_sentences = [b for b in slide['content'] if '**' in b or len(b) > 30]
                for sentence in context_sentences:
                    # Remove phonemic notation and Thai
                    if '/' in sentence and ':' in sentence:
                        continue  # This is the definition line
                    if re.search(r'[\u0E00-\u0E7F]', sentence):
                        continue  # Skip Thai sentences
                    # Check if English context sentence is too short
                    if len(sentence) < 50 and '**' in sentence:
                        self.warnings.append(
                            f"⚠️ Slide {slide['number']} (\"{slide['title']}\") has a short context sentence. "
                            f"Context sentences should ILLUSTRATE meaning, not just use the word."
                        )
    
    def _check_image_policy(self):
        """Enforce NO image placeholders policy."""
        forbidden_terms = ['[image', 'image:', '🖼️', 'placeholder', '[add image']
        
        for slide in self.slides:
            content_text = ' '.join(slide['content']).lower()
            title_lower = slide['title'].lower()
            
            for term in forbidden_terms:
                if term in content_text or term in title_lower:
                    self.errors.append(
                        f"❌ Slide {slide['number']} (\"{slide['title']}\") contains image placeholder reference. "
                        f"Per skill requirements: NO image placeholders allowed. Images added manually post-upload only."
                    )
                    break
    
    def _check_mechanistic_language(self):
        """Flag mechanistic/non-pedagogical language."""
        mechanistic_phrases = [
            'fill in the worksheet',
            'complete exercise',
            'do the activity',
            'answer the questions',
            'look at page'
        ]
        
        for slide in self.slides:
            content_text = ' '.join(slide['content']).lower()
            title_lower = slide['title'].lower()
            full_text = title_lower + ' ' + content_text
            
            for phrase in mechanistic_phrases:
                if phrase in full_text:
                    self.warnings.append(
                        f"⚠️ Slide {slide['number']} (\"{slide['title']}\") uses mechanistic language: \"{phrase}\". "
                        f"Consider reframing with analogies/metaphors (e.g., 'Be the Detective', 'Time to Build')."
                    )
                    break

    
    def print_report(self):
        """Print validation report."""
        print("\n" + "="*60)
        print("SLIDESHOW STRUCTURE VALIDATION REPORT")
        print("="*60 + "\n")
        
        print(f"Total Slides: {len(self.slides)}\n")
        
        # List questions and answers
        print("Question/Task Slides:")
        question_slides = [s for s in self.slides if self._is_question_slide(s)]
        if question_slides:
            for s in question_slides:
                print(f"  - Slide {s['number']}: {s['title']}")
        else:
            print("  (none detected)")
        
        print("\nAnswer Slides:")
        answer_slides = [s for s in self.slides if self._is_answer_slide(s)]
        if answer_slides:
            for s in answer_slides:
                print(f"  - Slide {s['number']}: {s['title']}")
        else:
            print("  (none detected)")
        
        print("\n" + "-"*60)
        
        if self.errors:
            print("\n🚫 VALIDATION FAILED\n")
            for error in self.errors:
                print(error)
        else:
            print("\n✅ VALIDATION PASSED")
            print("All answer slides are properly interleaved.")
        
        if self.warnings:
            print("\n⚠️ WARNINGS:\n")
            for warning in self.warnings:
                print(warning)
        
        print("\n" + "="*60 + "\n")


def validate_file(filepath):
    """Validate a markdown outline file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        outline_text = f.read()
    
    validator = SlideOutlineValidator(outline_text)
    is_valid = validator.validate()
    validator.print_report()
    
    return is_valid


def validate_text(outline_text):
    """Validate outline text directly."""
    validator = SlideOutlineValidator(outline_text)
    is_valid = validator.validate()
    validator.print_report()
    
    return is_valid


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python validate_slideshow_outline.py <outline.md>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    is_valid = validate_file(filepath)
    
    sys.exit(0 if is_valid else 1)
