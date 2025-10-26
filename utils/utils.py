import csv
from datetime import datetime
from collections import defaultdict

def show_menu():
    print("\n==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Category: ")
    description = input("Description: ")
    amount = float(input("Amount: "))

    with open('data/expenses.csv',"a",newline="") as f:
        writer=csv.writer(f)
        writer.writerow([date,category,description,amount])
    print("Expense updated")

def view_expenses():
    with open("data/expenses.csv", "r") as file:
        reader = csv.reader(file)
        total = 0
        print("\nDate\t\tCategory\tDescription\tAmount")
        print("-" * 50)
        for row in reader:
            if row:
                date, category, description, amount = row
                print(f"{date}\t{category}\t{description}\t${amount}")
                total += float(amount)
        print(f"\n💰 Total Spent: ${total}")

def delete_expense():
    expense=[]
    delete_description=input("Enter the description to delete :")
    with open('data/expenses.csv','r') as file:
        reader=csv.reader(file)
        for row in reader:
            if(row[2] != delete_description):
                expense.append(row)
    with open('data/expenses.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(expense)
    print(f"Expense Deleted : {delete_description}")