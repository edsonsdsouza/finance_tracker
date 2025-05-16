# Financial Tracker

A simple terminal-based Python application to track personal income and expenses using CSV files. The app allows users to add transactions and generate a financial report showing total income, total expenditure, and remaining balance.

## Requirements

- Python 3.x
- No external libraries needed (uses built-in `csv` and `os` modules)

## How It Works

- The app uses a CSV file (`ledger.csv`) to store all transactions.
- Users can enter income or expenditure transactions via a command-line menu.
- Income transactions do not require a category, while expenditures are categorized (e.g., Grocery, Electricity Bill).
- The financial report summarizes the total income, total expenditure, and remaining balance based on the stored data.
- The application uses Object-Oriented Programming principles and handles exceptions to ensure smooth operation.

## Project Structure

- `tracker/ledger.py`: Manages saving transactions to the CSV file.
- `tracker/transaction.py`: Handles user inputs and transaction flow.
- `tracker/utils.py`: Calculates and displays financial reports.
- `main.py`: Starts the application and shows the main menu.
