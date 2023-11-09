import streamlit as st
from dashboard.tools import update_options_with_defaults, update_options_with_user_overrides
from streamlit_echarts import st_echarts
from dashboard.plots import lines


def create(data, metadata, cfg):
    data = data["SingleKey"]
    metadata = metadata["SingleKey"]
    select = st.selectbox(
        label="Select time series to display",
        options=data.columns
    )

    df = data.loc[:, select].round(2)

    line_options = lines.line(
        data=df,
        metadata=metadata,
    )
    line_options = update_options_with_defaults(line_options)
    st_echarts(line_options)

    df = data.round(2)
    line_options = lines.multiline(
        data=df,
        metadata=metadata
    )
    line_options = update_options_with_defaults(line_options)
    st_echarts(line_options)

    df = data.loc[:, ["AwardedEnergy_Germany", "AwardedEnergy_Austria"]]
    line_y_axis_map = {
        "AwardedEnergy_Germany": 0,
        "AwardedEnergy_Austria": 1
    }
    line_options = lines.twolinetwoyaxes(
        data=df,
        metadata=metadata,
        axesmapping=line_y_axis_map
    )
    st_echarts(line_options, height=500)
