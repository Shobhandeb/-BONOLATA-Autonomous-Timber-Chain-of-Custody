import os

# ZeroGPU must be imported before torch/ML libraries.
import spaces
import gradio as gr
import uvicorn

from backend.main import app as bonolata_app
from backend.services.tree_detector import predict_tree_species

def space_status():
    return (
        "BONOLATA is running.\n\n"
        "Full dashboard: /dashboard.html\n"
        "API documentation: /docs\n"
        "Tree AI endpoint: /api/tree/detect\n\n"
        "The local Ollama chatbot is disabled unless an external Ollama-compatible "
        "service is configured."
    )

with gr.Blocks(title="BONOLATA — Timber Intelligence Platform") as demo:
    gr.Markdown("# 🌲 BONOLATA")
    gr.Markdown(
        "Autonomous Timber Chain of Custody, AI Verification & Intelligent Logistics Platform"
    )
    status = gr.Textbox(label="Deployment status", value=space_status(), interactive=False)
    gr.Markdown(
        "Open **/dashboard.html** on this Space for the original BONOLATA web dashboard."
    )

# Keep the original FastAPI application at the root so its existing frontend/API URLs remain usable.
bonolata_app = gr.mount_gradio_app(
    bonolata_app,
    demo,
    path="/gradio",
    ssr_mode=False,
)

if __name__ == "__main__":
    # Required for custom FastAPI + Gradio mounting on Spaces.
    try:
        if hasattr(spaces, "zero") and hasattr(spaces.zero, "startup"):
            spaces.zero.startup()
    except Exception as exc:
        print(f"[ZeroGPU] startup hook warning: {exc}")

    uvicorn.run(bonolata_app, host="0.0.0.0", port=7860)
