import streamlit as st
from PIL import Image

from dashboard.tools.configuration import DashboardConfiguration


def create(dash_cfg: DashboardConfiguration):
    if "style" not in st.session_state:
        st.session_state["style"] = "dark"

    if st.session_state["style"] == "dark":
        logo = Image.open("data/column-chart-line-icon-black.png")
        logo = logo.resize((150, 100))

        st.image(logo)
    else:
        logo = Image.open("data/column-chart-line-icon-white.png")
        logo = logo.resize((150, 100))

        st.image(logo)

    st.write("Dashboard")
    if dash_cfg.enable_darkmode_toggle:
        darkmode_enabled = st.toggle("enable dark mode for plots")
    else:
        darkmode_enabled = False

    if darkmode_enabled:
        st.session_state["style"] = "dark"
    else:
        st.session_state["style"] = "light"
