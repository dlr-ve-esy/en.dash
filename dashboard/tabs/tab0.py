import streamlit as st
from dashboard.tools import update_options_with_defaults
from streamlit_echarts import st_echarts
from dashboard.plots import lines

def create(data):
    st.header("tab 0")

    line_options = lines.stacked_area(data)

    st_echarts(line_options)
