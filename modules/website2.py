import streamlit as st
from modules.logging_module import log_event

# Dummy credentials for demonstration
USERNAME = "admin"
PASSWORD = "securepass"

def run():
    st.subheader("Website2 (Vulnerable)")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    attack_type = st.selectbox("Simulate Attack", ["None", "SQL Injection", "XSS"])

    if st.button("Login"):
        
        if username == USERNAME and password == PASSWORD:
            if attack_type != "None":
                log_event("Website2", f"Anomalous activity detected: {attack_type}")
                st.warning("Redirecting to a dummy page due to anomalous activity...")
                st.write("[Go to Dummy Page](#Dummy Page)")  # Redirect to Dummy Page
            else:
                log_event("Website2", "Successful login")
                st.success("Redirecting to Website1...")
                st.write("Website1: This is a secure website!")
        else:
            if attack_type != "None":
                log_event("Website2", f"Anomalous activity detected: {attack_type}")
                st.warning("Redirecting to a dummy page due to anomalous activity...")
                st.write("[Go to Dummy Page](#Dummy Page)")  # Redirect to Dummy Page
            else:
                log_event("Website2", "Failed login attempt")
                st.error("Login Failed!")
