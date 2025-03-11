import math
import json
import csv

# Farm Model
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Cow(Animal):
    def moo(self):
        print(f"{self.name} says Moo!")

class Chicken(Animal):
    def cluck(self):
        print(f"{self.name} says Cluck!")

class Sheep(Animal):
    def baa(self):
        print(f"{self.name} says Baa!")

# Bank Application
class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

class Bank:
    FILE_NAME = "accounts.txt"
    
    def __init__(self):
        self.accounts = {}
        self.load_from_file()
    
    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        print(f"Account created: {account_number}, Name: {name}, Balance: {initial_deposit}")
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account {account.account_number}: {account.name}, Balance: {account.balance}")
        else:
            print("Account not found.")
    
    def save_to_file(self):
        with open(self.FILE_NAME, "w") as file:
            for acc in self.accounts.values():
                file.write(f"{acc.account_number},{acc.name},{acc.balance}\n")
    
    def load_from_file(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    acc_number, name, balance = line.strip().split(",")
                    self.accounts[int(acc_number)] = Account(int(acc_number), name, float(balance))
        except FileNotFoundError:
            pass
