import os
import requests
from datacollective.api_utils import _get_api_url, _auth_headers

api_url = _get_api_url()
headers = _auth_headers()

# Try searching for en-AU
search_url = f"{api_url}/search?q=en-AU"

try:
    print(f"Probing: {search_url}")
    resp = requests.get(search_url, headers=headers)
    print(f"Status: {resp.status_code}")
    if resp.status_code == 200:
        print(resp.json())
    else:
        print(resp.text)
except Exception as e:
    print(f"Error: {e}")
