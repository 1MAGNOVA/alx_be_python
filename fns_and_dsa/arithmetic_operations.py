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
        'add': lambda num1, num2: num1 + num2,
        'subtract': lambda num1, num2: num1 - num2,
        'multiply': lambda num1, num2: num1 * num2,
        'divide': lambda num1, num2: num1/ num2,
        }

    try:
      if num1 > 0,
          return operation.divide()
        else:
             return "Error: Invalid operation. Please choose add, subtract, multiply, or divide."
