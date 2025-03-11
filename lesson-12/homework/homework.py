from bs4 import BeautifulSoup
import sqlite3
import requests
import json
import csv

def scrape_weather():
    with open("weather.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    weather_data = []
    rows = soup.find("tbody").find_all("tr")
    
    for row in rows:
        cols = row.find_all("td")
        day, temp, condition = cols[0].text, int(cols[1].text[:-2]), cols[2].text
        weather_data.append((day, temp, condition))
    
    highest_temp_day = max(weather_data, key=lambda x: x[1])
    sunny_days = [day for day, temp, condition in weather_data if condition == "Sunny"]
    avg_temp = sum(temp for _, temp, _ in weather_data) / len(weather_data)
    
    print("Weather Forecast:")
    for day, temp, condition in weather_data:
        print(f"{day}: {temp}°C, {condition}")
    print(f"\nHottest Day: {highest_temp_day[0]} with {highest_temp_day[1]}°C")
    print(f"Sunny Days: {', '.join(sunny_days)}")
    print(f"Average Temperature: {avg_temp:.2f}°C")

def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    job_listings = []
    jobs = soup.find_all("div", class_="card-content")
    
    for job in jobs:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        description = job.find("div", class_="description").text.strip()
        link = job.find("a")['href']
        job_listings.append((title, company, location, description, link))
    
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            link TEXT,
            UNIQUE(title, company, location)
        )
    """)
    
    for job in job_listings:
        cursor.execute("INSERT OR IGNORE INTO jobs (title, company, location, description, link) VALUES (?, ?, ?, ?, ?)", job)
    
    conn.commit()
    conn.close()
    print("Job data saved to SQLite database.")

def scrape_laptops():
    url = "https://demoblaze.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    laptops = []
    products = soup.find_all("div", class_="card-block")
    
    for product in products:
        name = product.find("h4", class_="card-title").text.strip()
        price = product.find("h5").text.strip()
        description = product.find("p", class_="card-text").text.strip()
        laptops.append({"name": name, "price": price, "description": description})
    
    with open("laptops.json", "w", encoding="utf-8") as file:
        json.dump(laptops, file, indent=4)
    print("Laptop data saved to JSON file.")

if __name__ == "__main__":
    scrape_weather()
    scrape_jobs()
    scrape_laptops()
