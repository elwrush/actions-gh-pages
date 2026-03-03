import os
import json
from google import genai
from google.genai import types

def segment_story(input_path, output_path):
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    prompt = f"""
    You are an expert script editor. Please segment the following story into a JSON array of objects.
    Each object must have "speaker" (Narrator, Hitchhiker, or Police Officer) and "text" (the verbatim text they speak, including the 'he said' tags if the Narrator is speaking those parts, or just the dialogue if it's a character).
    
    IMPORTANT: 
    - The Narrator speaks everything that is NOT direct speech from the Hitchhiker or the Police Officer.
    - When a character speaks, include ONLY their quoted dialogue in their turn.
    - Example:
      Text: The hitchhiker poked his head through the open window and said, "Going to London, guv'nor?". "Yes," I said. "Jump in".
      JSON:
      [
        {{"speaker": "Narrator", "text": "The hitchhiker poked his head through the open window and said, "}},
        {{"speaker": "Hitchhiker", "text": "Going to London, guv'nor?"}},
        {{"speaker": "Narrator", "text": ". "}},
        {{"speaker": "Narrator", "text": "\"Yes,\" I said. "}},
        {{"speaker": "Narrator", "text": "\"Jump in\". "}}
      ]
    - Actually, for smoother audio, if the Narrator says '"Yes," I said', it's better if the Narrator reads that whole part since "I" is the Narrator. 
    - Only the Hitchhiker's and Police Officer's direct quotes should be assigned to them.
    - Keep the text VERBATIM. 
    - Do not skip any text.

    Story:
    {text}
    """

    print("Segmenting story using Gemini...")
    response = client.models.generate_content(
        model="gemini-2.0-flash", # Use flash for fast segmentation
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        )
    )

    try:
        segments = json.loads(response.text)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(segments, f, indent=2)
        print(f"Segments saved to: {output_path}")
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        print("Response was:", response.text)

if __name__ == "__main__":
    src = r"G:\Other computers\My PC (1)\PROJECTS\LESSONS AND SLIDESHOWS 2\inputs\2026-02-11-B2-READING-AN-ADVENTURE-STORY\CLEAN-TEXT.md"
    dest = r"G:\Other computers\My PC (1)\PROJECTS\LESSONS AND SLIDESHOWS 2\inputs\2026-02-11-B2-READING-AN-ADVENTURE-STORY\segments.json"
    segment_story(src, dest)
