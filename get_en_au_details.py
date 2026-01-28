import os
from datacollective import get_dataset_details

dataset_id = "cmko7havo02f5nw07rbwwhowe" 

try:
    details = get_dataset_details(dataset_id)
    import json
    print(json.dumps(details, indent=2))
except Exception as e:
    print(f"Error: {e}")
