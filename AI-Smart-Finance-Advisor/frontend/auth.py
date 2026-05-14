import streamlit as st

def check_login():

    if "logged_in" not in st.session_state:

        st.session_state.logged_in = False

    return st.session_state.logged_in