import streamlit as st
import collections.abc


def __update(org, up):
    for k, v in up.items():
        if isinstance(v, collections.abc.Mapping):
            org[k] = __update(org.get(k, {}), v)
        else:
            org[k] = v
    return org


def update_options_with_defaults(options):
    defaults = {
        "backgroundColor": "#FFFFFF"
        if st.session_state["style"] != "dark"
        else "#0E1117",
        "feature": {
            "mark": {"show": "true"},
            "dataView": {"show": "true", "readOnly": "false"},
            "magicType": {"show": "true", "type": ["line", "bar"]},
            "restore": {"show": "true"},
            "saveAsImage": {"show": "true"},
        },
    }
    return __update(options, defaults)
