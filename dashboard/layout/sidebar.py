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

    st.write(dash_cfg.dashboard_label)
