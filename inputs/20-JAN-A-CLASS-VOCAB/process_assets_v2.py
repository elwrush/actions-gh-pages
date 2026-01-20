import os
import shutil

# Typst code for title
typst_title_code = r"""
#let title_graphic() = {
  block(
    width: 100%,
    height: 3cm,
    fill: gradient.linear(angle: 45deg, rgb("#D35400"), rgb("#E67E22"), rgb("#F39C12")),
    radius: 4pt,
    inset: 0pt,
    align(center + horizon)[
      #text(size: 36pt, weight: "black", fill: white, font: "Impact")[LOCAL TO GLOBAL BUSINESS]
    ]
  )
}
"""

def generate_assets():
    # Since we can't reliably generate images (429), and we have a baker image from Pixabay now.
    # We will rely on Typst-native graphics for the title if generation fails (which it did).
    pass

if __name__ == "__main__":
    generate_assets()
