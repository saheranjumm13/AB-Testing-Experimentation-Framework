import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import norm
from pathlib import Path

st.set_page_config(
    page_title="A/B Testing Framework",
    page_icon="📊",
    layout="wide"
)

st.title("A/B Testing & Experimentation Framework")
st.write("Compare conversion performance between two experiment groups.")


uploaded_file = st.file_uploader(
    "Upload your A/B testing CSV",
    type=["csv"]
)

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    default_path = (
        Path(__file__).resolve().parent
        / "data"
        / "ab_test_users.csv"
    )

    if default_path.exists():
        data = pd.read_csv(default_path)
        st.info("Using the example dataset.")
    else:
        st.warning("Upload your A/B testing CSV.")
        st.stop()

required = [
    "user_id", "group", "device",
    "visits", "clicks", "purchases", "revenue"
]

if not set(required).issubset(data.columns):
    st.error(f"Required columns: {required}")
    st.stop()

if data[required].isnull().any().any():
    st.error("Missing values found. Clean the dataset first.")
    st.stop()

if data["user_id"].duplicated().any():
    st.error("Duplicate user IDs found.")
    st.stop()

if not data["group"].isin(["A", "B"]).all():
    st.error("Group must contain only A and B.")
    st.stop()

if not data["purchases"].isin([0, 1]).all():
    st.error("Purchases must contain only 0 or 1.")
    st.stop()

numeric_cols = [
    "visits", "clicks", "purchases", "revenue"
]

if not data[numeric_cols].apply(
    lambda col: pd.to_numeric(col, errors="coerce")
).notna().all().all():
    st.error("Numeric columns contain invalid values.")
    st.stop()

if (data[numeric_cols] < 0).any().any():
    st.error("Negative values found.")
    st.stop()

if (data["visits"] < 1).any():
    st.error("Each user must have at least one visit.")
    st.stop()

if (data["clicks"] > data["visits"]).any():
    st.error("Clicks cannot exceed visits in this dataset.")
    st.stop()

if not data["revenue"].map(
    lambda value: np.isfinite(value)
).all():
    st.error("Revenue contains invalid numeric values.")
    st.stop()

if data["group"].nunique() != 2:
    st.error("Both groups A and B must be present.")
    st.stop()

a = data[data["group"] == "A"]
b = data[data["group"] == "B"]


if len(a) == 0 or len(b) == 0:
    st.error("Both groups A and B must contain users.")
    st.stop()



n_a, n_b = len(a), len(b)
x_a = int(a["purchases"].sum())
x_b = int(b["purchases"].sum())

p_a = x_a / n_a
p_b = x_b / n_b

pooled = (x_a + x_b) / (n_a + n_b)
se = np.sqrt(
    pooled * (1 - pooled) * (1/n_a + 1/n_b)
)

if se == 0:
    st.error("Z-test cannot be calculated for these outcomes.")
    st.stop()

z = (p_b - p_a) / se
p_value = 2 * norm.sf(abs(z))

absolute_lift = p_b - p_a
relative_lift = (
    (p_b - p_a) / p_a * 100
    if p_a > 0 else np.nan
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Users", f"{len(data):,}")
c2.metric("Group A Conversion", f"{p_a:.2%}")
c3.metric("Group B Conversion", f"{p_b:.2%}")
c4.metric(
    "Relative Lift",
    f"{relative_lift:.2f}%"
    if np.isfinite(relative_lift) else "N/A"
)

st.subheader("Conversion Rate Comparison")
st.bar_chart(pd.DataFrame({
    "Conversion Rate": [p_a, p_b]
}, index=["A", "B"]))

st.write(f"Z-statistic: {z:.4f}")
st.write(f"P-value: {p_value:.6f}")
st.write(f"Absolute lift: {absolute_lift * 100:.2f} percentage points")

alpha = 0.05

if p_value < alpha and p_b > p_a:
    st.success("B has a statistically significant higher conversion rate.")
elif p_value < alpha and p_b < p_a:
    st.warning("B has a statistically significant lower conversion rate.")
else:
    st.info("No statistically significant difference established.")

# Group-level business KPIs
kpis = data.groupby("group").agg(
    Users=("user_id", "nunique"),
    Purchases=("purchases", "sum"),
    Revenue=("revenue", "sum"),
    Clicks=("clicks", "sum"),
    Visits=("visits", "sum")
)

kpis["Revenue per User"] = kpis["Revenue"] / kpis["Users"]

# This dataset does not contain impressions.
# Therefore, report clicks per visit, not impressions-based CTR.
kpis["Click Rate per Visit"] = (
    kpis["Clicks"] / kpis["Visits"].replace(0, np.nan)
)

st.subheader("Business KPIs")
st.dataframe(kpis, use_container_width=True)
