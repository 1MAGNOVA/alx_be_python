#!/usr/bin/env python3

#Prompt for User Input:
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

#Ask for the type of operation they’d like to perform:
operation = input("Choose the operation (+, -, *, /): ") print(operation)

print(f"Choose the operation (+, -, *, /): {operations}")

#match Case
operations:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num2 - num1
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Cannot divide by zero.")

