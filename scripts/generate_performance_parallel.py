import os
import json
import time
import struct
import concurrent.futures
from google import genai
from google.genai import types

def convert_to_wav(audio_data: bytes, mime_type: str) -> bytes:
    """Generates a WAV file header for the given audio data (assuming 24kHz mono 16-bit)."""
    bits_per_sample = 16
    rate = 24000
    if "rate=" in mime_type:
        try:
            rate = int(mime_type.split("rate=")[1].split(";")[0])
        except:
            pass

    num_channels = 1
    data_size = len(audio_data)
    bytes_per_sample = bits_per_sample // 8
    block_align = num_channels * bytes_per_sample
    byte_rate = rate * block_align
    chunk_size = 36 + data_size

    header = struct.pack(
        "<4sI4s4sIHHIIHH4sI",
        b"RIFF", chunk_size, b"WAVE", b"fmt ", 16, 1, num_channels, rate, byte_rate, block_align, bits_per_sample, b"data", data_size
    )
    return header + audio_data

def generate_segment(client, i, seg, output_dir):
    speaker = seg['speaker']
    text = seg['text'].strip()
    if not text:
        return None

    filename = f"seg_{i:04d}.wav"
    filepath = os.path.join(output_dir, filename)

    # Idempotence: Skip if exists and has valid size
    if os.path.exists(filepath) and os.path.getsize(filepath) > 44: # > header size
        return {"file": filename, "speaker": speaker, "text": text}

    instructions = {
        "Narrator": "Read this in a warm, clear, professional British RP accent. You are the educated narrator of the story.",
        "Hitchhiker": "Read this in a sly, working-class British Estuary accent (Luton/Cockney style). Drop your 'h's and sound clever, quick, and 'ratty'.",
        "Police Officer": "Read this in a deep, booming, authoritarian British Police Officer's voice. You are intimidating and stern."
    }
    instruction = instructions.get(speaker, "Read this in a neutral British accent.")

    config = types.GenerateContentConfig(
        response_modalities=["audio"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Leda")
            )
        ),
    )

    full_prompt = f"Instruction: {instruction}\n\nText: {text}"

    max_retries = 5
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-pro-preview-tts",
                contents=full_prompt,
                config=config,
            )

            audio_data = b""
            mime_type = "audio/wav"
            
            if response.candidates and response.candidates[0].content.parts:
                for part in response.candidates[0].content.parts:
                    if part.inline_data:
                        audio_data += part.inline_data.data
                        mime_type = part.inline_data.mime_type or mime_type
            
            if audio_data:
                # Add WAV header (Gemini often sends raw PCM)
                final_wav = convert_to_wav(audio_data, mime_type)
                with open(filepath, 'wb') as f:
                    f.write(final_wav)
                return {"file": filename, "speaker": speaker, "text": text}
            
            print(f"Warning: No audio data for segment {i}")
            return None

        except Exception as e:
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                wait_time = (attempt + 1) * 30 # Longer backoff
                print(f"Quota hit for segment {i}. Waiting {wait_time}s...")
                time.sleep(wait_time)
            else:
                print(f"Error generating segment {i}: {e}")
                return None
    
    return None

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    seg_file = r"G:\Other computers\My PC (1)\PROJECTS\LESSONS AND SLIDESHOWS 2\inputs\2026-02-11-B2-READING-AN-ADVENTURE-STORY\segments.json"
    out_dir = r"G:\Other computers\My PC (1)\PROJECTS\LESSONS AND SLIDESHOWS 2\inputs\2026-02-11-B2-READING-AN-ADVENTURE-STORY\audio_segments"
    
    with open(seg_file, 'r', encoding='utf-8') as f:
        segments = json.load(f)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    print(f"Starting stabilized production with 2 workers for {len(segments)} segments...")
    
    results = [None] * len(segments)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_to_index = {executor.submit(generate_segment, client, i, seg, out_dir): i for i, seg in enumerate(segments)}
        
        for future in concurrent.futures.as_completed(future_to_index):
            idx = future_to_index[future]
            try:
                res = future.result()
                results[idx] = res
                completed = sum(1 for r in results if r is not None)
                if completed % 1 == 0: # Log every segment for visibility
                    print(f"[{completed}/{len(segments)}] Segment {idx} finished.")
            except Exception as e:
                print(f"Segment {idx} failed: {e}")

    final_metadata = [r for r in results if r is not None]
    with open(os.path.join(out_dir, "metadata.json"), 'w', encoding='utf-8') as f:
        json.dump(final_metadata, f, indent=2)
    
    print(f"Done! {len(final_metadata)} segments ready for assembly.")

if __name__ == "__main__":
    main()
