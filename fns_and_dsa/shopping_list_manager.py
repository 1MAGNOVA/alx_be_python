#!/usr/bin/env python3
"""
Create a Python script named shopping_list_manager.py that implements a simple interface for managing a shopping list.
This task focuses on using lists to store and manipulate data dynamically.
"""

"""
Use a loop to continuously display a menu with options to the user until they choose to exit.
The menu should offer options to add an item, remove an item, view the list, and exit.
"""
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")





def shopping_list(choice):

    shopping_list = [ ]
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        for item in shopping_list:
            if choice == "1":
                shopping_list[].append(item)
             elif choice == "2":
                shopping_list.remove(item)
            elif choice == "3":
                return shopping_list
            elif choice == "4":
                print("Goodbye!")
            else:
                print("Invalid choice. Please try again.")

choice = input("Enter your choice: ")
shopping_list(choice)
