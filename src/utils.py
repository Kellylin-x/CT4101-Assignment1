# Helper functions for CT4101 Assignment 1

import pandas as pd

def to_xy(df: pd.DataFrame, target: str):
    X = df.drop(columns=[target])
    y = df[target]
    return X, y
