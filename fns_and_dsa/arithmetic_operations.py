#!/usr/bin/env python3

#function named perform_operations

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations using lambda functions.

    Parameters:
    - num1 (float): The first number.
    - num2 (float): The second number.
    - operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    - Result of the operation, or a string message for invalid operations or division by zero.
    """
    if operations == "add":
        add = lambda num1, num2: num1 + num2
        return add
    elif operations == 'subtract': 
        subtract = lambda num1, num2: num1 - num2
        return subtract
    elif operations == 'multiply': 
        multiply = lambda num1, num2: num1 * num2
        return multiply
    else operation == 'divide': 
        if num == 0:
            return "error: invalid operation. number cannot be divided by zero"
        else:
            divide = lambda num1, num2: num1/ num2
            return divide
