from expense import Expense
import csv
import os

def header(filename):
    if not os.path.isfile(filename) or os.path.getsize(filename) == 0:
        head = ["amount", "date", "category", "description"]
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(head)

def save_expense(expense, filename):
    file_exists = os.path.isfile(filename)
    need_header = not file_exists or os.path.getsize(filename) == 0

    with open(filename, mode='a', newline='') as file:
        fieldnames = ["amount", "date", "category", "description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if need_header:
            writer.writeheader()
        writer.writerow({
            "amount": expense.amount,
            "date": expense.date,
            "category": expense.category,
            "description": expense.description
        })

def read_all_expenses(filename):
    expenses = []
    if not os.path.isfile(filename) or os.path.getsize(filename) == 0:
        return expenses
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expense = Expense.from_csv_row(row)
            expenses.append(expense)
    return expenses

        
        
        
        
        
        
        