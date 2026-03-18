# 🚀 AI Script Generator using RAG

## 📌 Overview
This project generates engaging content scripts using AI. It uses a Retrieval Augmented Generation (RAG) approach to fetch relevant content and generate scripts using Google Gemini.

## ✨ Features
- AI-powered script generation
- Semantic search using embeddings
- Context-aware content creation
- Streamlit UI
- Download generated scripts

## ⚙️ Tech Stack
- Python
- Streamlit
- Google Gemini API
- Sentence Transformers

## 📂 Project Structure
ai-Script-generator/
├── app.py
├── endee_db.py
├── data/
│   └── scripts.json
├── requirements.txt

## 🔄 How it works
1. User enters a topic
2. System retrieves relevant context
3. Context is sent to Gemini AI
4. AI generates:
   - Hook
   - Script
   - CTA
   - Hashtags

## ▶️ Run Locally
```bash
pip install -r requirements.txt
python -m streamlit run app.py