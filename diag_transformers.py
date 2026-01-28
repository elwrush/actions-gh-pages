import traceback
import sys

print(f"Python: {sys.version}")
try:
    from transformers import AutoProcessor
    print('Import Success')
except Exception:
    print("--- TRACEBACK START ---")
    traceback.print_exc()
    print("--- TRACEBACK END ---")
