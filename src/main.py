# src/main.py

import streamlit as st
from query import ask_question

st.set_page_config(
page_title="Document Q&A Bot",
page_icon="📚",
layout="wide"
)

st.title("📚 Document Q&A Bot")
st.write("Ask questions about your uploaded documents.")

question = st.text_input(
"Enter your question:",
placeholder="What is this document about?"
)

if st.button("Ask"):
    if question.strip():
        with st.spinner("Searching documents and generating answer..."):
            answer = ask_question(question)
        st.subheader("Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question.")
    
