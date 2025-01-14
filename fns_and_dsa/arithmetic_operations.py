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
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: "Error: Division by zero is not allowed." if y == 0 else x / y
    }

    func = operations.get(operation)
    if func:
        return func(num1, num2)
    else:
        return "Error: Invalid operation. Please choose add, subtract, multiply, or divide."
