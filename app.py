import streamlit as st
from datetime import datetime
from data_utils import load_data, filter_by_threshold

# Streamlit page config
st.set_page_config(page_title="Simple DS App", layout="centered")

# Sidebar: date/time info
st.sidebar.header("App Info")
st.sidebar.write(f"🕒 Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Main title
st.title("Simple Data Science App (Streamlit)")
st.write("Load a small CSV, filter rows, and preview results.")

# Load data
df = load_data("sample_data.csv")
st.subheader("Raw data")
st.dataframe(df, use_container_width=True)

# Filter controls
col = st.selectbox(
    "Column to threshold",
    options=[c for c in df.columns if df[c].dtype != "object"]
)
thr = st.slider(
    "Threshold",
    float(df[col].min()), float(df[col].max()), float(df[col].median())
)
keep = st.radio("Keep rows", ["≥ threshold", "< threshold"], horizontal=True)
ge = keep.startswith("≥")

# Apply filter
filtered = filter_by_threshold(df, column=col, threshold=thr, greater_equal=ge)
st.subheader("Filtered data")
st.dataframe(filtered, use_container_width=True)

st.caption("Tip: we’ll extend this later with charts & uploads.")

