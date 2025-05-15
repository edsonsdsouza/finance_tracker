"""File to get the input"""

import csv
import os

from tracker.ledger import Ledger

class Transaction:
    def __init__(self, filename = "../data/finance_tracker.csv"):
        self.ledger = Ledger()
        self.filename = filename
        self.create_csv_if_not_exist()
        self.transaction_menu()

    def transaction_menu(self):
        print("!!Please enter the details!!")
        amount_type = input("Enter the type (Income or Expenditure): ").strip().lower()
        amount = int(input("Enter the amount ₹"))
        if amount_type == "income":
            self.ledger.income(amount_type, amount)
        elif amount_type == "expenditure":
            category = input("Enter the category (Grocery, Online Shopping, Pharmacy, Electricity Bill, Water Bill, Other)").strip().lower()
            self.ledger.expenditure(amount_type, category, amount)
        else:
            print("Enter the valid input")
            self.transaction_menu()

    def create_csv_if_not_exist(self):
        try:
            if not os.path.exists(self.filename):
                with open(self.filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Type', 'Category', 'Amount'])
        except Exception as e:
            return f"Something went wrong {e}. Please try again"
            
    