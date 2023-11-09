import pandas as pd

from dashboard.tools import update_options_with_user_overrides


def _default_line_options():
    return {
        "title": {"text": None},
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"animation": False},
        },
        "axisPointer": {
            "link": [
                {"xAxisIndex": "all"}
            ]
        },
        "dataZoom": [
            {
                "type": 'slider',
                "start": 0,
                "end": 1,
                "xAxisIndex": 0,
                "zoomLock": True
            }
        ],
    }


def line(data, metadata):
    if not isinstance(data, pd.Series):
        msg = "Line function takes a series only!"
        raise TypeError(msg)

    label = metadata[data.name]["label"]
    unit = metadata[data.name]["unit"]
    options = {
        "legend": {"data": [metadata[data.name]["label"]]},
        "xAxis": {
            "type": "category",
            "data": data.index.tolist(),
        },
        "yAxis": {
            "type": "value",
            "name": f"{label} in {unit}",
            "nameLocation": "middle",
            "nameGap": 75
        },
        "series": [{
                "data": data.tolist(),
                "type": "line",
                "name": metadata[data.name]["label"]
            }
        ],
    }
    return update_options_with_user_overrides(_default_line_options(), options)


def  multiline(data, metadata):
    options = {
        "legend": {"data": [metadata[col]["label"] for col in metadata]},
        "xAxis": {
            "type": "category",
            "data": data.index.tolist(),
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": data[col].tolist(), "type": "line", "name": metadata[col]["label"]}
            for col in data.columns
        ],
    }
    return update_options_with_user_overrides(_default_line_options(), options)


def twolinetwoyaxes(data, metadata, axesmapping):
    options = {
        "legend": {"data": [metadata[col]["label"] for col in axesmapping]},
        "dataZoom": [
            {
                "show": True,
                "realtime": True,
                "start": 1,
                "end": 2,
                "xAxisIndex": [0, 1]
            },
            {
                "type": 'inside',
                "realtime": True,
                "start": 1,
                "end": 2,
                "xAxisIndex": [0, 1]
            }
        ],
        "grid": [
            {
                "left": 60,
                "right": 50,
                "height": '35%'
            },
            {
                "left": 60,
                "right": 50,
                "top": '55%',
                "height": '35%'
            }
        ],
        "xAxis": [
            {
                "type": 'category',
                "boundaryGap": False,
                "axisLine": { "onZero": True },
                "data": data.index.tolist()
            },
            {
                "gridIndex": 1,
                "type": 'category',
                "boundaryGap": False,
                "axisLine": { "onZero": True },
                "data": data.index.tolist(),
            }
        ],
        "yAxis": [
            {
                "gridindex": yaxisindex,
                "name": metadata[col]["label"],
                "type": 'value',
                "axisTick": True if yaxisindex == 1 else False
            } for col, yaxisindex in axesmapping.items()
        ],
        "series": [
            {
            "name": metadata[col]["label"],
            "type": 'line',
            "symbolSize": 8,
            "xAxisIndex": axesmapping[col],
            "yAxisIndex": axesmapping[col],
            "data": data[col].tolist()
            } for col in axesmapping
        ]
    }
    return update_options_with_user_overrides(_default_line_options(), options)



def stacked_area(data, metadata):
    datazoom = {
    "dataZoom": [
        {
            "type": 'slider',
            "start": 25,
            "end": 75,
            "xAxisIndex": 0,
            "zoomLock": True
        }
    ]
    }
    options = {
        "title": {"text": ""},
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"animation": False},
        },
        "legend": {"data": [col for col in data.columns]},
        "toolbox": {"feature": {
            "dataZoom": {
                "yAxisIndex": 'none'
            },
            "restore": {},
            "saveAsImage": {}
        }},
        "axisPointer": {
        "link": [
            {
            "xAxisIndex": 'all'
            }
        ]
        },
        "grid": {"left": "3%", "right": "4%", "bottom": "15%", "containLabel": True},
        "xAxis": [
            {
                "type": "category",
                "boundaryGap": True,
                "axisLine": {"onZero": True},
                "data": data.index.tolist(),
            }
        ],
        "yAxis": [{"type": "value"}],
        "series": [
            {
                "data": data[col].tolist(),
                "type": "line",
                "name": col,
                "stack": "stack0",
                "areaStyle": {},
                "emphasis": {"focus": "series"}
            }
            for col in data.columns
        ],
    }
    options["dataZoom"] = datazoom["dataZoom"]
    return options
