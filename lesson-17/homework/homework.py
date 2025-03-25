import pandas as pd
import sqlite3

conn = sqlite3.connect('chinook.db')
customers = pd.read_sql_query("SELECT * FROM customers", conn)
invoices = pd.read_sql_query("SELECT * FROM invoices", conn)

merged_data = customers.merge(invoices, on='CustomerId', how='inner')
total_invoices_per_customer = merged_data.groupby('CustomerId').size().reset_index(name='TotalInvoices')

movies = pd.read_csv('movie.csv')
df1 = movies[['director_name', 'color']].dropna()
df2 = movies[['director_name', 'num_critic_for_reviews']].dropna()

left_join = df1.merge(df2, on='director_name', how='left')
full_outer_join = df1.merge(df2, on='director_name', how='outer')

left_join_rows = left_join.shape[0]
full_outer_join_rows = full_outer_join.shape[0]

titanic = pd.read_excel('titanic.xlsx')
grouped_titanic = titanic.groupby('Pclass').agg({
    'Age': 'mean',
    'Fare': 'sum',
    'PassengerId': 'count'
}).rename(columns={'PassengerId': 'PassengerCount'})

grouped_movies = movies.groupby(['color', 'director_name']).agg({
    'num_critic_for_reviews': 'sum',
    'duration': 'mean'
})

flights = pd.read_parquet('flights.parquet')
grouped_flights = flights.groupby(['Year', 'Month']).agg({
    'FlightNum': 'count',
    'ArrDelay': 'mean',
    'DepDelay': 'max'
})

def classify_age(age):
    return 'Child' if age < 18 else 'Adult'

titanic['Age_Group'] = titanic['Age'].apply(classify_age)

employees = pd.read_csv('employee.csv')
employees['Normalized_Salary'] = employees.groupby('Department')['Salary'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))

def classify_duration(duration):
    if duration < 60:
        return 'Short'
    elif duration <= 120:
        return 'Medium'
    else:
        return 'Long'

movies['Duration_Category'] = movies['duration'].apply(classify_duration)

def process_titanic(df):
    df = df[df['Survived'] == 1]
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    df['Fare_Per_Age'] = df['Fare'] / df['Age']
    return df

titanic = titanic.pipe(process_titanic)

def process_flights(df):
    df = df[df['DepDelay'] > 30]
    df['Delay_Per_Hour'] = df['DepDelay'] / df['CRSDepTime']
    return df

flights = flights.pipe(process_flights)
