import streamlit as st
from theme import apply_dark_theme
from style import apply_custom_styles

# Custom CSS for styling the header and background
def set_custom_style():
    st.markdown("""
        <style>
        /* Main container styling */
        .stApp {
            background-color: black;
        }
        
        /* Header styling */
        .header-container {
            padding: 2rem;
            background: linear-gradient(90deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,1) 100%);
            border-bottom: 1px solid rgba(79, 70, 229, 0.1);
            text-align: center;
            animation: glow 4s infinite;
        }
        
        /* Title styling */
        .title {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 3.5rem;
            font-weight: bold;
            color: white;
            margin-bottom: 1rem;
            text-shadow: 0 0 10px rgba(79, 70, 229, 0.3);
        }
        
        /* Subtitle styling */
        .subtitle {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 1.5rem;
            color: #A5B4FC;
            margin-bottom: 1rem;
        }
        
        /* Tech stack styling */
        .tech-stack {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 1rem;
            color: #6366F1;
            opacity: 0.8;
        }
        
        /* Animation keyframes */
        @keyframes glow {
            0% { box-shadow: 0 0 20px rgba(79, 70, 229, 0.1); }
            50% { box-shadow: 0 0 30px rgba(79, 70, 229, 0.2); }
            100% { box-shadow: 0 0 20px rgba(79, 70, 229, 0.1); }
        }
        </style>
    """, unsafe_allow_html=True)

# Function to create the custom header
def create_header():
    header_html = """
        <div class="header-container">
            <div class="title">AI for Impact</div>
            <div class="subtitle">Building Tomorrow's Solutions Today</div>
            <div class="tech-stack">Python • Web Apps • Machine Learning • Data Analysis • Google Colab</div>
        </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)

def show_home():
    # Apply your dark theme and any other custom styles you already have
    apply_dark_theme()      
    apply_custom_styles()   
    
    # Instead of displaying an embedded video, we set the custom style and show our header.
    set_custom_style()
    create_header()

    # You can add more content below the header if you wish.
    st.markdown("---")
    st.write("## Welcome to AI for Impact")
    st.write("""
    Learn how to leverage Python and AI to create meaningful solutions.
    This course combines practical coding skills with real-world applications.
    """)
    
    # Polished Footer Messages with Custom Colors
    st.markdown('<div class="footer footer-assignments">📌 Access Quizzes and Assignments via the Sidebar</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer footer-partner">💡 AI For Impact © 2025 - Your Partner in Academic Success</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    show_home()
