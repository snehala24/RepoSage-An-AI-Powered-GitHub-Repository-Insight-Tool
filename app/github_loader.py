import os
import requests
import zipfile
import shutil

def download_repo(github_url: str, download_root: str = "data/raw_repo") -> str:
    """
    Download and extract a GitHub repository ZIP and return the path to the extracted folder.
    """

    # Clean previous repo data
    if os.path.exists(download_root):
        shutil.rmtree(download_root)
    os.makedirs(download_root, exist_ok=True)

    # Strip trailing slash if present
    github_url = github_url.rstrip("/")

    # Extract owner and repo
    try:
        owner, repo = github_url.split("/")[-2], github_url.split("/")[-1]
    except Exception:
        raise ValueError("❌ Invalid GitHub URL format.")

    # Fetch default branch from GitHub API
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"Accept": "application/vnd.github.v3+json"}
    resp = requests.get(api_url, headers=headers)

    if resp.status_code != 200:
        raise Exception(f"GitHub API Error: {resp.status_code} - {resp.text}")

    default_branch = resp.json().get("default_branch", "main")
    zip_url = f"https://github.com/{owner}/{repo}/archive/refs/heads/{default_branch}.zip"

    # Download the ZIP file
    zip_path = os.path.join(download_root, "repo.zip")
    r = requests.get(zip_url)
    if r.status_code != 200 or not r.content.startswith(b'PK'):
        raise Exception(f"❌ Failed to download valid ZIP file: {zip_url}")

    with open(zip_path, "wb") as f:
        f.write(r.content)

    # Extract the ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(download_root)

    # Identify the extracted repo folder
    extracted_folders = [
        f for f in os.listdir(download_root)
        if os.path.isdir(os.path.join(download_root, f)) and not f.endswith(".zip")
    ]

    if not extracted_folders:
        raise Exception("❌ ZIP extracted but no folder found.")

    return os.path.join(download_root, extracted_folders[0])
