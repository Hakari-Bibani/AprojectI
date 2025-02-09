import streamlit as st
import pandas as pd

def show():
    # Create tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs([
        "Introduction to Python",
        "You made it!",
        "What is Python?",
        "Python Script?",
        "Libraries",
        "Google Colab",
        "Assignment 1",
        "APIs",
        "Assignment 2",
        "Real-Time",
        "Quiz"
    ])

    with tab1:
        st.header("1.1 Introduction to Python - Recorded Session")
        st.video("https://www.youtube.com/watch?v=Scem9sKTtJo")
        st.subheader("**ChatGPT Prompts**")
        st.markdown("[Links to an external site](https://chatgpt.com/share/6733c214-7ac4-8004-92f1-227d11b644ff)")
        st.subheader("**Content**:")
        st.write(
            "In this session, we’ll introduce you to the basics of Python and how it can be a powerful tool for enhancing personal impact, "
            "whether you're looking to automate tasks, analyze data, or create small projects. We will cover foundational topics such as "
            "setting up your Python environment, understanding Python syntax, and exploring the practical applications of Python in everyday scenarios."
        )
    
    with tab2:
        st.header("1.2 You made it! Be prepared for your final project")
        st.video("https://www.youtube.com/watch?v=fD73oMb4NRg")
    
    with tab3:
        st.header("1.3 What is Python? Why We Chose It for Learning")
        st.write(
            "Python is a powerful, high-level programming language known for its readability and versatility. Used in everything from web "
            "development to scientific research, Python's syntax is clean and intuitive, making it a preferred language for both beginners and experts."
        )
    
    with tab4:
        st.header("1.4 What is in the Python Script?")
        st.write("A Python script is a set of instructions written in the Python programming language...")
    
    with tab5:
        st.header("1.5 Introduction to Python Libraries")
        st.write("Python libraries extend the functionality of the language, making it easier to perform complex tasks with simple commands.")
    
    with tab6:
        st.header("1.6 Top 10 Things to Know in Google Colab as a Beginner")
        st.write("Google Colab is a beginner-friendly, free platform that allows you to write and run Python code in the cloud.")
    
    with tab7:
        st.header("Assignment: Week 1 – Mapping Coordinates and Calculating Distances in Python")
        st.markdown('<p style="color: red; font-size: 20px;">📝 Select Assignment 1 from the sidebar in the Assignments section.</p>', unsafe_allow_html=True)
    
    with tab8:
        st.header("1.8 Understanding APIs: The Key to Real-Time Data Integration")
        st.write("An API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate...")
    
    with tab9:
        st.header("Assignment: Week 1 – Analyzing Real-Time Earthquake Data")
        st.markdown('<p style="color: red; font-size: 20px;">📝 Select Assignment 2 from the sidebar in the Assignments section.</p>', unsafe_allow_html=True)
    
    with tab10:
        st.header("1.10 Real-Time Applications of Google Colab")
        st.write("Google Colab is a powerful cloud-based platform that enables researchers, students, and professionals to execute Python code directly in their browsers...")
    
    with tab11:
        st.header("Quiz: Week 1")
        st.markdown('<p style="color: red; font-size: 20px;">📝 Select Quiz 1 from the sidebar in the Quizzes section.</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    show()
