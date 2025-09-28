"""
app.py - Streamlit CORD-19 Data Explorer

Run:
    streamlit run app.py
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os

st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")
sns.set(style="whitegrid")

DATA_PATH = os.path.join("data", "metadata_cleaned.csv")


@st.cache_data(show_spinner=False)
def load_data(path=DATA_PATH, nrows=None):
    if not os.path.exists(path):
        st.error(f"Cleaned data not found at {path}. Run prepare_data.py first.")
        return pd.DataFrame()

    df = pd.read_csv(path, low_memory=False)

    # Ensure datetime conversion
    if "last_updated" in df.columns:
        df["last_updated"] = pd.to_datetime(df["last_updated"], errors="coerce")
        df["year"] = df["last_updated"].dt.year
    else:
        df["year"] = None

    return df


df = load_data()
if df.empty:
    st.stop()

st.title("CORD-19 Data Explorer")
st.markdown(
    "Simple exploration of the CORD-19 metadata file (titles, abstracts, year, journal/source)."
)

# Sidebar controls
st.sidebar.header("Filters & Controls")
min_year = int(df["year"].dropna().min()) if not df["year"].dropna().empty else 2019
max_year = int(df["year"].dropna().max()) if not df["year"].dropna().empty else 2023
year_range = st.sidebar.slider("Year range", min_year, max_year, (min_year, max_year))

journal_col = "source_organization" if "source_organization" in df.columns else None
journal_options = ["All"]
if journal_col:
    journal_options += list(
        df[journal_col].fillna("Unknown").value_counts().index[:100]
    )
selected_journal = st.sidebar.selectbox("Source/Journal (top 100)", journal_options)

# Filter data
f = df.copy()
if "year" in f.columns:
    f = f[f["year"].between(year_range[0], year_range[1], inclusive="both")]
if selected_journal != "All" and journal_col:
    f = f[f[journal_col] == selected_journal]

st.write(f"Showing **{len(f):,}** papers (filtered).")

# Plots
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Publications by Year")
    if "year" in f.columns and not f["year"].dropna().empty:
        year_counts = f["year"].dropna().astype(int).value_counts().sort_index()
        fig, ax = plt.subplots(figsize=(8, 3))
        sns.barplot(x=year_counts.index.astype(str), y=year_counts.values, ax=ax)
        ax.set_xlabel("Year")
        ax.set_ylabel("Count")
        ax.set_title("Publications per Year")
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.info("No 'year' data available.")

with col2:
    st.subheader("Top Sources")
    if journal_col:
        top_j = f[journal_col].fillna("Unknown").value_counts().head(8)
        fig2, ax2 = plt.subplots(figsize=(4, 3))
        sns.barplot(y=top_j.index, x=top_j.values, ax=ax2)
        ax2.set_xlabel("Count")
        ax2.set_ylabel("")
        st.pyplot(fig2)
    else:
        st.info("No source/journal column available.")

# Word cloud
st.subheader("Word Cloud of Paper Titles")
title_col = "paper_title" if "paper_title" in f.columns else None
if title_col and not f[title_col].dropna().empty:
    text = " ".join(f[title_col].dropna().astype(str).tolist()).lower()
    wc = WordCloud(width=800, height=300, background_color="white").generate(text)
    fig3, ax3 = plt.subplots(figsize=(12, 4))
    ax3.imshow(wc, interpolation="bilinear")
    ax3.axis("off")
    st.pyplot(fig3)
else:
    st.info("No titles available to generate a word cloud.")

# Data sample
st.subheader("Sample of Filtered Papers")
cols_to_show = []
if "paper_title" in f.columns:
    cols_to_show.append("paper_title")
if journal_col:
    cols_to_show.append(journal_col)
if "last_updated" in f.columns:
    cols_to_show.append("last_updated")
if "description" in f.columns:
    cols_to_show.append("description")

if cols_to_show:
    st.dataframe(f[cols_to_show].head(25))
else:
    st.info("No suitable columns available to display sample papers.")
