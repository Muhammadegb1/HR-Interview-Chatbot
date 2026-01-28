# 💬 HR Interview Chatbot (Streamlit + OpenAI)

An interactive AI-powered HR Interview Chatbot built with **Streamlit** and the **OpenAI API**.  
This project simulates a real job interview experience and provides automated feedback and scoring based on the candidate’s performance.

## 🌐 Live Demo
You can try the HR Interview Chatbot directly online:

<p align="center">
  <a href="https://hr-interview-chatbot-53qxeri6no9qzaghykzrwl.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/🚀%20Launch%20Live%20Demo-Streamlit-brightgreen?style=for-the-badge" />
  </a>
</p>

---


## 🚀 Project Description

The **HR Interview Chatbot** is an interactive web application designed to help users practice technical and behavioral interviews.

The system acts as an HR interviewer, asking structured questions based on:

- Candidate background  
- Experience level  
- Selected job position  
- Target company  

After the interview is completed, the chatbot generates:

✅ Overall interview score (1–10)  
✅ Professional feedback summary  
✅ Suggestions for improvement  

---
## ✨ Features

- Interactive AI-driven interview simulation  
- Role and company customization  
- Chat-based UI with Streamlit  
- Automated performance evaluation  
- Final score + feedback generation  
- Clean modular project structure  
- Restart interview functionality
  
---
## 🧠 Supported Positions

The chatbot supports interviews for roles such as:

- Data Scientist  
- Data Engineer  
- Machine Learning Engineer  
- BI Analyst  
- Financial Analyst  

---

## 📂 Project Structure

```bash
📁 hr-interview-chatbot/
│
├── app.py              # Main Streamlit application (UI + flow)
├── chat_engine.py      # Interview chat logic using OpenAI
├── feedback.py         # Feedback & scoring generation
├── utils.py            # Helper functions (reset, setup, state)
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

## ⚙️ Installation & Setup
Follow these steps to run the project locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/hr-interview-chatbot.git
cd hr-interview-chatbot
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure OpenAI API Key
Create the following file:
```bash
.streamlit/secrets.toml
```
Inside it, add:
```toml
OPENAI_API_KEY="your_api_key_here"
```

### ▶️ Run the Application
```bash
streamlit run app.py
```




