
from functools import wraps
import os
import string
from collections import Counter

def check(func):
    @wraps(func)
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b
  
class EmployeeManager:
    FILE_NAME = "employees.txt"

    @staticmethod
    def add_employee(employee_id, name, position, salary):
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(f"{employee_id}, {name}, {position}, {salary}\n")

    @staticmethod
    def view_employees():
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        with open(EmployeeManager.FILE_NAME, "r") as file:
            records = file.readlines()
            for record in records:
                print(record.strip())

    @staticmethod
    def search_employee(employee_id):
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for record in file:
                if record.startswith(str(employee_id)):
                    print(record.strip())
                    return
        print("Employee not found.")

    @staticmethod
    def update_employee(employee_id, name=None, position=None, salary=None):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        updated_records = []
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for record in file:
                data = record.strip().split(", ")
                if data[0] == str(employee_id):
                    data[1] = name if name else data[1]
                    data[2] = position if position else data[2]
                    data[3] = str(salary) if salary else data[3]
                updated_records.append(", ".join(data))
        with open(EmployeeManager.FILE_NAME, "w") as file:
            file.write("\n".join(updated_records) + "\n")

    @staticmethod
    def delete_employee(employee_id):
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No employee records found.")
            return
        updated_records = []
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for record in file:
                if not record.startswith(str(employee_id)):
                    updated_records.append(record.strip())
        with open(EmployeeManager.FILE_NAME, "w") as file:
            file.write("\n".join(updated_records) + "\n")

def word_frequency():
    file_name = "sample.txt"
    report_file = "word_count_report.txt"
    
    if not os.path.exists(file_name):
        text = input("Enter text to create sample.txt: ")
        with open(file_name, "w") as file:
            file.write(text)
    
    with open(file_name, "r") as file:
        text = file.read().lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        words = text.split()
    
    word_counts = Counter(words)
    total_words = sum(word_counts.values())
    common_words = word_counts.most_common(5)
    
    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in common_words:
        print(f"{word} - {count} times")
    
    with open(report_file, "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top 5 Words:\n")
        for word, count in common_words:
            file.write(f"{word} - {count}\n")
