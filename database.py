import sqlite3
import streamlit as st

def create_tables():
    """Create the required tables in the database if they don't exist."""
    db_path = st.secrets["general"]["db_path"]
    
    # Pull the DB from GitHub at runtime (wrapped in try/except to avoid app crash)
    try:
        from github_sync import pull_db_from_github
        pull_db_from_github(db_path)
    except Exception as e:
        print(f"Error pulling DB from GitHub: {e}")
    
    # Now proceed with table creation
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            fullname TEXT,
            email TEXT,
            phone INTEGER,
            username TEXT UNIQUE,
            password TEXT,
            approved INTEGER DEFAULT 0
        )
    """)
    
    # Create the records table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS records (
            username TEXT,
            fullname TEXT,
            as1 REAL DEFAULT 0,
            as2 REAL DEFAULT 0,
            as3 REAL DEFAULT 0,
            as4 REAL DEFAULT 0,
            quiz1 REAL DEFAULT 0,
            quiz2 REAL DEFAULT 0,
            total REAL GENERATED ALWAYS AS (as1 + as2 + as3 + as4 + quiz1 + quiz2) STORED
        )
    """)
    
    # Create the tracks table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tracks (
            username TEXT,
            page TEXT
        )
    """)

    conn.commit()
    conn.close()
