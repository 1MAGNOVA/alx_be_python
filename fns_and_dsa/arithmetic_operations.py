#!/usr/bin/env python3

#function named perform_operation
def perform_operation (num1, num2):
    #for add
    add = lambda num1, num2 : num1 + num2
    return(num1 + num2)

    #for subtract
    subtract = lambda num1, num2 : num2 - num1 
    return(num2 - num1)

    #for multiply
    multiply = lambda num1, num2: num1 * num2
    return(num1 * num2)

    #for divide
    try:
        divide = lambda num1, num2: num2 / num1
        return (num2/num1)
    except ZeroError:
        print("Number can't divide zero nor be be used to divide zero")
