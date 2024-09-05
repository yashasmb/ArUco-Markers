import streamlit as st

# Define a function to initialize session state
def get_session_state():
    if "number" not in st.session_state:
        st.session_state.default_number = [23, 25, 30, 33]
        st.session_state.number = [23, 25, 30, 33]
    return st.session_state
