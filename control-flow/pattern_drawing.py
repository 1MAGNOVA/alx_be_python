#!/usr/bin/env python3

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in the row
    for _ in range(size):
        print("*", end="")
    # Print a newline after completing the row
    print()
    # Increment the row counter
    row += 1
