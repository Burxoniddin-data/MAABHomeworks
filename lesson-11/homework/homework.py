import sqlite3

def create_roster_db():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Roster (
            Name TEXT,
            Species TEXT,
            Age INTEGER
        )
    """)
    
    characters = [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ]
    
    cursor.executemany("INSERT INTO Roster VALUES (?, ?, ?)", characters)
    
    cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")
    
    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
    print("Bajoran characters:", cursor.fetchall())
    
    cursor.execute("DELETE FROM Roster WHERE Age > 100")
    
    cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
    ranks = [
        ("Benjamin Sisko", "Captain"),
        ("Ezri Dax", "Lieutenant"),
        ("Kira Nerys", "Major")
    ]
    for name, rank in ranks:
        cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", (rank, name))
    
    cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
    print("Characters sorted by Age:", cursor.fetchall())
    
    conn.commit()
    conn.close()

def create_library_db():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            Title TEXT,
            Author TEXT,
            Year_Published INTEGER,
            Genre TEXT
        )
    """)
    
    books = [
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
        ("1984", "George Orwell", 1949, "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
    ]
    
    cursor.executemany("INSERT INTO Books VALUES (?, ?, ?, ?)", books)
    
    cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")
    
    cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
    print("Dystopian books:", cursor.fetchall())
    
    cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")
    
    cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
    ratings = [
        ("To Kill a Mockingbird", 4.8),
        ("1984", 4.7),
        ("The Great Gatsby", 4.5)
    ]
    for title, rating in ratings:
        cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (rating, title))
    
    cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
    print("Books sorted by Year Published:", cursor.fetchall())
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_roster_db()
    create_library_db()
