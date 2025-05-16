import csv
import os

class Ledger:
    """
    Handles writing income and expenditure transactions to the ledger CSV file.
    """

    def __init__(self, file_path = None):

        if file_path:
            self.file_path = file_path
        else:
            # Dynamically constructs path to `data/ledger.csv` relative to this file's location
            self.file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'data', 'ledger.csv')
        
    def income(self, amount_type, amount):
        try:
            with open(self.file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([amount_type.capitalize(), 'N/A', amount]) # 'N/A' used as placeholder for category in income
        except Exception as e:
            print(f"Failed to record income!!: {e}") 
        else: 
            print("Income recorded")


    def expenditure(self, amount_type, category, amount):
        try:
            with open(self.file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([amount_type.capitalize(), category.capitalize(), amount]) # Category is included for expenditures
        except Exception as e: 
            print(f"Failed to record expenditure!!: {e}")
        else:
            print("Expenditure recorded")