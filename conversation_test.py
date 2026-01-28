import os
import torch
import soundfile as sf
import numpy as np
import onnxruntime as ort
from qwen_tts import Qwen3TTSModel

# --- 0. Fix SoX Path (WinGet Portable Installation) ---
SOX_DIR = r"C:\Users\elwru\AppData\Local\Microsoft\WinGet\Packages\ChrisBagwell.SoX_Microsoft.Winget.Source_8wekyb3d8bbwe\sox-14.4.2"
if SOX_DIR not in os.environ["PATH"]:
    os.environ["PATH"] = SOX_DIR + os.pathsep + os.environ["PATH"]

# --- 1. Optimization: Monkeypatch ONNX to use DirectML ---
# The internal library sometimes defaults to CPU. We force DirectML for the 780M.
original_session = ort.InferenceSession

class DMLLoader(original_session):
    def __init__(self, path_or_bytes, sess_options=None, providers=None, **kwargs):
        available = ort.get_available_providers()
        if 'DmlExecutionProvider' in available:
            providers = ['DmlExecutionProvider', 'CPUExecutionProvider']
            print(f"DEBUG: Forcing DirectML for {os.path.basename(str(path_or_bytes))}")
        super().__init__(path_or_bytes, sess_options=sess_options, providers=providers, **kwargs)

ort.InferenceSession = DMLLoader

def main():
    # Use 1.7B VoiceDesign for flexible voice creation
    model_name = "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign"
    print(f"Loading model: {model_name}...")
    
    # On AMD/Windows with CPU Torch, we use float32 or bfloat16 if supported
    # Note: device_map='cpu' is required since we don't have CUDA
    tts = Qwen3TTSModel.from_pretrained(
        model_name,
        device_map="cpu",
        torch_dtype=torch.float32 
    )

    dialogue = [
        ("Mia", "Hey Leo, are you busy? I'm thinking of heading to the mall.", 
         "A 14-year-old girl with a natural, clear Australian accent. Her voice is youthful but grounded and typical of a teenager, not squeaky."),
        ("Leo", "Not really, just finishing some homework. What do you need to get?", 
         "A 14-year-old boy with a friendly, casual Australian accent. His voice is clear and characteristic of a teenage boy."),
        ("Mia", "I need some new sneakers for gym class. The ones I have are falling apart, and they're starting to hurt my feet.", 
         "A 14-year-old girl with a natural, clear Australian accent. Her voice is youthful but grounded and typical of a teenager, not squeaky."),
        ("Leo", "Cool, I actually need to look for a birthday present for my brother. He wants a new gaming headset. Mind if I tag along?", 
         "A 14-year-old boy with a friendly, casual Australian accent. His voice is clear and characteristic of a teenage boy."),
        ("Mia", "Not at all! It’ll be better than shopping alone. Let’s meet at the bus stop in ten minutes?", 
         "A 14-year-old girl with a natural, clear Australian accent. Her voice is youthful but grounded and typical of a teenager, not squeaky."),
        ("Leo", "Sounds like a plan. See you then!", 
         "A 14-year-old boy with a friendly, casual Australian accent. His voice is clear and characteristic of a teenage boy.")
    ]

    all_wavs = []
    sample_rate = 24000 # Default for Qwen3-TTS

    print("\nStarting Synthesis...")
    for i, (speaker, text, instruct) in enumerate(dialogue):
        print(f"Generating {speaker}: \"{text[:30]}...\"")
        
        # generate_voice_design returns (List[np.ndarray], sampling_rate)
        wavs, sr = tts.generate_voice_design(
            text=text,
            instruct=instruct,
            language="English",
            max_new_tokens=1024
        )
        all_wavs.append(wavs[0])
        sample_rate = sr
        
        # Add a short silence (0.5s) between speakers
        silence = np.zeros(int(sample_rate * 0.5))
        all_wavs.append(silence)

    # Concatenate all parts
    final_audio = np.concatenate(all_wavs)
    
    output_file = "shopping_conversation.wav"
    sf.write(output_file, final_audio, sample_rate)
    print(f"\nSUCCESS! Audio saved to: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()
