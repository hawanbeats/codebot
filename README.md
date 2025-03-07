# Starcoder 2 Chatbot with Gradio & Ollama
## 📌 Features
- 💬 Interactive Chat - Users can chat with Starcoder 2 in a simple web interface.
- 🚀 Powered by Ollama - Runs locally with Ollama’s efficient model serving.
- 🖥 Gradio Web UI - Provides an easy-to-use chat interface.
- 🔧 Code Generation & Completion - Supports code-related queries.

## 🛠️ Installation & Setup

1.  Create a virtual environment and activate:
```
python -m venv myenv
myenv\Scripts\activate
```
2.  Download required libraries:
```
pip install ollama
pip install gradio
```
3.  Ensure Ollama is running:
```
ollama run starcoder2:15b
```
4.  Run the chatbot:
```
python app.py
```
Then, the Gradio web interface open automatically in your browser.
## Usage
1. Start the chatbot.
2. Type a message (e.g., "Write a Python function to add two numbers").
3. Receive AI-generated responses powered by Starcoder 2.

## 📄 License
This project is open-source under the MIT License. Feel free to contribute!
