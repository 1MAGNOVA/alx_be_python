#!/usr/bin/env python3

#function named perform_operations
def perform_operation(num1, num2):
    #for add
    add = lambda num1, num2 : num1 + num2
    return add

    #for subtract
    subtract = lambda num1, num2 : num2 - num1 
    return subtract

    #for multiply
    multiply = lambda num1, num2: num1 * num2
    return multiply
    #for divide
    try:
        divide = lambda num1, num2: num2 / num1
        return divide
    except ZeroError:
        print("Number can't divide zero nor be be used to divide zero")
