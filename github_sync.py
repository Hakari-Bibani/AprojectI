import requests
import base64
import streamlit as st
import time

def pull_db_from_github(db_file: str):
    """
    Pull the remote SQLite DB file from GitHub
    and overwrite the local db_file if found.
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
    except Exception as e:
        print(f"Error in pull_db_from_github: {e}")

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
    
    # Define the base URL without any query parameters (this is what GitHub expects)
    url_base = f"https://api.github.com/repos/{repo}/contents/{db_file}"
    
    # Use a cache buster only when getting the SHA
    cache_buster = str(int(time.time()))
    get_url = url_base + f"?t={cache_buster}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        # Get the current file's SHA using the cache-busted URL
        get_response = requests.get(get_url, headers=headers)
        if get_response.status_code == 200:
            get_data = get_response.json()
            sha = get_data.get("sha", None)
        else:
            sha = None

        data = {
            "message": "Update mydatabase.db",
            "content": encoded_content
        }
        if sha:
            data["sha"] = sha

        # Use the plain URL (without the cache buster) for the PUT request
        put_response = requests.put(url_base, json=data, headers=headers)
        if put_response.status_code in [200, 201]:
            print("Database pushed to GitHub successfully.")
        else:
            print("Error pushing DB to GitHub:", put_response.json())
    except Exception as e:
        print(f"Error in push_db_to_github: {e}")
