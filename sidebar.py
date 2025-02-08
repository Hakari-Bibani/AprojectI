import streamlit as st

def show_sidebar():
    # Custom CSS for the sidebar styling
    st.markdown("""
        <style>
        /* Sidebar styling */
        .css-1d391kg {
            padding: 2rem 1rem;
        }
        
        /* (Unused animated title styling removed from display) */
        .sidebar-title {
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
            background-size: 200% 200%;
            color: white;
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
            margin-bottom: 2rem;
            animation: gradient 5s ease infinite;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        
        @keyframes gradient {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }
        
        /* Expander styling */
        .streamlit-expanderHeader {
            background-color: #f0f2f6;
            border-radius: 5px;
            margin-bottom: 0.5rem;
        }
        
        /* Button styling */
        .stButton button {
            background-color: transparent;
            border: 1px solid #4ECDC4;
            color: #4ECDC4;
            transition: all 0.3s ease;
        }
        
        .stButton button:hover {
            background-color: #4ECDC4;
            color: white;
            transform: translateY(-2px);
        }
        </style>
        """, unsafe_allow_html=True)

    with st.sidebar:
        # Display the logo above the sidebar (ensure "logo.jpg" is in the same directory or adjust the path)
        st.image("logo.jpg", use_column_width=True)
        
        # The animated title is removed.
        # st.markdown('<div class="sidebar-title">AI For Impact</div>', unsafe_allow_html=True)

        # Home section
        with st.expander("🏠 HOME", expanded=False):
            if st.button("Home Page", key="home", use_container_width=True):
                st.session_state["page"] = "home"

        # Modules section (moved to be directly after HOME)
        with st.expander("📘 MODULES", expanded=False):
            if st.button("Introduction", key="modules_intro", use_container_width=True):
                st.session_state["page"] = "modules_intro"
            if st.button("Week 1: Introduction to Coding", key="modules_week1", use_container_width=True):
                st.session_state["page"] = "modules_week1"
            if st.button("Week 2: Generate Comprehensive Codings", key="modules_week2", use_container_width=True):
                st.session_state["page"] = "modules_week2"
            if st.button("Week 3: Deploy App through Github and Streamlit", key="modules_week3", use_container_width=True):
                st.session_state["page"] = "modules_week3"
            if st.button("Week 4: Data Week", key="modules_week4", use_container_width=True):
                st.session_state["page"] = "modules_week4"
            if st.button("Week 5: Finalizing and Showcasing Your Personalized Project", key="modules_week5", use_container_width=True):
                st.session_state["page"] = "modules_week5"

        # Assignments section
        with st.expander("📚 ASSIGNMENTS", expanded=False):
            if st.button("Assignment 1", key="as1", use_container_width=True):
                st.session_state["page"] = "as1"
            if st.button("Assignment 2", key="as2", use_container_width=True):
                st.session_state["page"] = "as2"
            if st.button("Assignment 3", key="as3", use_container_width=True):
                st.session_state["page"] = "as3"
            if st.button("Assignment 4", key="as4", use_container_width=True):
                st.session_state["page"] = "as4"

        # Quizzes section
        with st.expander("📝 QUIZZES", expanded=False):
            if st.button("Quiz 1", key="quiz1", use_container_width=True):
                st.session_state["page"] = "quiz1"
            if st.button("Quiz 2", key="quiz2", use_container_width=True):
                st.session_state["page"] = "quiz2"

        # Help section
        with st.expander("❓ HELP", expanded=False):
            if st.button("Help Center", key="help", use_container_width=True):
                st.session_state["page"] = "help"

        # Logout section
        with st.expander("🚪 LOGOUT", expanded=False):
            if st.button("Logout", key="logout", use_container_width=True):
                st.session_state["page"] = "logout"

    # Return the current page
    return st.session_state.get("page", "home")
