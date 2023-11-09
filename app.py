import streamlit as st
import numpy as np
import pathlib as pt
from dashboard.tabs import tab0, tab1, tab2, tab3, tab4, tab5
from dashboard.layout import sidebar
import pandas as pd
import json
from dashboard.tools.configuration import DashboardConfiguration, TabData
from streamlit_extras.markdownlit import mdlit
from collections import defaultdict


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

    plots_cfg = defaultdict(dict)
    for ifile in pt.Path("./configurations").glob("*.json"):
        cfg_data = json.load(ifile.open("r"))
        plots_cfg[ifile.stem] = cfg_data

    if dash_cfg.tabs[-1].id != "references":
        dash_cfg.tabs.append(TabData("references", "References"))

    if "style" not in st.session_state:
        st.session_state["style"] = "dark"

    st.set_page_config(page_title="sfc dashboard", layout="wide")

    data, metadata = load_data(pt.Path("./data/output.hdf5"))

    if "active_tab" not in st.session_state:
        st.session_state["active_tab"] = dash_cfg.tabs[0].id

    with st.sidebar:
        sidebar.create(dash_cfg)
        for idx, (_, itab) in enumerate(dash_cfg.tabs):
            res = st.button(f":bar_chart: {itab}", use_container_width=True)
            if res:
                st.session_state["active_tab"] = dash_cfg.tabs[idx].id

    root = st.container()

    with root:
        # with st.sidebar:
        #     st.session_state["active_tab"] = st.radio(
        #         label="select view", options=[i[0] for i in dash_cfg.tabs]
        #     )

        if st.session_state["active_tab"] == dash_cfg.tabs[0].id:
            st.header(dash_cfg.tabs[0].label)
            tab0.create(data["SingleKey"], metadata["SingleKey"])
        if st.session_state["active_tab"] == dash_cfg.tabs[1].id:
            st.header(dash_cfg.tabs[1].label)
            tab1.create(data["inst_power"], metadata["inst_power"])
        if st.session_state["active_tab"] == dash_cfg.tabs[2].id:
            st.header(dash_cfg.tabs[2].label)
            tab2.create(data)
        if st.session_state["active_tab"] == dash_cfg.tabs[3].id:
            st.header(dash_cfg.tabs[3].label)
            tab3.create(data["dataset1"], metadata, plots_cfg)
        if st.session_state["active_tab"] == dash_cfg.tabs[4].id:
            st.header(dash_cfg.tabs[4].label)
            tab4.create(data["Dispatch"], metadata["Dispatch"])
        if st.session_state["active_tab"] == dash_cfg.tabs[5].id:
            st.header(dash_cfg.tabs[5].label)
            tab5.create(data["SingleKey"], metadata["SingleKey"])

        if dash_cfg.enable_references:
            if st.session_state["active_tab"] == dash_cfg.tabs[-1].id:
                st.header(dash_cfg.tabs[-1].label)
                txt = "These are the references:\n\n"
                refs = "".join(["- {}\n\n"] * len(dash_cfg.references))
                mdlit(txt + refs.format(*dash_cfg.references))

    with st.sidebar:
        with st.expander("Options"):
            if dash_cfg.enable_darkmode_toggle:
                darkmode_enabled = st.toggle("enable dark mode for plots")
            else:
                darkmode_enabled = False

        if darkmode_enabled:
            st.session_state["style"] = "dark"
        else:
            st.session_state["style"] = "light"
