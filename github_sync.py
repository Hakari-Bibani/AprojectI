import requests
import base64
import streamlit as st
import time
import os

def push_db_to_github(db_file: str):
    """
    Pushes the local SQLite DB file to GitHub.
    It encodes the database file in base64 and uses the GitHub API to update
    the file in your repository. This function assumes that the local database file 
    has been updated (i.e., a new grade has overwritten the previous one) before calling it.
    """
    # Check file stats to ensure we are reading the updated file
    try:
        file_stat = os.stat(db_file)
        st.info(f"Local DB file size: {file_stat.st_size} bytes, modified: {time.ctime(file_stat.st_mtime)}")
    except Exception as e:
        st.error(f"Error retrieving file stats for {db_file}: {e}")
        return

    # Retrieve GitHub repository details from st.secrets
    try:
        repo = st.secrets["general"]["repo"]
        token = st.secrets["general"]["token"]
    except Exception as e:
        st.error(f"Secrets not found or misconfigured: {e}")
        return

    # Read the updated local database file
    try:
        with open(db_file, "rb") as f:
            content = f.read()
    except Exception as e:
        st.error(f"Error reading {db_file}: {e}")
        return

    # Encode the content in base64 for the GitHub API
    encoded_content = base64.b64encode(content).decode("utf-8")
    
    # Construct the GitHub API URL for the file
    url = f"https://api.github.com/repos/{repo}/contents/{db_file}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Get the current SHA of the file (if it exists) to update rather than create a new file
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            sha = response.json().get("sha")
        except Exception as e:
            st.error(f"Error parsing GitHub response: {e}")
            sha = None
    else:
        # If the file is not found, sha remains None
        sha = None

    # Prepare the commit data with a unique commit message using a timestamp
    commit_message = f"Update {db_file} at {int(time.time())}"
    data = {
        "message": commit_message,
        "content": encoded_content
    }
    if sha:
        data["sha"] = sha

    # Wait briefly to ensure that the file system has flushed all writes
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
    It decodes the base64 content returned by the GitHub API and writes it to the local file.
    """
    # Retrieve GitHub repository details from st.secrets
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

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            file_content = base64.b64decode(data["content"])
            with open(db_file, "wb") as f:
                f.write(file_content)
            st.info("Database pulled from GitHub successfully.")
        except Exception as e:
            st.error(f"Error processing GitHub response: {e}")
    else:
        st.error(f"Error pulling DB from GitHub: {response.json()}")
