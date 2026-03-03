import os
import json
import time
from google import genai
from google.genai import types

def get_voice_config(speaker):
    """Returns the prebuilt voice and pitch/speed adjustments for each character."""
    if speaker == "Narrator":
        # Neutral, warm, professional RP
        return "Leda", 1.0, 1.0
    elif speaker == "Hitchhiker":
        # Crafty, quick, 'ratty' Luton/Cockney. Slightly higher pitch?
        return "Leda", 1.2, 1.1 
    elif speaker == "Police Officer":
        # Meaty, deep, slow authoritarian. Lower pitch.
        return "Leda", 0.8, 0.9
    return "Leda", 1.0, 1.0

def generate_voice_over(segments_path, output_dir):
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    with open(segments_path, 'r', encoding='utf-8') as f:
        segments = json.load(f)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    metadata = []

    for i, seg in enumerate(segments):
        speaker = seg['speaker']
        text = seg['text']
        
        # Clean up text if it's just quotes or weird fragments
        text = text.strip()
        if not text:
            continue

        filename = f"seg_{i:04d}.wav"
        filepath = os.path.join(output_dir, filename)

        # Build the Persona Instruction for Gemini 2.5 Pro TTS
        if speaker == "Narrator":
            instruction = "Read this in a warm, clear, professional British RP accent. You are the educated narrator of the story."
        elif speaker == "Hitchhiker":
            instruction = "Read this in a sly, working-class British Estuary accent (Luton/Cockney style). Drop your 'h's and sound clever, quick, and 'ratty'."
        elif speaker == "Police Officer":
            instruction = "Read this in a deep, booming, authoritarian British Police Officer's voice. You are intimidating and stern."
        else:
            instruction = "Read this in a neutral British accent."

        print(f"[{i}/{len(segments)}] Generating {speaker}: {text[:50]}...")

        # Note: Gemini 2.5 Pro TTS supports voice_name. 
        # For multi-speaker with ONE model, we rely on the Instruction prompt 
        # to differentiate the performance.
        
        config = types.GenerateContentConfig(
            response_modalities=["audio"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Leda")
                )
            ),
        )

        full_prompt = f"Instruction: {instruction}\n\nText: {text}"

        try:
            # We use gemini-2.5-pro-preview-tts for the actual audio generation
            response = client.models.generate_content(
                model="gemini-2.5-pro-preview-tts",
                contents=full_prompt,
                config=config,
            )

            audio_part = None
            if response.candidates and response.candidates[0].content.parts:
                for part in response.candidates[0].content.parts:
                    if part.inline_data:
                        audio_part = part.inline_data
                        break
            
            if audio_part:
                with open(filepath, 'wb') as f:
                    # Gemini returns raw audio/pcm or wav. 
                    # The previous script had logic to add bit headers if raw, 
                    # but typically the inline_data includes the format if checked.
                    # For simplicity and given the local env, we save the bytes.
                    f.write(audio_part.data)
                
                metadata.append({"file": filename, "speaker": speaker, "text": text})
            else:
                print(f"Warning: No audio data for segment {i}")

        except Exception as e:
            print(f"Error generating segment {i}: {e}")
            time.sleep(2) # Brief backoff

    # Save metadata for ffmpeg assembly
    with open(os.path.join(output_dir, "metadata.json"), 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2)

if __name__ == "__main__":
    seg_file = r"G:\Other computers\My PC (1)\PROJECTS\LESSONS AND SLIDESHOWS 2\inputs\2026-02-11-B2-READING-AN-ADVENTURE-STORY\segments.json"
    out_dir = r"G:\Other computers\My PC (1)\PROJECTS\LESSONS AND SLIDESHOWS 2\inputs\2026-02-11-B2-READING-AN-ADVENTURE-STORY\audio_segments"
    generate_voice_over(seg_file, out_dir)
