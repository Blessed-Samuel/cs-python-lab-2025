import os
import pandas as pd

# ✅ Build correct path to metadata.csv inside data/
BASE_DIR = os.path.dirname(__file__)
INPUT = os.path.join(BASE_DIR, "data", "metadata.csv")
OUTPUT = os.path.join(BASE_DIR, "data", "metadata_cleaned.csv")


def main():
    print("Loading CSV (this can take a while for large files)...")
    df = pd.read_csv(INPUT, dtype=str, low_memory=False)

    print(f"Original shape: {df.shape}")

    # ---- Basic Cleaning ----
    # Convert publish_time to datetime
    if "publish_time" in df.columns:
        df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
        df["year"] = df["publish_time"].dt.year

    # Create abstract_word_count if abstracts exist
    if "abstract" in df.columns:
        df["abstract_word_count"] = (
            df["abstract"].fillna("").apply(lambda x: len(x.split()))
        )

    # Drop rows with no title or publish_time
    if "title" in df.columns:
        df = df.dropna(subset=["title"])
    if "publish_time" in df.columns:
        df = df.dropna(subset=["publish_time"])

    print(f"Cleaned shape: {df.shape}")

    # Save cleaned dataset
    os.makedirs(os.path.join(BASE_DIR, "data"), exist_ok=True)
    df.to_csv(OUTPUT, index=False)
    print(f"✅ Cleaned data saved to {OUTPUT}")


if __name__ == "__main__":
    main()
