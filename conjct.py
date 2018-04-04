# Aidan O'Connor - G00364756 - 06/02/2018 
# Exercise 3: The Collatz conjecture problem
# https://en.wikipedia.org/wiki/Collatz_conjecture

n = int(input("Please enter an integer: "))
while n > 1:    
  if (n % 2 == 0):        
    n = (n/2)        
    print(n)    
  elif n % 2 == 1:        
    n = ((n*3) + 1)        
    print(n)    
  else:        
    print("error")
