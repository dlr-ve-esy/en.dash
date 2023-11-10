import streamlit as st

from dashboard.plots.barplots import barplot_simple, barplot_grouped, barplot_stacked, barplot_grouped_stacked
from dashboard.tools import update_options_with_defaults, update_options_with_user_overrides
from streamlit_echarts import st_echarts
from streamlit_extras.chart_container import chart_container

import pandas as pd


def create(data, metadata, cfg):
    data = data['inst_power']
    metadata = metadata['inst_power']
    cfg = cfg['installed_power_plot']

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

        y_value = 'InstalledPower'
        foptions_x = list(data.reset_index(drop=True).columns)
        foptions_x = [item for item in foptions_x if item != y_value]
        fval_x = st.selectbox(
            label='x-axis',
            options=foptions_x
        )

        foptions_g = [item for item in foptions_x if item != fval_x]
        foptions_g_all = ['None'] + foptions_g
        fval_g = st.selectbox(
            label='grouped',
            options=foptions_g_all
        )

        foptions_s = [item for item in foptions_g if item != fval_g]
        foptions_s_all = ['None'] + foptions_s
        fval_s = st.selectbox(
            label='stacked',
            options=foptions_s_all
        )

        f_options_rest = [item for item in foptions_s if item != fval_s]

        if fval_g == 'None' and fval_s == 'None':
            plot_type = 'simple'
        elif fval_g != 'None' and fval_s == 'None':
            plot_type = 'grouped'
        elif fval_g == 'None' and fval_s != 'None':
            plot_type = 'stacked'
        elif fval_g != 'None' and fval_s != 'None':
            plot_type = 'grouped & stacked'

        config_plot = {
            'x': fval_x,
            'y': y_value,
            'filters': f_options_rest,
            'groups': fval_g,
            'stacks': fval_s,
        }

        if config_plot['filters']:
            st.write("Data filters")

        if plot_type == 'simple':
            data_plot = data.reset_index()
            filters_value = add_filters(config_plot, data_plot)
            for filter, value in filters_value.items():
                con = data_plot[filter] == value
                data_plot = data_plot.loc[con]
            data_plot = data_plot[[config_plot['x'], config_plot['y']]]
            plot_class = barplot_simple

        elif plot_type == 'grouped':
            data_plot = data.reset_index()
            filters_value = add_filters(config_plot, data_plot)
            for filter, value in filters_value.items():
                con = data_plot[filter] == value
                data_plot = data_plot.loc[con]
            data_plot = data_plot[[config_plot['x'], config_plot['y'], config_plot['groups']]]
            plot_class = barplot_grouped

        elif plot_type == 'stacked':
            data_plot = data.reset_index()
            filters_value = add_filters(config_plot, data_plot)
            for filter, value in filters_value.items():
                con = data_plot[filter] == value
                data_plot = data_plot.loc[con]
            data_plot = data_plot[[config_plot['x'], config_plot['y'], config_plot['stacks']]]
            plot_class = barplot_stacked

        elif plot_type == 'grouped & stacked':
            data_plot = data.reset_index()
            filters_value = add_filters(config_plot, data_plot)
            for filter, value in filters_value.items():
                con = data_plot[filter] == value
                data_plot = data_plot.loc[con]
            data_plot = data_plot[[config_plot['x'], config_plot['y'], config_plot['groups'], config_plot['stacks']]]
            plot_class = barplot_grouped_stacked

    with plotarea:
        with chart_container(pd.DataFrame(data)):
            options = plot_class(data_plot, metadata)
            options_update = {
                'yAxis': {
                    'name': f'{metadata[config_plot["y"]]["label"]} in {metadata[config_plot["y"]]["unit"]}'
                }
            }
            options = update_options_with_user_overrides(options, options_update)
            options = update_options_with_user_overrides(options, cfg)
            options = update_options_with_defaults(options)

            if plot_type != 'simple':
                for series_item in options['series']:
                    insert = {
                        # 'label': {
                        #     'show': True,
                        #     'align': 'right',
                        #     'position': 'bottom',
                        #     'rotate': 90,
                        #     'verticalAlign': 'middle',
                        #     'formatter': '{a}',
                        # }
                        # 'stackLabel': {
                        #     'show': True,
                        #     'align': 'right',
                        #     'position': 'bottom',
                        #     'rotate': 90,
                        #     'verticalAlign': 'middle',
                        #     'formatter': '{a}',
                        # }
                    }
                    series_item.update(insert)

            st_echarts(options=options, height="500px")
 


