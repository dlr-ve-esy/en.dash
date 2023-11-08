import random
import pandas as pd


def heatmap(data, metadata):


    hours = [f"{i:0>2}" for i in range(24)]
    days = list(range(1, 365))

    data["_datetime"] = pd.to_datetime(data.index)
    col = "StoredEnergy_Austria"
    df = data[["_datetime", col]].groupby(
        [data["_datetime"].dt.dayofyear, data["_datetime"].dt.hour]
    )[col].sum()
    df.index.names = ["day", "hour"]
    lower_bound = df.min()
    upper_bound = df.max()
    df = df.reset_index()
    df["day"] = df["day"].astype(int)
    df["hour"] = df["hour"].astype(int)
    data = df.values.tolist()

    # data = [[d, hours.index(h), random.randint(1, 10)] for d in days for h in hours]

    option = {
    "tooltip": {
        "position": 'top'
    },
    "grid": {
        "height": '50%',
        "top": '10%'
    },
    "yAxis": {
        "type": 'category',
        "data": hours,
        "splitArea": {
        "show": True
        }
    },
    "xAxis": {
        "type": 'category',
        "data": days,
        "splitArea": {
        "show": True
        }
    },
    "visualMap": {
        "min": lower_bound,
        "max": upper_bound,
        "calculable": True,
        "orient": 'horizontal',
        "left": 'center',
        "bottom": '15%'
    },
    "series": [
        {
        "name": 'Punch Card',
        "type": 'heatmap',
        "data": data,
        "label": {
            "show": False
        },
        "emphasis": {
            "itemStyle": {
            "shadowBlur": 10,
            "shadowColor": 'rgba(0, 0, 0, 0.5)'
            }
        }
        }
    ]
    }

    return option