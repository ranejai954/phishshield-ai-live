# 🛡️ PhishShield AI Live

> AI-Powered Phishing Detection & Threat Analysis Platform

PhishShield AI Live is a lightweight, deployment-ready cybersecurity application that analyzes suspicious emails, SMS messages, and text-based communications to identify potential phishing attacks. The platform leverages Large Language Models (LLMs) through the Groq API to perform intelligent threat analysis, calculate risk scores, classify threat levels, and generate downloadable security reports.

---

## 🚀 Features

### 🔍 AI-Powered Phishing Detection

* Analyze suspicious emails, SMS messages, and text communications
* Detect phishing indicators using Groq AI
* Identify social engineering tactics and malicious intent

### 📊 Risk Assessment Engine

* Generate phishing risk scores (0–100)
* Classify threats into:

  * LOW
  * MEDIUM
  * HIGH
  * CRITICAL
* Provide detailed explanations for detected threats

### 📄 PDF Report Generation

Generate downloadable PDF reports containing:

* Analysis ID
* Risk Score
* Threat Level
* Security Explanation
* Recommended Actions

### 🌐 Deployment Ready

* Lightweight architecture
* No database dependency
* Optimized for cloud deployment
* Compatible with Hugging Face Spaces

---

## 🏗️ System Architecture

```text
User Input
    │
    ▼
Streamlit Frontend
    │
    ▼
Groq AI Engine
    │
    ▼
Threat Analysis
    │
    ├── Risk Score
    ├── Threat Level
    ├── Indicators
    ├── Explanation
    └── Recommendations
    │
    ▼
PDF Report Generation
    │
    ▼
Download Report
```

---

## 🛠️ Tech Stack

| Component       | Technology          |
| --------------- | ------------------- |
| Frontend        | Streamlit           |
| AI Engine       | Groq API            |
| Backend Logic   | Python              |
| PDF Reports     | ReportLab           |
| Deployment      | Hugging Face Spaces |
| Version Control | Git & GitHub        |

---

## 📂 Project Structure

```text
PhishShield-AI-Live/
│
├── ai/
│   └── groq_engine.py
│
├── reports/
│   └── pdf_generator.py
│
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/ranejai954/phishshield-ai-live.git
cd phishshield-ai-live
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Running The Application

Start Streamlit:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 📋 Workflow

```text
User submits message
        │
        ▼
AI Analysis
        │
        ▼
Risk Assessment
        │
        ▼
Generate PDF Report
        │
        ▼
Download Results
```

---

## 🎯 Use Cases

* Cybersecurity Awareness Training
* Phishing Email Analysis
* SMS Scam Detection
* Security Education
* Threat Intelligence Demonstrations
* AI Security Research
* Student Cybersecurity Projects

---

## 🔮 Future Enhancements

* URL Reputation Analysis
* Email Header Inspection
* File Attachment Scanning
* Threat Intelligence Integration
* Browser Extension Support
* Multi-Language Phishing Detection
* Real-Time Threat Monitoring
* API-Based Analysis Service

---

## 👨‍💻 Author

**Jai Rane**

Cybersecurity | AI | Cloud Security

GitHub: https://github.com/ranejai954

---

## 📜 License

This project is developed for educational and research purposes as part of the IBM SkillsBuild AI Internship Program.


## 🔗 Related Repository

This repository contains the lightweight deployment-ready version of PhishShield AI designed for cloud hosting and public demonstrations.

For the complete version featuring:

* MySQL Database Integration
* Analysis History Tracking
* Security Analytics Dashboard
* Persistent Storage
* Advanced Project Architecture

visit the full project repository:

**PhishShield AI (Full Version)**

https://github.com/ranejai954/phishshield-ai

### Version Comparison

| Feature               | PhishShield AI Live | PhishShield AI (Full Version) |
| --------------------- | ------------------- | ----------------------------- |
| AI Phishing Detection | ✅                   | ✅                             |
| Risk Assessment       | ✅                   | ✅                             |
| PDF Report Generation | ✅                   | ✅                             |
| Deployment Ready      | ✅                   | ⚠️ Local Setup Required       |
| MySQL Database        | ❌                   | ✅                             |
| Analysis History      | ❌                   | ✅                             |
| Analytics Dashboard   | ❌                   | ✅                             |
| Persistent Storage    | ❌                   | ✅                             |

The full version is recommended for users who want to explore the complete architecture, database integration, analytics capabilities, and local deployment workflow.
