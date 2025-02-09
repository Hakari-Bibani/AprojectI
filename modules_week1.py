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
        st.markdown("* **Ease of Learning**: Python's syntax closely resembles human language, making it straightforward to pick up even if you're new to coding.")
        st.markdown("* **Wide Application**: Python powers a range of projects – from data analysis and machine learning to web apps and automation.")
        st.markdown("* **Strong Community Support**: With a large and active community, Python offers extensive resources, libraries, and frameworks for almost every purpose, so you’re never alone when troubleshooting or exploring new concepts.")
        st.markdown("* **Career Relevance**: Python is one of the most in-demand skills in tech, highly sought after in roles related to data science, AI, web development, and more.")
        st.subheader("**Python’s Applications Across Various Fields**")
        st.write("1. **Geosciences**")
        st.write("*Example:* Geoscientists use Python for **earthquake analysis, climate modeling, and geological surveys**. Tools like **GeoPandas** and **GDAL** help analyze spatial data and visualize geological information, while APIs like the **USGS Earthquake API** allow researchers to retrieve real-time earthquake data for analysis and predictions.")
        st.write("2. **Medical and Health Sciences**")
        st.write("*Example:* Python is applied in **medical image analysis**, patient data management, and drug discovery. Libraries like **SimpleITK** and **OpenCV** aid in analyzing X-rays, MRIs, and other medical images, supporting radiologists in diagnosing conditions faster and with greater accuracy.")
        st.write("3. **Finance**")
        st.write("*Example:* Financial analysts leverage Python for **algorithmic trading, risk assessment, and fraud detection**. Libraries like **Pandas** and **NumPy** are essential for managing large financial datasets, while **Scikit-Learn** supports predictive modeling for stock prices, making Python a valuable tool for strategic financial decisions.")
        st.write("4. **Education**")
        st.write("*Example:* In education, Python facilitates **student performance analysis, automation of grading**, and the creation of interactive learning apps. **Jupyter Notebooks** are commonly used by educators to deliver lessons and by students to practice hands-on coding.")
        st.write("5. **Engineering and Manufacturing**")
        st.write("*Example:* Engineers use Python to simulate **mechanical processes, optimize design structures, and manage production lines**. For example, **SciPy** and **Matplotlib** allow engineers to model and visualize different physical systems, helping them improve designs and operational efficiency.")
        st.write("6. **Entertainment and Media**")
        st.write("*Example:* In media, Python is widely used for **game development, animation, and content recommendation systems**. Libraries like **Pygame** support game development, while **Machine Learning** with **TensorFlow** and **Keras** enables platforms to recommend personalized content to users.")
        st.write("7. **Agriculture**")
        st.write("*Example:* Python helps in **crop yield predictions, soil health analysis, and pest detection**. Using remote sensing data and specialized libraries for NDVI calculations, Python can analyze plant health and provide actionable insights to farmers.")
        st.subheader("**More References**")
        st.markdown("[GeeksforGeeks – Python Applications in Real World](https://www.geeksforgeeks.org/python-applications-in-real-world/)")
        st.markdown("[Bocasay – 7 Applications of Python Programming](https://www.bocasay.com/7-applications-python-programming/)")
        st.markdown("[Trio – Python Applications](https://trio.dev/python-applications/)")
        
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
