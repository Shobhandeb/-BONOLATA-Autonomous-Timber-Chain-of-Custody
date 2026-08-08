# 🌳 TimberTrust: Autonomous Timber Chain of Custody & Logistics

<div align="center">
  <img src="https://github.com/user-attachments/assets/1db993a1-d6e2-43fa-880d-562052349908" alt="TimberTrust Hero Image" width="100%" />
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.100+-009688.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/PyTorch-ResNet18-EE4C2C.svg" alt="PyTorch">
  <img src="https://img.shields.io/badge/MediaPipe-Edge%20AI-00A67E.svg" alt="MediaPipe">
  <img src="https://img.shields.io/badge/Architecture-Edge%20Computing-ff69b4.svg" alt="Edge Computing">
  <img src="https://img.shields.io/badge/IEEE-Internship%20Project-00629B.svg" alt="IEEE">
</p>

<p align="center">
  <strong>An enterprise-grade, decentralized verification platform combating illegal deforestation, securing supply chains via cryptographic ledgers, and ensuring driver safety through Edge AI.</strong>
</p>

---

## 📑 Table of Contents
1. [Executive Summary](#-executive-summary)
2. [Project Team & Mentorship](#-project-team--mentorship)
3. [System Architecture & Data Flow](#-system-architecture--data-flow)
4. [Deep Dive: Core Modules](#-deep-dive-core-modules)
5. [Technology Stack](#-technology-stack)
6. [Directory Structure](#-directory-structure)
7. [Getting Started (Local Deployment)](#-getting-started-local-deployment)
8. [API Reference](#-api-reference-overview)
9. [Future Roadmap](#-future-roadmap)
10. [License & Acknowledgements](#-license--acknowledgements)

---

## 🌍 Executive Summary
The global timber trade is plagued by "timber laundering"—where illegally harvested, endangered wood is mixed with legal supply chains. Additionally, the logistics of transporting heavy timber from remote forests involve high-risk, fatigue-prone driving conditions. 

**TimberTrust** was engineered to solve these dual challenges. By operating at the intersection of **Applied Machine Learning**, **Immutable Cryptography**, and **IoT Telemetry**, TimberTrust creates a mathematically verifiable, end-to-end chain of custody. It ensures that the wood arriving at the sawmill is exactly what was logged in the forest, while actively monitoring the safety of the human operators transporting it.

---

## 👥 Project Team & Mentorship
Developed under the rigorous standards of an **IEEE Internship Project** focusing on smart logistics and blockchain technology.
* **Dr. Ramen Pal** — Academic & Technical Mentor
* **Rounak Singha** — Lead Developer & Researcher (IEEE Project Intern)
* **Shobhandeb Adak** — Lead Developer & Researcher (IEEE Project Intern)

---

## ⚙️ System Architecture & Data Flow

TimberTrust is designed with an **Edge-to-Cloud architecture**, acknowledging that logging camps often lack reliable internet connectivity.

1. **The Edge (Forest/Truck):** The ResNet18 species detection and MediaPipe safety monitor run *locally* on edge devices. This eliminates cloud latency and allows operations to continue offline.
2. **The Gateway (FastAPI):** Once connectivity is established, telemetry payloads and checkpoint logs are transmitted securely via REST API to the backend.
3. **The Ledger (SHA-256):** The backend processes the payloads, hashes them using SHA-256, and appends them to the immutable chain.
4. **The Command Center (Dashboard):** Dispatchers view real-time synchronized data, interactive maps, and AI chatbot analytics on a unified web interface.

---

## ✨ Deep Dive: Core Modules

### 1. 🌿 Edge AI Tree Species Detection (ResNet18)
To prevent botanical fraud, TimberTrust validates species composition at the point of origin.
* **Neural Architecture:** A heavily optimized **ResNet18 Convolutional Neural Network**.
* **Dataset (BarkVisionAI):** Custom-curated and trained on 13 specific botanical classes, specializing in high-value and at-risk species (e.g., *Shorea robusta*, *Tectona grandis*).
* **Offline Inference Engine:** Weights are compiled into `tree_model.pth` and executed locally via PyTorch, entirely bypassing cloud-compute bottlenecks.
* **Contextual Enrichment:** When online, the system hits the Wikipedia REST API to dynamically fetch conservation status, legal logging parameters, and biological data for the detected species.

> 📸 *[Add Screenshot Here: Show the AI Tree Species Detection interface analyzing a piece of bark, alongside the Wikipedia pop-up info]*

### 2. 👁️ Algorithmic Driver Safety Monitor
Fatigue-induced accidents in heavy timber transport are often fatal. TimberTrust acts as an algorithmic co-pilot.
* **Facial Landmark Tracking:** Utilizes Google MediaPipe Face Mesh to map 468 3D facial landmarks at 30+ FPS.
* **Mathematical Vigilance:** Calculates the **Eye Aspect Ratio (EAR)** in real-time. If the EAR moving average drops below the critical physiological threshold for micro-sleep, the system interrupts the event.
* **Automated Intervention:** Triggers cabin alarms and instantly dispatches an asynchronous high-priority alert to the centralized dashboard.

> 📸 *[Add Screenshot Here: Show the Driver Safety module with the facial mesh overlay and a visible EAR reading]*

### 3. ⛓️ Cryptographic Chain of Custody (SHA-256 Ledger)
Data integrity is paramount. A standard database can be altered; a cryptographic chain cannot.
* **Immutable Blocks:** Every transit checkpoint, custody transfer, and driver alert is packaged as a JSON payload, hashed via SHA-256, and strictly linked to the `previous_hash`.
* **Tamper-Evident UI (The Winding Road):** The frontend renders the blockchain as an interactive, horizontal winding road. If database injection or tampering occurs, the hash verification fails, triggering a dynamic "broken chain" UI animation that isolates the compromised block.

> 📸 *[Add Screenshot Here: Show the Winding Road UI displaying the verified blocks, and a second image showing the "broken chain" state]*

### 4. 🛰️ Live IoT Telemetry & Dispatch Center
* **Spatial Tracking:** Implemented via Leaflet.js and OpenStreetMap (OSM) for lightweight, high-performance GIS tracking of the active fleet.
* **Geofencing & Deviation Algorithms:** Automatically monitors expected routes. Unauthorized stops or deviations trigger security protocols to prevent cargo theft.

> 📸 *[Add Screenshot Here: Show the main Control Center/Dashboard map with live truck pins and route lines]*

### 5. 🤖 "Riya" AI Assistant
A built-in Natural Language Processing (NLP) widget designed as a command-line alternative for dispatchers. Riya handles instant compliance querying, UI navigation shortcuts, and logistics diagnostics without requiring the user to dig through menus.

---

## 🛠️ Technology Stack

| Domain | Technologies Used |
| :--- | :--- |
| **Backend & API** | Python 3.9+, FastAPI, Uvicorn, Pydantic |
| **AI & Computer Vision** | PyTorch, Torchvision, Google MediaPipe |
| **Cryptographic Security** | Python `hashlib` (SHA-256 Implementation) |
| **Frontend UI/UX** | HTML5, CSS3, Vanilla JS, Leaflet.js (GIS) |
| **External APIs** | Wikipedia REST API, OpenStreetMap |

---

## 📂 Directory Structure

```text
TimberTrust/
├── backend/
│   ├── main.py                 # FastAPI application, CORS, & route inclusion
│   ├── services/
│   │   ├── tree_detector.py    # PyTorch ResNet18 model loader & tensor processing
│   │   └── ledger.py           # Core SHA-256 hashing and chain validation logic
│   ├── routes/                 # Separated API routers (Timber, Shipments, Ledger)
│   ├── chatbot/                # Riya AI NLP parsing and response logic
│   └── tree_model.pth          # Saved PyTorch Model Weights (Do not alter)
├── frontend/
│   ├── dashboard.html          # Main Control Center UI (Map, Ledger, Chatbot)
│   ├── driver-safety.html      # Isolated Edge AI webcam interface
│   ├── css/
│   │   └── style.css           # Custom UI styling and Winding Road animations
│   ├── js/                     
│   │   ├── dashboard.js        # API polling, Leaflet map logic, DOM updates
│   │   ├── chatbot.js          # Riya AI client & navigation interceptor
│   │   └── driver-safety.js    # Canvas manipulation and MediaPipe integration
│   └── images/                 # Static assets, placeholders, and avatars
├── .env.example                # Example environment variables required
├── requirements.txt            # Python dependencies mapping
└── README.md                   # Project documentation
