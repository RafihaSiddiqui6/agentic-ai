## Rafiha's AI Assistant
A Python-based Streamlit application that serves as an intelligent AI assistant, leveraging the OpenRouter API with OpenAI's GPT-3.5-turbo model to provide conversational responses. The assistant is tailored with information about Rafiha Siddiqui, a passionate web developer exploring AI and web development projects.
Features

- Interactive Chat Interface: Clean and user-friendly UI built with Streamlit.
- Custom System Prompt: Includes context about Rafiha Siddiqui as a dedicated web developer.
- API Integration: Uses OpenRouter API to interact with GPT-3.5-turbo for intelligent responses.
- Session Management: Maintains chat history using Streamlit's session state.
- Clear Chat Option: Allows users to reset the conversation easily.

# Prerequisites

- Python 3.8+
- A valid OpenRouter API key (sign up at OpenRouter).
- .env file with your OPENROUTER_API_KEY.

# Installation

Clone the Repository:
git clone https://github.com/RafihaSiddiqui6/agentic-ai.git
cd agentic-ai


# Install Dependencies:
``` pip install -r requirements.txt

# Ensure you have the following in requirements.txt:
- streamlit==1.38.0
- requests==2.32.3
- python-dotenv==1.0.1


## Set Up Environment Variables:Create a .env file in the project root and add your OpenRouter API key:
## OPENROUTER_API_KEY=your-openrouter-api-key


## Run the Application:
streamlit run app.py



# Usage

- Open the application in your browser (default: http://localhost:8501).
- Type your message in the chat input field to interact with the AI assistant.
- View the conversation history displayed in a clean, styled format.
- Click the "Clear Chat" button to reset the conversation.

# Project Structure

- app.py: Main Streamlit application file containing the AI assistant logic.
- .env: Stores the OpenRouter API key (not tracked in Git).
- requirements.txt: Lists Python dependencies for the project.

# Contributing
- Contributions are welcome! Please:
