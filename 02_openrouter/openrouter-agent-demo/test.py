import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Rafiha's AI Assistant", page_icon="🤖")

# Simple clean CSS
st.markdown("""
<style>
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .main-title {
        text-align: center;
        font-size: 2rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 2rem;
        padding: 1rem 0;
        border-bottom: 1px solid #eee;
    }
    
    .chat-message {
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 10px;
    }
    
    .user-msg {
        background-color: #f0f0f0;
        text-align: right;
    }
    
    .bot-msg {
        background-color: #e8f4fd;
    }
</style>
""", unsafe_allow_html=True)

# Centered Title
st.markdown('<h1 class="main-title">🤖 Rafiha\'s AI Assistant</h1>', unsafe_allow_html=True)

# System prompt with Rafiha info
SYSTEM_PROMPT = """You are an AI assistant. You know that Rafiha Siddiqui is a web developer who is dedicated and passionate about exploring web development and AI tools. She actively works on practical projects to enhance her skills and knowledge."""

# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Get API key from environment
api_key = os.getenv("OPENROUTER_API_KEY")
model = "openai/gpt-3.5-turbo"

# Display chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-message user-msg"><b>You:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-message bot-msg"><b>AI:</b> {msg["content"]}</div>', unsafe_allow_html=True)

# Chat input
if prompt := st.chat_input("Type your message..."):
    if not api_key:
        st.error("Please set OPENROUTER_API_KEY in your .env file")
        st.stop()
    
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get AI response
    try:
        # Prepare messages for API
        api_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        api_messages.extend(st.session_state.messages)
        
        # API headers
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://localhost:8501",
            "X-Title": "Rafiha's AI Assistant"
        }
        
        # API payload
        payload = {
            "model": model,
            "messages": api_messages,
            "temperature": 0.7,
            "max_tokens": 1000
        }
        
        # Make API call
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        # Check response
        if response.status_code == 200:
            result = response.json()
            if "choices" in result and len(result["choices"]) > 0:
                reply = result["choices"][0]["message"]["content"]
                st.session_state.messages.append({"role": "assistant", "content": reply})
                st.rerun()
            else:
                st.error("No response from AI")
        else:
            st.error(f"API Error: {response.status_code}")
            
    except Exception as e:
        st.error("Something went wrong. Please try again.")

# Clear chat button (simple)
if st.session_state.messages:
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()