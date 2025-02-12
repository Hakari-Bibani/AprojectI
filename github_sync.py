import requests
import base64
import streamlit as st

def push_db_to_github(db_file: str):
    """
    Pushes the local SQLite DB file to GitHub.
    Overwrites the existing file if it exists.
    """
    repo = st.secrets["general"]["repo"]
    token = st.secrets["general"]["token"]

    try:
        with open(db_file, "rb") as f:
            content = f.read()
    except Exception as e:
        st.error(f"Error reading {db_file}: {e}")
        return

    encoded_content = base64.b64encode(content).decode("utf-8")
    url = f"https://api.github.com/repos/{repo}/contents/{db_file}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Attempt to get the current file's SHA (if it exists)
    get_response = requests.get(url, headers=headers)
    if get_response.status_code == 200:
        try:
            sha = get_response.json()["sha"]
        except KeyError:
            st.error("Could not retrieve file SHA from GitHub response.")
            return
    else:
        sha = None

    # Prepare the data payload for the PUT request
    data = {
        "message": "Update mydatabase.db",
        "content": encoded_content
    }
    if sha:
        data["sha"] = sha

    put_response = requests.put(url, json=data, headers=headers)
    if put_response.status_code in [200, 201]:
        st.info("Database pushed to GitHub successfully.")
    else:
        # Show the full error details from GitHub
        error_details = put_response.json()
        st.error(f"Error pushing DB to GitHub: {error_details}")
