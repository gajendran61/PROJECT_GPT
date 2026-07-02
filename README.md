# 🚀 PlacementGPT – AI-Powered Placement Eligibility & Career Guidance System

## 📌 Overview

**PlacementGPT** is an AI-powered Placement Eligibility and Career Guidance System designed to help students evaluate their placement readiness through a conversational ChatGPT-like interface.

The application leverages **Large Language Models (LLMs)**, **Retrieval-Augmented Generation (RAG)**, **Machine Learning**, and **Student Performance Analytics** to provide personalized placement guidance, eligibility checks, readiness scores, and career improvement recommendations.

Unlike traditional placement portals, PlacementGPT does not simply display eligibility criteria. Instead, it intelligently analyzes student performance, compares it against company requirements, predicts placement outcomes, and explains every decision in natural language.

---

# 🎯 Project Objectives

* Automate placement eligibility verification.
* Predict student placement readiness.
* Provide AI-powered career guidance.
* Explain placement decisions using LLMs.
* Identify strengths and skill gaps.
* Help placement officers screen students efficiently.
* Offer a ChatGPT-style conversational experience.

---

# 🧠 Key Features

### 👨‍🎓 Student Features

* ChatGPT-like AI Assistant
* Placement Eligibility Check
* Placement Readiness Score
* Skill Gap Analysis
* Personalized Career Recommendations
* Company-wise Eligibility Verification
* Interview Preparation Suggestions
* Resume Improvement Guidance
* Certification Recommendations
* Internship Recommendations

### 👨‍💼 Placement Officer Features

* Student Performance Analysis
* Candidate Screening
* Placement Prediction
* Company Eligibility Filtering
* Batch-wise Analytics
* Placement Reports

---

# 🏗️ Project Architecture

```
Student
     │
     ▼
Next.js Frontend
(ChatGPT Interface)
     │
     ▼
FastAPI Backend
     │
 ┌───┴──────────────┐
 │                  │
 ▼                  ▼
Machine Learning    RAG Pipeline
Prediction          (LangChain)
 │                  │
 ▼                  ▼
Placement Model     ChromaDB
 │                  │
 └──────┬───────────┘
        ▼
 Llama 3.2 1B Instruct
        ▼
 AI Placement Assistant
        ▼
 Eligibility Report & Career Guidance
```

---

# 🛠 Technology Stack

## Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS
* Axios
* React Icons

---

## Backend

* Python
* FastAPI
* Uvicorn
* Pydantic
* Pandas
* NumPy

---

## Artificial Intelligence

* Llama 3.2 1B Instruct
* Ollama
* LangChain
* Sentence Transformers
* Retrieval-Augmented Generation (RAG)

---

## Machine Learning

* Scikit-learn
* Random Forest Classifier
* XGBoost (Optional)
* Joblib

---

## Vector Database

* ChromaDB

---

## Embedding Model

```
all-MiniLM-L6-v2
```

---

## Data Processing

* Pandas
* NumPy

---

## Dataset

CSV Dataset containing student academic and placement information.

Sample attributes:

* Student ID
* Student Name
* Gender
* Department
* CGPA
* 10th Percentage
* 12th Percentage
* Aptitude Score
* Communication Score
* Technical Score
* Coding Score
* Projects Completed
* Internships
* Certifications
* Attendance
* Backlogs
* Placement Status

---

# 📂 Project Structure

```
PlacementGPT/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   ├── services/
│   │   ├── styles/
│   │   └── types/
│   ├── package.json
│   └── next.config.js
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── rag/
│   │   ├── models/
│   │   ├── services/
│   │   ├── database/
│   │   └── main.py
│   │
│   ├── data/
│   │   ├── placement_dataset.csv
│   │   └── company_criteria.csv
│   │
│   ├── requirements.txt
│   └── .env
│
├── docs/
│
└── README.md
```

---

# 🤖 AI Workflow

```
User asks a question
          │
          ▼
Next.js Chat Interface
          │
          ▼
FastAPI API
          │
          ▼
Retrieve Student Profile
          │
          ▼
Retrieve Company Criteria
          │
          ▼
Generate Embeddings
          │
          ▼
Search ChromaDB
          │
          ▼
Relevant Context Retrieved
          │
          ▼
Placement Prediction Model
          │
          ▼
Llama 3.2 1B
          │
          ▼
AI Generated Response
          │
          ▼
Display Response to User
```

---

# 🔍 Retrieval-Augmented Generation (RAG)

The project uses RAG to enhance the accuracy of AI-generated responses.

Workflow:

1. Student data and company criteria are converted into vector embeddings.
2. Embeddings are stored in ChromaDB.
3. User queries trigger semantic search.
4. Relevant context is retrieved.
5. The retrieved context is passed to the Llama model.
6. Llama generates accurate and context-aware placement guidance.

---

# 📈 Machine Learning Module

A supervised machine learning model predicts placement probability based on student performance.

### Input Features

* CGPA
* Aptitude Score
* Technical Score
* Communication Score
* Coding Score
* Projects Completed
* Internships
* Certifications
* Attendance
* Backlogs

### Output

* Placed
* Not Placed

The prediction is explained by the LLM in natural language to improve transparency.

---

# 💬 Example User Questions

* Am I eligible for TCS?
* What is my placement readiness score?
* Which skills should I improve?
* Why am I not eligible for Infosys?
* Suggest certifications for better placements.
* Compare my profile with Amazon requirements.
* How can I improve my chances of getting placed?

---

# 📊 Example AI Response

```
Eligibility Status:
Eligible

Placement Readiness Score:
86/100

Strengths
✔ Good CGPA
✔ Strong Coding Score
✔ No Active Backlogs
✔ Internship Experience

Areas for Improvement
• Improve Communication Skills
• Complete Cloud Certification

Recommendations
• Practice Mock Interviews
• Build One Full Stack Project
• Improve Data Structures & Algorithms

Reasoning

Based on your academic performance, coding ability,
internship experience, and company eligibility criteria,
you satisfy most placement requirements.
```

---

# 🔒 Security Features

* Input Validation
* Secure API Communication
* Prompt Injection Protection
* No Exposure of Internal System Prompts
* Context-Based AI Responses
* Environment Variable Configuration

---

# 🚀 Future Enhancements

* Multi-LLM Support
* Resume Analyzer
* AI Mock Interview
* Voice-Based Placement Assistant
* Company Recommendation Engine
* LinkedIn Profile Analysis
* Real-Time Placement Dashboard
* PDF Placement Report Generation
* Student Authentication
* Admin Dashboard
* Multi-College Support

---

# 📚 Learning Outcomes

This project demonstrates practical implementation of:

* Full Stack Development
* Artificial Intelligence
* Machine Learning
* Large Language Models
* Prompt Engineering
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* FastAPI Development
* Next.js Development
* REST API Design
* Data Processing
* Model Integration
* Explainable AI

---

# 👨‍💻 Developed By

**Gajendran K**

Final Year Artificial Intelligence & Machine Learning Student

---

# ⭐ Project Summary

PlacementGPT combines **Machine Learning**, **Large Language Models**, **Retrieval-Augmented Generation (RAG)**, and **Full Stack Web Development** to build an intelligent placement assistant capable of predicting placement readiness, checking company eligibility, explaining AI predictions, and providing personalized career guidance through a modern ChatGPT-like conversational interface.
