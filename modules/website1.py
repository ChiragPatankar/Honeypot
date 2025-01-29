import streamlit as st
from modules.logging_module import log_event

def run():
    st.subheader("Website1 (Secure)")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "securepass":
            st.success("Login Successful!")
            log_event("Website1", "Successful login attempt")
        else:
            st.error("Login Failed!")
            log_event("Website1", "Failed login attempt")
