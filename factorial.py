# Aidan O'Connor - G00364756 - 12/03/2018 
# Week 7_Exercise 6,Topic 6: factorial.py
# Code adapted from lectures given by Dr. Ian McGLouglin through the Programming module in the Data Analytics course


# Instructions for Exercise 6:
# Please complete the following exercise this week. 
# Write a Python script containing a function called factorial() that,
# takes a single input/argument which is a positive integer and,
# returns its factorial. The factorial of a number is that number,
# multiplied by all of the positive numbers less than it. 
# For example, the factorial of 5 is 5x4x3x2x1 which equals 120. 
# You should, in your script, test the function by calling it with,
# the values 5, 7, and 10.

def factorial(number):
    """Calculates the factorial of an inputted number"""
    product = number # set the product to the number inputted by user so the function has a starting point for its range
    for i in range ((number - 1), 1, -1): #runs through the range of the number inputted by the user all the way down to the integer "1" and decriments by a step of 1.
        product = product*i #multiplies the variable product by every value of i in the range "((number-1), 1, -1)""
    return(product)

print(factorial(number = int(input("Please enter an integer: ")))) # allows user to input the integer that is to be used in the factorial function and outputs the result
print(factorial(5)) #tests the result of 5 factorial, prints output
print(factorial(7)) #tests the result of 5 factorial, prints output
print(factorial(10)) #tests the result of 5 factorial, prints output
