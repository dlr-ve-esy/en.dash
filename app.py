import streamlit as st
import numpy as np
import pathlib as pt
from dashboard.tabs import tab0, tab1, tab2, tab3, tab4
from dashboard.layout import sidebar
import pandas as pd
import json


def get_meta(store: object, hdfpackage_path: str) -> dict:
    return json.loads(store.get_storer(hdfpackage_path).attrs["plot_metadata"])


def load_data(path: pt.Path) -> dict:
    # with zipfile.ZipFile(path.as_posix()) as zf:
    #     data = pd.read_csv(io.BytesIO(zf.read("Mark_Ie_Daten.csv")))

    load = pd.HDFStore(path=path, mode="r")

    datasets = {}
    metadata = {}
    hdfpackage_path ="TimeSeries/SingleKey"
    datasets["SingleKey"] = load.get(hdfpackage_path)
    metadata["SingleKey"] = get_meta(load, hdfpackage_path)
    datasets["dataset1"] = np.random.randint(1, 999, (2, 100))
    metadata["dataset1"] = {}
    hdfpackage_path = "TimeSeries/MultiKey/Dispatch"
    datasets["Dispatch"] = load.get(hdfpackage_path)
    metadata["Dispatch"] = get_meta(load, hdfpackage_path)

    return datasets, metadata


if __name__ == "__main__":
    if "style" not in st.session_state:
        st.session_state["style"] = "dark"

    tab_names = ["tab0", "tab1", "tab2", "tab3", "tab4"]

    st.set_page_config(page_title="sfc dashboard", layout="wide")

    data, metadata = load_data(pt.Path("./data/output.hdf5"))

    with st.sidebar:
        sidebar.create()

    root = st.container()

    if "active_tab" not in st.session_state:
        st.session_state["active_tab"] = tab_names[0]

    with root:
        with st.sidebar:
            st.session_state["active_tab"] = st.radio(
                label="select view", options=tab_names
            )

        if st.session_state["active_tab"] == tab_names[0]:
            tab0.create(data["SingleKey"], metadata["SingleKey"])
        if st.session_state["active_tab"] == tab_names[1]:
            tab1.create(data)
        if st.session_state["active_tab"] == tab_names[2]:
            tab2.create(data)
        if st.session_state["active_tab"] == tab_names[3]:
            tab3.create(data["dataset1"])
        if st.session_state["active_tab"] == tab_names[4]:
            tab4.create(data["Dispatch"], metadata["Dispatch"])
