import streamlit as st

from dashboard.plots.barplots import BarplotSimple, BarplotGrouped, BarplotStacked, BarplotGroupedStacked
from dashboard.tools import update_options_with_defaults, update_options_with_user_overrides
from streamlit_echarts import st_echarts
from streamlit_extras.chart_container import chart_container

import pandas as pd



def create(data, metadata):
    print(data)
    print(metadata)

    def add_filters(config, data):
        filters_value = dict()
        if 'filters' in config:
            for filter in config['filters']:
                filters_value[filter] = st.selectbox(
                    label=filter,
                    options=list(data[filter].unique())
                )
        return filters_value
    
    navbar, plotarea = st.columns([0.2, 0.8])
    with navbar:
        st.write("Plot configuration")
        plot_type = st.selectbox(
            label='Plot type',
            options=['simple', 'grouped', 'stacked', 'grouped & stacked'],
        )

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
            plot_class = BarplotSimple

        elif plot_type == 'grouped':
            config_plot = {
                'filters': ['Region'],
                'x': 'Year',
                'y': 'InstalledPower',
                'groups': 'Technology'
            }
            data_plot = data.reset_index()
            filters_value = add_filters(config_plot, data_plot)
            for filter, value in filters_value.items():
                con = data_plot[filter] == value
                data_plot = data_plot.loc[con]
            data_plot = data_plot[[config_plot['x'], config_plot['y'], config_plot['groups']]]
            plot_class = BarplotGrouped

        elif plot_type == 'stacked':
            config_plot = {
                'filters': ['Region'],
                'x': 'Year',
                'y': 'InstalledPower',
                'stacks': 'Technology'
            }
            data_plot = data.reset_index()
            filters_value = add_filters(config_plot, data_plot)
            for filter, value in filters_value.items():
                con = data_plot[filter] == value
                data_plot = data_plot.loc[con]
            data_plot = data_plot[[config_plot['x'], config_plot['y'], config_plot['stacks']]]
            plot_class = BarplotStacked

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
            data_plot = data_plot[[config_plot['x'], config_plot['y'], config_plot['groups'], config_plot['stacks']]]
            plot_class = BarplotGroupedStacked
        else:
            options = {}

    with plotarea:
        with chart_container(pd.DataFrame(data)):
            plot_obj = plot_class(data_plot, metadata)
            options = plot_obj.build_options()
            options_update = {
                'yAxis': {
                    'name': f'{metadata[config_plot["y"]]["label"]} in {metadata[config_plot["y"]]["unit"]}'
                }
            }
            options = update_options_with_user_overrides(options, options_update)
            options = update_options_with_defaults(options)

            st_echarts(options=options, height="400px")
 


