import json
import pandas as pd
import streamlit as st

def load_logs(website):
    log_file = f"logs/{website}_logs.json"
    try:
        with open(log_file, "r") as file:
            return [json.loads(line) for line in file.readlines()]
    except FileNotFoundError:
        return []

def generate_report():
    st.subheader("Attack Reports")

    # Load logs
    website2_logs = load_logs("Website2")

    # Convert logs to a DataFrame
    if website2_logs:
        website2_df = pd.DataFrame(website2_logs)
        st.write("Website2 Logs")
        st.dataframe(website2_df)

        # Filter logs for successful logins
        successful_logins = website2_df[website2_df["event"].str.contains("Successful login", na=False)]
        st.write("Successful Logins")
        st.dataframe(successful_logins)

        # Filter logs for anomalous activities
        anomalies = website2_df[website2_df["event"].str.contains("Anomalous activity", na=False)]
        st.write("Anomalous Activities")
        st.dataframe(anomalies)
    else:
        st.info("No logs available for Website2.")
