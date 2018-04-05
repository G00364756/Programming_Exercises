# Aidan O'Connor - G00364756 - 22/02/2018
# Exercise 4, Topic 4: euler5.py
# Each new term in the Fibonacci sequence is generated,
# by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence,
# whose values do not exceed four million, find the sum of the even-valued terms.
# Code adapted from code created by Dr. Ian McGloughlin

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0 # setting an initial value for i
  j = 1 # setting an initial value for 1
  b = 0 # setting an initial value for b

  while i <= 4000000: # Loop which ends the code once i reaches a value above or equal to 4000000.
    i, j = j, i + j # i becomes the previous j value for the next iteration of code, and j becomes the prvious i value plus the previous j value
    if i % 2 == 0: # if i modulus 2 gives no remainder...
        b = b + i # add the i value to b and continue looping

  return (b) # once i reaches a value above or equal to 4000000, print the final value of b

print(fib(1)) # runs the fib formula and print the value to the terminal
