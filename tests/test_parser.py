import unittest

# We expect this import to fail initially (Red Phase)
from scripts.jinja_parser import parse_directives

class TestDirectiveParser(unittest.TestCase):
    def test_reveal_directive_parsing(self):
        """Test that the [REVEAL: text] directive is converted to the correct HTML."""
        input_text = "Here is a [REVEAL: secret] word."
        expected_html = "Here is a <span class=\"fragment\">secret</span> word."
        self.assertEqual(parse_directives(input_text), expected_html)

    def test_strike_directive_parsing(self):
        """Test that the [STRIKE: text] directive is converted to the correct HTML."""
        input_text = "This is a [STRIKE: mistake] test."
        expected_html = "This is a <span class=\"fragment strike-anim\">mistake</span> test."
        self.assertEqual(parse_directives(input_text), expected_html)

    def test_highlight_directive_parsing(self):
        """Test that the [HIGHLIGHT: text] directive is converted to the correct HTML."""
        input_text = "This is [HIGHLIGHT: important]."
        expected_html = "This is <span class=\"highlight\" style=\"color: #FFD700;\">important</span>."
        self.assertEqual(parse_directives(input_text), expected_html)

    def test_multiple_directives(self):
        """Test multiple directives in the same string."""
        input_text = "[STRIKE: Wrong] [REVEAL: Right]."
        expected_html = "<span class=\"fragment strike-anim\">Wrong</span> <span class=\"fragment\">Right</span>."
        self.assertEqual(parse_directives(input_text), expected_html)

if __name__ == '__main__':
    unittest.main()
