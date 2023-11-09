
import streamlit as st
from dashboard.tools import update_options_with_defaults
from streamlit_echarts import st_echarts
from dashboard.plots import heatmaps
import random
import pandas as pd


idx = pd.IndexSlice


def create(data, metadata, cfg):
    data = data["SingleKey"]
    metadata = metadata["SingleKey"]
    heat_options = heatmaps.heatmap(data, metadata)
    st_echarts(heat_options)
