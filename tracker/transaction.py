import csv
import os

from tracker.ledger import Ledger

class Transaction:
    """
    This class handles user input for income and spending,
    and saves the data using the Ledger class.
    It also makes sure the CSV file is created if it doesn't exist.
    """

    def __init__(self, filename = None):
        if filename is None:
            # Build the path to the CSV file in the 'data' folder
            base_dir = os.path.dirname(os.path.abspath(__file__)) # points to /tracker
            parent_dir = os.path.dirname(base_dir) # points to the parent folder             
            self.filename = os.path.join(parent_dir, 'data', 'ledger.csv')
        else:
            self.filename = filename
        
        # Create Ledger object with the correct file path
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
                continue # Go back to the top if input is wrong

            # Ask if the user wants to enter more transactions
            again = input("Do you want to add another transaction? (yes/no): ").strip().lower()
            if again != 'yes':
                print("Exiting... Thank you!!")
                break # Stop the loop if they say no

    def create_csv_if_not_exist(self):
        try:
            # Make sure the folder exists
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)

            # Create the file with headers if it doesn't exist
            if not os.path.exists(self.filename):
                with open(self.filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Type', 'Category', 'Amount']) # Write the headers
                print(f"CSV will be created at: {self.filename}")
            else:
                print(f"CSV already exists at: {self.filename}")
        except Exception as e:
            return f"Something went wrong {e}. Please try again"
            
    