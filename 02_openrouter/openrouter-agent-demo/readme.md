# Rafiha's AI Assistant

A **Python-based Streamlit application** that serves as an intelligent AI assistant, leveraging the **OpenRouter API** with **OpenAI's GPT-3.5-turbo** model to provide conversational responses. The assistant is tailored with information about **Rafiha Siddiqui**, a passionate web developer exploring AI and web development projects.

---

## 🚀 Features

- **Interactive Chat Interface**: Clean and user-friendly UI built with Streamlit.  
- **Custom System Prompt**: Includes context about Rafiha Siddiqui as a dedicated web developer.  
- **API Integration**: Uses OpenRouter API to interact with GPT-3.5-turbo for intelligent responses.  
- **Session Management**: Maintains chat history using Streamlit's session state.  
- **Clear Chat Option**: Allows users to reset the conversation easily.  

---

## 📦 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/RafihaSiddiqui6/agentic-ai.git
cd agentic-ai

# Install dependencies
pip install -r requirements.txt

# Create a .env file and add your OpenRouter API key
# Replace 'your-openrouter-api-key' with your actual key
GEMINI_API_KEY = "your-openrouter-api-key" 

# Run the Streamlit application
streamlit run app.py
