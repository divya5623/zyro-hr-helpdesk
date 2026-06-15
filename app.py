import streamlit as st

st.set_page_config(page_title="Zyro HR Help Desk", page_icon="💼")

st.title("💼 Zyro Dynamics HR Help Desk")
st.write("Ask questions about Zyro Dynamics HR policies.")

question = st.text_input("Enter your HR question")

if question:
    st.success("RAG chatbot connected successfully.")
    st.write("Question:", question)
    st.write("This app is deployed for the Zyro Dynamics HR Help Desk RAG Challenge.")
