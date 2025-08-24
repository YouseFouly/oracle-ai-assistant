# OracAI – AI-Powered Oracle Assistant

**OracAI** is a comprehensive AI assistant designed for Oracle users, developers, and DBAs. It combines the power of AI with Oracle expertise to provide:

- Chat-based assistance
- ERD diagram interpretation
- Cloud architecture analysis
- Oracle troubleshooting guidance

---

## 🚀 Features

### 1. ChatBot
- Interact with an AI Oracle expert.
- Ask questions related to Oracle Database, OCI, Fusion Apps, and MySQL HeatWave.
- Receive clear, step-by-step, and context-aware answers.

### 2. ERD Diagram Interpreter
- Upload ERD images (JPG/PNG).
- Automatically identify tables, attributes, primary/foreign keys, and relationships.
- Receive guidance on database implementation, normalization, and practical insights.

### 3. Cloud Architecture Diagram Assistant
- Upload Oracle Cloud Infrastructure diagrams.
- Analyze components, data flow, and security practices.
- Get recommendations for scalability, availability, and cost efficiency.

### 4. Oracle Troubleshooter
- Describe Oracle errors, performance issues, or configuration problems.
- Receive step-by-step troubleshooting instructions.
- Learn best practices to prevent future issues.

---

## 📦 Installation

1. Clone the repository

2. Install dependencies:
pip install -r requirements.txt

## ⚡ Usage

Run the Streamlit app:
streamlit run main.py

## 🛠️ Configuration

{
    "GOOGLE_API_KEY": "YOUR_API_KEY_HERE"
}

Important: Do not commit config.json with your API key to GitHub. Consider using environment variables or GitHub Secrets.

## 💡 Notes & Tips

Lottie animations are cached for performance.

Images uploaded for diagram analysis are resized automatically to improve processing speed.

AI responses may take a few seconds depending on image complexity and prompt size.

Streamlit reruns the script on each interaction—session state is used to retain uploaded images and chat history.

## 📁 Repository Structure

oracai/

├── app/

│   ├── main.py               # Main Streamlit app

│   ├── gemini_utility.py     # AI helper functions

│   ├── config.json           # API key config (keep private)

│   └── assets/               # Optional: images, Lottie JSON files

├── requirements.txt          # Python dependencies

├── .gitignore                # Ignored files like __pycache__, config.json

└── README.md                 # Project documentation

## 📌 Dependencies

Python 3.10+

Streamlit

Pillow

requests

streamlit-lottie

streamlit-option-menu

google-generativeai

