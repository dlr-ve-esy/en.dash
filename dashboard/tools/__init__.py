import streamlit as st
import collections.abc


def update_options_with_defaults(options):
    defaults = {
        "backgroundColor": "#FFFFFF"
        if st.session_state["style"] != "dark"
        else "#0E1117",
    }
    for k, v in defaults.items():
        if isinstance(v, collections.abc.Mapping):
            options[k] = update_options_with_defaults(options.get(k, {}), v)
        else:
            options[k] = v
    return options
