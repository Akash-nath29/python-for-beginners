# This file containes all the key concepts of variables. It covers the following topics:
# 1. Variables
# 2. Variable assignment
# 3. Data types
# 4. Type conversion
# 5. Variable naming conventions
# 6. Multiple assignment
# 7. Constants
# 9. Printing variables

# 1. Variables:
# Variables are used to store data. They are used to store data temporarily in the memory. Variables are like empty buckets. You can put anything in them. You can change the value of a variable as many times as you want. You can call the variable with any name you like.

#Eg:

a = 10

# Here 'a' is a variable. It is used to store the value 10. The value of 'a' can be changed as many times as you want and you can call the variable with any name you like. In the above statement we are instructing the computer to store the value 10 in the memory location of variable 'a'.

# 2. Variable assignment:
# Variable assignment is the process of assigning a value to a variable. It is done using the assignment operator '='.
# Eg:
a = 15
# Here we are assigning the value 10 to the variable named 'a' using the assignment operator '='. The value of 'a' is now 10.



# 3. Data types:
# Data types are used to specify the type of data that a variable can store. Python has the following primitive data types:
# a. int
# b. float
# c. str
# d. bool

# a. int:
# Integers are whole numbers. They can be positive or negative. Eg: 0, 1, 2, 3, -1, -2, -3 etc.
#Eg:
a = 100
# Here 'a' is a variable of type int. It is used to store the value 100.

# b. float:
# Floats are real numbers. They can be positive or negative. They can have decimal points. Eg: 0.0, 1.0, 2.0, 3.0, -1.0, -2.0, -3.0 etc.
#Eg:
a = 100.5
# Here 'a' is a variable of type float. It is used to store the value 100.5.

# c. str:
# Strings are sequences of characters. They are enclosed within single quotes('') or double quotes(""). Eg: 'Hello', "World", "123" etc.
#Eg:
a = "Hello"
# Here 'a' is a variable of type str. It is used to store the value "Hello".

# d. bool:
# Booleans are used to represent the truth values. They can have two values: True or False.
#Eg:
a = True
# Here 'a' is a variable of type bool. It is used to store the value True.


# 4. Type conversion:
# Type conversion is the process of converting one data type to another. Python has the following built in functions for type conversion:
# a. int()
# b. float()
# c. str()
# d. bool()

# a. int():
# int() function is used to convert a data type to int.
#Eg:
a = 10.5
b = int(a)
print(b) #Output: 10
# Here 'a' is a variable of type float. We are converting the float to int using the int() function. The value of 'b' will be 10.

c = "100"
d = int(c)
print(d) #Output: 100
# Here 'c' is a variable of type str. We are converting the str to int using the int() function. The value of 'd' will be 100.

# b. float():
# float() function is used to convert a data type to float.
#Eg:
a = 10
b = float(a)
print(b) #Output: 10.0
# Here 'a' is a variable of type int. We are converting the int to float using the float() function. The value of 'b' will be 10.0.

c = "100"
d = float(c)
print(d) #Output: 100.0
# Here 'c' is a variable of type str. We are converting the str to float using the float() function. The value of 'd' will be 100.0.

# c. str():
# str() function is used to convert a data type to str.
#Eg:
a = 10
b = str(a)
print(b) #Output: "10"
# Here 'a' is a variable of type int. We are converting the int to str using the str() function. The value of 'b' will be "10".

c = 100.5
d = str(c)
print(d) #Output: "100.5"
# Here 'c' is a variable of type float. We are converting the float to str using the str() function. The value of 'd' will be "100.5".

# d. bool():
# bool() function is used to convert a data type to bool.
#Eg:
a = 1
b = bool(a)
print(b) #Output: True
# Here 'a' is a variable of type int. We are converting the int to bool using the bool() function. The value of 'b' will be True.

c = 0
d = bool(c)
print(d) #Output: False
# Here 'c' is a variable of type int. We are converting the int to bool using the bool() function. The value of 'd' will be False.


# 5. Variable naming conventions:
# Variable names are case sensitive. They can contain letters, digits and underscores. They cannot start with a digit. They cannot contain spaces. They cannot be a keyword. They should be descriptive and meaningful. They should be in lowercase. They should not be too long. They should not be too short. They should not be too cryptic. They should not be too similar to other variables.

#Eg:
#Valid variable names:
a = 10
b = 20
c = 30
d = 40
e = 50

#Invalid variable names:
# 1a = 10
# a b = 20
# a-b = 30
# a$b = 40
# a b = 50
# if = 10
# while = 20


# 6. Multiple assignment:
# Multiple assignment is the process of assigning multiple values to multiple variables in a single statement. It is done using the assignment operator '='.
#Eg:
a, b, c = 10, 20, 30
# Here we are assigning the value 10 to the variable 'a', the value 20 to the variable 'b' and the value 30 to the variable 'c' in a single statement.


# 7. Constants:
# Constants are variables whose values cannot be changed. They are used to store values that are not supposed to be changed. They are written in uppercase letters.
#Eg:
PI = 3.14
# Here 'PI' is a constant. It is used to store the value 3.14. The value of 'PI' cannot be changed.
PI = "Pie"
# This will throw an error. The value of a constant cannot be changed.


# 8. Printing variables:
# You can print the value of a variable using the print() function. As you have seen in the 'basics.py' file, the print() function is used to display the output on the console. You can pass the variable as an argument to the print() function to print the value of the variable.
#Eg:
a = 10
print(a) #Output: 10

b = 20
print(b) #Output: 20


# That's all for the variables in python. In the next file, we will cover the operators in python. (operators.py)