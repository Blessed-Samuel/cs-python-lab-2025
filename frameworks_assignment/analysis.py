"""
analysis.py
Performs simple analyses on data/metadata_clean.csv and writes plots to outputs/.
Run after prepare_data.py.

Usage:
    python analysis.py
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
from wordcloud import WordCloud

sns.set(style="whitegrid")
INPUT = os.path.join("data", "metadata_clean.csv")
OUTDIR = "outputs"
os.makedirs(OUTDIR, exist_ok=True)


def top_publications_by_year(
    df, outpath=os.path.join(OUTDIR, "publications_by_year.png")
):
    if "year" not in df.columns:
        print("No 'year' column found — skipping publications_by_year.")
        return
    counts = df["year"].dropna().astype(int).value_counts().sort_index()
    plt.figure(figsize=(8, 4))
    sns.barplot(x=counts.index.astype(str), y=counts.values)
    plt.title("Publications by Year")
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()
    print(f"Wrote {outpath}")


def top_journals(df, n=15, outpath=os.path.join(OUTDIR, "top_journals.png")):
    if "journal" not in df.columns:
        print("No 'journal' column found — skipping top_journals.")
        return
    counts = df["journal"].fillna("Unknown").value_counts().head(n)
    plt.figure(figsize=(8, 5))
    sns.barplot(y=counts.index, x=counts.values)
    plt.title(f"Top {n} Journals (by paper count)")
    plt.xlabel("Count")
    plt.ylabel("Journal")
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()
    print(f"Wrote {outpath}")


def word_freq_in_titles(df, n=30, outpath=os.path.join(OUTDIR, "title_word_freq.png")):
    if "title" not in df.columns:
        print("No 'title' column found — skipping title_word_freq.")
        return
    titles = df["title"].dropna().astype(str).str.lower()
    words = []
    for t in titles:
        # simple tokenization
        tokens = re.findall(r"[a-zA-Z]{2,}", t)
        words.extend(tokens)

    stopwords = set(
        [
            "covid",
            "sars",
            "coronavirus",
            "2019",
            "study",
            "analysis",
            "review",
            "new",
            "using",
            "based",
            "infection",
            "clinical",
            "patients",
            "pandemic",
            "from",
            "and",
            "the",
            "of",
            "in",
            "with",
        ]
    )
    filtered = [w for w in words if w not in stopwords]
    counts = Counter(filtered)
    most = counts.most_common(n)
    if not most:
        print("No words found in titles.")
        return
    words_list, cnts = zip(*most)
    plt.figure(figsize=(8, 6))
    sns.barplot(x=list(cnts), y=list(words_list))
    plt.title("Top Words in Titles")
    plt.xlabel("Count")
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()
    print(f"Wrote {outpath}")


def wordcloud_titles(df, outpath=os.path.join(OUTDIR, "title_wordcloud.png")):
    if "title" not in df.columns:
        print("No 'title' column found — skipping wordcloud.")
        return
    text = " ".join(df["title"].dropna().astype(str).tolist()).lower()
    wc = WordCloud(width=800, height=400, background_color="white", collocations=False)
    wc.generate(text)
    wc.to_file(outpath)
    print(f"Wrote {outpath}")


def source_distribution(df, outpath=os.path.join(OUTDIR, "source_distribution.png")):
    if "source_x" not in df.columns:
        print("No 'source_x' column found — skipping source_distribution.")
        return
    counts = df["source_x"].fillna("Unknown").value_counts().head(10)
    plt.figure(figsize=(8, 5))
    sns.barplot(y=counts.index, x=counts.values)
    plt.title("Top Sources")
    plt.xlabel("Count")
    plt.ylabel("Source")
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()
    print(f"Wrote {outpath}")


def main():
    if not os.path.exists(INPUT):
        raise FileNotFoundError(
            f"Please run prepare_data.py and place cleaned file at {INPUT}"
        )
    df = pd.read_csv(INPUT, parse_dates=["publish_time"], low_memory=False)
    print("Loaded", len(df), "rows")

    top_publications_by_year(df)
    top_journals(df, n=15)
    word_freq_in_titles(df, n=30)
    wordcloud_titles(df)
    source_distribution(df)

    # Save a small sample to inspect quickly
    df.sample(10).to_csv(os.path.join(OUTDIR, "sample_data.csv"), index=False)
    print("Saved sample_data.csv")


if __name__ == "__main__":
    main()
