import streamlit as st
from streamlit_echarts import st_echarts
from tools import update_options_with_defaults


def create(data):
    options = {
        "title": {
            "text": "the name of the game is quarks",
            "left": "center",
            "textStyle": {
                "color": "#999",
                "fontWeight": "normal",
                "fontSize": 14,
            },
        },
        "series": [
            {
                "name": "test 1",
                "type": "pie",
                "radius": "30%",
                "left": "0%",
                "right": "40%",
                "top": "0%",
                "bottom": "0%",
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
                "data": [
                    {"name": "charm", "value": 5.6},
                    {"name": "top", "value": 1},
                    {"name": "down", "value": 0.8},
                    {"name": "bottom", "value": 0.5},
                    {"name": "up", "value": 0.5},
                    {"name": "strange", "value": 3.8},
                ],
            },
            {
                "name": "test 2",
                "type": "pie",
                "radius": "30%",
                "left": "40%",
                "right": "0%",
                "top": "0%",
                "bottom": "0%",
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
                "data": [
                    {"name": "charm1", "value": 5.6},
                    {"name": "top2", "value": 1},
                    {"name": "down3", "value": 0.8},
                    {"name": "bottom4", "value": 0.5},
                    {"name": "up5", "value": 0.5},
                    {"name": "strange6", "value": 3.8},
                ],
            },
        ],
    }
    options = update_options_with_defaults(options)
    st_echarts(
        options=options,
        height="400px",
    )
