import streamlit as st
from streamlit.components import v1 as components
from pyecharts import charts


def create(data, metadata, cfg):

    import pyecharts.options as opts
    from pyecharts.charts import MapGlobe
    from pyecharts.faker import POPULATION

    data = [x for _, x in POPULATION[1:]]
    low, high = min(data), max(data)

    c = (
        MapGlobe()
        .add_schema()
        .add(
            maptype="world",
            series_name="World Population",
            data_pair=POPULATION[1:],
            is_map_symbol_show=False,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                min_=low,
                max_=high,
                range_text=["max", "min"],
                is_calculable=True,
                range_color=["lightskyblue", "yellow", "orangered"],
            )
        )
    )
    print(c.options["series"])
    # c.__dict__["options"]["series"] +=
    c.options["series"] += [{"type": "lines3D", "data": [[[0, 0], [10, 10]]], "coordinateSystem": "geo3D"}]
    print(c.render_embed())
    components.html(c.render_embed(), height=1000)

    # c = charts.chart.Chart3D(
    #     # init_opts=opts.InitOpts(bg_color="#000", renderer=opts.RenderOpts(is_embed_js=True))
    # )
    # c.add_globe(
    #     base_texture="/app/static/data/world.topo.bathy.200401.jpg",
    #     displacement_scale=0.2,
    #     shading="realistic",
    #     environment="/app/static/data/starfield.jpg",

    # )
    # components.html(c.render_embed(), height=1000)
