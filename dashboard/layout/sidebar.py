import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from dashboard.tools.configuration import DashboardConfiguration


def create_default_sidebar(dash_cfg: DashboardConfiguration):
    if st.session_state["style"] == "dark":
        logo = Image.open("data/column-chart-line-icon-white.png")
        logo = logo.resize((150, 100))

        st.image(logo, output_format="png")
    elif st.session_state["style"] == "light":
        logo = Image.open("data/column-chart-line-icon-black.png")
        logo = logo.resize((150, 100))

        st.image(logo, output_format="png")

    selected = option_menu(
        dash_cfg.dashboard_label,
        [i.label for i in dash_cfg.tabs],
        icons=[i.icon for i in dash_cfg.tabs],  # bootstrap icons
        menu_icon=dash_cfg.sidemenu_icon,
        default_index=1,
    )

    for i in dash_cfg.tabs:
        if i.label == selected:
            st.session_state["active_tab"] = i.id

    with st.expander("Options"):
        if dash_cfg.enable_darkmode_toggle:
            darkmode_enabled = st.toggle("enable dark mode for plots")
        else:
            darkmode_enabled = False

        if darkmode_enabled:
            st.session_state["style"] = "dark"
        else:
            st.session_state["style"] = "light"
