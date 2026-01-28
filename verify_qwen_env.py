import torch
import onnxruntime as ort
import sys
import os

print("--- Hardware Detection ---")
print(f"Python Version: {sys.version}")

# 1. Check Torch (CPU Logic)
print(f"Torch Version: {torch.__version__} (CPU-only is normal for Python 3.13 on AMD)")

# 2. Check ONNX Runtime (Hardware acceleration for 780M)
try:
    providers = ort.get_available_providers()
    print(f"Available ONNX Providers: {providers}")
    if 'DmlExecutionProvider' in providers:
        print("ONNX DirectML Provider: ✅ DETECTED (Optimal for your 780M)")
    else:
        print("ONNX DirectML Provider: ❌ MISSING (Check onnxruntime-directml installation)")
except Exception as e:
    print(f"ONNX Detection Error: {e}")

print("\n--- Summary ---")
if 'DmlExecutionProvider' in providers:
    print("READY: Your AZW SER8 is configured for Qwen3-TTS via ONNX acceleration.")
else:
    print("NOT READY: Hardware acceleration is missing. Please follow the Updated Implementation Plan.")

