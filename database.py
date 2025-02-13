import sqlite3
import streamlit as st

def create_tables():
    db_path = st.secrets["general"]["db_path"]  # Ensure this is set to 'mydatabase.db' if that's what you're using.

    # Pull the DB from GitHub at runtime (if applicable)
    try:
        from github_sync import pull_db_from_github
        pull_db_from_github(db_path)
    except Exception as e:
        print(f"Error pulling DB from GitHub: {e}")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        fullname TEXT,
        email TEXT,
        phone INTEGER,
        username TEXT,
        password TEXT,
        approved INTEGER DEFAULT 0
    )
    ''')

    # Create the records table
    cursor.execute('''
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
    ''')

    # Create the tracks table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tracks (
        username TEXT,
        page TEXT
    )
    ''')

    # Create a trigger to insert into records table when a new user is added
    cursor.execute('''
    CREATE TRIGGER IF NOT EXISTS after_user_insert
    AFTER INSERT ON users
    FOR EACH ROW
    BEGIN
        INSERT INTO records (username, fullname) VALUES (NEW.username, NEW.fullname);
    END;
    ''')

    conn.commit()
    conn.close()
