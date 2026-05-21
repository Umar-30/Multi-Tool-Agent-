import streamlit as st
import asyncio
import pandas as pd
import sqlite3
import sys
import os

# Add current directory to path to find 'app'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.agent import MultiToolAgent
from app.tools.database import init_db

# Page Configuration
st.set_page_config(
    page_title="AI Agent Pro",
    page_icon="🦾",
    layout="centered"
)

# Custom Dark Theme Styling
st.markdown("""
    <style>
    /* Full Page Background */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* Global Text Color */
    html, body, [class*="css"], .stText, .stMarkdown, p, span, li, label {
        color: #ffffff !important;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    /* Text Input and Area Styling */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #0d1117 !important;
        color: #ffffff !important;
        border: 1px solid #30363d !important;
    }
    
    /* Ensure all input text is white */
    input, textarea {
        color: #ffffff !important;
    }

    /* HTML Table Styling (for History) */
    table {
        width: 100%;
        border-collapse: collapse;
        color: white !important;
        background-color: #0d1117 !important;
    }
    th {
        background-color: #161b22 !important;
        color: #58a6ff !important;
        text-align: left;
        padding: 8px;
        border: 1px solid #30363d;
    }
    td {
        background-color: #0d1117 !important;
        color: #ffffff !important;
        padding: 8px;
        border: 1px solid #30363d;
    }
    
    /* Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #238636;
        color: white;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #2ea043;
        color: white;
    }

    /* Cards/Containers */
    .stChatMessage, .stExpander {
        background-color: #161b22;
        border: 1px solid #30363d;
    }

    /* Headers */
    h1, h2, h3 {
        color: #58a6ff !important;
    }
    
    /* Success/Info Boxes */
    .stAlert {
        background-color: #161b22;
        border: 1px solid #30363d;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

async def run_agent_logic(prompt, email):
    agent = MultiToolAgent()
    return await agent.run(user_prompt=prompt, email=email)

def get_history():
    conn = sqlite3.connect("agent.db")
    df = pd.read_sql_query("SELECT * FROM searches ORDER BY id DESC LIMIT 10", conn)
    conn.close()
    return df

def main():
    # Advanced Title with Icon
    col1, col2 = st.columns([0.15, 0.85])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/6134/6134346.png", width=70)
    with col2:
        st.title("Multi-Tool AI Agent Pro")
    
    st.subheader("Autonomous Web Search & Email Automation")

    # Sidebar for History & Functions
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/6134/6134346.png", width=100)
        st.header("⚙️ Dashboard")
        
        # 1. Statistics Function
        try:
            history_df = get_history()
            st.metric("Total Tasks Completed", len(history_df))
        except:
            st.metric("Total Tasks Completed", 0)

        st.markdown("---")
        st.header("📜 Recent History")
        
        # 2. Refresh Function
        if st.button("🔄 Refresh View"):
            st.rerun()

        # 3. Clear History Function
        if st.button("🗑️ Clear All History"):
            try:
                conn = sqlite3.connect("agent.db")
                conn.execute("DELETE FROM searches")
                conn.commit()
                conn.close()
                st.success("History Cleared!")
                st.rerun()
            except Exception as e:
                st.error(f"Error clearing history: {e}")

        st.markdown("---")
        
        # 4. History Display with Expanders (Shows result on click)
        try:
            if not history_df.empty:
                for idx, row in history_df.iterrows():
                    # Sanitize row data for display
                    q = str(row['query']).strip('"')
                    with st.expander(f"🔍 {q[:30]}..."):
                        st.markdown(f"**Full Query:** {q}")
                        st.markdown(f"**AI Result:** {row['result']}")
            else:
                st.write("No history found.")
        except Exception:
            st.write("Database error or not initialized.")

    # Main Input Section
    with st.container():
        user_prompt = st.text_area("What do you want to find?", placeholder="e.g., Latest news about SpaceX Mars mission")
        user_email = st.text_input("Receiver Email Address", placeholder="test@example.com")
        
        if st.button("Run Agent"):
            if not user_prompt or not user_email:
                st.error("Please provide both a prompt and an email address.")
            else:
                with st.spinner("Agent is working... (Searching 🌐, Saving 💾, Emailing 📧)"):
                    try:
                        # Initialize DB
                        asyncio.run(init_db())
                        
                        # Run Agent
                        result_data = asyncio.run(run_agent_logic(user_prompt, user_email))
                        
                        st.success("✅ Task Completed!")
                        
                        # Professional Response Display
                        st.markdown("---")
                        st.markdown("### 🤖 AI Response")
                        with st.chat_message("assistant", avatar="https://cdn-icons-png.flaticon.com/512/6134/6134346.png"):
                            st.markdown(result_data['result'])
                        st.markdown("---")
                        
                        st.balloons()
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
