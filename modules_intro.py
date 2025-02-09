import streamlit as st

def show():
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["Welcome", "Course Instructions", "Stay Connected"])
    
   with tab1: 
        st.markdown("<h1 style='color: gold;'>Welcome</h1>", unsafe_allow_html=True)
        st.write("Welcome to the introduction module. Here you'll get an overview of the course and what to expect.")

        # Embed YouTube video
        st.video("https://www.youtube.com/watch?v=G8BC2NIfpAs")
    
    with tab2:
        st.markdown("<h1 style='color: gold;'>Course Instructions</h1>", unsafe_allow_html=True)
        st.markdown("""
        This course is designed to span **5 weeks**, structured to provide you with a comprehensive learning and hands-on experience:

        * **Weeks 1–3:** Focus on learning foundational concepts and developing your Python skills through tutorials, assignments, and guided exercises.
        * **Weeks 4–5:** Dedicated to working on your personalized project, applying what you've learned to create a meaningful and impactful application.

        ## Weekly Structure
        1. Each week begins with a **video tutorial** that introduces the core concepts.
        2. Follow up with related materials, assignments, and discussions to deepen your understanding.

        ## Online Sessions:
        * To schedule one-on-one sessions, **stay in contact with the instructor** for organizing a convenient time.
        * These sessions are designed to address your queries, provide feedback, and guide you through challenges.

        ## Assignment Submission:
        * Submit assignments promptly and ensure all required files and links are included.
        * **For Google Colab projects**, ensure they are **set to public** so your peers and the instructor can access and review them.
        """)
    
    with tab3:
    # Use st.markdown with HTML/CSS for the pale orange title
        st.markdown(
            "<h1 style='color: #FFD3A3;'>Stay Connected: Join Our Discord Server!</h1>", 
            unsafe_allow_html=True
    )
    
    st.markdown("""
    **Enhance your learning experience by joining our Discord server**, a dedicated space for collaboration, support, and community engagement.

    ## Why Join Our Discord Server?
    * **Stay Updated:** Get instant updates about the course, assignments, and materials.
    * **Connect with Peers:** Engage with fellow learners, ask questions, and share your progress.
    * **Exclusive Opportunities:** Be the first to know about new projects, learning resources, and events.
    * **Direct Support:** Reach out for help from the instructor or peers in real-time.

    Discord is a powerful platform for building an active learning community. It's simple to use and ensures you're always in the loop.

    ## Join Now
    Become part of the conversation today! 

    **Discord Invite Link:** [Click to Join](https://discord.gg/JnybQncM)
    """)
