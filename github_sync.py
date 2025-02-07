# github_sync.py
import requests
import base64
import streamlit as st
import os

def pull_db_from_github(db_file: str):
    """
    Pull the remote SQLite DB file from GitHub
    and overwrite the local db_file if found.
    """
    repo = st.secrets["general"]["repo"]
    token = st.secrets["general"]["token"]
    url = f"https://api.github.com/repos/{repo}/contents/{db_file}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # File exists in GitHub
        content = response.json().get("content", "")
        if content:
            decoded = base64.b64decode(content)
            with open(db_file, "wb") as f:
                f.write(decoded)
            print(f"Pulled latest {db_file} from GitHub.")
        else:
            print(f"No content found in {db_file} on GitHub.")
    else:
        print(f"Could not find {db_file} in the GitHub repo. Using local copy if exists.")

def push_db_to_github(db_file: str):
    """
    Pushes the local SQLite DB file to GitHub.
    Overwrites the existing file if it exists.
    """
    repo = st.secrets["general"]["repo"]
    token = st.secrets["general"]["token"]
    
    with open(db_file, "rb") as f:
        content = f.read()
    encoded_content = base64.b64encode(content).decode("utf-8")
    
    url = f"https://api.github.com/repos/{repo}/contents/{db_file}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    get_response = requests.get(url, headers=headers)
    sha = get_response.json()["sha"] if get_response.status_code == 200 else None
    
    data = {"message": "Update mydatabase.db", "content": encoded_content}
    if sha:
        data["sha"] = sha
    
    put_response = requests.put(url, json=data, headers=headers)
    if put_response.status_code in [200, 201]:
        print("Database pushed to GitHub successfully.")
    else:
        print("Error pushing DB to GitHub:", put_response.json())
