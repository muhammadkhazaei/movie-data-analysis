import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# -----------------------------
# Project paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "movies.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)


# -----------------------------
# Load dataset
# -----------------------------

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully.")
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")


# -----------------------------
# Initial inspection
# -----------------------------

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())


# -----------------------------
# Data cleaning
# -----------------------------

# Remove duplicate rows
df = df.drop_duplicates()

# Convert numeric columns when available
numeric_columns = [
    "budget",
    "revenue",
    "runtime",
    "vote_average",
    "vote_count",
    "popularity"
]

for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")


# Convert release date
if "release_date" in df.columns:
    df["release_date"] = pd.to_datetime(
        df["release_date"],
        errors="coerce"
    )

    df["release_year"] = df["release_date"].dt.year


# Remove rows without title
if "title" in df.columns:
    df = df.dropna(subset=["title"])


print("\nData cleaning completed.")
print(f"Rows after cleaning: {df.shape[0]:,}")


# -----------------------------
# Basic statistics
# -----------------------------

print("\nBasic statistics:")

available_numeric = [
    column for column in numeric_columns
    if column in df.columns
]

if available_numeric:
    print(df[available_numeric].describe())


# -----------------------------
# Top rated movies
# -----------------------------

if "vote_average" in df.columns and "vote_count" in df.columns:

    top_rated = (
        df[df["vote_count"] >= 100]
        .sort_values("vote_average", ascending=False)
        .head(10)
    )

    print("\nTop 10 rated movies:")
    print(
        top_rated[
            ["title", "vote_average", "vote_count"]
        ].to_string(index=False)
    )


# -----------------------------
# Most popular movies
# -----------------------------

if "popularity" in df.columns:

    top_popular = (
        df.sort_values("popularity", ascending=False)
        .head(10)
    )

    print("\nTop 10 most popular movies:")
    print(
        top_popular[
            ["title", "popularity"]
        ].to_string(index=False)
    )


# -----------------------------
# Revenue analysis
# -----------------------------

if "revenue" in df.columns:

    top_revenue = (
        df[df["revenue"] > 0]
        .sort_values("revenue", ascending=False)
        .head(10)
    )

    print("\nTop 10 movies by revenue:")
    print(
        top_revenue[
            ["title", "revenue"]
        ].to_string(index=False)
    )


# -----------------------------
# Budget vs Revenue
# -----------------------------

if "budget" in df.columns and "revenue" in df.columns:

    revenue_data = df[
        (df["budget"] > 0) &
        (df["revenue"] > 0)
    ].copy()

    if not revenue_data.empty:

        plt.figure(figsize=(10, 6))

        sns.scatterplot(
            data=revenue_data,
            x="budget",
            y="revenue",
            alpha=0.5
        )

        plt.title("Budget vs Revenue")
        plt.xlabel("Budget")
        plt.ylabel("Revenue")
        plt.tight_layout()

        plt.savefig(
            OUTPUT_DIR / "budget_vs_revenue.png",
            dpi=300
        )

        plt.close()


# -----------------------------
# Popularity distribution
# -----------------------------

if "popularity" in df.columns:

    plt.figure(figsize=(10, 6))

    sns.histplot(
        df["popularity"].dropna(),
        bins=40,
        kde=True
    )

    plt.title("Movie Popularity Distribution")
    plt.xlabel("Popularity")
    plt.ylabel("Number of Movies")
    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "popularity_distribution.png",
        dpi=300
    )

    plt.close()


# -----------------------------
# Rating distribution
# -----------------------------

if "vote_average" in df.columns:

    plt.figure(figsize=(10, 6))

    sns.histplot(
        df["vote_average"].dropna(),
        bins=30,
        kde=True
    )

    plt.title("Movie Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Number of Movies")
    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "rating_distribution.png",
        dpi=300
    )

    plt.close()


# -----------------------------
# Movies released by year
# -----------------------------

if "release_year" in df.columns:

    yearly_movies = (
        df.dropna(subset=["release_year"])
        .groupby("release_year")
        .size()
    )

    yearly_movies = yearly_movies[
        yearly_movies.index >= 1980
    ]

    plt.figure(figsize=(12, 6))

    yearly_movies.plot()

    plt.title("Number of Movies Released by Year")
    plt.xlabel("Release Year")
    plt.ylabel("Number of Movies")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "movies_by_year.png",
        dpi=300
    )

    plt.close()


# -----------------------------
# Average revenue by year
# -----------------------------

if "release_year" in df.columns and "revenue" in df.columns:

    yearly_revenue = (
        df[
            (df["revenue"] > 0) &
            df["release_year"].notna()
        ]
        .groupby("release_year")["revenue"]
        .mean()
    )

    yearly_revenue = yearly_revenue[
        yearly_revenue.index >= 1980
    ]

    plt.figure(figsize=(12, 6))

    yearly_revenue.plot()

    plt.title("Average Movie Revenue by Year")
    plt.xlabel("Release Year")
    plt.ylabel("Average Revenue")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "average_revenue_by_year.png",
        dpi=300
    )

    plt.close()


# -----------------------------
# Correlation analysis
# -----------------------------

correlation_columns = [
    column for column in [
        "budget",
        "revenue",
        "runtime",
        "vote_average",
        "vote_count",
        "popularity"
    ]
    if column in df.columns
]

if len(correlation_columns) >= 2:

    correlation_matrix = df[
        correlation_columns
    ].corr()

    plt.figure(figsize=(10, 7))

    sns.heatmap(
        correlation_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0
    )

    plt.title("Correlation Matrix")
    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "correlation_matrix.png",
        dpi=300
    )

    plt.close()


# -----------------------------
# Save cleaned dataset
# -----------------------------

cleaned_path = OUTPUT_DIR / "cleaned_movies.csv"

df.to_csv(
    cleaned_path,
    index=False
)


print("\nAnalysis completed successfully.")
print(f"Output files saved in: {OUTPUT_DIR}")
