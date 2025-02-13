import requests
import base64
import streamlit as st
import time
import os

def push_db_to_github(db_file: str):
    """
    Pushes the local SQLite DB file to GitHub.
    
    Steps:
    1. Checks and logs file stats.
    2. Reads the file content and encodes it in base64.
    3. Retrieves the current file SHA (if the file exists on GitHub).
    4. Commits the updated file to GitHub via the API.
    """
    # Verify file stats (size and modified time)
    try:
        file_stat = os.stat(db_file)
        st.info(f"Local DB file: {db_file} | Size: {file_stat.st_size} bytes | Modified: {time.ctime(file_stat.st_mtime)}")
    except Exception as e:
        st.error(f"Error retrieving file stats for {db_file}: {e}")
        return

    # Get repository details from st.secrets
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

    # Encode the file content in base64 for the GitHub API
    encoded_content = base64.b64encode(content).decode("utf-8")

    # Construct the GitHub API URL for the file (ensure db_file path is correct)
    url = f"https://api.github.com/repos/{repo}/contents/{db_file}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Retrieve the current SHA of the file if it exists on GitHub
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            sha = response.json().get("sha")
            st.info(f"Current SHA on GitHub: {sha}")
        except Exception as e:
            st.error(f"Error parsing GitHub response: {e}")
            sha = None
    else:
        # File does not exist on GitHub yet
        sha = None

    # Prepare commit data with a unique commit message using a timestamp
    commit_message = f"Update {db_file} at {int(time.time())}"
    data = {
        "message": commit_message,
        "content": encoded_content
    }
    if sha:
        data["sha"] = sha

    # Wait briefly to ensure the file system has flushed any recent changes
    time.sleep(1)
    
    # Perform the PUT request to push the updated file to GitHub
    put_response = requests.put(url, json=data, headers=headers)
    if put_response.status_code in [200, 201]:
        st.success("Database pushed to GitHub successfully.")
        st.write("GitHub response:", put_response.json())
    else:
        st.error("Error pushing DB to GitHub:")
        st.error(put_response.json())

def pull_db_from_github(db_file: str):
    """
    Pulls the latest version of the SQLite DB file from GitHub and writes it locally.
    
    Steps:
    1. Retrieves the file content from GitHub via the API.
    2. Decodes the base64 content.
    3. Writes the content to the local file.
    """
    # Get repository details from st.secrets
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
