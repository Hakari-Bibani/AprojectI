import streamlit as st
import folium
import pandas as pd
from geopy.distance import geodesic
from io import StringIO
from streamlit_folium import st_folium
from utils.style1 import set_page_style
import sqlite3
from github_sync import push_db_to_github, pull_db_from_github

def show():
    # Apply the custom page style
    set_page_style()

    # Initialize session state variables
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

    # Define db_path globally
    db_path = st.secrets["general"]["db_path"]

    st.title("Assignment 1: Mapping Coordinates and Calculating Distances")

    # ─────────────────────────────────────────────────────────────────
    # STEP 1: ENTER YOUR USERNAME
    # (Password verification removed – only username existence is checked)
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
            In this assignment, you will write a Python script to plot three geographical coordinates on a map and calculate the distance between each pair of points in kilometers. This will help you practice working with geospatial data and Python libraries for mapping and calculations.

            ### Assignment: Week 1 – Mapping Coordinates and Calculating Distances in Python
            **Objective:**
            Write a script that:
            - Plots three specific coordinates on an interactive map.
            - Calculates and displays the distances (in kilometers) between each pair of points.
            """)
            with st.expander("See More"):
                st.markdown("""
            **Task Requirements:**
            1. **Plot the Three Coordinates on a Map:**
               - Use Python libraries to plot three locations in the Kurdistan Region.
               - The map must show markers for each coordinate.
            2. **Calculate the Distances:**
               - Compute the distances (in kilometers) between:
                 - Point 1 and Point 2.
                 - Point 2 and Point 3.
                 - Point 1 and Point 3.
               - Display these distances in a text summary.
            
            **Coordinates:**
            - Point 1: Latitude: 36.325735, Longitude: 43.928414
            - Point 2: Latitude: 36.393432, Longitude: 44.586781
            - Point 3: Latitude: 36.660477, Longitude: 43.840174

            **Libraries to Use:**
            - geopy (for distance calculations),
            - folium (for the interactive map),
            - pandas (for the summary DataFrame).
                """)

        with tab2:
            st.markdown("""
            ### Detailed Grading Breakdown
            #### 1. Code Structure and Implementation (30 points)
            - Library imports, coordinate definitions, execution without errors, and code quality.
            
            #### 2. Map Visualization (40 points)
            - Proper initialization of folium.Map, markers, polylines, and popups.
            
            #### 3. Distance Calculations (30 points)
            - Accurate use of geopy.distance.geodesic and correctness within a 100-meter tolerance.
            """)
            with st.expander("See More"):
                st.markdown("Additional grading details...")

        # ─────────────────────────────────────────────────────────────────
        # STEP 3: RUN AND SUBMIT YOUR CODE
        # ─────────────────────────────────────────────────────────────────
        st.markdown('<h1 style="color: #ADD8E6;">Step 3: Run and Submit Your Code</h1>', unsafe_allow_html=True)
        st.markdown('<p style="color: white;">📝 Paste Your Code Here</p>', unsafe_allow_html=True)
        code_input = st.text_area("", height=300)

        # Run Code Button
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

                # Capture printed output
                st.session_state["captured_output"] = captured_output.getvalue()

                # Look for specific outputs (folium.Map, pandas.DataFrame)
                map_object = next((obj for obj in local_context.values() if isinstance(obj, folium.Map)), None)
                dataframe_object = next((obj for obj in local_context.values() if isinstance(obj, pd.DataFrame)), None)

                # Store outputs in session state
                st.session_state["map_object"] = map_object
                st.session_state["dataframe_object"] = dataframe_object

                # Mark the run as successful
                st.session_state["run_success"] = True

            except Exception as e:
                sys.stdout = sys.__stdout__
                st.error(f"An error occurred while running your code: {e}")

        # Display Outputs if code ran successfully
        if st.session_state["run_success"]:
            st.markdown('<h3 style="color: white;">📄 Captured Output</h3>', unsafe_allow_html=True)
            if st.session_state["captured_output"]:
                formatted_output = st.session_state["captured_output"].replace('\n', '<br>')
                st.markdown(f'<pre style="color: white; white-space: pre-wrap; word-wrap: break-word;">{formatted_output}</pre>', unsafe_allow_html=True)
            else:
                st.markdown('<p style="color: white;">No text output captured.</p>', unsafe_allow_html=True)

            if st.session_state["map_object"]:
                st.markdown("### 🗺️ Map Output")
                st_folium(st.session_state["map_object"], width=1000, height=500)

            if st.session_state["dataframe_object"] is not None:
                st.markdown("### 📊 DataFrame Output")
                st.dataframe(st.session_state["dataframe_object"])

        # ─────────────────────────────────────────────────────────────────
        # SUBMIT CODE BUTTON (each submission overwrites the previous grade)
        # ─────────────────────────────────────────────────────────────────
        submit_button = st.button("Submit Code", key="submit_code_button")
        if submit_button:
            if not st.session_state.get("run_success", False):
                st.error("Please run your code successfully before submitting.")
            elif st.session_state.get("username", ""):
                # Grade the submission
                from grades.grade1 import grade_assignment
                grade = grade_assignment(code_input)

                # Pull the latest DB from GitHub before updating
                pull_db_from_github(db_path)
                
                # Update the grade in the users table for this username (resubmission allowed)
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute("UPDATE users SET as1 = ? WHERE username = ?", (grade, st.session_state["username"]))
                conn.commit()
                conn.close()

                st.info("Grade updated locally. Pushing changes to GitHub...")

                # Push the updated DB to GitHub
                push_db_to_github(db_path)

                # Re-open connection to re-query the updated grade
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute("SELECT as1 FROM users WHERE username = ?", (st.session_state["username"],))
                new_grade = cursor.fetchone()[0]
                conn.close()

                st.success(f"Submission successful! Your grade: {new_grade}/100")
            else:
                st.error("Please enter your username to submit.")
