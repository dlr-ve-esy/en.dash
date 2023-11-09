
import streamlit as st
from dashboard.tools import update_options_with_defaults, update_options_with_user_overrides
from streamlit_echarts import st_echarts
from dashboard.plots import lines
import random
import pandas as pd


idx = pd.IndexSlice


def create(data, metadata, cfg):
    st.header("tab 4")

    config = {"selector" : "Region", "stacker": "Technology", "xaxis": "TimeStamp", "value": "AwardedPower"}
    radio_option = st.radio(
        label="Select country",
        options=data.index.get_level_values(config["selector"]).unique().tolist(),
        key="tab4radio"
    )

    df = pd.pivot_table(
        data.xs(radio_option, level=config["selector"]),
        columns=config["stacker"],
        index=config["xaxis"],
        values=config["value"]
    ).dropna(how="any", axis=0)

    plotoptions = {
        "yAxis": [{
            "name": f'{metadata[config["value"]]["label"]} in {metadata[config["value"]]["unit"]}',
            "nameLocation": "middle",
            "nameGap": 50
        }]
    }

    line_options = lines.stacked_area(
        df,
        metadata
    )
    line_options = update_options_with_defaults(line_options)
    line_options = update_options_with_user_overrides(line_options, plotoptions)
    st_echarts(line_options)
