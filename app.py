import streamlit as st
import numpy as np
import pathlib as pt
from dashboard.tabs import tab0, tab1, tab2, tab3
from dashboard.layout import sidebar


def load_data(path: pt.Path) -> dict:
    # with zipfile.ZipFile(path.as_posix()) as zf:
    #     data = pd.read_csv(io.BytesIO(zf.read("Mark_Ie_Daten.csv")))

    return {"dataset1": np.random.randint(1, 999, (2, 100))}


if __name__ == "__main__":
    if "style" not in st.session_state:
        st.session_state["style"] = "dark"

    st.set_page_config(page_title="sfc dashboard", layout="wide")

    data = load_data(pt.Path("./Mark_Ie_Daten.zip"))

    with st.sidebar:
        sidebar.create()

    root = st.container()

    with root:
        tabs = st.tabs(["tab0", "tab1", "tab2", "tab3"])

        with tabs[0]:
            tab0.create(data)
        with tabs[1]:
            tab1.create(data)
        with tabs[2]:
            tab2.create(data)
        with tabs[3]:
            tab3.create(data["dataset1"])
