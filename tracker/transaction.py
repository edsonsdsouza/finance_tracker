"""File to get the input"""

import csv
import os

from tracker.ledger import Ledger

class Transaction:
    def __init__(self, filename = None):
        if filename is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))  # .../tracker
            parent_dir = os.path.dirname(base_dir)                 # .../ledger
            self.filename = os.path.join(parent_dir, 'data', 'ledger.csv')

        else:
            self.filename = filename
        
        self.ledger = Ledger(self.filename)
        self.create_csv_if_not_exist()

    def transaction_menu(self):
        while True: 
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
                continue

            again = input("Do you want to add another transaction? (yes/no): ").strip().lower()
            if again != 'yes':
                print("Exiting... Thank you!!")
                break

    def create_csv_if_not_exist(self):
        try:
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)

            if not os.path.exists(self.filename):
                with open(self.filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Type', 'Category', 'Amount'])
                print(f"CSV will be created at: {self.filename}")
            else:
                print(f"CSV already exists at: {self.filename}")
        except Exception as e:
            return f"Something went wrong {e}. Please try again"
            
    