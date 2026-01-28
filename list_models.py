import google.generativeai as genai
import os

API_KEY = os.environ.get("GOOGLE_API_KEY")
if not API_KEY:
    # Try alternate name
    API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

print("Listing available models...")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
