def scatterplot(data, metadata):
    options = {
        "xAxis": {},
        "yAxis": {},
        "series": {
            "symbolSize": 10,
            "data": data.tolist(),
            "type": "scatter",
        },
    }
    return options