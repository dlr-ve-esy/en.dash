import streamlit as st
from markdownlit import mdlit
import pathlib as pt
import pandas as pd


def setup_default_tabs(dash_cfg, data, metadata, plots_cfg):
    for itab in dash_cfg.tabs:
        if itab.id in ["references", "contacts"]:
            continue
        if st.session_state["active_tab"] == itab.id:
            st.header(itab.label)
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


def add_contact_widget(dash_cfg):
    itab = None
    for i in dash_cfg.tabs:
        if i.id == "contacts":
            itab = i

    if st.session_state["active_tab"] == itab.id:
        st.header(itab.label)
        mdlit("".join(pt.Path("./contact_info.md").open().readlines()))


def add_reference_widget(dash_cfg):
    if dash_cfg.enable_references:
        itab = None
        for i in dash_cfg.tabs:
            if i.id == "references":
                itab = i
        if st.session_state["active_tab"] == itab.id:
            st.header(itab.label)
            txt = "These are the references:\n\n"
            refs = "".join(["- {}\n\n"] * len(dash_cfg.references))
            mdlit(txt + refs.format(*dash_cfg.references))


def add_data_download_button(
    data: pd.DataFrame, file_name="data", label="download data"
):
    st.download_button(
        label,
        data.to_csv().encode("utf-8"),
        f"{file_name}.csv",
        "text/csv",
    )
