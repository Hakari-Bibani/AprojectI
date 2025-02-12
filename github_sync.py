import requests
import base64
import streamlit as st
import time

def push_db_to_github(db_file: str):
    """
    Pushes the local SQLite DB file to GitHub.
    Overwrites the existing file if it exists.
    """
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
    
    # Define the base URL (without query parameters) as required by GitHub.
    url_base = f"https://api.github.com/repos/{repo}/contents/{db_file}"
    
    # Use a cache buster only when GETting the SHA to force a fresh lookup.
    cache_buster = str(int(time.time()))
    get_url = url_base + f"?t={cache_buster}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        # GET the current file's SHA using the cache-busted URL.
        get_response = requests.get(get_url, headers=headers)
        if get_response.status_code == 200:
            get_data = get_response.json()
            sha = get_data.get("sha", None)
        else:
            sha = None

        # Use a unique commit message each time (append a timestamp).
        commit_message = f"Update mydatabase.db at {int(time.time())}"
        data = {
            "message": commit_message,
            "content": encoded_content
        }
        if sha:
            data["sha"] = sha

        # For the PUT request, use the clean URL (no query parameter).
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
