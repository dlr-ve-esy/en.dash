import streamlit as st
from streamlit.components import v1 as components
from pyecharts import charts
import json


def create(data, metadata, cfg):
    c = charts.chart.Chart3D()

    c.options["backgroundColor"] = '#000'
    c.options["globe"] = {
      "baseTexture": '/app/static/data/world.topo.bathy.200401.jpg',
      "heightTexture": '/app/static/data/world.topo.bathy.200401.jpg',
      "shading": 'lambert',
      "environment": '/app/static/data/starfield.jpg',
      "light": {
        "ambient": {
          "intensity": 0.5
        },
        "main": {
            "intensity": 0.1
        }
      },
      "viewControl": {
        "autoRotate": False
      },
    }
    data = json.load(open('./data/lines.geojson', encoding="utf-8"))

    routes = [i['geometry']['coordinates']  for i in data['features']]

    c.options["series"] = [
      {"type": 'lines3D',
        "coordinateSystem": 'globe',
        "blendMode": 'lighter',
        "lineStyle": {
          "width": 2,
          "color": "#3399ff",
          "opacity": 0.5
        },
        "data": routes,
        "globeIndex": 0,
        "geo3DIndex": 0,
        "zlevel": -10,
        "polyline": False,
        "silent": True,
        "effect": {
            "show": False,
            "period": 4,
            "trailWidth": 4,
            "trailLength": 0.2,
            "spotIntensity": 6,
        }
      }
    ]
  
    components.html(c.render_embed(), height=1000)
