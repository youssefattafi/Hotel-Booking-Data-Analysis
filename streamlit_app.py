"""Interactive hotel booking EDA dashboard. Run: streamlit run streamlit_app.py"""
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Hotel Booking Analytics", page_icon="🏨", layout="wide")
st.title("🏨 Hotel Booking Analytics Dashboard")
st.caption("Explore booking patterns, cancellation rates, room pricing, and guest origins. Descriptive analysis only.")

@st.cache_data(show_spinner="Loading hotel bookings...")
def load_data():
    path = Path(__file__).resolve().parent / "hotel_bookings.csv"
    df = pd.read_csv(path)
    invalid = df[["adults", "children", "babies"]].fillna(0).sum(axis=1).eq(0)
    cleaned = df.loc[~invalid].drop_duplicates().copy()
    return cleaned, len(df), int(invalid.sum())

df, raw_count, excluded_guests = load_data()
st.sidebar.header("Filters")
hotels = st.sidebar.multiselect("Hotel type", sorted(df["hotel"].dropna().unique()), default=sorted(df["hotel"].dropna().unique()))
years = st.sidebar.multiselect("Arrival year", sorted(df["arrival_date_year"].dropna().unique()), default=sorted(df["arrival_date_year"].dropna().unique()))
segments = st.sidebar.multiselect("Market segment", sorted(df["market_segment"].dropna().unique()), default=sorted(df["market_segment"].dropna().unique()))
status = st.sidebar.selectbox("Booking status", ["All bookings", "Not cancelled", "Cancelled"])
view = df[df["hotel"].isin(hotels) & df["arrival_date_year"].isin(years) & df["market_segment"].isin(segments)].copy()
if status == "Not cancelled":
    view = view[view["is_canceled"].eq(0)]
elif status == "Cancelled":
    view = view[view["is_canceled"].eq(1)]
if view.empty:
    st.warning("No bookings match the selected filters. Change the sidebar selections.")
    st.stop()

st.info(f"Dataset: {raw_count:,} raw records; {excluded_guests:,} zero-guest rows excluded, followed by exact deduplication to {len(df):,} records. Identical rows may represent separate reservations.")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Filtered bookings", f"{len(view):,}")
m2.metric("Cancellation rate", f"{view['is_canceled'].mean():.1%}")
m3.metric("Median lead time", f"{view['lead_time'].median():,.0f} days")
m4.metric("Median ADR", f"{view['adr'].median():,.2f}")

tab1, tab2, tab3, tab4 = st.tabs(["Cancellations", "Channels & segments", "Rates & seasonality", "Guest origins"])
with tab1:
    st.subheader("Cancellation rate by hotel")
    by_hotel = view.groupby("hotel", as_index=False).agg(bookings=("is_canceled", "size"), cancellation_rate=("is_canceled", "mean"))
    fig = px.bar(by_hotel, x="hotel", y="cancellation_rate", text="bookings", labels={"hotel": "Hotel", "cancellation_rate": "Cancellation rate"})
    fig.update_yaxes(tickformat=".0%")
    st.plotly_chart(fig, use_container_width=True)
    st.caption("When filtering to cancelled or non-cancelled bookings, cancellation rates become 100% or 0% by definition.")
    bins = [-1, 7, 30, 90, 180, np.inf]
    names = ["0–7", "8–30", "31–90", "91–180", "181+"]
    view["lead_time_band"] = pd.cut(view["lead_time"], bins=bins, labels=names)
    by_lead = view.groupby("lead_time_band", observed=True).agg(bookings=("is_canceled","size"), cancellation_rate=("is_canceled","mean")).reset_index()
    fig = px.bar(by_lead, x="lead_time_band", y="cancellation_rate", hover_data=["bookings"], labels={"lead_time_band":"Lead time (days)", "cancellation_rate":"Cancellation rate"})
    fig.update_yaxes(tickformat=".0%")
    st.plotly_chart(fig, use_container_width=True)
with tab2:
    st.subheader("Market segment booking volume")
    by_segment = view.groupby("market_segment", as_index=False).agg(bookings=("is_canceled","size"), cancellation_rate=("is_canceled","mean")).sort_values("bookings", ascending=False)
    st.plotly_chart(px.bar(by_segment.head(12), x="market_segment", y="bookings", hover_data=["cancellation_rate"], labels={"market_segment":"Market segment"}), use_container_width=True)
    st.dataframe(by_segment.style.format({"cancellation_rate":"{:.1%}"}), hide_index=True, use_container_width=True)
with tab3:
    st.subheader("ADR by hotel")
    st.caption("ADR uses the dataset's recorded units; non-cancelled bookings only. Negative ADR values and extreme outliers warrant review.")
    non_cancelled = view[view["is_canceled"].eq(0)].copy()
    if non_cancelled.empty:
        st.info("Select All bookings or Not cancelled to view ADR and arrival charts.")
    else:
        top = non_cancelled["adr"].quantile(0.99)
        shown = non_cancelled[non_cancelled["adr"].between(0, top)]
        st.plotly_chart(px.box(shown, x="hotel", y="adr", labels={"adr":"Average daily rate", "hotel":"Hotel"}, title="ADR distribution (0 to 99th percentile shown)"), use_container_width=True)
        months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        arrivals = non_cancelled.groupby("arrival_date_month").size().reindex(months, fill_value=0).reset_index(name="bookings")
        st.plotly_chart(px.bar(arrivals, x="arrival_date_month", y="bookings", labels={"arrival_date_month":"Arrival month"}), use_container_width=True)
        st.caption("Month totals are not normalized for observation-period coverage or hotel capacity.")
with tab4:
    st.subheader("Top guest origin codes")
    origins = view[view["is_canceled"].eq(0)]["country"].fillna("Unknown").value_counts().head(15).rename_axis("country").reset_index(name="bookings")
    if origins.empty:
        st.info("Select All bookings or Not cancelled to view guest origins.")
    else:
        st.plotly_chart(px.bar(origins, x="country", y="bookings"), use_container_width=True)
        st.caption("Country codes reflect recorded booking origins; missing values are shown as Unknown.")

st.divider()
st.markdown("**Interpretation limits:** These are observational booking records, not verified stays or occupancy. Exact duplicate removal can exclude legitimate reservations. Filtered rates and totals are not causal estimates.")
st.markdown("[Source notebook and methodology](https://github.com/youssefattafi/Hotel-Booking-Data-Analysis)")
