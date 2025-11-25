import pandas as pd

def preprocess_input(data: dict, feature_cols: list, cat_cols: list):
    df = pd.DataFrame([data])
    for c in cat_cols:
        df[c] = df[c].astype(str)

    df = df[feature_cols]

    return df
