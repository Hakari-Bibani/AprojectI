import streamlit as st
import streamlit.components.v1 as components
from theme import apply_dark_theme
from style import apply_custom_styles

def show_home():
    apply_dark_theme()      # ensures background is dark
    apply_custom_styles()   # ensures animated styles

    # Inject custom CSS to remove top padding/margin of the main container.
    st.markdown(
        """
        <style>
            /* Remove top padding from the main block container */
            .block-container {
                padding-top: 0rem;
                margin-top: 0rem;
            }
            /* Optionally, hide the Streamlit header if you want a full-screen experience */
            header { 
                visibility: hidden;
                height: 0;
            }
            /* Remove body margin */
            body {
                margin: 0;
                padding: 0;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Render the SVG graphic at the very top using components.html.
    svg_code = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400">
        <defs>
            <!-- Light Grey Wave Gradient -->
            <linearGradient id="impactWave" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#d3d3d3"/>
                <stop offset="50%" style="stop-color:#d3d3d3"/>
                <stop offset="100%" style="stop-color:#d3d3d3"/>
            </linearGradient>

            <!-- Enhanced glow effects -->
            <filter id="primaryGlow" x="-50%" y="-50%" width="200%" height="200%">
                <feGaussianBlur stdDeviation="4" result="blur"/>
                <feFlood flood-color="#d3d3d3" flood-opacity="0.3" result="color"/>
                <feComposite in="color" in2="blur" operator="in" result="glow"/>
                <feMerge>
                    <feMergeNode in="glow"/>
                    <feMergeNode in="SourceGraphic"/>
                </feMerge>
            </filter>
        </defs>

        <!-- Pure black background -->
        <rect width="800" height="400" fill="#000000"/>

        <!-- Course title with impact animation -->
        <g transform="translate(400, 80)" filter="url(#primaryGlow)">
            <text text-anchor="middle" font-family="Plus Jakarta Sans, sans-serif" font-size="56" fill="#FFFFFF" font-weight="bold">
                AI for Impact
                <animate attributeName="opacity" values="0.9;1;0.9" dur="4s" repeatCount="indefinite"/>
            </text>
        </g>
    </svg>
    """

    # Render the SVG using components.html and ensure there is no extra margin.
    components.html(
        f"""
        <div style="margin:0; padding:0;">
            {svg_code}
        </div>
        """,
        height=500,
    )

    # Footer Messages
    st.markdown('<div class="footer footer-assignments">📌 Access Quizzes and Assignments via the Sidebar</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    show_home()
