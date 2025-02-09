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
    
    # For this example, ensure a username exists in session state.
    # In your application, you should set this when the user logs in.
    if "username" not in st.session_state:
        st.session_state["username"] = "testuser"  # Replace with your actual unique user value

    # Define the database path
    db_path = 'database.db'  # or use st.secrets["general"]["db_path"] if that's how you store it

    st.title("Assignment 1: Mapping Coordinates and Calculating Distances")

    # ─────────────────────────────────────────────────────────────────
    # STEP 2: REVIEW ASSIGNMENT DETAILS
    # ─────────────────────────────────────────────────────────────────
    st.markdown('<h1 style="color: #ADD8E6;">Step 2: Review Assignment Details</h1>', unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["Assignment Details", "Grading Details"])

    with tab1:
        st.markdown("""
            ### Objective
            In this assignment, you will write a Python script to plot three geographical coordinates on a map and calculate the distance between each pair of points in kilometers. This will help you practice working with geospatial data and Python libraries for mapping and calculations.
            
            **Assignment: Week 1 – Mapping Coordinates and Calculating Distances in Python**
            - **Plot the Three Coordinates on a Map:** The coordinates represent three locations in the Kurdistan Region.
            - **Calculate the Distance Between Each Pair of Points:** Specifically, calculate:
                - Point 1 to Point 2
                - Point 2 to Point 3
                - Point 1 to Point 3
            """)
        with st.expander("See More"):
            st.markdown("""
            **Task Requirements:**
            1. **Plot the Three Coordinates on a Map:**  
               Use Python libraries to plot the points and display their locations on an interactive map.
            2. **Calculate the Distance Between Each Pair of Points:**  
               Calculate the distances in kilometers using libraries like `geopy`.
            3. **Display a Summary:**  
               Show the calculated distances (formatted to two decimal places) and the map with markers, polylines, and popups.
            """)
    
    with tab2:
        st.markdown("""
            ### Detailed Grading Breakdown
            #### 1. Code Structure and Implementation (30 points)
            - **Library Imports:** (5 points)
            - **Coordinate Handling:** (5 points)
            - **Code Execution:** (10 points)
            - **Code Quality:** (10 points)
            """)
        with st.expander("See More"):
            st.markdown("""
            #### 2. Map Visualization (40 points)
            - **Map Generation:** (15 points)
            - **Markers:** (15 points)
            - **Polylines and Popups:** (10 points)
            
            #### 3. Distance Calculations (30 points)
            - **Geodesic Implementation:** (10 points)
            - **Distance Accuracy:** (20 points)
            """)

    # ─────────────────────────────────────────────────────────────────
    # STEP 3: RUN AND SUBMIT YOUR CODE
    # ─────────────────────────────────────────────────────────────────
    st.markdown('<h1 style="color: #ADD8E6;">Step 3: Run and Submit Your Code</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: white;">📝 Paste Your Code Here</p>', unsafe_allow_html=True)
    code_input = st.text_area("", height=300)  # User pastes their code here

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

    # Submit Code Button and Database Update
    submit_button = st.button("Submit Code", key="submit_code_button")
    if submit_button:
        if not st.session_state.get("run_success", False):
            st.error("Please run your code successfully before submitting.")
        else:
            # Grade the submission
            from grades.grade1 import grade_assignment
            grade = grade_assignment(code_input)

            # Connect to the database and update the as1 grade for the current user
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            # Update the as1 column for the user whose username matches
            cursor.execute("UPDATE users SET as1 = ? WHERE username = ?", (grade, st.session_state["username"]))
            conn.commit()
            conn.close()

            # Push the updated DB to GitHub
            push_db_to_github(db_path)

            st.success(f"Submission successful! Your grade: {grade}/100")

if __name__ == "__main__":
    show()
