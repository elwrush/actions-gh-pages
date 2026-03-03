import os
import json
import re
from google import genai
from google.genai import types

def segment_chunk(client, text, model="gemini-2.0-flash"):
    prompt = f"""
    You are an expert script editor. Please segment the following story chunk into a JSON array of objects.
    Each object must have "speaker" (Narrator, Hitchhiker, or Police Officer) and "text".
    
    IMPORTANT: 
    - The Narrator speaks everything that is NOT direct speech from the Hitchhiker or the Police Officer.
    - When a character speaks, include ONLY their quoted dialogue in their turn.
    - Keep the text VERBATIM. 
    - Output ONLY the JSON array.

    Story Chunk:
    {text}
    """

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        )
    )
    return json.loads(response.text)

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    src = r"G:\Other computers\My PC (1)\PROJECTS\LESSONS AND SLIDESHOWS 2\inputs\2026-02-11-B2-READING-AN-ADVENTURE-STORY\CLEAN-TEXT.md"
    with open(src, 'r', encoding='utf-8') as f:
        text = f.read()

    # Split into 4 roughly equal chunks
    chunk_size = len(text) // 4
    chunks = []
    for i in range(4):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < 3 else len(text)
        # Try to break at a newline
        if i < 3:
            next_nl = text.find('\n', end)
            if next_nl != -1:
                end = next_nl
        chunks.append(text[start:end])

    all_segments = []
    for i, chunk in enumerate(chunks):
        print(f"Segmenting chunk {i+1}/4...")
        segments = segment_chunk(client, chunk)
        all_segments.extend(segments)

    dest = r"G:\Other computers\My PC (1)\PROJECTS\LESSONS AND SLIDESHOWS 2\inputs\2026-02-11-B2-READING-AN-ADVENTURE-STORY\segments.json"
    with open(dest, 'w', encoding='utf-8') as f:
        json.dump(all_segments, f, indent=2)
    print(f"All segments saved to: {dest}")

if __name__ == "__main__":
    main()
