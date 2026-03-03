import fitz

doc = fitz.open('test9.pdf')
page = doc[0]

print("Text Blocks:")
for block in page.get_text('dict')['blocks']:
    if block['type'] == 0:
        for line in block['lines']:
            for span in line['spans']:
                if '1.' in span['text']:
                    print(f"Text '1.': bbox={span['bbox']}, origin={span['origin']}, ascender={span['ascender']}, descender={span['descender']}")

print("\nDrawings (Lines/Paths):")
for path in page.get_drawings():
    print(path['rect'])
