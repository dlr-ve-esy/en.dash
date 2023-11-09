import streamlit as st
from PIL import Image

from dashboard.tools.configuration import DashboardConfiguration


def create(dash_cfg: DashboardConfiguration):
    if st.session_state["style"] == "dark":
        logo = Image.open("data/column-chart-line-icon-black.png")
        logo = logo.resize((150, 100))

        st.image(logo, output_format="png")
    elif st.session_state["style"] == "light":
        logo = Image.open("data/column-chart-line-icon-white.png")
        logo = logo.resize((150, 100))

        st.image(logo, output_format="png")
    st.header(dash_cfg.dashboard_label)
