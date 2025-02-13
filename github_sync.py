import requests
import base64
import streamlit as st
import time

def push_db_to_github(db_file: str):
    """
    Pushes the local SQLite DB file to GitHub.
    It encodes the database file in base64 and uses the GitHub API to update
    the file in your repository. This function assumes that the local database file 
    has been updated (e.g., a new grade has overwritten the previous one) before calling it.
    """
    # Retrieve GitHub repo details from st.secrets
    try:
        repo = st.secrets["general"]["repo"]
        token = st.secrets["general"]["token"]
    except Exception as e:
        st.error(f"Secrets not found or misconfigured: {e}")
        return

    # Read the local database file
    try:
        with open(db_file, "rb") as f:
            content = f.read()
    except Exception as e:
        st.error(f"Error reading {db_file}: {e}")
        return

    # Encode the file content in base64
    encoded_content = base64.b64encode(content).decode("utf-8")

    # Construct the GitHub API URL for the file (make sure db_file path is correct)
    url = f"https://api.github.com/repos/{repo}/contents/{db_file}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Get the current SHA of the file (if it exists)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            sha = response.json().get("sha")
        except Exception as e:
            st.error(f"Error parsing GitHub response: {e}")
            sha = None
    else:
        # If the file doesn't exist yet, leave sha as None.
        sha = None

    # Prepare commit data with a unique commit message (using a timestamp)
    commit_message = f"Update {db_file} at {int(time.time())}"
    data = {
        "message": commit_message,
        "content": encoded_content
    }
    if sha:
        data["sha"] = sha

    # Perform the PUT request to update the file on GitHub
    put_response = requests.put(url, json=data, headers=headers)
    if put_response.status_code in [200, 201]:
        st.success("Database pushed to GitHub successfully.")
        st.write("GitHub response:", put_response.json())
    else:
        st.error("Error pushing DB to GitHub:")
        st.error(put_response.json())

def pull_db_from_github(db_file: str):
    """
    Pulls the latest version of the SQLite DB file from GitHub and saves it locally.
    This function decodes the base64 content returned by the GitHub API and writes it
    to the local file system.
    """
    # Retrieve GitHub repo details from st.secrets
    try:
        repo = st.secrets["general"]["repo"]
        token = st.secrets["general"]["token"]
    except Exception as e:
        st.error(f"Secrets not found or misconfigured: {e}")
        return

    url = f"https://api.github.com/repos/{repo}/contents/{db_file}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Get the file content from GitHub
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            # Decode the base64 content
            file_content = base64.b64decode(data["content"])
            # Write the updated content back to the local file
            with open(db_file, "wb") as f:
                f.write(file_content)
            st.info("Database pulled from GitHub successfully.")
        except Exception as e:
            st.error(f"Error processing GitHub response: {e}")
    else:
        st.error(f"Error pulling DB from GitHub: {response.json()}")
