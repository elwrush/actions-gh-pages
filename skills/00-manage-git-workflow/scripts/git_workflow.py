import subprocess
import sys
import argparse
import os

def run_command(cmd, shell=True):
    try:
        result = subprocess.run(cmd, shell=shell, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

def scrub():
    """Aggressively remove system junk and reserved device names."""
    print("[SCRUB] Removing desktop.ini and reserved files (nul)...")
    # Using the \\?\ prefix to handle reserved names like 'nul'
    commands = [
        'Get-ChildItem -Path . -Recurse -Include "desktop.ini" -Force -ErrorAction SilentlyContinue | Remove-Item -Force',
        'Remove-Item -LiteralPath "\\\\?\\' + os.getcwd() + '\\nul" -Force -ErrorAction SilentlyContinue'
    ]
    for cmd in commands:
        subprocess.run(['powershell', '-Command', cmd])
    print("✅ System junk scrubbed.")

def commit(message):
    """Commits and pushes changes. MANDATORY: Only call if user explicitly asked to commit."""
    scrub()
    
    # Ensure nul is in .gitignore to prevent git from crashing on Windows
    ensure_nul_ignored()
    
    print(f"[COMMIT] Staging and committing: {message}...")
    run_command("git add .")
    run_command("git reset dist/")
    run_command('git commit -m "' + message + '"')
    print("[PUSH] Pushing to source...")
    run_command("git push source main")
    print("✅ Changes saved to source repository.")

def ensure_nul_ignored():
    """Ensure the reserved 'nul' device name is in .gitignore."""
    gitignore_path = os.path.join(os.getcwd(), ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "nul" not in content.lower():
            with open(gitignore_path, "a", encoding="utf-8") as f:
                f.write("\n# Problematic Windows Device Files\nnul\nNUL\n")

def release(version, description):
    scrub()
    print(f"[RELEASE] Creating annotated tag: {version}...")
    run_command(f'git tag -a {version} -m "{description}"')
    run_command("git push source --tags")
    print(f"✅ Released version {version}")

def status():
    print("--- Git Workflow Status ---")
    branch = run_command("git rev-parse --abbrev-ref HEAD")
    # Handle case where no tags exist yet
    last_tag = run_command("git describe --tags --abbrev=0") or "None"
    print(f"Branch: {branch}")
    print(f"Last Tag: {last_tag}")
    print("\nPending Changes (Status):")
    print(run_command("git status -s"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Git Workflow Automation")
    
    if len(sys.argv) < 2:
        status()
        sys.exit(0)
        
    command = sys.argv[1]
    
    if command == "commit":
        msg = sys.argv[2] if len(sys.argv) > 2 else "chore: save work"
        commit(msg)
    elif command == "release":
        if len(sys.argv) < 4:
            print("Usage: python git_workflow.py release <version> <description>")
        else:
            release(sys.argv[2], sys.argv[3])
    elif command == "scrub":
        scrub()
    elif command == "status":
        status()
    else:
        print("Unknown command. Use: status, commit, release, scrub")
