# data_utils.py
import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load CSV into a DataFrame with basic validation."""
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError("Loaded dataframe is empty.")
    return df

def filter_by_threshold(df: pd.DataFrame, column: str, threshold: float, greater_equal: bool = True) -> pd.DataFrame:
    """Filter rows by a numeric threshold on a given column."""
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not in dataframe.")
    if not pd.api.types.is_numeric_dtype(df[column]):
        raise TypeError(f"Column '{column}' must be numeric.")
    mask = df[column] >= threshold if greater_equal else df[column] < threshold
    return df.loc[mask].reset_index(drop=True)

