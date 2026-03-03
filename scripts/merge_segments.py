import json
import os

def merge_segments(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        segments = json.load(f)

    merged = []
    if not segments:
        return

    current_speaker = segments[0]['speaker']
    current_text = segments[0]['text']

    for i in range(1, len(segments)):
        speaker = segments[i]['speaker']
        text = segments[i]['text']

        if speaker == current_speaker:
            # Add a small space between merged sentences for better TTS cadence
            current_text += " " + text
        else:
            merged.append({"speaker": current_speaker, "text": current_text})
            current_speaker = speaker
            current_text = text

    # Add the last block
    merged.append({"speaker": current_speaker, "text": current_text})

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(merged, f, indent=2)
    
    print(f"Merged {len(segments)} segments into {len(merged)} blocks.")

if __name__ == "__main__":
    src = r"G:\Other computers\My PC (1)\PROJECTS\LESSONS AND SLIDESHOWS 2\inputs\2026-02-11-B2-READING-AN-ADVENTURE-STORY\segments.json"
    dest = r"G:\Other computers\My PC (1)\PROJECTS\LESSONS AND SLIDESHOWS 2\inputs\2026-02-11-B2-READING-AN-ADVENTURE-STORY\segments_merged.json"
    merge_segments(src, dest)
