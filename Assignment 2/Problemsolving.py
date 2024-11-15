'''
Author: Girisha Daggula
Student ID: 100974333
Date: 15/11/2024
Description: Displays the results of monthly expenses using pandas and matplotlib library
'''

import pandas as pd   #Importing Pandas to manipulate and analyze data
import matplotlib.pyplot as plt  # importing matplotlib for data visualization

class FinanceTracker:   # To tarck the transactions and expenses
    def __init__(self):     #intializing the finance tracker to store the data
        self.data = pd.DataFrame(columns=["Date", "Category", "Amount", "Type"])
    
    def add_transaction(self, date, category, amount, transaction_type):     #Adding a transaction to the tracker
    
        try:
           date = pd.to_datetime(date)    #Converting date to a pandas datetime object
           if transaction_type not in ["Income", "Expense"]:
            raise ValueError("Transaction type must be 'Income' or 'Expense'")
           amount = float(amount)       #Amount should be numeric
           new_transaction = pd.DataFrame([{       #creating a new transaction
                "Date": date,
                "Category": category,
                "Amount": amount,
                "Type": transaction_type
           }])
           if new_transaction.isnull().values.any():     #Checking if new transaction containing a valid data
            new_transaction = new_transaction.dropna()      
           if not new_transaction.empty:
               self.data = pd.concat([self.data, new_transaction], ignore_index=True)     # Concatinating the new data if it has a valid data
           else: 
            print("The transaction contains no data and will not be added.")
        except Exception as e:
            print(f"Error adding transaction: {e}")
    
    def monthly_summary(self, month):        # generates a monthly summary
        monthly_data = self.data[self.data['Date'].dt.month == month]         # transactions by the specified month
        if monthly_data.empty:
            return "No transactions for the specified month."
        summary = monthly_data.groupby('Category')['Amount'].sum()        #Calculate the total amount for each category
        return summary
    
    def visualize_expenses(self, month):               #Transactions for a given month as a bar graph
        monthly_data = self.data[self.data['Date'].dt.month == month]
        expenses = monthly_data[monthly_data['Type'] == 'Expense']       #Transactions are filtered for the specified by the month and type
        if expenses.empty:  
            print("No expenses to display for this month.")
            return
        plt.figure(figsize=(10, 6))                   # Shows up the bar graph by category
        expenses.groupby('Category')['Amount'].sum().plot(kind='bar')
        plt.title('Monthly Expenses by Category')      # Title
        plt.xlabel('Category')      #X-axis
        plt.ylabel('Amount')        #Y-axis
        plt.xticks(rotation=45)
        plt.tight_layout()          #Layout for better display
        plt.show()

if __name__ == "__main__":
    tracker = FinanceTracker()
    tracker.add_transaction("2024-11-12", "Salary", 3000, "Income")       #Below 3 are Sample transactions
    tracker.add_transaction("2024-11-13", "Groceries", 150, "Expense")
    tracker.add_transaction("2024-11-15", "Utilities", 100, "Expense")
    
    print(tracker.monthly_summary(11))      #printing a monthly summary
    tracker.visualize_expenses(11)             # Visualizing the expenses done in a month
