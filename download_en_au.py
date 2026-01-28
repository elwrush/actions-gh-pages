import os
from datacollective import save_dataset_to_disk

dataset_id = "cmko7havo02f5nw07rbwwhowe" 
download_dir = "c:/PROJECTS/LESSONS AND SLIDESHOWS 2/datasets"

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

try:
    print(f"Downloading dataset {dataset_id} to {download_dir}...")
    archive_path = save_dataset_to_disk(dataset_id, download_directory=download_dir)
    print(f"Dataset downloaded to: {archive_path}")
except Exception as e:
    print(f"Error: {e}")
