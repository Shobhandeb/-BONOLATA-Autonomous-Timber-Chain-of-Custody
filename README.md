# 🌳 TimberTrust: Autonomous Timber Chain of Custody

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-ResNet18-EE4C2C.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Edge%20AI-00A67E.svg)
![IEEE](https://img.shields.io/badge/IEEE-Internship%20Project-00629B.svg)

**TimberTrust** is an enterprise-grade, decentralized verification platform designed to combat illegal deforestation, monitor physical timber assets via IoT telemetry, ensure driver vigilance through Edge AI computer vision, and guarantee chain-of-custody integrity with immutable cryptographic hashing.

Developed as an **IEEE Internship Project** focusing on smart logistics, blockchain technology, and applied computer vision.

---

## 👥 Project Team & Mentorship
* **Academic & Technical Mentor:** Dr. Ramen Pal
* **Lead Developer & Researcher:** Rounak Singha (IEEE Project Intern)
* **Lead Developer & Researcher:** Shobhandeb Adak (IEEE Project Intern)

---

## ✨ Core Features & Architecture

### 1. 🌿 AI Tree Species Detection (ResNet18)
To prevent timber misclassification and fraud at the source, TimberTrust utilizes a custom-trained **ResNet18 Neural Network**.
* **Dataset:** BarkVisionAI (Trained on 13 specific botanical classes including *Shorea robusta*, *Tectona grandis*, etc.)
* **Live Knowledge Base:** Integrates dynamically with the Wikipedia REST API to provide instant, localized encyclopedic data about the detected species.
* **Architecture:** Fully disconnected offline capability utilizing PyTorch weights (`tree_model.pth`).

### 2. 👁️ Edge AI Driver Safety Monitor
Fatigue-induced accidents are a severe risk in timber transport logistics.
* **Technology:** Google MediaPipe Face Mesh.
* **Mechanism:** Calculates the real-time **Eye Aspect Ratio (EAR)** of the driver. If the EAR drops below a critical threshold (indicating drowsiness), the system triggers visual and auditory alerts and logs the event to the centralized dashboard.

### 3. ⛓️ SHA-256 Blockchain Ledger
Every custody transfer, checkpoint clearance, and driver alert is cryptographically sealed.
* **Immutable Tracking:** Blocks are linked via previous hashes.
* **Tamper Detection:** The frontend features an interactive, horizontal curved "winding road" UI. If a block's data is tampered with, the UI triggers a "broken chain" snap animation, instantly flagging the compromised data.

### 4. 🛰️ Live IoT Telemetry & Control Center
* **Live GIS Tracking:** Implemented via Leaflet.js to monitor active truck shipments in real-time.
* **Geofencing:** Detects route deviations and unauthorized stops, instantly triggering security alerts to the dispatch center.

### 5. 🤖 Riya AI Assistant
A built-in conversational AI widget designed to assist dispatchers with instant compliance querying, system navigation, and logistics diagnostics.

---

## 📂 Directory Structure

```text
TimberTrust/
├── backend/
│   ├── main.py                 # FastAPI application & lifespan manager
│   ├── services/
│   │   └── tree_detector.py    # PyTorch ResNet18 model loader & inference
│   ├── routes/                 # API endpoints (Timber, Shipments, Ledger)
│   ├── chatbot/                # Riya AI logic
│   └── tree_model.pth          # Saved PyTorch Model Weights
├── frontend/
│   ├── dashboard.html          # Main Control Center UI
│   ├── driver-safety.html      # MediaPipe EAR tracking interface
│   ├── css/
│   ├── js/                     
│   │   ├── dashboard.js        # Dashboard state & AI Vision integration
│   │   ├── chatbot.js          # Riya AI client & navigation interceptor
│   │   └── driver-safety.js    # Edge AI webcam logic
│   └── images/                 # Team avatars and assets
├── requirements.txt            # Python dependencies
└── README.md