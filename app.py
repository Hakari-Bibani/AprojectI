import streamlit as st
import sqlite3

# --- Database Helper Functions ---
def get_db_connection():
    # Connect to the same SQLite database created by database.py
    return sqlite3.connect('mydatabase.db')

def insert_user(fullname, email, phone, username, password, approved, as1, as2, as3, as4, quiz1, quiz2):
    conn = get_db_connection()
    cursor = conn.cursor()
    insert_query = '''
    INSERT INTO users (fullname, email, phone, username, password, approved, as1, as2, as3, as4, quiz1, quiz2)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(insert_query, (fullname, email, phone, username, password, approved, as1, as2, as3, as4, quiz1, quiz2))
    conn.commit()
    conn.close()

def fetch_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

# --- Module to Handle Assignments and Quizzes ---
def handle_modules():
    st.header("Handle Modules")
    st.write("Enter and calculate assignment and quiz scores separately.")

    # Input fields for assignments
    as1 = st.number_input("Assignment 1 Score", min_value=0.0, step=0.1, key="as1_module")
    as2 = st.number_input("Assignment 2 Score", min_value=0.0, step=0.1, key="as2_module")
    as3 = st.number_input("Assignment 3 Score", min_value=0.0, step=0.1, key="as3_module")
    as4 = st.number_input("Assignment 4 Score", min_value=0.0, step=0.1, key="as4_module")
    
    # Input fields for quizzes
    quiz1 = st.number_input("Quiz 1 Score", min_value=0.0, step=0.1, key="quiz1_module")
    quiz2 = st.number_input("Quiz 2 Score", min_value=0.0, step=0.1, key="quiz2_module")
    
    if st.button("Calculate Total"):
        total = as1 + as2 + as3 + as4 + quiz1 + quiz2
        st.success(f"Total Score: {total}")

    st.info("Use these scores later when adding a user or updating records.")

# --- Main App ---
def main():
    st.title("Streamlit Web App with Modular Assignment/Quiz Handling")
    
    # Sidebar Menu for Navigation
    menu = st.sidebar.selectbox("Menu", ["Home", "Handle Modules", "View Users"])
    
    if menu == "Home":
        st.header("Home - Enter User Information")
        # User information fields
        fullname = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        approved = st.checkbox("Approved")

        # If you want, you can include assignment and quiz fields here too;
        # however, they can also be handled solely in the Handle Modules section.
        st.subheader("Enter Scores (if not using Handle Modules)")
        as1 = st.number_input("Assignment 1 Score", min_value=0.0, step=0.1, key="as1_home")
        as2 = st.number_input("Assignment 2 Score", min_value=0.0, step=0.1, key="as2_home")
        as3 = st.number_input("Assignment 3 Score", min_value=0.0, step=0.1, key="as3_home")
        as4 = st.number_input("Assignment 4 Score", min_value=0.0, step=0.1, key="as4_home")
        quiz1 = st.number_input("Quiz 1 Score", min_value=0.0, step=0.1, key="quiz1_home")
        quiz2 = st.number_input("Quiz 2 Score", min_value=0.0, step=0.1, key="quiz2_home")

        if st.button("Submit User Data"):
            # Convert the approved checkbox to an integer (1 if True, 0 if False)
            insert_user(fullname, email, phone, username, password, int(approved), as1, as2, as3, as4, quiz1, quiz2)
            st.success("User data inserted successfully!")

    elif menu == "Handle Modules":
        handle_modules()
        
    elif menu == "View Users":
        st.header("View User Records")
        users = fetch_users()
        st.write(users)

if __name__ == "__main__":
    main()
