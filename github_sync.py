# github_sync.py
import requests
import base64
import streamlit as st
import time

def pull_db_from_github(db_file: str):
    """
    Pull the remote SQLite DB file from GitHub
    and overwrite the local db_file if found.
    """
    repo = st.secrets["general"]["repo"]
    token = st.secrets["general"]["token"]
    branch = st.secrets["general"].get("branch", "main")
    url = f"https://api.github.com/repos/{repo}/contents/{db_file}?ref={branch}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
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
    branch = st.secrets["general"].get("branch", "main")
    
    # Read the local database file and encode it in base64
    try:
        with open(db_file, "rb") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {db_file}: {e}")
        return

    encoded_content = base64.b64encode(content).decode("utf-8")
    
    url = f"https://api.github.com/repos/{repo}/contents/{db_file}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # To avoid cached GET responses (which might return an old sha),
    # add a unique query parameter (e.g., current time)
    get_url = f"{url}?ref={branch}&_={int(time.time())}"
    get_response = requests.get(get_url, headers=headers)
    try:
        get_data = get_response.json()
    except Exception as e:
        print("Error decoding GET response JSON:", e)
        get_data = {}
    sha = get_data.get("sha", None)
    print("Existing file SHA:", sha)
    
    # Prepare the data payload for the PUT request
    data = {
        "message": "Update database file with new assignment grade",
        "content": encoded_content,
        "branch": branch
    }
    if sha:
        data["sha"] = sha

    # Execute the PUT request to update the file on GitHub
    put_response = requests.put(url, json=data, headers=headers)
    print("PUT response status:", put_response.status_code)
    print("PUT response text:", put_response.text)
    if put_response.status_code in [200, 201]:
        print("Database pushed to GitHub successfully.")
    else:
        print("Error pushing DB to GitHub:", put_response.json())
