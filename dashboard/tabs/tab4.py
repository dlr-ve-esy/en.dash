
import streamlit as st
from dashboard.tools import update_options_with_defaults
from streamlit_echarts import st_echarts
from dashboard.plots import lines
import random
import pandas as pd


idx = pd.IndexSlice


def create(data):
    st.header("tab 4")

    radio_option = st.radio(
        label="Select country",
        options=data.index.get_level_values("Region").unique().tolist(),
        key="tab4radio"
    )

    df = pd.pivot_table(
        data.loc[idx[radio_option, :, :]],
        columns="Technology",
        index="TimeStep",
        values="AwardedPower"
    ).dropna(how="any", axis=0)

    line_options = lines.stacked_area(
        df.index.tolist(),
        *[df[col].tolist() for col in df.columns],
        # title=radio_option
    )
    line_options = update_options_with_defaults(line_options)
    st_echarts(line_options)
