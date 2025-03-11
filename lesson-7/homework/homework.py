import math
import json
import csv

class Vector:
    def __init__(self, *components):
        self.components = tuple(components)

    def __repr__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
        elif isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions")
            return sum(a * b for a, b in zip(self.components, other.components))
        raise TypeError("Multiplication with unsupported type")

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*[a / mag for a in self.components])

    def __rmul__(self, other):
        return self * other


class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"
    
    def add_employee(self, employee):
        with open(self.FILE_NAME, "a") as file:
            file.write(f"{employee}\n")
        print("Employee added successfully!")
    
    def view_all_employees(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                employees = file.readlines()
                if not employees:
                    print("No records found.")
                else:
                    for emp in employees:
                        print(emp.strip())
        except FileNotFoundError:
            print("No records found.")
    
    def search_employee(self, emp_id):
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    if line.startswith(emp_id):
                        print("Employee Found:", line.strip())
                        return
            print("Employee not found.")
        except FileNotFoundError:
            print("No records found.")


class TaskManager:
    def __init__(self, file_format="json"):
        self.file_format = file_format
        self.tasks = []
        self.load_tasks()
    
    def add_task(self, task_id, title, description, due_date, status):
        self.tasks.append({
            "task_id": task_id,
            "title": title,
            "description": description,
            "due_date": due_date,
            "status": status
        })
        print("Task added successfully!")
    
    def save_tasks(self):
        if self.file_format == "json":
            with open("tasks.json", "w") as file:
                json.dump(self.tasks, file, indent=4)
        elif self.file_format == "csv":
            with open("tasks.csv", "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["task_id", "title", "description", "due_date", "status"])
                writer.writeheader()
                writer.writerows(self.tasks)
        print("Tasks saved successfully!")
    
    def load_tasks(self):
        try:
            if self.file_format == "json":
                with open("tasks.json", "r") as file:
                    self.tasks = json.load(file)
            elif self.file_format == "csv":
                with open("tasks.csv", "r") as file:
                    reader = csv.DictReader(file)
                    self.tasks = list(reader)
        except FileNotFoundError:
            self.tasks = []

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def filter_tasks(self, status):
        filtered = [task for task in self.tasks if task["status"].lower() == status.lower()]
        for task in filtered:
            print(task)
