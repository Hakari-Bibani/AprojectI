import streamlit as st
import streamlit.components.v1 as components

def show():
    # Full HTML document with inline CSS to remove margins
    html_code = """
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8">
        <style>
          /* Remove default margins/padding from the document */
          body, html {
            margin: 0;
            padding: 0;
            overflow: hidden;
            background: #000000;
          }
          /* Center the SVG container */
          .svg-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 800px;
            height: 450px;
            margin: 0 auto;
          }
        </style>
      </head>
      <body>
        <div class="svg-container">
          <svg xmlns="http://www.w3.org/2000/svg"
               viewBox="0 0 800 450"
               width="800"
               height="450"
               preserveAspectRatio="xMidYMid meet">
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
  
            <!-- Black background -->
            <rect width="800" height="450" fill="#000000"/>
  
            <!-- Dynamic wave representation -->
            <g transform="translate(50,50)" filter="url(#primaryGlow)" opacity="0.3">
              <path d="M0 150 C150 100 250 200 400 150 S700 100 800 150"
                    stroke="url(#impactWave)" stroke-width="2" fill="none">
                <animate attributeName="d" dur="8s"
                         values="M0 150 C150 100 250 200 400 150 S700 100 800 150;
                                 M0 170 C150 120 250 220 400 170 S700 120 800 170;
                                 M0 150 C150 100 250 200 400 150 S700 100 800 150"
                         repeatCount="indefinite"/>
              </path>
            </g>
  
            <!-- Title text with animation -->
            <text x="400" y="80" text-anchor="middle"
                  font-family="Plus Jakarta Sans, sans-serif"
                  font-size="32" fill="#FFFFFF" font-weight="bold">
              Utilize AI and Machine Learning Faster and Smarter
              <animate attributeName="opacity" values="0.9;1;0.9" dur="4s" repeatCount="indefinite"/>
            </text>
  
            <!-- Animated impact points -->
            <g class="impact-points">
              <circle cx="100" cy="120" r="3" fill="#d3d3d3">
                <animate attributeName="r" values="3;5;3" dur="3s" repeatCount="indefinite"/>
              </circle>
              <circle cx="300" cy="140" r="3" fill="#d3d3d3">
                <animate attributeName="r" values="3;5;3" dur="3s" begin="1s" repeatCount="indefinite"/>
              </circle>
              <circle cx="500" cy="130" r="3" fill="#d3d3d3">
                <animate attributeName="r" values="3;5;3" dur="3s" begin="2s" repeatCount="indefinite"/>
              </circle>
            </g>
  
            <!-- Python code elements -->
            <g transform="translate(500,140)" filter="url(#primaryGlow)">
              <text x="0" y="0" font-family="JetBrains Mono, monospace"
                    fill="#A5B4FC" font-size="14">
                class KurdistanFuture:
                <animate attributeName="opacity" values="0.7;1;0.7" dur="4s" repeatCount="indefinite"/>
              </text>
              <text x="20" y="25" font-family="JetBrains Mono, monospace"
                    fill="#A5B4FC" font-size="14">
                def innovate(self):
                <animate attributeName="opacity" values="0.7;1;0.7" dur="4s" begin="0.5s" repeatCount="indefinite"/>
              </text>
              <text x="40" y="50" font-family="JetBrains Mono, monospace"
                    fill="#A5B4FC" font-size="14">
                return AI.transform_region()
                <animate attributeName="opacity" values="0.7;1;0.7" dur="4s" begin="1s" repeatCount="indefinite"/>
              </text>
            </g>
  
            <!-- Subtitle texts -->
            <text x="400" y="330" text-anchor="middle"
                  font-family="Plus Jakarta Sans, sans-serif"
                  font-size="24" fill="#A5B4FC">
              Building Tomorrow's Solutions Today
              <animate attributeName="fill" values="#A5B4FC;#818CF8;#A5B4FC" dur="6s" repeatCount="indefinite"/>
            </text>
  
            <text x="400" y="420" text-anchor="middle"
                  font-family="Plus Jakarta Sans, sans-serif"
                  font-size="22" fill="#FFFFFF">
              Transform your business into a data-driven, more resilient enterprise with us!
            </text>
          </svg>
        </div>
      </body>
    </html>
    """
    # Embed the HTML document using components.html.
    components.html(html_code, height=450, scrolling=False)
