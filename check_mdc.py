import os
from datacollective import get_dataset_details

dataset_id = "cmko7havo02f5nw07rbwwhowe" 

try:
    print(f"Checking MDC_API_KEY...")
    key = os.getenv("MDC_API_KEY")
    if key:
        print(f"API Key found (starts with: {key[:4]}...)")
    else:
        print("API Key NOT found in environment.")

    print(f"Fetching details for dataset: {dataset_id}")
    details = get_dataset_details(dataset_id)
    print("Dataset Details:")
    for k, v in details.items():
        if k != "downloadUrl":
            print(f"  {k}: {v}")
            
except Exception as e:
    print(f"Error: {e}")
