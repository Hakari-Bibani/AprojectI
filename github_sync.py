import sqlite3
import time
import streamlit as st
from github_sync import push_db_to_github

def update_grade_and_push(db_path, username, new_grade):
    """
    Update the grade in the records table and push the updated DB file to GitHub.
    """
    # Open a connection to the local database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Verify that the record exists by checking the current grade
    cursor.execute("SELECT as1 FROM records WHERE username = ?", (username,))
    row = cursor.fetchone()
    if row is None:
        st.error(f"No record found for username '{username}'.")
        conn.close()
        return

    # Update the grade in the records table
    cursor.execute("UPDATE records SET as1 = ? WHERE username = ?", (new_grade, username))
    conn.commit()

    # Verify the update
    cursor.execute("SELECT as1 FROM records WHERE username = ?", (username,))
    updated = cursor.fetchone()
    conn.close()

    if updated:
        st.info(f"Local grade for {username} after update: {updated[0]}")
    else:
        st.error("Local update failed!")
        return

    # Wait briefly to ensure changes are flushed to disk
    time.sleep(1)

    # Push the updated database file to GitHub
    push_db_to_github(db_path)

# Example usage (for instance, in your submission handler):
db_path = st.secrets["general"]["db_path"]  # e.g., "mydatabase.db"
username = st.session_state.get("username", "").strip()  # ensure no extra spaces
new_grade = 98.0  # Replace with your calculated grade

if username:
    update_grade_and_push(db_path, username, new_grade)
else:
    st.error("Username not provided. Cannot update grade.")
