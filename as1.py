# as1.py
import streamlit as st
import folium
import pandas as pd
from geopy.distance import geodesic
from io import StringIO
from streamlit_folium import st_folium
from utils.style1 import set_page_style
import sqlite3
import time
from github_sync import push_db_to_github, pull_db_from_github

def show():
    # Apply the custom page style
    set_page_style()

    # Initialize session state variables if not already set
    if "run_success" not in st.session_state:
        st.session_state["run_success"] = False
    if "map_object" not in st.session_state:
        st.session_state["map_object"] = None
    if "dataframe_object" not in st.session_state:
        st.session_state["dataframe_object"] = None
    if "captured_output" not in st.session_state:
        st.session_state["captured_output"] = ""
    if "username_entered" not in st.session_state:
        st.session_state["username_entered"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = ""
    # We'll store the code input for grading if needed.
    if "code_input" not in st.session_state:
        st.session_state["code_input"] = ""

    # Define the database path
    db_path = st.secrets["general"]["db_path"]
    # Pull the database only once per session
    if "db_loaded" not in st.session_state:
        pull_db_from_github(db_path)
        st.session_state["db_loaded"] = True

    st.title("Assignment 1: Mapping Coordinates and Calculating Distances")

    # ─────────────────────────────────────────────────────────────────
    # STEP 1: ENTER YOUR USERNAME (no password required)
    # ─────────────────────────────────────────────────────────────────
    st.markdown('<h1 style="color: #ADD8E6;">Step 1: Enter Your Username</h1>', unsafe_allow_html=True)
    username_input = st.text_input("Username", key="as1_username")
    enter_username = st.button("Enter")
    if enter_username and username_input:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username_input,))
        user_record = cursor.fetchone()
        if user_record:
            st.session_state["username_entered"] = True
            st.session_state["username"] = username_input
        else:
            st.error("Invalid username. Please enter a registered username.")
            st.session_state["username_entered"] = False
        conn.close()

    if st.session_state.get("username_entered", False):
        # ─────────────────────────────────────────────────────────────────
        # STEP 2: REVIEW ASSIGNMENT DETAILS
        # ─────────────────────────────────────────────────────────────────
        st.markdown('<h1 style="color: #ADD8E6;">Step 2: Review Assignment Details</h1>', unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["Assignment Details", "Grading Details"])

        with tab1:
            st.markdown("""
            ### Objective
            In this assignment, you will write a Python script to plot three geographical coordinates on a map and calculate the distance between each pair of points in kilometers.
            
            **Assignment: Week 1 – Mapping Coordinates and Calculating Distances in Python**
            - Plot three coordinates on an interactive map.
            - Calculate and display the distances (in kilometers) between each pair.
            """)
            with st.expander("See More"):
                st.markdown("""
            **Task Requirements:**
            1. **Map the Three Coordinates:** Use libraries such as `folium` to display markers for each coordinate.
            2. **Distance Calculations:** Use `geopy.distance.geodesic` to compute the distances between:
               - Point 1 and Point 2.
               - Point 2 and Point 3.
               - Point 1 and Point 3.
            
            **Coordinates:**
            - Point 1: 36.325735, 43.928414  
            - Point 2: 36.393432, 44.586781  
            - Point 3: 36.660477, 43.840174
                """)

        with tab2:
            st.markdown("""
            ### Detailed Grading Breakdown
            - **Code Structure and Implementation (30 points)**
            - **Map Visualization (40 points)**
            - **Distance Calculations (30 points)
            """)
            with st.expander("See More"):
                st.markdown("Additional grading details...")

        # ─────────────────────────────────────────────────────────────────
        # STEP 3: RUN AND SUBMIT YOUR CODE
        # ─────────────────────────────────────────────────────────────────
        st.markdown('<h1 style="color: #ADD8E6;">Step 3: Run and Submit Your Code</h1>', unsafe_allow_html=True)
        st.markdown('<p style="color: white;">📝 Paste Your Code Here</p>', unsafe_allow_html=True)
        code_input = st.text_area("", height=300)
        # Save code input to session state for grading later
        st.session_state["code_input"] = code_input

        run_button = st.button("Run Code", key="run_code_button")
        if run_button and code_input:
            st.session_state["run_success"] = False
            st.session_state["captured_output"] = ""
            try:
                from io import StringIO
                import sys

                captured_output = StringIO()
                sys.stdout = captured_output

                # Execute the user's code in a controlled environment
                local_context = {}
                exec(code_input, {}, local_context)

                # Restore stdout
                sys.stdout = sys.__stdout__

                st.session_state["captured_output"] = captured_output.getvalue()

                # Look for outputs (folium.Map, pandas.DataFrame)
                map_object = next((obj for obj in local_context.values() if isinstance(obj, folium.Map)), None)
                dataframe_object = next((obj for obj in local_context.values() if isinstance(obj, pd.DataFrame)), None)

                st.session_state["map_object"] = map_object
                st.session_state["dataframe_object"] = dataframe_object

                st.session_state["run_success"] = True

            except Exception as e:
                sys.stdout = sys.__stdout__
                st.error(f"An error occurred while running your code: {e}")

        if st.session_state["run_success"]:
            st.markdown('<h3 style="color: white;">📄 Captured Output</h3>', unsafe_allow_html=True)
            if st.session_state["captured_output"]:
                formatted_output = st.session_state["captured_output"].replace('\n', '<br>')
                st.markdown(f'<pre style="color: white; white-space: pre-wrap;">{formatted_output}</pre>', unsafe_allow_html=True)
            else:
                st.markdown('<p style="color: white;">No text output captured.</p>', unsafe_allow_html=True)

            if st.session_state["map_object"]:
                st.markdown("### 🗺️ Map Output")
                st_folium(st.session_state["map_object"], width=1000, height=500)

            if st.session_state["dataframe_object"] is not None:
                st.markdown("### 📊 DataFrame Output")
                st.dataframe(st.session_state["dataframe_object"])

        # ─────────────────────────────────────────────────────────────────
        # SUBMIT CODE BUTTON (users can resubmit anytime; new grade is saved under as1 on GitHub)
        # ─────────────────────────────────────────────────────────────────
        submit_button = st.button("Submit Code", key="submit_code_button")
        if submit_button:
            if not st.session_state.get("run_success", False):
                st.error("Please run your code successfully before submitting.")
            elif st.session_state.get("username", ""):
                # Grade the submission
                from grades.grade1 import grade_assignment
                grade = grade_assignment(code_input)

                # Update the grade in the local database for this username
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute("UPDATE users SET as1 = ? WHERE username = ?", (grade, st.session_state["username"]))
                conn.commit()
                conn.close()

                st.info("Grade updated locally. Preparing to push changes to GitHub...")
                time.sleep(1)  # Ensure all writes are flushed to disk

                # (Optional Debug) Verify the updated grade from the local file
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute("SELECT as1 FROM users WHERE username = ?", (st.session_state["username"],))
                current_grade = cursor.fetchone()[0]
                conn.close()
                st.write("Local grade now is:", current_grade)

                # Push the updated database file to GitHub
                push_db_to_github(db_path)

                st.success(f"Submission successful! Your grade: {current_grade}/100")
                # Reset our flag so that a future full reload pulls the updated file
                st.session_state["db_loaded"] = False
            else:
                st.error("Please enter your username to submit.")
