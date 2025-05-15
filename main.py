import sys

from tracker.transaction import Transaction

class FinancialTracker:
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
        except ValueError as e:
            print(f"ValueError: {e}")
            self.menu()
        except KeyboardInterrupt as e:
            print(e)
        else:
            if user_input == 1:
                self.transaction = Transaction()
                self.transaction.transaction_menu()
            elif user_input == 2:
                pass
            else:
                sys.exit(0)

if __name__ == "__main__":
    FinancialTracker()