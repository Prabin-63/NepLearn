# 🎓 NepLearn

> An AI-driven question recommendation system for personalized undergraduate exam preparation.

NepLearn leverages machine learning, natural language processing, and a chatbot interface to help students study smarter — clustering past exam questions, predicting important topics, and generating answers on demand.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Dataset](#-dataset)
- [Installation & Setup](#-installation--setup)
- [Environment Variables](#-environment-variables)
- [Model Training](#-model-training)
- [Limitations](#-limitations)
- [Future Enhancements](#-future-enhancements)
- [Authors](#-authors)

---

## 📖 Overview

Many students struggle to find organized, exam-focused study materials despite the abundance of online resources. **NepLearn** addresses this by:

- Clustering historical exam questions using ML techniques
- Predicting high-relevance questions based on learned exam patterns
- Generating contextual answers using a language model
- Delivering everything through a clean, user-friendly web interface

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 Authentication | Secure user registration and login |
| 🤖 ML Recommendations | Question suggestions based on exam patterns |
| 📊 Question Clustering | K-Means and DBSCAN clustering algorithms |
| 🎯 Relevance Prediction | Random Forest and XGBoost classifiers |
| ✍️ Question Generation | Prompt-based generation from learned patterns |
| 💬 AI Answer Generation | Powered by TinyLlama-1.1B-Chat-v1.0 |
| 🗣️ Chatbot Interface | Interactive learning via conversational UI |
| 🌐 Web Frontend | Responsive interface built with React.js |

---

## 🛠️ Technologies Used

### Languages
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)

### Frameworks & Libraries

| Category | Tools |
|---|---|
| Frontend | React.js |
| Backend | FastAPI |
| ML / Data | scikit-learn, XGBoost, NumPy, Pandas |
| NLP / LLM | Hugging Face Transformers, sentence-transformers (MiniLM), TinyLlama |

### Tools & Infrastructure

| Tool | Purpose |
|---|---|
| PostgreSQL | Primary database |
| pytesseract | OCR for PDF extraction |
| Git & GitHub | Version control |
| VS Code / Jupyter | Development environment |

---

## 📂 Dataset

- **1,000+** C Programming questions
- Sourced from past university exam papers and textbooks
- Preprocessed with text cleaning and normalization
- Encoded into **384-dimensional embeddings** using MiniLM
- Stored in JSON format with metadata

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.8+
- React.js 16+
- PostgreSQL

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Prabin-63/NepLearn.git
cd neplearn
```

---

### 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv

# Activate virtual environment
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

Start the backend server:

```bash
uvicorn main:app --reload
```

> Backend runs at: **http://127.0.0.1:8000**

---

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm start
```

> Frontend runs at: **http://localhost:3000**

---

### 4️⃣ Database Setup

1. Install [PostgreSQL](https://www.postgresql.org/download/)
2. Create a new database:

```sql
CREATE DATABASE neplearn;
```

3. Update database credentials in your `.env` file (see [Environment Variables](#-environment-variables))

---

## 🔐 Environment Variables

Create a `.env` file in the `backend/` directory:

```env
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgresql://user:password@localhost:5432/neplearn
ALGORITHM=HS256
```

> ⚠️ **Important:** Add `.env` to your `.gitignore` to keep credentials out of version control.

```bash
echo ".env" >> .gitignore
```

---

## 🧪 Model Training

The ML pipeline follows these steps:

1. **Embedding Generation** — Questions encoded into 384-dim vectors using MiniLM
2. **Clustering** — K-Means and DBSCAN applied to group similar questions
3. **Classification** — Random Forest and XGBoost trained to predict question relevance
---

## 🚧 Limitations

- Currently supports **C Programming questions only**
- Relatively small dataset size
- Chatbot does **not** maintain conversation history across sessions
- Performance may be slower on **CPU-only systems** due to LLM inference
- Not yet tested for large-scale deployment

---

## 🚀 Future Enhancements

- [ ] Multi-subject support beyond C Programming
- [ ] Larger and more diverse question datasets
- [ ] Context-aware, multi-turn chatbot
- [ ] Advanced recommendation models (e.g., transformer-based)
- [ ] Cloud deployment with horizontal scalability
- [ ] User feedback loop for continuous model improvement

---

## 📘 Conclusion

NepLearn demonstrates a practical application of machine learning and conversational AI in the education domain. The system successfully organizes academic questions, predicts exam-relevant content, and supports students through intelligent recommendations and AI-generated answers — providing a strong foundation for future intelligent learning platforms.

---

## 👤 Authors
**Prabin Babu Basel**<br>
**Sahaj Wagle**<br>
**Saksham Dallakoti**
