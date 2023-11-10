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

        d_label_key = dict()

        xaxis_options = ['ElectricityPrice', 'AwardedEnergy', 'Shortage', 'StoredEnergy']
        for xaxis_option in xaxis_options:
            xaxis_option_label = metadata[xaxis_option]['label']
            d_label_key[xaxis_option_label] = xaxis_option

        xaxis_options = d_label_key.keys()
        selected_x_label = st.selectbox(
            label='X-Axis',
            options=xaxis_options
        )
        selected_x = d_label_key[selected_x_label]

        yaxis_options = [item for item in xaxis_options if item != selected_x_label]
        selected_y_label = st.selectbox(
            label='Y-Axis',
            options=yaxis_options
        )
        selected_y = d_label_key[selected_y_label]

        data = data.loc[data['Region'] == selected_region][[selected_x, selected_y]].values

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