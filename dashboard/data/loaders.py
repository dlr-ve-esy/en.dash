import numpy as np
import pandas as pd
import json
import pathlib as pt


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
