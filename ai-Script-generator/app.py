import streamlit as st
import json
import os
from google import genai
from endee_db import store_data, search

# Gemini API
client = genai.Client(api_key="AIzaSyDURbAp_yGjS9EQAM583viqFH79NL5NvCo")

# Page settings
st.set_page_config(page_title="AI Script Generator", layout="centered")

# Title
st.title("🚀 AI Script Generator")
st.markdown("Generate engaging scripts using AI + semantic search")

st.divider()

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    st.write("AI Script Generator using RAG")
    st.write("Built with Streamlit + Gemini")

# Load data
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), "data", "scripts.json")

    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}")
        return []

    with open(file_path, "r", encoding="utf-8-sig") as f:
        return json.load(f)

# Input
topic = st.text_input("🎯 Enter your topic:")

# Button
if st.button("✨ Generate Script"):
    data = load_data()

    if not data:
        st.stop()

    store_data(data)
    results = search(topic)
    context = " ".join(results)

    prompt = f"""
You are a content creator.

Topic: {topic}

Context:
{context}

Generate:
- Hook
- Script
- CTA
- Hashtags
"""

    with st.spinner("🤖 Generating..."):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

    st.success("✅ Script Generated!")

    st.markdown("## 📝 Generated Script")

    st.code(response.text)

    st.download_button(
        label="📥 Download Script",
        data=response.text,
        file_name="script.txt",
        mime="text/plain"
    )