# # Aidan O'Connor - G00364756 - 03/02/2018 
# Week 2_Exercise 2: fibname.py
# 
#  Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.

# Instructions for Exercise 2: 
# https://github.com/ianmcloughlin/python-fib/blob/master/fibname.py
# Dr Ian McGloughlin's paragraph:
# Above is a link to a program I wrote that works similarly
# to last week's exercise. Copy and run the program yourself.
# Change the string variable to contain your own surname,
# and rerun it. Can you figure out what ord() does? 
# Try to Google it to find out. Post the output of the program,
#  along with any insight you have as to what ord() does,
#  to the discussions forum.


def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0 # set inital value of i to 0
  j = 1 # set inital value of j to 1
  n = n - 1 # whatever value is inputed for n, take 1 away from the value of n and set this value as the new value of n

  while n >= 0: # while n is greater of less than 0 do the following...
    i, j = j, i + j # i becomes the previous j value for the next iteration of code, and j becomes the prvious i value plus the previous j value
    n = n - 1 # take 1 away from n and set n as this new value
  
  return i # when the above loop has finished return the value i

name = "O'Connor" # name is set to "O'Connor" in this case
first = name[0] # give variable 'first' the value of the first letter in the string 'name'
last = name[-1] # give variable 'last' the value of the last letter in the string 'name'
firstno = ord(first) # give variable 'firstno' the value of the Unicode of the variable 'first'
lastno = ord(last) # give variable 'lastno' the value of the Unicode of the variable 'last'
x = firstno + lastno # set variable x to the value of the addition of 'firstno' and 'lastno'

ans = fib(x) # set variable ans to the value of the function fib(x)
print("My surname is", name) # Print the string and the variable 'name' to the terminal
print("The first letter", first, "is number", firstno) # Print the string and the variable 'first', and another string and the variable 'firstno' to the terminal
print("The last letter", last, "is number", lastno) # Print the string and the variable 'last'', and another string and the variable 'lastno' to the terminal
print("Fibonacci number", x, "is", ans) # Print the string and the variable 'x', and another string and the variable 'ans' to the terminal