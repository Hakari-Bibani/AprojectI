import sqlite3
import streamlit as st

def create_tables():
    db_path = st.secrets["general"]["db_path"]

    try:
        from github_sync import pull_db_from_github
        pull_db_from_github(db_path)
    except Exception as e:
        st.error(f"Error pulling DB from GitHub: {e}")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the users table (unchanged)
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

    # Create the records table with UNIQUE constraint
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS records (
        username TEXT UNIQUE,
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

    # Create the tracks table (unchanged)
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
        INSERT OR IGNORE INTO records (username, fullname) VALUES (NEW.username, NEW.fullname);
    END;
    ''')

    conn.commit()
    conn.close()
    # The following line has been removed:
    # st.info("Database created/updated successfully.")

if __name__ == "__main__":
    create_tables()
