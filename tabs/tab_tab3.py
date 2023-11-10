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

from dashboard.plots.scatterplots import scatterplot


def create(data, metadata, plots_cfg):
    # strompreis vs. last (awardedpower)

    data = data['Line/TwoKey']
    metadata = metadata['Line/TwoKey']

    data = data.reset_index()

    navbar, plotarea = st.columns([0.2, 0.8])

    with navbar:
        selected_region = st.selectbox(
            label='Region Selection',
            options=data['Region'].unique()
        )

        xaxis_options = ['ElectricityPrice', 'AwardedEnergy', 'Shortage', 'StoredEnergy']
        selected_x = st.selectbox(
            label='X-Axis',
            options=xaxis_options
        )

        yaxis_options = [item for item in xaxis_options if item != selected_x]
        selected_y = st.selectbox(
            label='Y-Axis',
            options=yaxis_options
        )

        data = data.loc[data['Region'] == selected_region][[selected_x, selected_y]].values
        # data = data.set_index(selected_x, drop=True)

    with plotarea:
        options = scatterplot(data, metadata)

        user = delete_barred_user_overrides(
            plots_cfg["scatterplot"],
            {
                "xAxis": None,
                "yAxis": None,
            },
        )

        options = update_options_with_user_overrides(options, user)
        options = update_options_with_defaults(options)

        options_update = {
                'yAxis': {
                    'name': f'{metadata[selected_y]["label"]} in {metadata[selected_y]["unit"]}'
                },
                'xAxis': {
                    'name': f'{metadata[selected_x]["label"]} in {metadata[selected_x]["unit"]}'
                }
            }
        options = update_options_with_user_overrides(options, options_update)

        st_echarts(
            options=options,
            theme="dark",
            height="500px",
            width="700px",
        )