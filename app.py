import streamlit as st
import numpy as np
import pathlib as pt
from dashboard.layout import sidebar
import pandas as pd
import json
from dashboard.tools.configuration import DashboardConfiguration, TabData
from streamlit_extras.markdownlit import mdlit
from collections import defaultdict
from PIL import Image
import dashboard.tabs
import importlib.util

from streamlit_option_menu import option_menu

tab_hooks = {}

for i in pt.Path("./dashboard/tabs").glob("tab_*.py"):
    spec = importlib.util.spec_from_file_location(f"dashboard.tabs.{i.stem}", i)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    tab_hooks[i.stem[4:]] = mod


def get_meta(store: object, hdfpackage_path: str) -> dict:
    return json.loads(store.get_storer(hdfpackage_path).attrs["plot_metadata"])


def load_data(path: pt.Path) -> dict:
    # with zipfile.ZipFile(path.as_posix()) as zf:
    #     data = pd.read_csv(io.BytesIO(zf.read("Mark_Ie_Daten.csv")))

    datasets = {}
    metadata = {}

    if path.exists():
        load = pd.HDFStore(path=path, mode="r")
        hdfpackage_path = "TimeSeries/SingleKey"
        datasets["SingleKey"] = load.get(hdfpackage_path)
        metadata["SingleKey"] = get_meta(load, hdfpackage_path)
        datasets["dataset1"] = np.random.randint(1, 999, (2, 100))
        metadata["dataset1"] = {}
        hdfpackage_path = "TimeSeries/MultiKey/Dispatch"
        datasets["Dispatch"] = load.get(hdfpackage_path)
        metadata["Dispatch"] = get_meta(load, hdfpackage_path)

        hdfpackage_path = "Bar/Capacity"
        df = load.get(hdfpackage_path).reset_index()
        df2 = df.copy()
        df2["Year"] = 2020
        df2["InstalledPower"] = df["InstalledPower"] + 100
        df_new = pd.concat([df, df2])
        datasets["inst_power"] = df_new
        metadata["inst_power"] = get_meta(load, hdfpackage_path)
    else:
        datasets["SingleKey"] = pd.DataFrame()
        metadata["SingleKey"] = {}
        datasets["dataset1"] = np.random.randint(1, 999, (2, 100))
        metadata["dataset1"] = {}
        datasets["Dispatch"] = pd.DataFrame()
        metadata["Dispatch"] = {}

    return datasets, metadata


if __name__ == "__main__":
    dash_cfg = DashboardConfiguration.load(pt.Path("./dashboard_config.json"))

    if dash_cfg.enable_references:
        if dash_cfg.tabs[-1].id != "references":
            dash_cfg.tabs.append(
                TabData("references", "References", dash_cfg.references_icon)
            )

    for itab in dash_cfg.tabs:
        if itab.id in tab_hooks:
            itab.tab_ref = tab_hooks[itab.id]
        itab.display_infobox = True
        if itab.text is None and itab.path is None:
            itab.display_infobox = False
        elif itab.path is not None and not itab.path.exists():
            itab.display_infobox = False

    plots_cfg = defaultdict(dict)
    for ifile in pt.Path("./configurations").glob("*.json"):
        cfg_data = json.load(ifile.open("r"))
        plots_cfg[ifile.stem] = cfg_data

    if "style" not in st.session_state:
        st.session_state["style"] = "light"

    st.set_page_config(page_title="sfc dashboard", layout="wide")

    data, metadata = load_data(pt.Path("./data/output.hdf5"))

    if "active_tab" not in st.session_state:
        st.session_state["active_tab"] = dash_cfg.tabs[0].id

    # tab_management = {k: v for k, v in zip(dash_cfg.tabs, tab_hooks)}
    with st.sidebar:
        if st.session_state["style"] == "dark":
            logo = Image.open("data/column-chart-line-icon-white.png")
            logo = logo.resize((150, 100))

            st.image(logo, output_format="png")
        elif st.session_state["style"] == "light":
            logo = Image.open("data/column-chart-line-icon-black.png")
            logo = logo.resize((150, 100))

            st.image(logo, output_format="png")

        selected = option_menu(
            dash_cfg.dashboard_label,
            [i.label for i in dash_cfg.tabs],
            icons=[i.icon for i in dash_cfg.tabs],  # bootstrap icons
            menu_icon=dash_cfg.sidemenu_icon,
            default_index=1,
        )

        for i in dash_cfg.tabs:
            if i.label == selected:
                st.session_state["active_tab"] = i.id

        with st.expander("Options"):
            if dash_cfg.enable_darkmode_toggle:
                darkmode_enabled = st.toggle("enable dark mode for plots")
            else:
                darkmode_enabled = False

            if darkmode_enabled:
                st.session_state["style"] = "dark"
            else:
                st.session_state["style"] = "light"

    root = st.container()

    with root:
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

        if dash_cfg.enable_references:
            if st.session_state["active_tab"] == dash_cfg.tabs[-1].id:
                st.header(dash_cfg.tabs[-1].label)
                txt = "These are the references:\n\n"
                refs = "".join(["- {}\n\n"] * len(dash_cfg.references))
                mdlit(txt + refs.format(*dash_cfg.references))
