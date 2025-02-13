import sqlite3
import time
import streamlit as st
from github_sync import push_db_to_github

def update_grade_and_push(db_path, username, new_grade):
    # Open connection and update the grade
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE records SET as1 = ? WHERE username = ?", (new_grade, username))
    conn.commit()
    updated_rows = cursor.rowcount
    st.info(f"Updated {updated_rows} row(s) for user {username}.")
    
    # Immediately verify the update
    cursor.execute("SELECT as1 FROM records WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result:
        st.info(f"Local grade for {username}: {result[0]}")
    else:
        st.error("Local update failed!")
    
    # Wait briefly to ensure all changes are flushed to disk
    time.sleep(2)
    
    # Push the updated database file to GitHub
    push_db_to_github(db_path)

# Example usage:
db_path = st.secrets["general"]["db_path"]  # should be "mydatabase.db"
username = st.session_state.get("username", "")  # Make sure this is set from your login logic
new_grade = 98.0  # For example, the new grade calculated from grade_assignment()

if username:
    update_grade_and_push(db_path, username, new_grade)
else:
    st.error("Username not provided. Cannot update grade.")
