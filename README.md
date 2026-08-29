Movie Data Analysis
An exploratory movie data analysis project built with Python, Pandas, Matplotlib, and Seaborn.
Project Overview
This project analyzes a dataset of 1,000 movies to explore movie ratings, revenue, popularity, votes, runtime, and release trends.
The goal is to demonstrate a practical data analysis workflow, including data inspection, cleaning, exploratory analysis, statistical summaries, and data visualization.
Business Questions
This project explores questions such as:
Which movies have the highest ratings?
Which movies generate the most revenue?
Which movies receive the most votes?
How are movie ratings distributed?
How does movie revenue vary across the dataset?
How has the number of movies released changed over time?
How has average movie rating changed over time?
How has average movie revenue changed over time?
Is there a relationship between movie ratings and the number of votes?
Which numerical variables are correlated?
Dataset
The dataset contains 1,000 movie records with information including:
Movie title
Genre
Description
Director
Actors
Release year
Runtime
Rating
Number of votes
Revenue
Metascore
The dataset is used for educational and portfolio purposes.
Tech Stack
Python 3
Pandas
Matplotlib
Seaborn
Project Structure
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
└── README.md
Analysis Workflow
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
Cleaned Dataset & Charts
Data Cleaning
The analysis script performs several basic data quality operations:
Removes duplicate records
Converts numeric columns to appropriate numeric types
Handles invalid numeric values
Removes rows missing important analysis fields
Filters out movies with non-positive revenue for revenue-based analysis
Analysis
Top Rated Movies
The project identifies the highest-rated movies while considering the number of votes.
Revenue Analysis
Movies are ranked by revenue to identify the highest-grossing titles in the dataset.
Rating Distribution
A histogram is used to examine how movie ratings are distributed.
Revenue Distribution
The distribution of movie revenue is visualized to identify the overall pattern and spread of revenue values.
Release Trends
The project analyzes the number of movies released by year and calculates the average rating and average revenue over time.
Runtime Analysis
Movie runtimes are analyzed to understand the distribution of movie lengths.
Votes vs Rating
A scatter plot is used to explore the relationship between movie ratings and the number of votes.
Correlation Analysis
A correlation matrix is calculated for selected numerical variables, including:
Year
Runtime
Rating
Votes
Revenue
Metascore
Visualizations
The analysis generates the following visualizations:
Top 10 Movies by Revenue
Movie Rating Distribution
Movie Revenue Distribution
Number of Movies Released by Year
Average Movie Rating by Year
Average Movie Revenue by Year
Movie Runtime Distribution
Votes vs Rating
Correlation Matrix
All generated charts are saved in the outputs/ directory.
Getting Started
1. Clone the repository
git clone https://github.com/muhammadkhazaei/movie-data-analysis.git
cd movie-data-analysis
2. Install dependencies
pip install -r requirements.txt
3. Run the analysis
python src/analysis.py
The analysis results and generated charts will be saved in the outputs/ directory.
Output
Running the analysis generates:
outputs/
├── top_10_movies_by_revenue.png
├── rating_distribution.png
├── revenue_distribution.png
├── movies_by_year.png
├── average_rating_by_year.png
├── average_revenue_by_year.png
├── runtime_distribution.png
├── votes_vs_rating.png
├── correlation_matrix.png
└── cleaned_movies.csv
Limitations
This dataset contains a limited number of movie records and is intended primarily for exploratory analysis.
The analysis describes patterns in the available data and does not establish causal relationships between variables.
License
This project is licensed under the MIT License.
Author
Muhammad Reza Khazaei
GitHub: muhammadkhazaei
