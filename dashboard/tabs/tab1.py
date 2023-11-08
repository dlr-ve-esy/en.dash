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
    
    plot_type = st.multiselect(
        label='Plot type',
        options=['simple', 'grouped', 'staced']
    )

    if plot_type == 'simple':
        pass
    elif plot_type == 'grouped':
        pass
    elif plot_type == 'stacked':
        pass

    
    # data_plot1 = data['data1']
    # config_barplot1 = {
    #     'title': 'Installable Capacities',
    #     'x': 'Year',
    #     'y': 'InstalledPower',
    #     'filters': ['Technology', 'Region']
    # }
    # st.header(config_barplot1['title'])
    # filters_value_plot1 = add_filters(config_barplot1, data_plot1)
    # for filter, value in filters_value_plot1.items():
    #     con = data_plot1[filter] == value
    #     data_plot1 = data_plot1.loc[con]
    # data_plot1 = data_plot1[[config_barplot1['x'], config_barplot1['y']]]
    # data_plot1.columns = ['x', 'y']
    # s = BarplotSimple(data_plot1)
    # options = s.gen_options()
    # options = update_options_with_defaults(options)
    # st_echarts(options=options, height="400px")

    # data_plot2 = data['data2']
    # config_barplot2 = {
    #     'title': 'Installable Capacities',
    #     'x': 'Year',
    #     'y': 'InstalledPower',
    #     'filters': ['Region'],
    #     'group': 'Technology'
    # }
    # st.header(config_barplot2['title'])
    # filters_value_plot2 = add_filters(config_barplot2, data_plot2)
    # for filter, value in filters_value_plot2.items():
    #     con = data_plot2[filter] == value
    #     data_plot2 = data_plot2.loc[con]
    # data_plot2 = data_plot2[[config_barplot2['x'], config_barplot2['y'], config_barplot2['stack']]]
    # data_plot2.columns = ['x', 'y', 'stack']
    # s = BarplotGrouped(data_plot2)
    # options = s.gen_options()
    # options = update_options_with_defaults(options)
    # st_echarts(options=options, height="400px")

    # data_plot2 = data['data3']
    # config_barplot2 = {
    #     'title': 'Installable Capacities',
    #     'x': 'Year',
    #     'y': 'InstalledPower',
    #     'filters': ['Region', 'Technology'],
    #     'stack': 'Technology'
    # }
    # st.header(config_barplot2['title'])
    # filters_value_plot2 = add_filters(config_barplot2, data_plot2)
    # for filter, value in filters_value_plot2.items():
    #     con = data_plot2[filter] == value
    #     data_plot2 = data_plot2.loc[con]
    # data_plot2 = data_plot2[[config_barplot2['x'], config_barplot2['y'], config_barplot2['stack']]]
    # data_plot2.columns = ['x', 'y', 'groups']
    # s = BarplotGrouped(data_plot2)
    # options = s.gen_options()
    # options = update_options_with_defaults(options)
    # st_echarts(options=options, height="400px")

    # st.multiselect()

    # data_plot = data.reset_index()
    # config_barplot = {
    #     'title': 'Installable Capacities',
    #     'x': 'Year',
    #     'y': 'InstalledPower',
    #     'filters': ['Region'],
    #     'stack': 'Technology'
    # }
    # st.header(config_barplot['title'])
    # filters_value_plot2 = add_filters(config_barplot, data_plot)
    # for filter, value in filters_value_plot2.items():
    #     con = data_plot[filter] == value
    #     data_plot = data_plot.loc[con]
    # data_plot = data_plot[[config_barplot['x'], config_barplot['y'], config_barplot['stack']]]
    # data_plot.columns = ['x', 'y', 'groups']
    # s = BarplotGrouped(data_plot)
    # options = s.gen_options()
    # options = update_options_with_defaults(options)
    # st_echarts(options=options, height="400px")




    data_plot = data.reset_index()
    config_barplot = {
        'title': 'Installable Capacities',
        'x': 'Year',
        'y': 'InstalledPower',
        'filters': ['Region'],
        'stacks': 'Technology'
    }
    st.header(config_barplot['title'])
    filters_value_plot2 = add_filters(config_barplot, data_plot)
    for filter, value in filters_value_plot2.items():
        con = data_plot[filter] == value
        data_plot = data_plot.loc[con]
    data_plot = data_plot[[config_barplot['x'], config_barplot['y'], config_barplot['stacks']]]
    data_plot.columns = ['x', 'y', 'stacks']
    s = BarplotStacked(data_plot)
    options = s.gen_options()
    options = update_options_with_defaults(options)
    st_echarts(options=options, height="400px")


