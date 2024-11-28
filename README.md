# MSXHAN_AI
Flask Chatbot with Microsoft DialoGPT
This repository contains a Flask application for a chatbot powered by the Microsoft DialoGPT model. The chatbot can engage in conversations and generate human-like responses based on the conversation history.

Features:

Uses Microsoft DialoGPT for conversation generation
Stores and utilizes recent conversation history
Provides a simple chat interface (requires separate HTML template)
Error handling with informative responses
Requirements:

Python 3.x
Flask
transformers
torch
Installation:

Clone this repository.
Create a virtual environment (recommended) and activate it:
Bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate.bat  # Windows
Use code with caution.

Install the required dependencies:
Bash
pip install -r requirements.txt
Use code with caution.

Running the App:

Make sure you have the index.html template file created and placed in the root directory (see notes below).
Start the development server:
Bash
python app.py
Use code with caution.

Open http://127.0.0.1:5000/ in your web browser to access the chat interface. (Default port is 5000, adjust if needed)
Notes:

This code provides a starting point for the chatbot. You'll need to create the index.html template file to provide the user interface for interacting with the chatbot. This template should include a form to submit user messages and a way to display the conversation history and bot responses.
The provided code limits the generated response length (max_new_tokens) for faster performance. You can adjust this parameter and other model parameters in the chat route to fine-tune the chatbot's behavior.
You can further enhance the chatbot by adding features like user authentication, conversation history persistence, or integrating external knowledge sources.
Contributing:

We welcome contributions to this project! Feel free to fork the repository, make changes, and submit pull requests.
