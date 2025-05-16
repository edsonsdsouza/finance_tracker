import sys

from tracker.transaction import Transaction
from tracker.utils import FinancialReport

class FinancialTracker:
    """
    Main class to run the Financial Tracker app.
    Shows menu to add transactions or view financial report.
    """

    def __init__(self):
        self.menu()

    def menu(self):
        try: 
            user_input = int(input("""
            !!Welcome to Financial Tracker Application!!
                            
            1. Enter 1 to add transaction
            2. Enter 2 to get the financial report
            3. Enter anything else to exit
            """))
        except Exception as e:
            print(f"Something went wrong: {e}. Please try again!!")
        else:
            self.transaction = Transaction()
            
            if user_input == 1:
                self.transaction.transaction_menu()
            elif user_input == 2:
                # Reuse the same file used by the Transaction class
                report = FinancialReport(self.transaction.filename)
                report.calculate_amount()
            else:
                sys.exit(0)

if __name__ == "__main__":
    FinancialTracker()