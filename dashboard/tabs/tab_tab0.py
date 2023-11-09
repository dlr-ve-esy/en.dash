import streamlit as st
from dashboard.tools import update_options_with_defaults
from streamlit_echarts import st_echarts
from dashboard.plots import lines
import random


def create(data, metadata, cfg):
    data = data["SingleKey"]
    metadata = metadata["SingleKey"]

    st.header("tab 0")

    radio_option = st.radio(
        label="Select time series to display",
        options=["Electricity Prices", "Storage Levels"],
    )

    if radio_option == "Electricity Prices":
        col = "ElectricityPrice"
    else:
        col = "StoredEnergy"

    df = data.loc[:, [f"{col}_Germany", f"{col}_Austria"]].round(2)

    line_options = lines.line(
        data=df,
        metadata=metadata,
        # title=radio_option
    )
    line_options = update_options_with_defaults(line_options)
    st_echarts(line_options)
