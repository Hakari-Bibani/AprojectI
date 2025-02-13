import streamlit as st
import folium
import pandas as pd
from geopy.distance import geodesic
from io import StringIO
from streamlit_folium import st_folium
from utils.style1 import set_page_style
import sqlite3
from github_sync import push_db_to_github  # , pull_db_from_github  # Uncomment if needed

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

    # Define the database path from secrets (ensure this points to your updated database file)
    db_path = st.secrets["general"]["db_path"]

    st.title("Assignment 1: Mapping Coordinates and Calculating Distances")

    # ──────────────────────────────────────────────────────────────
    # Step 1: Enter Your Username
    # ──────────────────────────────────────────────────────────────
    st.markdown('<h1 style="color: #ADD8E6;">Step 1: Enter Your Username</h1>', unsafe_allow_html=True)
    username_input = st.text_input("Username", key="as1_username")
    enter_username = st.button("Enter")
    if enter_username and username_input:
        # Check in the records table (not the users table)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM records WHERE username = ?", (username_input,))
        user_record = cursor.fetchone()
        if user_record:
            st.session_state["username_entered"] = True
            st.session_state["username"] = username_input
        else:
            st.error("Invalid username. Please enter a registered username.")
            st.session_state["username_entered"] = False
        conn.close()

    if st.session_state.get("username_entered", False):
        # ──────────────────────────────────────────────────────────────
        # Step 2: Review Assignment Details
        # ──────────────────────────────────────────────────────────────
        st.markdown('<h1 style="color: #ADD8E6;">Step 2: Review Assignment Details</h1>', unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["Assignment Details", "Grading Details"])

        with tab1:
            st.markdown("""
            ### Objective
            In this assignment, you will write a Python script to plot three geographical coordinates on a map and calculate the distance between each pair of points in kilometers.
            """)
            with st.expander("See More"):
                st.markdown("""
            **Assignment:** Week 1 – Mapping Coordinates and Calculating Distances in Python

            **Task Requirements:**
            1. Plot three specific coordinates on an interactive map.
            2. Calculate and display the distances (in kilometers) between:
               - Point 1 and Point 2.
               - Point 2 and Point 3.
               - Point 1 and Point 3.

            **Coordinates:**
        - Point 1: Latitude: 36.325735, Longitude: 43.928414
        - Point 2: Latitude: 36.393432, Longitude: 44.586781
        - Point 3: Latitude: 36.660477, Longitude: 43.840174
        **Python Libraries You Will Use:**
        - `geopy` for calculating the distance between two coordinates.
        - `folium` for plotting the points on an interactive map.
        - `pandas` to create a DataFrame that displays the distances between the points.
        **Expected Output:**
        1. A map showing the three coordinates.
        2. A text summary (express values to two decimal places) showing the calculated distances (in kilometers) between:
           - Point 1 and Point 2.
           - Point 2 and Point 3.
           - Point 1 and Point 3.
        """)

        with tab2:
            st.markdown("""
            ### Detailed Grading Breakdown
            - **Code Structure and Implementation:** 30 points
            - **Map Visualization:** 40 points
            - **Distance Calculations:** 30 points
            """)
            with st.expander("See More"):
        st.markdown("""
        #### 2. Map Visualization (40 points)
        - **Map Generation (15 points):**
            - Checks if the `folium.Map` is correctly initialized.
        - **Markers (15 points):**
            - Checks if markers are added to the map for each coordinate.
        - **Polylines (5 points):**
            - Checks if polylines are used to connect the points.
        - **Popups (5 points):**
            - Checks if popups are added to the markers.
        #### 3. Distance Calculations (30 points)
        - **Geodesic Implementation (10 points):**
            - Checks if the `geodesic` function is used correctly to calculate distances.
        - **Distance Accuracy (20 points):**
            - Checks if the calculated distances are accurate within a 100-meter tolerance.
        """)

        # ──────────────────────────────────────────────────────────────
        # Step 3: Run and Submit Your Code
        # ──────────────────────────────────────────────────────────────
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
                st.markdown(f'<pre style="color: white; white-space: pre-wrap; word-wrap: break-word;">{formatted_output}</pre>', unsafe_allow_html=True)
            else:
                st.markdown('<p style="color: white;">No text output captured.</p>', unsafe_allow_html=True)

            if st.session_state["map_object"]:
                st.markdown("### 🗺️ Map Output")
                st_folium(st.session_state["map_object"], width=1000, height=500)

            if st.session_state["dataframe_object"] is not None:
                st.markdown("### 📊 DataFrame Output")
                st.dataframe(st.session_state["dataframe_object"])

        # ──────────────────────────────────────────────────────────────
        # Submit Code Button (updates grade and pushes DB)
        # ──────────────────────────────────────────────────────────────
        submit_button = st.button("Submit Code", key="submit_code_button")
        if submit_button:
            if not st.session_state.get("run_success", False):
                st.error("Please run your code successfully before submitting.")
            elif st.session_state.get("username", ""):
                # Grade the submission using your grading function
                from grades.grade1 import grade_assignment
                grade = grade_assignment(code_input)

                # Optionally, avoid pulling the DB from GitHub here if it might overwrite your changes.
                # pull_db_from_github(db_path)  # Uncomment only if necessary

                # Update the grade in the records table for this username
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute("UPDATE records SET as1 = ? WHERE username = ?", (grade, st.session_state["username"]))
                conn.commit()
                updated_rows = cursor.rowcount  # Check how many rows were updated
                conn.close()

                if updated_rows == 0:
                    st.error("No record updated. Please check the username or database integrity.")
                else:
                    st.info("Grade updated locally. Pushing changes to GitHub...")
                    push_db_to_github(db_path)

                    # Re-open connection to verify the updated grade
                    conn = sqlite3.connect(db_path)
                    cursor = conn.cursor()
                    cursor.execute("SELECT as1 FROM records WHERE username = ?", (st.session_state["username"],))
                    result = cursor.fetchone()
                    conn.close()

                    if result:
                        new_grade = result[0]
                        st.success(f"Submission successful! Your grade: {new_grade}/100")
                    else:
                        st.error("Error retrieving the updated grade.")
            else:
                st.error("Please enter your username to submit.")

if __name__ == "__main__":
    show()
