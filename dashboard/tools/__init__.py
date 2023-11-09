import streamlit as st
import collections.abc
from streamlit_extras.markdownlit import mdlit
import pathlib as pt
import importlib
import pandas as pd


def __update(org, up):
    for k, v in up.items():
        if isinstance(v, collections.abc.Mapping):
            org[k] = __update(org.get(k, {}), v)
        else:
            org[k] = v
    return org


def __delete(org, dels):
    for k, v in dels.items():
        if k not in org:
            continue
        if v is None:
            del org[k]
        if isinstance(v, collections.abc.Mapping):
            org[k] = __delete(org[k])
    return org


def delete_barred_user_overrides(options, deletes=None):
    deletes = deletes if deletes is not None else {}
    options = __delete(options, deletes)
    return options


def update_options_with_user_overrides(options, user):
    return __update(options, user)


def update_options_with_defaults(options):
    defaults = {
        "backgroundColor": "#FFFFFF"
        if st.session_state["style"] != "dark"
        else "#0E1117",
        "toolbox": {
            "orient": "vertical",
            "show": True,
            "feature": {
                "dataView": {"readOnly": False},
                "restore": {},
            },
        },
    }
    return __update(options, defaults)


def setup_default_tabs(dash_cfg, data, metadata, plots_cfg):
    for itab in dash_cfg.tabs:
        if itab.id in ["references"]:
            continue
        if st.session_state["active_tab"] == itab.id:
            st.header(dash_cfg.tabs[0].label)
            if itab.display_infobox:
                with st.expander(
                    f"{itab.display_icon} {itab.display_label}",
                    expanded=itab.display_enabled,
                ):
                    st.markdown(
                        itab.text
                        if itab.text is not None
                        else "".join(itab.path.open().readlines())
                    )
            itab.tab_ref.create(data, metadata, plots_cfg)


def add_reference_widget(dash_cfg):
    if dash_cfg.enable_references:
        if st.session_state["active_tab"] == dash_cfg.tabs[-1].id:
            st.header(dash_cfg.tabs[-1].label)
            txt = "These are the references:\n\n"
            refs = "".join(["- {}\n\n"] * len(dash_cfg.references))
            mdlit(txt + refs.format(*dash_cfg.references))


def load_tab_modules():
    tab_hooks = {}

    for i in pt.Path("./dashboard/tabs").glob("tab_*.py"):
        spec = importlib.util.spec_from_file_location(f"dashboard.tabs.{i.stem}", i)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        tab_hooks[i.stem[4:]] = mod

    return tab_hooks


def add_data_download_button(
    data: pd.DataFrame, file_name="data", label="download data"
):
    st.download_button(
        label,
        data.to_csv().encode("utf-8"),
        f"{file_name}.csv",
        "text/csv",
    )
