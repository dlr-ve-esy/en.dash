import streamlit as st
from streamlit_echarts import st_echarts, JsCode
from dashboard.tools import (
    update_options_with_defaults,
    delete_barred_user_overrides,
    update_options_with_user_overrides,
)
import numpy as np
from streamlit_extras.chart_container import chart_container
import pandas as pd


def create(data, metadata, plots_cfg):
    data = data["dataset1"]
    metadata = metadata["dataset1"]

    st.subheader("test plots")
    navbar, plotarea = st.columns([0.2, 0.8])

    with navbar:
        st.write("this is a nav bar")

    with plotarea:
        chart_container(pd.DataFrame(data), tabs=["Export"])
        options = {
            "title": {
                "text": "scattering the scatters",
                "left": "center",
                "textStyle": {
                    "color": "#999",
                    "fontWeight": "normal",
                    "fontSize": 14,
                },
            },
            "tooltip": {"position": "top"},
            "visualMap": {
                "min": 0,
                "max": 1000,
                "text": ["high", "low"],
                "realtime": True,
                "calculable": True,
                "left": "2px",
                "top": "20px",
            },
            "grid": {"left": "200px"},
            "xAxis": {},
            "yAxis": {},
            "series": {
                # "symbolSize": JsCode("function (val) { return val[1] * 0.01;}").js_code,
                "symbolSize": 10,
                "data": data.T.tolist(),
                "type": "scatter",
                "encode": {"tooltip": [0, 1]},
            },
        }
        user = delete_barred_user_overrides(
            plots_cfg["experimental_plot"],
            {
                "xAxis": None,
                "yAxis": None,
            },
        )
        options = update_options_with_user_overrides(options, user)
        options = update_options_with_defaults(options)

        st_echarts(
            options=options,
            theme="dark",
            height="500px",
            width="700px",
        )
