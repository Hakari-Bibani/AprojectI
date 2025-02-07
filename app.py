
import streamlit as st
from theme import apply_dark_theme
from database import create_tables
from login import show_login_create_account
from sidebar import show_sidebar
from home import show_home

def main():
    # Must be the FIRST Streamlit command
    st.set_page_config(page_title="Code for Impact", layout="wide")

    # Apply dark theme
    apply_dark_theme()
    
    # Ensure tables exist (and DB is pulled from GitHub if you're doing that in create_tables)
    create_tables()

    # Track login state
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if st.session_state["logged_in"]:
        # Use your sidebar to get the chosen page
        selected = show_sidebar()

        if selected == "logout":
            st.session_state["logged_in"] = False
            st.rerun()

        elif selected == "home":
            show_home()

        # ─────────────────────────────────────────────────────────────────
        # Handle Assignments
        # ─────────────────────────────────────────────────────────────────
        elif selected == "as1":
            import as1
            as1.show()

        elif selected == "as2":
            import as2
            as2.show()

        elif selected == "as3":
            import as3
            as3.show()

        elif selected == "as4":
            import as4
            as4.show()

        # ─────────────────────────────────────────────────────────────────
        # Handle Quizzes
        # ─────────────────────────────────────────────────────────────────
        elif selected == "quiz1":
            import quiz1
            quiz1.show()

        elif selected == "quiz2":
            import quiz2
            quiz2.show()

        # ─────────────────────────────────────────────────────────────────
        # Handle Help (if you have a help.py module)
        # ─────────────────────────────────────────────────────────────────
        elif selected == "help":
            import help
            help.show()

        # ─────────────────────────────────────────────────────────────────
        # Handle Modules
        # ─────────────────────────────────────────────────────────────────
        elif selected == "modules_intro":
            import modules_intro
            modules_intro.show()

        elif selected == "modules_week1":
            import modules_week1
            modules_week1.show()

        elif selected == "modules_week2":
            import modules_week2
            modules_week2.show()

        elif selected == "modules_week3":
            import modules_week3
            modules_week3.show()

        elif selected == "modules_week4":
            import modules_week4
            modules_week4.show()

        elif selected == "modules_week5":
            import modules_week5
            modules_week5.show()

        else:
            st.warning("Unknown selection.")

    else:
        # If not logged in, show login/create account pages
        show_login_create_account()

if __name__ == "__main__":
    main()

