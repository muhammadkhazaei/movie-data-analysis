import pandas as pd
import matplotlib.pyplot as plt
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

print("\nMissing values:")
print(df.isnull().sum())


# -----------------------------
# Data cleaning
# -----------------------------

df = df.drop_duplicates().copy()

numeric_columns = [
    "Rank",
    "Year",
    "Runtime (Minutes)",
    "Rating",
    "Votes",
    "Revenue (Millions)",
    "Metascore",
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

required_columns = [
    "Title",
    "Year",
    "Rating",
    "Votes",
    "Revenue (Millions)",
]

df = df.dropna(subset=required_columns).copy()

print("\nData cleaning completed.")
print(f"Rows after cleaning: {df.shape[0]:,}")


# -----------------------------
# Basic statistics
# -----------------------------

print("\nBasic statistics:")
print(
    df[
        [
            "Year",
            "Runtime (Minutes)",
            "Rating",
            "Votes",
            "Revenue (Millions)",
            "Metascore",
        ]
    ].describe()
)


# -----------------------------
# Top 10 rated movies
# -----------------------------

top_rated = (
    df.sort_values(
        ["Rating", "Votes"],
        ascending=[False, False]
    )
    .head(10)
)

print("\nTop 10 rated movies:")
print(
    top_rated[
        ["Title", "Rating", "Votes"]
    ].to_string(index=False)
)


# -----------------------------
# Top 10 movies by revenue
# -----------------------------

top_revenue = (
    df[df["Revenue (Millions)"] > 0]
    .sort_values("Revenue (Millions)", ascending=False)
    .head(10)
)

print("\nTop 10 movies by revenue:")
print(
    top_revenue[
        ["Title", "Revenue (Millions)"]
    ].to_string(index=False)
)


# -----------------------------
# Top 10 movies by votes
# -----------------------------

top_votes = (
    df.sort_values("Votes", ascending=False)
    .head(10)
)

print("\nTop 10 movies by votes:")
print(
    top_votes[
        ["Title", "Votes"]
    ].to_string(index=False)
)


# -----------------------------
# Top 10 movies by revenue
# -----------------------------

plot_data = top_revenue.sort_values("Revenue (Millions)")

plt.figure(figsize=(10, 6))
plt.barh(
    plot_data["Title"],
    plot_data["Revenue (Millions)"],
)
plt.title("Top 10 Movies by Revenue")
plt.xlabel("Revenue (Millions)")
plt.ylabel("Movie")
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "top_10_movies_by_revenue.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()


# -----------------------------
# Rating distribution
# -----------------------------

plt.figure(figsize=(10, 6))
plt.hist(df["Rating"], bins=25)
plt.title("Movie Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "rating_distribution.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()


# -----------------------------
# Revenue distribution
# -----------------------------

revenue_data = df[df["Revenue (Millions)"] > 0]

plt.figure(figsize=(10, 6))
plt.hist(revenue_data["Revenue (Millions)"], bins=30)
plt.title("Movie Revenue Distribution")
plt.xlabel("Revenue (Millions)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "revenue_distribution.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()


# -----------------------------
# Movies released by year
# -----------------------------

movies_by_year = (
    df.groupby("Year")
    .size()
    .sort_index()
)

plt.figure(figsize=(12, 6))
plt.plot(movies_by_year.index, movies_by_year.values, marker="o")
plt.title("Number of Movies Released by Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Movies")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "movies_by_year.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()


# -----------------------------
# Average rating by year
# -----------------------------

average_rating_by_year = (
    df.groupby("Year")["Rating"]
    .mean()
    .sort_index()
)

plt.figure(figsize=(12, 6))
plt.plot(
    average_rating_by_year.index,
    average_rating_by_year.values,
    marker="o",
)
plt.title("Average Movie Rating by Year")
plt.xlabel("Release Year")
plt.ylabel("Average Rating")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "average_rating_by_year.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()


# -----------------------------
# Average revenue by year
# -----------------------------

average_revenue_by_year = (
    revenue_data.groupby("Year")["Revenue (Millions)"]
    .mean()
    .sort_index()
)

plt.figure(figsize=(12, 6))
plt.plot(
    average_revenue_by_year.index,
    average_revenue_by_year.values,
    marker="o",
)
plt.title("Average Movie Revenue by Year")
plt.xlabel("Release Year")
plt.ylabel("Average Revenue (Millions)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "average_revenue_by_year.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()


# -----------------------------
# Runtime distribution
# -----------------------------

plt.figure(figsize=(10, 6))
plt.hist(df["Runtime (Minutes)"], bins=25)
plt.title("Movie Runtime Distribution")
plt.xlabel("Runtime (Minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "runtime_distribution.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()


# -----------------------------
# Votes vs Rating
# -----------------------------

plt.figure(figsize=(10, 6))
plt.scatter(
    df["Rating"],
    df["Votes"],
    alpha=0.6,
)
plt.title("Votes vs Rating")
plt.xlabel("Rating")
plt.ylabel("Votes")
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "votes_vs_rating.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()


# -----------------------------
# Correlation analysis
# -----------------------------

correlation_columns = [
    "Year",
    "Runtime (Minutes)",
    "Rating",
    "Votes",
    "Revenue (Millions)",
    "Metascore",
]

correlation_matrix = df[correlation_columns].corr()

fig, ax = plt.subplots(figsize=(9, 7))
image = ax.imshow(correlation_matrix, vmin=-1, vmax=1)
ax.set_xticks(range(len(correlation_columns)))
ax.set_yticks(range(len(correlation_columns)))
ax.set_xticklabels(correlation_columns, rotation=45, ha="right")
ax.set_yticklabels(correlation_columns)

for i in range(len(correlation_columns)):
    for j in range(len(correlation_columns)):
        ax.text(
            j,
            i,
            f"{correlation_matrix.iloc[i, j]:.2f}",
            ha="center",
            va="center",
        )

fig.colorbar(image, ax=ax)
ax.set_title("Correlation Matrix")
fig.tight_layout()
fig.savefig(
    OUTPUT_DIR / "correlation_matrix.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close(fig)


# -----------------------------
# Save cleaned dataset
# -----------------------------

cleaned_path = OUTPUT_DIR / "cleaned_movies.csv"

df.to_csv(
    cleaned_path,
    index=False,
)

print("\nAnalysis completed successfully.")
print(f"Output files saved in: {OUTPUT_DIR}")
