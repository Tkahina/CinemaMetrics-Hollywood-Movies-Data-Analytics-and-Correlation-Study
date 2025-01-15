# 🎬 CinemaMetrics: Hollywood Movies Data Analytics and Correlation Study

## 📊 Project Overview
This project analyzes a dataset of movies to uncover insights
about the film industry. It explores relationships between various
factors such as budget, gross earnings, ratings, and more. 
The analysis includes data cleaning, exploratory data analysis, 
and correlation studies.

## Dataset

- **Source:** Kaggle movie dataset
The dataset contains information on 7668 movies, including:
- Numerical data: Year, Budget, Gross Earnings, Runtime, Score, Votes
- Categorical data: Company, Country, Director, Genre, Name, Rating, Star,Writer
- Date information: Release Date

## 🛠 Requirements
- Python 3.13.1
- Libraries: Pandas, NumPy, Matplotlib, Seaborn

To install the required libraries:
pip install pandas seaborn matplotlib numpy

## Project Structure
- `movie_analysis.py`: Main script containing all the analysis code
- `movies.csv`: Dataset file 
- `Function.py`: Custom functions used in the analysis (analyze_outliers)

## Key Analyses
1. Data Cleaning and Preprocessing
2. Top Grossing Movies Identification
3. Outlier Detection in Gross Earnings, Budget, and Votes
4. Top Production Companies by Total Gross Earnings
5. Top Directors by Total Gross Earnings
6. Box Office Performance Distribution by Country
7. Movie Production Trends Over Time
8. Correlation Analysis between various factors

## 🔑 Key Insights
- A strong positive correlation exists between budget and gross earnings, indicating that higher-budget films tend to perform better at the box office.
- The USA dominates global box office earnings, with significant variations observed across other countries.
- Outlier analysis revealed several blockbuster films that significantly exceed average earnings, suggesting targeted marketing strategies could be beneficial for similar productions.

## How to Run
1. Ensure you have all the required libraries installed.
2. Place `movies.csv` and `Function.py` in the same directory as `movie_analysis.py`.
3. Run the script.

## 🔮 Future Work

- Implement predictive machine learning models
- Expand dataset with more recent movies
- Develop interactive visualization dashboard












