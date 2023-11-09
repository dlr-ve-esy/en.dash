
import streamlit as st
from dashboard.tools import update_options_with_defaults
from streamlit_echarts import st_echarts
from dashboard.plots import heatmaps
import random
import pandas as pd


idx = pd.IndexSlice


def create(data, metadata, cfg):
    data = data["SingleKey"]
    metadata = metadata["SingleKey"]

    select = st.selectbox(
        label="Select storage level to display",
        options=["Germany", "Austria"]
    )

    if select == "Germany":
        select = "StoredEnergy_Germany"
    else:
        select = "StoredEnergy_Austria"

    df = data.loc[:, select].round(2)

    heat_options = heatmaps.heatmap(df, metadata)
    st_echarts(heat_options)
