# login.py - Manages user authentication, registration, and password recovery
import streamlit as st
import sqlite3
import smtplib
from email.message import EmailMessage
from database import create_tables
from theme import apply_dark_theme
from github_sync import push_db_to_github  # Ensure this function uses st.secrets["general"]["repo"] and st.secrets["general"]["token"]

def send_password_email(recipient_email, username, password):
    """
    Sends an email with the user's password using TLS on port 587.
    """
    try:
        # Get SMTP configuration from st.secrets.
        smtp_server = st.secrets["smtp"]["server"]
        smtp_port = st.secrets["smtp"]["port"]
        smtp_email = st.secrets["smtp"]["email"]
        smtp_password = st.secrets["smtp"]["password"]

        msg = EmailMessage()
        msg.set_content(
            f"Hi {username},\n\n"
            "We received a request to send you back your password.\n"
            f"Here is your password: {password}\n\n"
            "If you have any questions, please contact us.\n\n"
            "AI For Impact team"
        )
        msg["Subject"] = "Password Recovery"
        msg["From"] = smtp_email
        msg["To"] = recipient_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(smtp_email, smtp_password)
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False

def register_user(fullname, email, phone, username, password):
    """
    Registers a new user in the database with approved=0.
    """
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()

    # Check if the password is already taken.
    cursor.execute("SELECT 1 FROM users WHERE password = ?", (password,))
    if cursor.fetchone() is not None:
        conn.close()
        return False

    try:
        cursor.execute(
            "INSERT INTO users (fullname, email, phone, username, password) VALUES (?, ?, ?, ?, ?)",
            (fullname, email, phone, username, password)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False

    conn.close()
    return True

def login_user(username, password):
    """
    Validates username/password and checks if the user is approved.
    Returns the user row if valid and approved, "not_approved" if the user exists but is not approved,
    or None if credentials are invalid.
    """
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        approved = user[5]  # 6th column is 'approved'
        if approved != 1:
            return "not_approved"
    return user

def show_login_create_account():
    """
    Renders the login, create account, and forgot password pages using a left-hand navigation
    and displays an SVG on the right. (Other logic remains unchanged.)
    """
    apply_dark_theme()
    create_tables()  # Ensure database and tables exist

    # Create two columns: left for the login interface (half width), right for the SVG.
    col_left, col_right = st.columns(2)

    with col_left:
        # Use a vertical radio button to select the option
        option = st.radio("", ["Login", "Create Account", "Forgot Password"], index=0)
        if option == "Login":
            st.subheader("🔑 Login")
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")
            if st.button("Login"):
                user = login_user(username, password)
                if user == "not_approved":
                    st.error("Your account has not been approved yet. Please wait for admin approval.")
                elif user:
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = username
                    st.success("✅ Login successful!")
                    if hasattr(st, "experimental_rerun"):
                        st.experimental_rerun()
                else:
                    st.error("❌ Invalid username or password.")

        elif option == "Create Account":
            st.subheader("🆕 Create Account")
            reg_fullname = st.text_input("Full Name", key="reg_fullname")
            reg_email = st.text_input("Email", key="reg_email")
            reg_phone = st.text_input("Mobile Number", key="reg_phone")
            reg_username = st.text_input("Username", key="reg_username")
            reg_password = st.text_input("Password", type="password", key="reg_password")
            if st.button("Register"):
                if all([reg_fullname, reg_email, reg_phone, reg_username, reg_password]):
                    try:
                        phone_int = int(reg_phone)
                    except ValueError:
                        st.error("❌ Please enter a valid phone number (digits only).")
                        return
                    if not register_user(reg_fullname, reg_email, phone_int, reg_username, reg_password):
                        st.error("⚠️ Username or Password already exists. Choose a different one.")
                    else:
                        st.success("✅ Account created! Please wait for admin approval before logging in.")
                        # Push changes to GitHub; ensure push_db_to_github uses the repo and token from st.secrets
                        push_db_to_github(st.secrets["general"]["db_path"])
                else:
                    st.error("⚠️ Please fill out all fields.")

        elif option == "Forgot Password":
            st.subheader("🔒 Forgot Password")
            forgot_email = st.text_input("Enter your registered email", key="forgot_email")
            if st.button("Retrieve Password"):
                if not forgot_email:
                    st.error("Please enter an email address.")
                else:
                    conn = sqlite3.connect(st.secrets["general"]["db_path"])
                    cursor = conn.cursor()
                    cursor.execute("SELECT username, password FROM users WHERE email=?", (forgot_email,))
                    result = cursor.fetchone()
                    conn.close()

                    if result:
                        username, password = result
                        if send_password_email(forgot_email, username, password):
                            st.success("Your password has been sent to your email address.")
                        else:
                            st.error("Failed to send email. Please try again later.")
                    else:
                        st.error("This email is not registered in our system.")

    with col_right:
        # Display the provided SVG on the right column.
        st.markdown(
            """
            <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400">
                <defs>
                    <!-- Impact wave gradient -->
                    <linearGradient id="impactWave" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" style="stop-color:#4F46E5"/>
                        <stop offset="50%" style="stop-color:#7C3AED"/>
                        <stop offset="100%" style="stop-color:#EC4899"/>
                    </linearGradient>
    
                    <!-- Enhanced glow effects -->
                    <filter id="primaryGlow" x="-50%" y="-50%" width="200%" height="200%">
                        <feGaussianBlur stdDeviation="4" result="blur"/>
                        <feFlood flood-color="#4F46E5" flood-opacity="0.3" result="color"/>
                        <feComposite in="color" in2="blur" operator="in" result="glow"/>
                        <feMerge>
                            <feMergeNode in="glow"/>
                            <feMergeNode in="SourceGraphic"/>
                        </feMerge>
                    </filter>
    
                    <!-- Tech pattern -->
                    <pattern id="techGrid" x="0" y="0" width="50" height="50" patternUnits="userSpaceOnUse">
                        <path d="M25 0 v50 M0 25 h50" stroke="#333333" stroke-width="0.5" opacity="0.15"/>
                        <circle cx="25" cy="25" r="1" fill="#333333" opacity="0.2"/>
                    </pattern>
    
                    <!-- Binary rain effect -->
                    <filter id="binaryRain">
                        <feTurbulence type="fractalNoise" baseFrequency="0.01" numOctaves="5" seed="5"/>
                        <feDisplacementMap in="SourceGraphic" scale="5"/>
                    </filter>
                </defs>
    
                <!-- Pure black background -->
                <rect width="800" height="400" fill="#000000"/>
                <rect width="800" height="400" fill="url(#techGrid)"/>
    
                <!-- Dynamic world map representation -->
                <g transform="translate(50, 50)" filter="url(#primaryGlow)" opacity="0.3">
                    <path d="M0 150 Q200 100 400 150 T800 150" stroke="url(#impactWave)" stroke-width="2" fill="none">
                        <animate attributeName="d" 
                                 dur="8s" 
                                 values="M0 150 Q200 100 400 150 T800 150;
                                        M0 170 Q200 120 400 170 T800 170;
                                        M0 150 Q200 100 400 150 T800 150"
                                 repeatCount="indefinite"/>
                    </path>
                    <!-- Connection points representing global impact -->
                    <g class="impact-points">
                        <circle cx="100" cy="120" r="3" fill="#4F46E5">
                            <animate attributeName="r" values="3;5;3" dur="3s" repeatCount="indefinite"/>
                        </circle>
                        <circle cx="300" cy="140" r="3" fill="#7C3AED">
                            <animate attributeName="r" values="3;5;3" dur="3s" begin="1s" repeatCount="indefinite"/>
                        </circle>
                        <circle cx="500" cy="130" r="3" fill="#EC4899">
                            <animate attributeName="r" values="3;5;3" dur="3s" begin="2s" repeatCount="indefinite"/>
                        </circle>
                    </g>
                </g>
    
                <!-- Advanced neural network visualization -->
                <g transform="translate(100, 100)" filter="url(#primaryGlow)">
                    <g class="neural-network">
                        <path d="M0 100 C100 50 200 150 300 100" stroke="url(#impactWave)" stroke-width="1.5" fill="none" opacity="0.6">
                            <animate attributeName="stroke-dasharray" values="0,1000;1000,0" dur="5s" repeatCount="indefinite"/>
                        </path>
                        <path d="M0 150 C100 100 200 200 300 150" stroke="url(#impactWave)" stroke-width="1.5" fill="none" opacity="0.6">
                            <animate attributeName="stroke-dasharray" values="0,1000;1000,0" dur="5s" begin="0.5s" repeatCount="indefinite"/>
                        </path>
                    </g>
                </g>
    
                <!-- Python code elements with impact focus -->
                <g transform="translate(500, 140)" filter="url(#primaryGlow)">
                    <g class="code-snippet" opacity="0.8">
                        <text x="0" y="0" font-family="JetBrains Mono, monospace" fill="#A5B4FC" font-size="14">
                            class SocialImpact:
                            <animate attributeName="opacity" values="0.7;1;0.7" dur="4s" repeatCount="indefinite"/>
                        </text>
                        <text x="20" y="25" font-family="JetBrains Mono, monospace" fill="#A5B4FC" font-size="14">
                            def analyze_data(self):
                            <animate attributeName="opacity" values="0.7;1;0.7" dur="4s" begin="0.5s" repeatCount="indefinite"/>
                        </text>
                        <text x="40" y="50" font-family="JetBrains Mono, monospace" fill="#A5B4FC" font-size="14">
                            return AI.transform()
                            <animate attributeName="opacity" values="0.7;1;0.7" dur="4s" begin="1s" repeatCount="indefinite"/>
                        </text>
                    </g>
                </g>
    
                <!-- Web development elements -->
                <g transform="translate(500, 230)" filter="url(#primaryGlow)">
                    <g class="web-elements" opacity="0.6">
                        <text x="0" y="0" font-family="JetBrains Mono, monospace" fill="#818CF8" font-size="14">&lt;div class="impact"&gt;</text>
                        <text x="20" y="25" font-family="JetBrains Mono, monospace" fill="#818CF8" font-size="14">&lt;App /&gt;</text>
                        <text x="0" y="50" font-family="JetBrains Mono, monospace" fill="#818CF8" font-size="14">&lt;/div&gt;</text>
                    </g>
                </g>
    
                <!-- Course title with impact animation -->
                <g transform="translate(400, 80)" filter="url(#primaryGlow)">
                    <text text-anchor="middle" font-family="Plus Jakarta Sans, sans-serif" font-size="56" fill="#FFFFFF" font-weight="bold">
                        AI for Impact
                        <animate attributeName="opacity" values="0.9;1;0.9" dur="4s" repeatCount="indefinite"/>
                    </text>
                </g>
    
                <!-- Inspiring subtitle -->
                <g transform="translate(400, 330)" filter="url(#primaryGlow)">
                    <text text-anchor="middle" font-family="Plus Jakarta Sans, sans-serif" font-size="24" fill="#A5B4FC">
                        Building Tomorrow's Solutions Today
                        <animate attributeName="fill" values="#A5B4FC;#818CF8;#A5B4FC" dur="6s" repeatCount="indefinite"/>
                    </text>
                </g>
    
                <!-- Technology stack with icons -->
                <g transform="translate(400, 370)" filter="url(#primaryGlow)">
                    <text text-anchor="middle" font-family="Plus Jakarta Sans, sans-serif" font-size="16" fill="#6366F1">
                        Python • Web Apps • Machine Learning • Data Analysis • Google Colab
                    </text>
                </g>
    
                <!-- Floating particles representing data points -->
                <g class="particles" filter="url(#binaryRain)">
                    <circle cx="150" cy="200" r="2" fill="#4F46E5" opacity="0.5">
                        <animate attributeName="cy" values="200;220;200" dur="4s" repeatCount="indefinite"/>
                    </circle>
                    <circle cx="650" cy="180" r="2" fill="#7C3AED" opacity="0.5">
                        <animate attributeName="cy" values="180;200;180" dur="4s" begin="1s" repeatCount="indefinite"/>
                    </circle>
                    <circle cx="400" cy="150" r="2" fill="#EC4899" opacity="0.5">
                        <animate attributeName="cy" values="150;170;150" dur="4s" begin="2s" repeatCount="indefinite"/>
                    </circle>
                </g>
            </svg>
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == '__main__':
    show_login_create_account()
