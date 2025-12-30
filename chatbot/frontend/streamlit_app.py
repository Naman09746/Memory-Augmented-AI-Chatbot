# frontend/streamlit_app.py

import streamlit as st
import requests

API_URL = "http://localhost:8000/api/chat"

st.set_page_config(page_title="Memory Chatbot", page_icon="🧠")
st.title("🧠 Memory-Augmented Chatbot")

user_input = st.text_input("You:")

if user_input:
    res = requests.post(API_URL, json={"message": user_input})
    st.markdown(f"**Bot:** {res.json()['response']}")
