import streamlit as st
from streamlit_echarts import st_echarts
from streamlit_echarts import JsCode, Map
import json


def create(data, metadata, cfg):
    st.header("A Map")
    formatter = JsCode(
        "function (params) {"
        + "var value = (params.value + '').split('.');"
        + "value = value[0].replace(/(\d{1,3})(?=(?:\d{3})+(?!\d))/g, '$1,');"
        + "return params.seriesName + '<br/>' + params.name + ': ' + value;}"
    ).js_code

    with open("./data/flexmex.geojson", "r", encoding="utf-8") as f:
        map = Map(
            "Europe",
            json.loads(f.read())
        )

    options = {
        "title": {
            "text": "Europe",
            "subtext": None,
            "sublink": None,
            "left": "right",
        },
        "tooltip": {
            "trigger": "item",
            "showDelay": 0,
            "transitionDuration": 0.2,
            "formatter": formatter,
        },
        "visualMap": {
            "left": "right",
            "min": 500000,
            "max": 38000000,
            "inRange": {
                "color": [
                    "#313695",
                    "#4575b4",
                    "#74add1",
                    "#abd9e9",
                    "#e0f3f8",
                    "#ffffbf",
                    "#fee090",
                    "#fdae61",
                    "#f46d43",
                    "#d73027",
                    "#a50026",
                ]
            },
            "text": ["High", "Low"],
            "calculable": True,
        },
        "toolbox": {
            "show": True,
            "left": "left",
            "top": "top",
            "feature": {
                "dataView": {"readOnly": False},
                "restore": {},
                "saveAsImage": {},
            },
        },
        "series": [
            {
                "name": "Capacity Expansion PV",
                "type": "map",
                "roam": True,
                "map": "Europe",
                "emphasis": {"label": {"show": True}},
                "data": [
                    {"name": "France", "value": 4822023},
                    {"name": "Germany", "value": 12312341}
                ],
            }
        ],
    }
    st_echarts(options, map=map)
