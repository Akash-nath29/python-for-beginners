# This file contains all the key points of 'input' function in Python. It covers the following topics:
# 1. Input function
# 2. Type conversion

# 1. Input function:
# The input function is used to take input from the user. It is a pre-defined function in Python. The input function takes a string as an argument which is displayed on the console. The user can enter the input in the console and press enter. The input function returns the input entered by the user as a string. 
# Eg:
name = input("Enter your name: ")
print("Hello", name)
# Here, we are taking the input from the user using the input function. The string "Enter your name: " is displayed on the console. The user enters the name and presses enter. The input entered by the user is stored in the variable 'name'. The value of 'name' is then printed using the print function.

age = input("Enter your age: ")
print("You are", age, "years old")
# Here, we are taking the input from the user using the input function. The string "Enter your age: " is displayed on the console. The user enters the age and presses enter. The input entered by the user is stored in the variable 'age'. The value of 'age' is then printed using the print function.

# 2. Type conversion:
# The input function always returns the input entered by the user as a string. If we want to perform any operations on the input, we need to convert it to the appropriate data type. We can use the following built-in functions for type conversion: 
# a. int()
# b. float()
# c. str()
# d. bool()

# Eg:
age = input("Enter your age: ")
age = int(age)
print("You are", age, "years old")
# Here, we are taking the input from the user using the input function. The input entered by the user is stored in the variable 'age'. We are converting the input to an integer using the int() function. The value of 'age' is then printed using the print function.

height = input("Enter your height in meters: ")
height = float(height)
print("Your height is", height, "meters")
# Here, we are taking the input from the user using the input function. The input entered by the user is stored in the variable 'height'. We are converting the input to a float using the float() function. The value of 'height' is then printed using the print function.

# That's all for the 'input' function in Python. In the next file, we will cover the 'if-else-elif' statement in Python. (if-else-elif.py)