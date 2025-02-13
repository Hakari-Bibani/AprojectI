import requests
import base64
import streamlit as st
import time

def push_db_to_github(db_file: str):
    # [Your existing push implementation here]
    try:
        repo = st.secrets["general"]["repo"]
        token = st.secrets["general"]["token"]
    except Exception as e:
        print(f"Secrets not found or misconfigured: {e}")
        return

    try:
        with open(db_file, "rb") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {db_file}: {e}")
        return

    encoded_content = base64.b64encode(content).decode("utf-8")
    
    url_base = f"https://api.github.com/repos/{repo}/contents/{db_file}"
    cache_buster = str(int(time.time()))
    get_url = url_base + f"?t={cache_buster}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        get_response = requests.get(get_url, headers=headers)
        if get_response.status_code == 200:
            get_data = get_response.json()
            sha = get_data.get("sha", None)
        else:
            sha = None

        commit_message = f"Update {db_file} at {int(time.time())}"
        data = {
            "message": commit_message,
            "content": encoded_content
        }
        if sha:
            data["sha"] = sha

        put_response = requests.put(url_base, json=data, headers=headers)
        response_json = put_response.json()
        print("PUT response status:", put_response.status_code)
        print("PUT response JSON:", response_json)
        if put_response.status_code in [200, 201]:
            print("Database pushed to GitHub successfully.")
        else:
            print("Error pushing DB to GitHub:", response_json)
    except Exception as e:
        print(f"Error in push_db_to_github: {e}")

def pull_db_from_github(db_file: str):
    """
    Pulls the latest version of the database file from GitHub.
    This is a placeholder implementation—replace with your actual logic.
    """
    try:
        repo = st.secrets["general"]["repo"]
        token = st.secrets["general"]["token"]
    except Exception as e:
        print(f"Secrets not found or misconfigured: {e}")
        return

    url = f"https://api.github.com/repos/{repo}/contents/{db_file}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            file_content = base64.b64decode(data["content"])
            with open(db_file, "wb") as f:
                f.write(file_content)
            print("Database pulled from GitHub successfully.")
        else:
            print("Error pulling DB from GitHub:", response.json())
    except Exception as e:
        print(f"Error in pull_db_from_github: {e}")
