#!/usr/bin/env python3

from datetime import *


#display function display_current_datetime
def display_current_datetime():
    current_date = datetime.datetime.now()  # Get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date in YYYY-MM-DD HH:MM:SS
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    # Prompt user to enter number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))

    current_date = datetime.datetime.now()  # Get current date and time
    future_date = current_date + datetime.timedelta(days=days_to_add)  # Calculate future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date in YYYY-MM-DD
    print(f"Future date: {formatted_future_date}")

# Main function to execute the script
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
