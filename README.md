# Movie Data Analysis

An exploratory movie data analysis project built with Python, Pandas, and Matplotlib.

## Project Overview

This project performs exploratory data analysis (EDA) on a movie dataset to identify patterns and relationships between movie ratings, revenue, runtime, votes, and release years.

The project demonstrates a practical data analysis workflow, including data loading, cleaning, validation, analysis, and visualization.

## Business Questions

The analysis explores questions such as:

- Which movies have the highest ratings?
- Which movies generate the most revenue?
- Which movies receive the most votes?
- How are movie ratings distributed?
- How is movie revenue distributed?
- How does the number of movie releases change over time?
- How does average movie rating change over time?
- How does average movie revenue change over time?
- Is there a relationship between votes and ratings?
- Which numerical variables are correlated?

## Dataset

The dataset contains 1,000 movie records with information including:

- Movie title
- Genre
- Director
- Actors
- Release year
- Runtime
- Rating
- Number of votes
- Revenue
- Metascore

The original dataset is stored in:

```text
data/movies.csv# Movie Data Analysis

An exploratory movie data analysis project built with Python, Pandas, and Matplotlib.

## Project Overview

This project performs exploratory data analysis (EDA) on a movie dataset to identify patterns and relationships between movie ratings, revenue, runtime, votes, and release years.

The project demonstrates a practical data analysis workflow, including data loading, cleaning, validation, analysis, and visualization.

## Business Questions

The analysis explores questions such as:

- Which movies have the highest ratings?
- Which movies generate the most revenue?
- Which movies receive the most votes?
- How are movie ratings distributed?
- How is movie revenue distributed?
- How does the number of movie releases change over time?
- How does average movie rating change over time?
- How does average movie revenue change over time?
- Is there a relationship between votes and ratings?
- Which numerical variables are correlated?

## Dataset

The dataset contains 1,000 movie records with information including:

- Movie title
- Genre
- Director
- Actors
- Release year
- Runtime
- Rating
- Number of votes
- Revenue
- Metascore

The original dataset is stored in:

```text
data/movies.csv
```

The dataset is used for educational and portfolio purposes.

## Technologies

- Python 3
- Pandas
- Matplotlib

## Project Structure

```text
movie-data-analysis/
├── data/
│   └── movies.csv
├── notebooks/
│   └── .gitkeep
├── outputs/
│   ├── top_10_movies_by_revenue.png
│   ├── rating_distribution.png
│   ├── revenue_distribution.png
│   ├── movies_by_year.png
│   ├── average_rating_by_year.png
│   ├── average_revenue_by_year.png
│   ├── runtime_distribution.png
│   ├── votes_vs_rating.png
│   └── correlation_matrix.png
├── src/
│   └── analysis.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Analysis Workflow

```text
Raw Dataset
     ↓
Data Loading
     ↓
Data Inspection
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Statistical Analysis
     ↓
Data Visualization
     ↓
Analysis Outputs
```

## Data Cleaning

The analysis performs basic data quality checks and cleaning operations, including:

- Removing duplicate records
- Converting numeric columns to appropriate numeric types
- Converting invalid numeric values to missing values
- Removing rows with missing values in required analysis fields
- Filtering invalid revenue values where required for revenue analysis

## Analysis Performed

### Top Rated Movies

Movies are ranked primarily by rating, with votes used as a secondary sorting criterion when ratings are equal.

### Revenue Analysis

Movies are analyzed by revenue to identify the highest-grossing movies in the dataset.

### Rating Distribution

The distribution of movie ratings is visualized to understand the overall rating pattern.

### Revenue Distribution

Movie revenue values are visualized to examine their distribution and spread.

### Release Trends

The number of movies released by year is analyzed to identify changes in release activity over time.

### Average Rating by Year

Average movie ratings are calculated and visualized by release year.

### Average Revenue by Year

Average movie revenue is calculated and visualized by release year.

### Runtime Analysis

Movie runtimes are analyzed using a distribution plot.

### Votes vs. Rating

A scatter plot is used to explore the relationship between movie ratings and the number of votes.

### Correlation Analysis

A correlation matrix is generated for selected numerical variables to identify statistical relationships between them.

## Visualizations

The analysis generates the following charts:

- Top 10 Movies by Revenue
- Rating Distribution
- Revenue Distribution
- Movies by Year
- Average Rating by Year
- Average Revenue by Year
- Runtime Distribution
- Votes vs. Rating
- Correlation Matrix

All generated charts are saved in the `outputs/` directory.

## Installation

Clone the repository:

```bash
git clone https://github.com/muhammadkhazaei/movie-data-analysis.git
cd movie-data-analysis
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Analysis

Run the analysis script from the project root:

```bash
python src/analysis.py
```

The script loads the dataset, performs data cleaning and analysis, and generates the visualization files in the `outputs/` directory.

## Limitations

This project is intended for exploratory and educational purposes.

The dataset represents a limited sample of movies, so the findings should not be interpreted as general conclusions about the entire movie industry.

Correlation between variables does not imply causation.

## License

This project is licensed under the MIT License.

## Author

Muhammad Reza Khazaei

GitHub: muhammadkhazaei
