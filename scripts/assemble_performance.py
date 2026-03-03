import os
import json
import subprocess

def assemble_audio(audio_dir, output_file):
    metadata_path = os.path.join(audio_dir, "metadata.json")
    if not os.path.exists(metadata_path):
        print(f"Error: Metadata not found in {audio_dir}")
        return

    with open(metadata_path, 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    # Create a concat list file for ffmpeg
    concat_list_path = os.path.join(audio_dir, "concat_list.txt")
    with open(concat_list_path, 'w', encoding='utf-8') as f:
        for item in metadata:
            file_path = os.path.abspath(os.path.join(audio_dir, item['file']))
            # Escape single quotes for ffmpeg
            escaped_path = file_path.replace("'", "'\\''")
            f.write(f"file '{escaped_path}'\n")

    print(f"Assembling {len(metadata)} segments into {output_file}...")
    
    # Run FFMPEG concatenation
    # -f concat: use the concat demuxer
    # -safe 0: allow absolute paths
    # -c copy: just stitch them without re-encoding (if formats match)
    # However, since we might want consistent volume, let's re-encode with a simple filter
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list_path,
        "-filter:a", "loudnorm", # Normalize volume across speaker turns
        output_file
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"SUCCESS! Final audio saved to: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"FFMPEG Error: {e}")

if __name__ == "__main__":
    audio_dir = r"G:\Other computers\My PC (1)\PROJECTS\LESSONS AND SLIDESHOWS 2\inputs\2026-02-11-B2-READING-AN-ADVENTURE-STORY\audio_segments"
    out_file = r"G:\Other computers\My PC (1)\PROJECTS\LESSONS AND SLIDESHOWS 2\inputs\2026-02-11-B2-READING-AN-ADVENTURE-STORY\fingersmith_audio.mp3"
    assemble_audio(audio_dir, out_file)
