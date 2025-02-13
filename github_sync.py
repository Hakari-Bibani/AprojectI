import requests
import base64
import streamlit as st
import time

def push_db_to_github(db_file: str):
    try:
        repo = st.secrets["general"]["repo"]
        token = st.secrets["general"]["token"]
    except Exception as e:
        st.error(f"Secrets not found or misconfigured: {e}")
        return

    try:
        with open(db_file, "rb") as f:
            content = f.read()
    except Exception as e:
        st.error(f"Error reading {db_file}: {e}")
        return

    encoded_content = base64.b64encode(content).decode("utf-8")
    
    # GitHub API URL for the file (ensure the path is correct)
    url = f"https://api.github.com/repos/{repo}/contents/{db_file}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Get the current SHA of the file (if it exists)
    get_response = requests.get(url, headers=headers)
    if get_response.status_code == 200:
        try:
            sha = get_response.json()["sha"]
        except Exception as e:
            st.error(f"Error parsing GitHub response: {e}")
            sha = None
    else:
        sha = None

    commit_message = f"Update {db_file} at {int(time.time())}"
    data = {
        "message": commit_message,
        "content": encoded_content
    }
    if sha:
        data["sha"] = sha

    put_response = requests.put(url, json=data, headers=headers)
    if put_response.status_code in [200, 201]:
        st.success("Database pushed to GitHub successfully.")
        st.write("GitHub response:", put_response.json())
    else:
        st.error("Error pushing DB to GitHub:")
        st.error(put_response.json())
