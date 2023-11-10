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

    # data = data['Line/SingleKey']
    # metadata = metadata['Line/SingleKey']
    data = data['Line/TwoKey']
    metadata = metadata['Line/TwoKey']
    print(metadata)

    data = data.reset_index()




    data = data[["StoredEnergy_Austria", "StoredEnergy_Germany"]].values

    
    st.subheader("test plots")
    navbar, plotarea = st.columns([0.2, 0.8])

    with navbar:
        st.write("this is a nav bar")

        st.selectbox(
            options=data['Region'].unique()
        )

    with plotarea:

        options = scatterplot(data, metadata)

        # chart_container(pd.DataFrame(data), tabs=["Export"])
        # options = {
        #     "xAxis": {},
        #     "yAxis": {},
        #     "series": {
        #         "symbolSize": 10,
        #         "data": data.tolist(),
        #         "type": "scatter",
        #     },
        # }
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
