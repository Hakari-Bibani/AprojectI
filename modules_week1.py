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
    st.markdown("<h2 style='color: #FFE5B4;'>1.1 Introduction to Python - Recorded Session</h2>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=Scem9sKTtJo")
    st.subheader("**ChatGPT Prompts**")
    st.markdown("[Links to an external site](https://chatgpt.com/share/6733c214-7ac4-8004-92f1-227d11b644ff)")
    st.subheader("**Content**:")
    st.write(
        "In this session, we'll introduce you to the basics of Python and how it can be a powerful tool for enhancing personal impact, "
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
            "development to scientific research, Python's syntax is clean and intuitive, making it a preferred language for both beginners and experts. "
            
            "Here’s why Python is ideal for learning:"
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
        st.markdown("[Trio – Python Applications](https://trio.dev/python-applications/)"
        )

    with tab4:
        st.header("1.4 What is in the Python Script?")
        st.write(
            "A Python script combines libraries, variables, functions, and loops to create structured workflows. In a Python script, you’ll find a set of instructions "
            "written in the Python programming language. These instructions, also called code, tell the computer exactly what to do, step by step. "
            "Think of a Python script like a recipe in a cookbook, where each line of code is an instruction for completing part of the overall task."
        )
        st.write("**Importing Libraries:** Often, the script starts by importing libraries. Libraries are collections of pre-built code that allow the script to perform specific tasks—like handling data, creating visuals, or connecting to the internet—without needing to write these functions from scratch.")
        st.write("Example: `import pandas as pd` – this line imports a library for handling data tables.")
        st.write("**Defining Variables:** Variables are like labeled containers that store information, such as numbers or text. These containers hold data that might be needed later in the script.")
        st.write("Example: `temperature = 72` – stores the number 72 in a variable called `temperature`.")
        st.write("**Functions and Loops:** Functions are small, reusable chunks of code that perform specific tasks, while loops are instructions that repeat tasks multiple times. They make your code more efficient and reduce repetition.")
        st.write("Example: `for item in list:` – starts a loop that goes through each item in a list.")
        st.write("**Data Processing and Analysis:** Many scripts work with data—cleaning, calculating, or organizing it to prepare for further analysis.")
        st.write("Example: Cleaning data or calculating averages using built-in functions.")
        st.write("**Output and Visualization:** Finally, scripts often display results to the user by printing text, creating charts, or saving files.")
        st.write("Example: `print(\"The average temperature is:\", average_temp)` displays the result.")
        st.code(
            """
# 1. Importing Libraries
import pandas as pd  # This library helps manage and analyze data in tables
import matplotlib.pyplot as plt  # This library helps create visualizations like charts
# 2. Defining Variables
data = {'Temperature': [70, 75, 80, 85, 90], 'Humidity': [30, 45, 50, 60, 70]}  # Creating sample data
city = "Kurdistan"  # Name of the location for the data
# 3. Creating a DataFrame and Calculating the Average Temperature
df = pd.DataFrame(data)  # Convert the data dictionary into a table
average_temp = df['Temperature'].mean()  # Calculate the average temperature
# 4. Loop through Data to Print Each Temperature
print(f"Weather data for {city}:")
for temp in df['Temperature']:
    print(f"- Temperature: {temp}°F")
# 5. Visualize Data: Plotting Temperature and Humidity
plt.plot(df['Temperature'], label='Temperature', color='red')
plt.plot(df['Humidity'], label='Humidity', color='blue')
plt.xlabel('Day')
plt.ylabel('Value')
plt.title(f"Weather Data for {city}")
plt.legend()
plt.show()
# 6. Output the Result
print(f"The average temperature in {city} is {average_temp}°F.")
            """,
            language="python",
        )

    with tab5:
        st.header("1.5 Introduction to Python Libraries")
        st.write(
            "Python libraries extend the functionality of the language, making it easier to perform complex tasks with simple commands. "
            "Below is a polished overview of essential Python libraries, their primary purposes, and examples of projects where they can be applied."
        )

        # Data for the table
        data = {
            'Library': [
                'Pandas', 'NumPy', 'Matplotlib', 'Seaborn', 'Scikit-Learn', 'TensorFlow', 'Keras',
                'NLTK', 'SpaCy', 'OpenCV', 'BeautifulSoup', 'Requests', 'Flask', 'Django',
                'Streamlit', 'Pygame', 'PySpark', 'Plotly', 'SQLAlchemy'
            ],
            'Purpose': [
                'Data manipulation and analysis',
                'Numerical computations and matrix operations',
                'Creating static visualizations and charts',
                'Statistical data visualization and exploratory analysis',
                'Building machine learning models and data modeling',
                'Developing deep learning models and neural networks',
                'Simplified deep learning model prototyping',
                'Natural language processing (NLP) tasks and text analysis',
                'Advanced NLP for large-scale text processing',
                'Computer vision and image processing applications',
                'Web scraping to extract data from websites',
                'Sending HTTP requests to access and interact with APIs',
                'Lightweight web development and creating RESTful APIs',
                'Full-stack web development for large-scale applications',
                'Developing interactive data applications and dashboards',
                'Game development and interactive simulations',
                'Distributed data processing and large-scale analytics',
                'Interactive, web-based visualizations and dashboards',
                'Database management and object-relational mapping (ORM)'
            ],
            'Project Examples': [
                'Cleaning and analyzing CSV/Excel data, financial data processing, and generating reports.',
                'Scientific computing, handling large-scale datasets, and performing linear algebra operations.',
                'Plotting trends, creating line/bar/pie charts, and visualizing statistical data.',
                'Generating heatmaps, pair plots, and interactive visual reports for data insights.',
                'Building classification models, predictive analytics, clustering, and recommendation engines.',
                'Developing image recognition systems, object detection, and natural language processing models.',
                'Rapid prototyping for image recognition, text classification, and other deep learning projects.',
                'Chatbots, sentiment analysis, language translation, and text-based data mining projects.',
                'Entity recognition, document classification, and large-scale language modeling projects.',
                'Face recognition, object detection, and motion tracking for real-time image processing.',
                'Scraping news sites, aggregating data from multiple sources, and building data collection tools.',
                'Accessing weather data, stock market APIs, and automating data retrieval tasks.',
                'Building small web apps, dashboards, and RESTful services for rapid prototyping.',
                'Developing e-commerce platforms, content management systems (CMS), and large-scale websites.',
                'Creating interactive dashboards, data apps, and visualizations without extensive coding.',
                'Developing 2D games, educational simulations, and interactive entertainment projects.',
                'Handling big data tasks, real-time analytics, and processing large datasets efficiently.',
                'Building interactive graphs, 3D visualizations, and dynamic dashboards for data analysis.',
                'Managing databases, developing CRUD applications, and integrating backend services.'
            ]
        }

        df = pd.DataFrame(data)

        # Style the DataFrame: white text, blue borders, and a dark background for contrast.
        styled_df = (
            df.style
              .set_table_styles([
                  {"selector": "th", "props": [("color", "white"), ("border", "2px solid blue"), ("background-color", "black")]},
                  {"selector": "td", "props": [("color", "white"), ("border", "2px solid blue"), ("background-color", "black")]}
              ])
              .set_properties(**{'text-align': 'left'})
        )

        # Render the styled table.
        st.table(styled_df)

    with tab6:
        st.header("1.6 Top 10 Things to Know in Google Colab as a Beginner")
        st.write(
            "Google Colab is a beginner-friendly, free platform that allows you to write and run Python code in the cloud. "
            "If you're new to coding or data analysis, here are the top 10 things you should know about Google Colab to get started:"
        )

        st.markdown('<p style="color: #ADD8E6;"><strong>1. Free Access to Powerful Computing</strong></p>', unsafe_allow_html=True)
        st.write(
            "Google Colab provides free access to powerful hardware like GPUs and TPUs, which are essential for tasks like "
            "machine learning and data analysis. You can use these resources without needing expensive hardware."
        )
        st.markdown("---")

        st.markdown('<p style="color: #ADD8E6;"><strong>2. No Installation Required</strong></p>', unsafe_allow_html=True)
        st.write(
            "With Google Colab, you don’t need to install Python or any software. You can run your code directly in your browser, "
            "making it easy to start coding from anywhere."
        )
        st.markdown("---")

        st.markdown('<p style="color: #ADD8E6;"><strong>3. Seamless Integration with Google Drive</strong></p>', unsafe_allow_html=True)
        st.write(
            "Colab integrates with Google Drive, so you can save your notebooks (files with .ipynb extensions) directly to your Drive. "
            "This ensures your work is safe, organized, and accessible across devices."
        )
        st.markdown("---")

        st.markdown('<p style="color: #ADD8E6;"><strong>4. Beginner-Friendly Interface</strong></p>', unsafe_allow_html=True)
        st.write(
            "Colab’s interface is straightforward:\n"
            "- **Code Cells:** Write and run Python code.\n"
            "- **Text Cells:** Add explanations, instructions, or notes using Markdown.\n\n"
            "This mix of code and text makes your projects more readable."
        )
        st.markdown("---")

        st.markdown('<p style="color: #ADD8E6;"><strong>5. Built-In Libraries</strong></p>', unsafe_allow_html=True)
        st.write(
            "Colab comes pre-installed with popular Python libraries like Pandas, NumPy, and Matplotlib. "
            "You can start analyzing data or creating visualizations without needing to install these libraries manually."
        )
        st.markdown("---")

        st.markdown('<p style="color: #ADD8E6;"><strong>6. Collaboration Made Easy</strong></p>', unsafe_allow_html=True)
        st.write(
            "Share your Colab notebook with others (just like a Google Doc). Collaborators can view or edit your code in real time, "
            "making it ideal for group projects or peer reviews."
        )
        st.markdown("---")

        st.markdown('<p style="color: #ADD8E6;"><strong>7. Data Integration</strong></p>', unsafe_allow_html=True)
        st.write(
            "Easily upload datasets or connect directly to Google Sheets, databases, or APIs. "
            "This is perfect for beginners working with small to medium-sized datasets."
        )
        st.markdown("---")

        st.markdown('<p style="color: #ADD8E6;"><strong>8. Visualization Tools</strong></p>', unsafe_allow_html=True)
        st.write(
            "Colab supports interactive visualizations with libraries like Matplotlib, Plotly, and Seaborn. "
            "You can quickly turn raw data into graphs and charts for better insights."
        )
        st.markdown("---")

        st.markdown('<p style="color: #ADD8E6;"><strong>9. Simple Debugging</strong></p>', unsafe_allow_html=True)
        st.write(
            "Colab provides error messages that help you debug your code step by step. "
            "It’s a great way to learn how Python works and fix common issues as you practice."
        )
        st.markdown("---")

        st.markdown('<p style="color: #ADD8E6;"><strong>10. Access to Tutorials and Demos</strong></p>', unsafe_allow_html=True)
        st.write(
            "Explore Colab’s built-in tutorials and code snippets. These resources guide you through common tasks like creating machine learning models or analyzing datasets, "
            "even if you’re just starting out."
        )
        st.markdown("---")

        st.markdown('<p style="color: #ADD8E6;"><strong>Bonus Tip: Keep Practicing!</strong></p>', unsafe_allow_html=True)
        st.write(
            "Google Colab is an excellent tool for hands-on learning. Start with small projects, such as analyzing a dataset, creating a simple graph, or automating tasks. "
            "With consistent practice, you’ll become comfortable coding in no time."
        )

    with tab7:
        st.header("Assignment: Week 1 – Mapping Coordinates and Calculating Distances in Python")
        st.markdown('<p style="color: red; font-size: 20px;">📝 Select Assignment 1 from the sidebar in the Assignments section.</p>', unsafe_allow_html=True)

    with tab8:
        st.header("1.8 Understanding APIs: The Key to Real-Time Data Integration")

        st.markdown("<h3 style='color: goldenrod;'>What is an API?</h3>", unsafe_allow_html=True)
        st.write(
            "An API (Application Programming Interface) is a set of rules and protocols that allows different software applications "
            "to communicate with each other. Think of it as a bridge that lets one piece of software request and retrieve data or services "
            "from another. APIs define how requests for information or actions are made, the format of these requests, and the expected responses, "
            "allowing applications to interact without needing to understand the inner workings of each other."
        )

        st.markdown("<h3 style='color: goldenrod;'>Why is an API Important?</h3>", unsafe_allow_html=True)
        st.write(
            "APIs are crucial because they enable software systems to share data and functionality, which is especially useful for developers "
            "and organizations. With APIs, applications can be made more powerful and flexible by integrating external data or services. "
            "This ability to pull in real-time data from other platforms, or let users perform specific tasks from different systems without leaving "
            "the primary application, enhances user experiences and broadens application capabilities."
        )

        st.markdown("<h3 style='color: goldenrod;'>How is an API Used? (Example)</h3>", unsafe_allow_html=True)
        st.write(
            "To use an API, you usually send a request to an endpoint URL with specific parameters that define what data or action you’re interested in. "
            "Let’s use the USGS Earthquake API as an example:"
        )
        st.code(
            "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=YYYY-MM-DD&endtime=YYYY-MM-DD",
            language="bash"
        )
        st.write("Here’s a breakdown of each part:")
        st.write("• **https://earthquake.usgs.gov/fdsnws/event/1/query:** This is the endpoint URL where the API is hosted.")
        st.write("• **format=geojson:** This parameter specifies that the response should be in GeoJSON format, a format for encoding geographical data.")
        st.write("• **starttime=YYYY-MM-DD and endtime=YYYY-MM-DD:** These parameters allow you to set a date range for the data, where YYYY-MM-DD should be replaced with actual dates (e.g., starttime=2024-01-01&endtime=2024-01-31 to get data for January 2024).")
        st.write(
            "When a request is sent with the filled-in parameters, the API returns data, often in JSON format, containing details about all recorded "
            "earthquakes within that time range. Each record includes information such as location, magnitude, depth, and time."
        )

        st.markdown("<h3 style='color: goldenrod;'>Why Use an API Like the USGS Earthquake API?</h3>", unsafe_allow_html=True)
        st.write(
            "Using APIs like the USGS Earthquake API allows developers to pull in constantly updated earthquake data directly into their applications "
            "without manually collecting, processing, and updating it themselves. This real-time data can be visualized on maps, used in alerts, "
            "or integrated into research dashboards."
        )

    with tab9:
        st.header("Assignment: Week 1 – Analyzing Real-Time Earthquake Data")
        st.markdown('<p style="color: red; font-size: 20px;">📝 Select Assignment 2 from the sidebar in the Assignments section.</p>', unsafe_allow_html=True)

    with tab10:
        st.markdown("<h1 style='color:gold;'>1.10 Real-Time Applications of Google Colab</h1>", unsafe_allow_html=True)
        st.write(
            "Google Colab is a powerful cloud-based platform that enables researchers, students, and professionals to execute Python code directly in their browsers. "
            "Its versatility makes it a valuable tool for solving real-world problems in various fields. Below are some fascinating real-time applications of Google Colab:"
        )

        st.markdown(
            "• **Real-Time Voice Cloning:** Using pre-trained models, users can clone voices from audio samples and generate new speech. "
            "This is helpful in personalized speech synthesis and assistive technologies. "
            "[Explore an example here](https://colab.research.google.com/github/tugstugi/dl-colab-notebooks/blob/master/notebooks/RealTimeVoiceCloning.ipynb)"
        )
        st.markdown(
            "• **Real-Time Object Detection:** Implement models like YOLO (You Only Look Once) for real-time object detection. "
            "Applications include autonomous vehicles and surveillance systems. "
            "[Learn more here](https://expertbeacon.com/real-time-object-detection-using-yolo-in-google-colab/)"
        )
        st.markdown(
            "• **Real-Time Data Analysis and Visualization:** Colab allows users to connect to live data sources for immediate processing and visualization, "
            "enabling faster decision-making in fields like finance and research."
        )
        st.markdown(
            "• **Collaborative Coding and Education:** Google Colab's real-time collaboration feature is ideal for educators and teams working together on coding projects. "
            "This makes it a powerful tool for interactive learning and group tasks. "
            "[Explore more here](https://devpost.com/software/actually-colab-real-time-collaborative-jupyter-editor)"
        )
        st.markdown(
            "• **Real-Time Machine Learning Model Training:** Leverage GPUs and TPUs for faster training of machine learning models. "
            "Colab supports iterative development, making it a go-to platform for AI and data science projects."
        )
        st.write(
            "These applications demonstrate how Google Colab can enhance your research, learning, and development processes. "
            "Its real-time capabilities and collaborative features make it a valuable asset for tackling complex challenges and exploring innovative solutions."
        )

    with tab11:
        st.header("Quiz: Week 1")
        st.markdown('<p style="color: red; font-size: 20px;">📝 Select Quiz 1 from the sidebar in the Quizzes section.</p>', unsafe_allow_html=True)

    with tab12:
        st.write("Content for Tab 12")
    with tab13:
        st.write("Content for Tab 13")

if __name__ == "__main__":
    show()
