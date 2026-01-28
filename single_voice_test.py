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
original_session = ort.InferenceSession
class DMLLoader(original_session):
    def __init__(self, path_or_bytes, sess_options=None, providers=None, **kwargs):
        available = ort.get_available_providers()
        if 'DmlExecutionProvider' in available:
            providers = ['DmlExecutionProvider', 'CPUExecutionProvider']
        super().__init__(path_or_bytes, sess_options=sess_options, providers=providers, **kwargs)
ort.InferenceSession = DMLLoader

def main():
    model_name = "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign"
    print(f"Loading model: {model_name}...")
    
    tts = Qwen3TTSModel.from_pretrained(
        model_name,
        device_map="cpu",
        dtype=torch.float32 
    )

    text = "I went to the shops to buy some icecream but it was closed."
    # Refined instruction for a grounded Australian accent
    instruct = "A 14-year-old Australian teenager with a natural, grounded, and slightly lower-pitched Australian accent. The vowels should be distinctly Australian, especially the 'i' in ice cream. The voice should sound authentic to an Australian high schooler and not squeaky."

    print(f"\nGenerating: \"{text}\"")
    wavs, sr = tts.generate_voice_design(
        text=text,
        instruct=instruct,
        language="English",
        max_new_tokens=512
    )
    
    output_file = "australian_teen_test.wav"
    sf.write(output_file, wavs[0], sr)
    print(f"\nSUCCESS! Audio saved to: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()
