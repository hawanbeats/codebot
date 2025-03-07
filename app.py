import gradio as gr #type: ignore
import ollama #type: ignore

MODEL_NAME = "starcoder2:15b"

def chat_with_starcoder(prompt, history=[]):
    """Generates a response from the Starcoder 2 model using Ollama."""
    response = ollama.chat(model=MODEL_NAME, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

iface = gr.ChatInterface(fn=chat_with_starcoder, title="Starcoder 2 Chatbot", description="Chat with Starcoder 2 (15B) via Ollama.")

if __name__ == "__main__":
    iface.launch()