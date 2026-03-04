import os
import requests
import sys
import base64
import json
import time
from pathlib import Path

# Configuration for Global Reference Repositories
# Updated 2026-03-04: Fixed 'reference' mapping to elwrush/lesson-plan-agent
REPOS = {
    "typst": "typst/typst",
    "typst-packages": "typst/packages",
    "revealjs": "hakimel/reveal.js",
    "fontawesome": "FortAwesome/Font-Awesome",
    "reference": "elwrush/lesson-plan-agent",
    "meander": "Vanille-N/meander.typ",
}

# The PAT provided by the user in the environment
TOKEN = os.getenv("GITHUB_MCP_PAT")

def get_headers():
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Gemini-CLI-Repo-Reader"
    }
    if TOKEN:
        # Fine-grained tokens work better with 'Bearer'
        auth_prefix = "Bearer" if TOKEN.startswith("github_pat_") else "token"
        headers["Authorization"] = f"{auth_prefix} {TOKEN}"
    return headers

def search_gh_content(alias, query):
    """
    Searches for code within a specific repository.
    """
    repo = REPOS.get(alias)
    if not repo:
        return f"Error: Alias '{alias}' not found. Available: {', '.join(REPOS.keys())}"
    
    # Use the GitHub Search API
    url = f"https://api.github.com/search/code?q={query}+repo:{repo}"
    headers = get_headers()
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            items = data.get("items", [])
            if not items:
                return f"No results found for '{query}' in {repo}."
            output = [f"[OK] Found {len(items)} results (showing top 10):"]
            for item in items[:10]:
                output.append(f"  - FILE: {item['path']}")
            return "\n".join(output)
        elif response.status_code == 403:
            return "Error: 403 Forbidden. This might be a search API rate limit. Authenticated search is limited to 30 requests per minute."
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"

def get_gh_content(alias_path):
    """
    Fetches file content or directory listings from GitHub.
    Usage: <alias>:<path>
    """
    if ":" not in alias_path:
        return f"Error: Usage must be <alias>:<path>. Available aliases: {', '.join(REPOS.keys())}"

    alias, path = alias_path.split(":", 1)
    # Strip leading slashes from path
    path = path.lstrip("/")
    
    repo = REPOS.get(alias)
    if not repo:
        return f"Error: Alias '{alias}' not found in REPOS mapping."
    
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    headers = get_headers()
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                output = [f"[DIR] {repo}/{path}"]
                for item in data:
                    item_type = "DIR " if item['type'] == 'dir' else "FILE"
                    output.append(f"  {item_type} {item['path']}")
                return "\n".join(output)
            
            if data.get("encoding") == "base64":
                content = base64.b64decode(data['content']).decode('utf-8')
                return content
            
            return f"Error: Unexpected response format from GitHub API."
        elif response.status_code == 404:
            return f"Error: 404 Not Found ({repo}/{path})."
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gh_fetch.py <alias>:<path>")
        print("       python gh_fetch.py search <alias> <query>")
        sys.exit(1)
        
    if sys.argv[1] == "search" and len(sys.argv) >= 4:
        result = search_gh_content(sys.argv[2], sys.argv[3])
    else:
        result = get_gh_content(sys.argv[1])
    print(result)
