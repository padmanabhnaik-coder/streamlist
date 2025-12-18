import streamlit as st

st.title("Hello, Streamlit! 👋")

name = st.text_input("What's your name?")
if name:
    st.success(f"Nice to meet you, {name}!")
