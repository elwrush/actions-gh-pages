import os
from google import genai
from google.genai import types

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

prompt = "An abstract representation of an adrenaline rush. A burst of amber and maroon energy lines radiating from a center point, dark background, electric feel, high contrast, cinematic."

print(f"Generating adrenaline_rush.png...")

result = client.models.generate_images(
    model="imagen-4.0-generate-001",
    prompt=prompt,
    config=types.GenerateImagesConfig(
        number_of_images=1,
        include_rai_reason=True,
        output_mime_type="image/png"
    )
)

if result.generated_images:
    image = result.generated_images[0]
    output_path = "c:/PROJECTS/LESSONS AND SLIDESHOWS 2/presentations/18-01-26_Fight-or-Flight/images/adrenaline_rush.png"
    with open(output_path, "wb") as f:
        f.write(image.image.image_bytes)
    print(f"Successfully saved to {output_path}")
    print(f"File size: {len(image.image.image_bytes)} bytes")
else:
    print("No image generated")
