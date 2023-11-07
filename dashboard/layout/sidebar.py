import streamlit as st


def create():
    st.write("this is the sidebar")
    darkmode_enabled = st.toggle("enable dark mode")
    with st.spinner(text="switching style ..."):
        if darkmode_enabled:
            st.session_state["style"] = "dark"
        else:
            st.session_state["style"] = "light"
