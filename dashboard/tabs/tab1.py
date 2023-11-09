import streamlit as st

from ..plots.barplots import BarplotSimple, BarplotGrouped, BarplotStacked
from dashboard.tools import update_options_with_defaults
from streamlit_echarts import st_echarts

import pandas as pd



def create(data, metadata):
    print(data)
    print(metadata)

    def add_filters(config, data):
        filters_value = dict()
        for filter in config['filters']:
            print(filter)
            filters_value[filter] = st.selectbox(
                label=filter,
                options=list(data[filter].unique())
            )
        return filters_value
    
    plot_type = st.selectbox(
        label='Plot type',
        options=['simple', 'grouped', 'stacked', 'grouped & stacked'],
    )

    # plot_type = 'grouped'
    if plot_type == 'simple':
        config_plot = {
            'x': 'Year',
            'y': 'InstalledPower',
            'filters': ['Technology', 'Region']
        }
        data_plot = data.reset_index()
        filters_value = add_filters(config_plot, data_plot)
        for filter, value in filters_value.items():
            con = data_plot[filter] == value
            data_plot = data_plot.loc[con]
        data_plot = data_plot[[config_plot['x'], config_plot['y']]]
        data_plot.columns = ['x', 'y']
        s = BarplotSimple(data_plot)
        options = s.build_options()
    elif plot_type == 'grouped':
        config_plot = {
            'x': 'Year',
            'y': 'InstalledPower',
            'filters': ['Region'],
            'groups': 'Technology'
        }
        data_plot = data.reset_index()
        filters_value = add_filters(config_plot, data_plot)
        for filter, value in filters_value.items():
            con = data_plot[filter] == value
            data_plot = data_plot.loc[con]
        data_plot = data_plot[[config_plot['x'], config_plot['y'], config_plot['groups']]]
        data_plot.columns = ['x', 'y', 'groups']
        s = BarplotGrouped(data_plot)
        options = s.build_options()
    elif plot_type == 'stacked':
        config_plot = {
            'x': 'Year',
            'y': 'InstalledPower',
            'filters': ['Region'],
            'stacks': 'Technology'
        }
        data_plot = data.reset_index()
        filters_value = add_filters(config_plot, data_plot)
        for filter, value in filters_value.items():
            con = data_plot[filter] == value
            data_plot = data_plot.loc[con]
        data_plot = data_plot[[config_plot['x'], config_plot['y'], config_plot['stacks']]]
        data_plot.columns = ['x', 'y', 'stacks']
        s = BarplotStacked(data_plot)
        options = s.build_options()
    elif plot_type == 'grouped & stacked':
        config_plot = {
            'x': 'Year',
            'y': 'InstalledPower',
            'groups': 'Region',
            'stacks': 'Technology'
        }
        data_plot = data.reset_index()
        filters_value = add_filters(config_plot, data_plot)
        for filter, value in filters_value.items():
            con = data_plot[filter] == value
            data_plot = data_plot.loc[con]
        data_plot = data_plot[[config_plot['x'], config_plot['y'], config_plot['stacks']]]
        data_plot.columns = ['x', 'y', 'stacks']
        s = BarplotStacked(data_plot)
        options = s.build_options()
    else:
        options = {}

    st.header('Installable Capacities')

    options = update_options_with_defaults(options)
    st_echarts(options=options, height="400px")


