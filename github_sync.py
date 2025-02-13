import sqlite3
import time
import streamlit as st
from github_sync import push_db_to_github  # Make sure this is the updated version without circular imports

def update_grade_and_push(db_path, username, new_grade):
    # Open connection and update the grade
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Log the current grade
    cursor.execute("SELECT as1 FROM records WHERE username = ?", (username,))
    before = cursor.fetchone()
    st.info(f"Grade before update for {username}: {before[0] if before else 'None'}")
    
    # Update the grade in the records table for this username
    cursor.execute("UPDATE records SET as1 = ? WHERE username = ?", (new_grade, username))
    conn.commit()
    st.info(f"Rows updated: {cursor.rowcount}")
    
    # Verify the update
    cursor.execute("SELECT as1 FROM records WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        st.info(f"Local grade for {username} after update: {result[0]}")
    else:
        st.error("Local update failed!")
        return
    
    # Wait briefly to ensure changes are flushed to disk
    time.sleep(2)
    
    # Push the updated database file to GitHub
    push_db_to_github(db_path)

# Example usage:
db_path = st.secrets["general"]["db_path"]  # e.g., "mydatabase.db"
username = st.session_state.get("username", "")  # This should be set from your login logic
new_grade = 98.0  # Change this value to something different if you want to test resubmission

if username:
    update_grade_and_push(db_path, username, new_grade)
else:
    st.error("Username not provided. Cannot update grade.")
