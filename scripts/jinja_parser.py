import re

def parse_directives(text: str) -> str:
    """
    Parses proprietary bracketed directives into HTML framework-specific tags.
    Supported directives:
    - [REVEAL: word] -> <span class="fragment">word</span>
    - [STRIKE: word] -> <span class="fragment strike-anim">word</span>
    - [HIGHLIGHT: word] -> <span class="highlight" style="color: #FFD700;">word</span>
    """
    if not text:
        return text
        
    # Replace [REVEAL: text]
    text = re.sub(
        r'\[REVEAL:\s*(.+?)\]',
        r'<span class="fragment">\1</span>',
        text
    )
    
    # Replace [STRIKE: text]
    text = re.sub(
        r'\[STRIKE:\s*(.+?)\]',
        r'<span class="fragment strike-anim">\1</span>',
        text
    )
    
    # Replace [HIGHLIGHT: text]
    text = re.sub(
        r'\[HIGHLIGHT:\s*(.+?)\]',
        r'<span class="highlight" style="color: #FFD700;">\1</span>',
        text
    )
    
    return text
