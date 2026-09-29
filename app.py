import gradio as gr

from backend.main import app as bonolata_app

def project_info():
    return """BONOLATA — Autonomous Timber Chain of Custody

The project contains the full FastAPI dashboard and REST API.

Core modules:
• Timber and shipment management
• SHA-256 chain-of-custody verification
• Tree species AI detection
• Route and checkpoint monitoring
• Driver safety monitoring
• RAG-based assistant

Hosted note:
The chatbot's local Ollama dependency is not available automatically in Hugging Face Spaces and requires an external Ollama-compatible service.
"""

demo = gr.Interface(
    fn=project_info,
    inputs=[],
    outputs=gr.Textbox(label="BONOLATA"),
    title="BONOLATA — Timber Intelligence Platform",
    description="AI-powered timber traceability, verification, logistics and safety platform."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
