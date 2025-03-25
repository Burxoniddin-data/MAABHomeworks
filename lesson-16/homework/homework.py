import pandas as pd
import sqlite3

# Part 1: Reading Files

# 1. Read customers table from chinook.db
conn = sqlite3.connect('chinook.db')
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print(customers_df.head(10))
conn.close()

# 2. Load iris.json
iris_df = pd.read_json('iris.json')
print("Shape:", iris_df.shape)
print("Columns:", iris_df.columns)

# 3. Load titanic.xlsx
titanic_df = pd.read_excel('titanic.xlsx')
print(titanic_df.head())

# 4. Load Flights parquet file
flights_df = pd.read_parquet('flights.parquet')
print(flights_df.info())

# 5. Load movie.csv
movie_df = pd.read_csv('movie.csv')
print(movie_df.sample(10))

# Part 2: Exploring DataFrames

# 1. iris.json DataFrame
iris_df.columns = iris_df.columns.str.lower()
selected_iris = iris_df[['sepal_length', 'sepal_width']]

# 2. titanic.xlsx DataFrame
filtered_titanic = titanic_df[titanic_df['age'] > 30]
gender_counts = titanic_df['sex'].value_counts()

# 3. Flights parquet DataFrame
flights_subset = flights_df[['origin', 'dest', 'carrier']]
unique_destinations = flights_df['dest'].nunique()

# 4. movie.csv DataFrame
long_movies = movie_df[movie_df['duration'] > 120]
sorted_movies = long_movies.sort_values(by='director_facebook_likes', ascending=False)

# Part 3: Challenges and Explorations

# 1. Statistics on iris.json
descriptive_stats = iris_df.describe()

# 2. Age stats from titanic.xlsx
age_min = titanic_df['age'].min()
age_max = titanic_df['age'].max()
age_sum = titanic_df['age'].sum()

# 3. movie.csv Challenges
top_director = movie_df.groupby('director_name')['director_facebook_likes'].sum().idxmax()
top_5_longest_movies = movie_df.nlargest(5, 'duration')[['title', 'director_name']]

# 4. Handling missing values in flights.parquet
missing_values = flights_df.isnull().sum()
numeric_columns = flights_df.select_dtypes(include=['number']).columns
flights_df[numeric_columns] = flights_df[numeric_columns].fillna(flights_df[numeric_columns].mean())

# Display results
print("Filtered Titanic Data:", filtered_titanic.head())
print("Gender Counts:", gender_counts)
print("Unique Destinations:", unique_destinations)
print("Top Director with Most Likes:", top_director)
print("Top 5 Longest Movies:", top_5_longest_movies)
print("Missing Values:", missing_values)
