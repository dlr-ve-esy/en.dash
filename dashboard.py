# SPDX-FileCopyrightText: 2023 German Aerospace Center
# SPDX-License-Identifier: CC-BY-4.0


import streamlit as st
import pandas as pd
from bokeh.plotting import figure


def load_data() -> pd.DataFrame:

    df = pd.read_csv("data/Mark_Ie_Daten.csv", index_col=0, header=0)
    return df


df = load_data()


st.write(df)
st.line_chart(df, x=None, y="unemployment")
option = st.selectbox(
    label="Parameter",
    options=df.columns
)

p = figure(
    title='unemployment over model iterations',
    x_axis_label='model iteration',
    y_axis_label='unemployment rate'
)
p.line(df.index, df[option], legend_label='Trend', line_width=2)
st.bokeh_chart(p, use_container_width=True)
