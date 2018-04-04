# Aidan O'Connor - G00364756 - 06/02/2018 
# Week 6 Exercise 5 - Format output of the iris.csv file
# Link to csv file = https://archive.ics.uci.edu/ml/datasets/iris
# Code adapted from Dr. Ian McGloughlin's lectures during Week 6 of the Programming and Scripting module.

# Exercise 5:- 
# Please complete the following exercise this week. 
# Write a Python script that reads the Iris data set in 
# and prints the four numerical values on each row in a nice format. 
# That is, on the screen should be printed the petal length,
# petal width, sepal length and sepal width, 
# and these values should have the decimal places aligned, 
# with a space between the columns.

with open("Data_sets/iris.csv") as f:#Opens the csv file
    for line in f:
        jay = line.split(",") #splits the data in the csv file into separate lists of strings based on the length of the line of the data set.
        print('{:6}{:6}{:6}{:6}{:6}'.format(jay[0],jay[1],jay[2],jay[3],jay[4]),end="") # Chooses the strings in position 0,1,2,3 and 4 of each line of the list "jay"(each line contains 5 strings) and formats the output to justify by 6 spaces for each string in the line.