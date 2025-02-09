''' theme.py - Manages black theme for the entire app, 
    but with tabs and outlines styled as in the first (dark theme) script '''
import streamlit as st

def apply_dark_theme():
    st.markdown(
        '''
        <style>
        /* Global background and text color */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"],
        .block-container, .stApp {
            background-color: #000000 !important;
            color: #ffffff !important;
        }
        
        /* Set input labels to orange and bold */
        .stTextInput > label, .stSelectbox > label, .stButton > button {
            color: #FFA500 !important;  /* Orange */
            font-weight: bold;
        }
        
        /* Text Input Box and Button Styling 
           -- using dark gray background and green outline from the first script */
        .stTextInput, .stSelectbox, .stButton > button {
            background-color: #1e1e1e !important;  /* Dark gray */
            color: white !important;
            border-radius: 8px !important;
            border: 1px solid #32CD32 !important;  /* Green border */
            padding: 10px;
            box-shadow: 0px 0px 5px rgba(50, 205, 50, 0.5); /* Green glow */
        }
        
        /* Hover effect on buttons */
        .stButton > button:hover {
            background-color: #32CD32 !important;
            color: black !important;
            transition: 0.3s ease-in-out;
        }
        
        /* Styling for login and create account tabs 
           -- reverting to first script’s look */
        /* (Removed display:flex/justify-content to keep original placement) */
        div[data-testid="stTabs"] button {
            border-radius: 50px !important;  /* Rounded tabs */
            padding: 10px 20px !important;
            font-weight: bold !important;
            color: white !important;
            background-color: #1e1e1e !important;
            border: 2px solid #32CD32 !important;
        }
        div[data-testid="stTabs"] button[aria-selected="true"] {
            background-color: #32CD32 !important;
            color: black !important;
        }
        
        /* Custom Error Message Styling - Set to Red */
        .error-text {
            color: #FF0000 !important;
            font-weight: bold !important;
            font-size: 16px !important;
            padding: 5px;
        }
        
        /* Sidebar Styling */
        [data-testid="stSidebar"], .sidebar-content {
            background-color: #000000 !important;
            color: #ffffff !important;
            border-right: 1px solid #808080 !important;
        }
        [data-testid="stSidebar"] div {
            color: white !important;
        }
        
        /* Sidebar menu item styling */
        .css-1d391kg, .css-18e3th9 {
            color: white !important;
        }
        
        /* Sidebar menu hover effect */
        .css-1d391kg:hover, .css-18e3th9:hover {
            background-color: #d3d3d3 !important;
            color: black !important;
            border-radius: 8px;
            transition: 0.3s ease-in-out;
        }
        
        /* Scrollbar Customization */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #000000;
        }
        ::-webkit-scrollbar-thumb {
            background-color: #808080;
            border-radius: 10px;
        }
        </style>
        ''',
        unsafe_allow_html=True
    )
