import streamlit as st
import numpy as np
import pathlib as pt
from dashboard.tabs import tab0, tab1, tab2, tab3
from dashboard.layout import sidebar

from dashboard.tools import update_options_with_defaults
from streamlit_echarts import st_echarts
from streamlit_extras.chart_container import chart_container
import pandas as pd

from streamlit_extras.switch_page_button import switch_page


def load_data(path: pt.Path) -> dict:
    # with zipfile.ZipFile(path.as_posix()) as zf:
    #     data = pd.read_csv(io.BytesIO(zf.read("Mark_Ie_Daten.csv")))

    return {"dataset1": np.random.randint(1, 999, (2, 100))}


if __name__ == "__main__":
    if "style" not in st.session_state:
        st.session_state["style"] = "dark"

    tab_names = ["tab0", "tab1", "tab2", "tab3"]

    st.set_page_config(page_title="sfc dashboard", layout="wide")

    data = load_data(pt.Path("./Mark_Ie_Daten.zip"))

    with st.sidebar:
        sidebar.create()

    root = st.container()

    if "active_tab" not in st.session_state:
        st.session_state["active_tab"] = tab_names[0]

    with root:
        with st.sidebar:
            st.session_state["active_tab"] = st.radio(
                label="select view", options=tab_names
            )

        if st.session_state["active_tab"] == tab_names[0]:
            tab0.create(data)
        if st.session_state["active_tab"] == tab_names[1]:
            tab1.create(data)
        if st.session_state["active_tab"] == tab_names[2]:
            tab2.create(data)
        if st.session_state["active_tab"] == tab_names[3]:
            tab3.create(data["dataset1"])

        # tabs = st.tabs(["tab0", "tab1", "tab2", "tab3"])

        # with tabs[0]:
        #     tab0.create(data)
        # with tabs[1]:
        #     tab1.create(data)
        # with tabs[2]:
        #     tab2.create(data)
        # with tabs[3]:
        #     tab3.create(data["dataset1"])

    # if "rerun" not in st.session_state:
    #     st.session_state["rerun"] = True

    # if st.session_state["rerun"]:
    #     st.session_state["rerun"] = False
    #     st.rerun()

    # if want_to_contribute:
    #     with chart_container(pd.DataFrame(data["dataset1"])):
    #         options = {
    #             "title": {
    #                 "text": "scattering the scatters",
    #                 "left": "center",
    #                 "textStyle": {
    #                     "color": "#999",
    #                     "fontWeight": "normal",
    #                     "fontSize": 14,
    #                 },
    #             },
    #             "tooltip": {"position": "top"},
    #             "visualMap": {
    #                 "min": 0,
    #                 "max": 1000,
    #                 "text": ["high", "low"],
    #                 "realtime": True,
    #                 "calculable": True,
    #                 "left": "2px",
    #                 "top": "20px",
    #             },
    #             "grid": {"left": "200px"},
    #             "xAxis": {},
    #             "yAxis": {},
    #             "series": {
    #                 # "symbolSize": JsCode("function (val) { return val[1] * 0.01;}").js_code,
    #                 "symbolSize": 10,
    #                 "data": data["dataset1"].T.tolist(),
    #                 "type": "scatter",
    #                 "encode": {"tooltip": [0, 1]},
    #             },
    #         }
    #         options = update_options_with_defaults(options)
    #         st_echarts(
    #             options=options,
    #             theme="dark",
    #             height="500px",
    #             width="700px",
    #             key="test",
    #         )
