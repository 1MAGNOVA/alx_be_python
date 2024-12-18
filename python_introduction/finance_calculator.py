#!/usr/bin/env python3

# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses
total_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - total_expenses

# Project the annual savings with a 5% interest rate
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display the results
print(f"Your monthly savings are: {monthly_savings:.2f}")
print(f"Your projected annual savings with interest are: {annual_savings:.2f}")














