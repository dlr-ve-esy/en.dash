def line(data, metadata, title=""):
    options = {
        "title": {"text": title},
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"animation": False},
        },
        "legend": {"data": [metadata[col]["label"] for col in metadata]},
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
    return options


def stacked_area(x, *y):
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
        "title": {"text": "堆叠区域图"},
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"animation": False},
        },
        "legend": {"data": ["邮件营销", "联盟广告", "视频广告", "直接访问", "搜索引擎"]},
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
                "boundaryGap": False,
                "axisLine": {"onZero": True},
                "data": x,
            }
        ],
        "yAxis": [{"type": "value"}],
        "series": [
            {
                "name": "邮件营销",
                "type": "line",
                "stack": "1",
                "areaStyle": {},
                "emphasis": {"focus": "series"},
                "data": _y,
            } for _y in y
        ],
    }
    options["dataZoom"] = datazoom["dataZoom"]
    return options
