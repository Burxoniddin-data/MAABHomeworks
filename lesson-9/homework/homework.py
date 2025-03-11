import csv
import json

class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException("A member can borrow only up to 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def add_member(self, name):
        self.members.append(Member(name))

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found in the library.")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise ValueError("Member not found.")
        book = self.find_book(book_title)
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise ValueError("Member not found.")
        book = self.find_book(book_title)
        member.return_book(book)

def calculate_average_grades(input_file, output_file):
    grades = {}
    counts = {}
    
    with open(input_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            subject = row['Subject']
            grade = int(row['Grade'])
            if subject in grades:
                grades[subject] += grade
                counts[subject] += 1
            else:
                grades[subject] = grade
                counts[subject] = 1

    averages = {subject: grades[subject] / counts[subject] for subject in grades}
    
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg in averages.items():
            writer.writerow([subject, avg])


def load_tasks(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def calculate_task_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0
    return {
        "Total tasks": total_tasks,
        "Completed tasks": completed_tasks,
        "Pending tasks": pending_tasks,
        "Average priority": avg_priority
    }

def convert_json_to_csv(json_file, csv_file):
    tasks = load_tasks(json_file)
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])

if __name__ == "__main__":
    library = Library()
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_member("Alice")
    
    try:
        library.borrow_book("Alice", "1984")
        library.return_book("Alice", "1984")
    except Exception as e:
        print(e)
    
    calculate_average_grades("grades.csv", "average_grades.csv")
    
    tasks = load_tasks("tasks.json")
    display_tasks(tasks)
    stats = calculate_task_stats(tasks)
    print(stats)
    convert_json_to_csv("tasks.json", "tasks.csv")
