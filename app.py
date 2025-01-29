import streamlit as st
from modules import website2, dummy_page, reporting

def main():
    st.title("Cybersecurity Educational Platform")
    menu = ["Website2", "Reporting"]
    choice = st.sidebar.selectbox("Choose Page", menu)

    if choice == "Website2":
        website2.run()
    elif choice == "Reporting":
        reporting.generate_report()
    elif choice == "Dummy Page":
        dummy_page.run()

if __name__ == "__main__":
    main()
