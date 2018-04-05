# Aidan O'Connor - G00364756 - 06/02/2018 
# Exercise 3, Topics 3: conjct.py 
# The Collatz conjecture problem
# https://en.wikipedia.org/wiki/Collatz_conjecture

def conjct(x):
  """Formula to use the collatz conjecture for any number inputted by the user"""
  n = int(input("Please enter an integer: ")) # This prompts the user to input an integer at the start of the python program
  while n > 1:    # The collatz conjecture is a function wjich continues until it reaches the number 1
    if (n % 2 == 0):  # 1st condition of collatz, if integer modulus 2 gives no remainder do the following...
      n = (n/2)  # Divide the integer by 2      
      print(n)    # print the new value
    elif n % 2 == 1:   # 2nd condition of collatz, if integer modulus 2 gives a remainder of 1 do the following...
      n = ((n*3) + 1)  # multiply the integer by 3 and add 1    
      print(n)    # print the new value 
    else:        # If none of these conditions are met there is an error with the code...
      print("error") # Print the an error message

print(conjct(1)) # print the values of the function conjct(1) to the terminal