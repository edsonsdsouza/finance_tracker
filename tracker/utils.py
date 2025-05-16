import csv
import os

class FinancialReport:
    """
    A utility class to generate a financial summary from a ledger CSV file.
    """
    
    def __init__(self, file_path):
        self.file_path = file_path
    

    def calculate_amount(self):
        """
        Calculates and displays total income, total expenditure, and balance.

        Returns:
            tuple: (total_income, total_expenditure, balance)
        """

        total_income = 0
        total_expenditure = 0

        if not os.path.exists(self.file_path):
            print(f"No ledger file found at {self.file_path}")

        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                amount = float(row['Amount'])
                if row['Type'].lower() == 'income':
                    total_income += amount
                elif row['Type'].lower() == 'expenditure':
                    total_expenditure += amount

        balance = total_income -  total_expenditure

        print(f"!!Financial Report!!")
        print(f"Total Income: ₹{total_income}")
        print(f"Total Expenditure: ₹{total_expenditure}")
        print(f"Remaining Balance: ₹{balance}")

        return total_income, total_expenditure, balance