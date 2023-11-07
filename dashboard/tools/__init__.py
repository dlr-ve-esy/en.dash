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
        "toolbox": {
            "feature": {
                # "mark": {"show": True},
                # "dataView": {"show": True, "readOnly": False},
                # "restore": {"show": True},
                "saveAsImage": {"show": True},
            },
        },
    }
    return __update(options, defaults)
