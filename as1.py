import streamlit as st
import folium
import pandas as pd
from geopy.distance import geodesic
from io import StringIO
from streamlit_folium import st_folium
from utils.style1 import set_page_style
import sqlite3
from github_sync import push_db_to_github

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

    # Define db_path globally
    db_path = st.secrets["general"]["db_path"]

    st.title("Assignment 1: Mapping Coordinates and Calculating Distances")

    # ─────────────────────────────────────────────────────────────────
    # STEP 1: REVIEW ASSIGNMENT DETAILS
    # ─────────────────────────────────────────────────────────────────
    st.markdown('<h1 style="color: #ADD8E6;">Step 1: Review Assignment Details</h1>', unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["Assignment Details", "Grading Details"])

    with tab1:
        st.markdown("""
        ### Objective
        In this assignment, you will write a Python script to plot three geographical coordinates on a map and calculate the distance between each pair of points in kilometers. This will help you practice working with geospatial data and Python libraries for mapping and calculations.

        ### Assignment: Week 1 – Mapping Coordinates and Calculating Distances in Python
        **Objective:**
        In this assignment, you will write a Python script to plot three geographical coordinates on a map and calculate the distance between each pair of points in kilometers. This will help you practice working with geospatial data and Python libraries for mapping and calculations.
        """)
        with st.expander("See More"):
            st.markdown("""
        **Task Requirements:**
        1. **Plot the Three Coordinates on a Map:**
           - The coordinates represent three locations in the Kurdistan Region.
           - You will use Python libraries to plot these points on a map.
           - The map should visually display the exact locations of the coordinates.
        2. **Calculate the Distance Between Each Pair of Points:**
           - You will calculate the distances between the three points in kilometers.
           - Specifically, calculate:
             - The distance between Point 1 and Point 2.
             - The distance between Point 2 and Point 3.
             - The distance between Point 1 and Point 3.
           - Add Markers to the map for each coordinate.
           - Add polylines to connect the points.
           - Add popups to display information about the distance.

        **Coordinates:**
        - Point 1: Latitude: 36.325735, Longitude: 43.928414
        - Point 2: Latitude: 36.393432, Longitude: 44.586781
        - Point 3: Latitude: 36.660477, Longitude: 43.840174

        **Python Libraries You Will Use:**
        - geopy for calculating the distance between two coordinates.
        - folium for plotting the points on an interactive map.
        - pandas to create a DataFrame that displays the distances between the points.

        **Expected Output:**
        1. A map showing the three coordinates.
        2. A text summary (Express values to two decimal places.): showing the calculated distances (in kilometers) between:
           - Point 1 and Point 2.
           - Point 2 and Point 3.
           - Point 1 and Point 3.
        """)

    with tab2:
        st.markdown("""
        ### Detailed Grading Breakdown
        #### 1. Code Structure and Implementation (30 points)
        - **Library Imports (5 points):**
            - Checks if the required libraries (folium, geopy, geodesic) are imported.
        - **Coordinate Handling (5 points):**
            - Checks if the correct coordinates are defined in the code.
        - **Code Execution (10 points):**
            - Checks if the code runs without errors.
        - **Code Quality (10 points):**
            - **Variable Naming:** 2 points (deducted if single-letter variables are used).
            - **Spacing:** 2 points (deducted if improper spacing is found, e.g., no space after =).
            - **Comments:** 2 points (deducted if no comments are present).
            - **Code Organization:** 2 points (deducted if no blank lines are used for separation).
        """)
        with st.expander("See More"):
            st.markdown("""
        #### 2. Map Visualization (40 points)
        - **Map Generation (15 points):**
            - Checks if the folium.Map is correctly initialized.
        - **Markers (15 points):**
            - Checks if markers are added to the map for each coordinate.
        - **Polylines (5 points):**
            - Checks if polylines are used to connect the points.
        - **Popups (5 points):**
            - Checks if popups are added to the markers.

        #### 3. Distance Calculations (30 points)
        - **Geodesic Implementation (10 points):**
            - Checks if the geodesic function is used correctly to calculate distances.
        - **Distance Accuracy (20 points):**
            - Checks if the calculated distances are accurate within a 100-meter tolerance.
        """)

    # ─────────────────────────────────────────────────────────────────
    # STEP 2: RUN AND SUBMIT YOUR CODE
    # ─────────────────────────────────────────────────────────────────
    st.markdown('<h1 style="color: #ADD8E6;">Step 2: Run and Submit Your Code</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: white;">📝 Paste Your Code Here</p>', unsafe_allow_html=True)
    code_input = st.text_area("", height=300)  # Removed label since we're using custom markdown above

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

    # Display Outputs
    if st.session_state["run_success"]:
        st.markdown('<h3 style="color: white;">📄 Captured Output</h3>', unsafe_allow_html=True)
        if st.session_state["captured_output"]:
            # Format the output with preserved whitespace and line breaks
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

    # Submit Code Button
    submit_button = st.button("Submit Code", key="submit_code_button")
    if submit_button:
        if not st.session_state.get("run_success", False):
            st.error("Please run your code successfully before submitting.")
        else:
            # Grade the submission
            from grades.grade1 import grade_assignment
            grade = grade_assignment(code_input)

            # Update the grade in the users table for the current user
            username = st.session_state.get("username")  # Retrieve username from session state
            if username:
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()

                # Update the as1 grade for the user
                cursor.execute("UPDATE users SET as1 = ? WHERE username = ?", (grade, username))
                conn.commit()
                conn.close()

                # Push the updated DB to GitHub
                push_db_to_github(db_path)

                st.success(f"Submission successful! Your grade: {grade}/100")
            else:
                st.error("Username not found. Please log in again.")
