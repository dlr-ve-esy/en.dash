# SPDX-FileCopyrightText: 2023 German Aerospace Center
# SPDX-License-Identifier: CC-BY-4.0


import streamlit as st
import pandas as pd
from bokeh.plotting import figure


def load_data() -> pd.DataFrame:

    df = pd.read_csv("data/Mark_Ie_Daten.csv", index_col=0, header=0)
    return df


df = load_data()


option = st.selectbox(
    label="Parameter",
    options=df.columns
)
options = [option, "gdp"]

p = figure(
    title=f'{option} over model iterations',
    x_axis_label='model iteration',
    y_axis_label=option
)
[p.line(df.index, df[o], legend_label=o, line_width=2) for o in options]
# p.line(df.index, df[option], legend_label='Trend', line_width=2)
st.bokeh_chart(p, use_container_width=True)
