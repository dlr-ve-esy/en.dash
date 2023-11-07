import streamlit as st
from PIL import Image


def create():
    if st.session_state["style"] == "dark":
        logo = Image.open("data/column-chart-line-icon-black.png")
        logo = logo.resize((150, 100))

        st.image(logo)
    else:
        logo = Image.open("data/column-chart-line-icon-white.png")
        logo = logo.resize((150, 100))

        st.image(logo)
    st.write("Dashboard")
    darkmode_enabled = st.toggle("enable dark mode for plots")
    if darkmode_enabled:
        st.session_state["style"] = "dark"
    else:
        st.session_state["style"] = "light"
