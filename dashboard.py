# SPDX-FileCopyrightText: 2023 German Aerospace Center
# SPDX-License-Identifier: CC-BY-4.0


import streamlit as st
import pandas as pd
from bokeh.plotting import figure
from esyplots.layouts.simple import create_layout
from esyplots.plots.line import Line


def load_data() -> pd.DataFrame:

    df = pd.read_csv("data/Mark_Ie_Daten.csv", index_col=0, header=0)
    return df


df = load_data()

my_line = Line(df, title="1")
my_other_line = Line(df, title="2")
elements = [
    {"radio_label": "select1", "radio_options": df.columns, "plotting_function": my_line},
    {"radio_label": "selectanother", "radio_options": [_ for _ in df.columns], "plotting_function": my_other_line}
]
create_layout(elements)
# create_layout("Please select", df.columns, plotting_function=my_line, data=df)
