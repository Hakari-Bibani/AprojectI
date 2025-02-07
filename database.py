# database.py
import sqlite3
import streamlit as st
from github_sync import pull_db_from_github

def create_tables():
    """Create the required tables in the database if they don't exist."""
    db_path = st.secrets["general"]["db_path"]

    # 1) Pull the DB from GitHub to ensure the local copy is updated.
    pull_db_from_github(db_path)

    # 2) Connect to the database and create the 'users' table.
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            fullname TEXT,
            email TEXT,
            phone INTEGER,
            username TEXT UNIQUE,
            password TEXT,
            approved INTEGER DEFAULT 0,
            as1 REAL DEFAULT 0.0,
            as2 REAL DEFAULT 0.0,
            as3 REAL DEFAULT 0.0,
            as4 REAL DEFAULT 0.0,
            quiz1 REAL DEFAULT 0.0,
            quiz2 REAL DEFAULT 0.0,
            total REAL GENERATED ALWAYS AS (as1 + as2 + as3 + as4 + quiz1 + quiz2) STORED
        )
    """)

    conn.commit()
    conn.close()
