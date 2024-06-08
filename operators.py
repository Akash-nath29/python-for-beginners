# This file contains all the key concepts of operators. It covers the following topics:
# 1. Arithmetic operators
# 2. Assignment operators
# 3. Comparison operators
# 4. Logical operators
# 5. Identity operators
# 6. Membership operators
# 7. Bitwise operators

# 1. Arithmetic operators:
# Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication etc.
# Python supports the following arithmetic operators:
# a. Addition (+)
# b. Subtraction (-)
# c. Multiplication (*)
# d. Division (/)
# e. Modulus (%)
# f. Exponentiation (**)
# g. Floor division (//)

# a. Addition (+):
a = 10
b = 20
c = a + b
print(c) #Output: 30

# b. Subtraction (-):
a = 10
b = 20
c = a - b
print(c) #Output: -10

# c. Multiplication (*):
a = 10
b = 20
c = a * b
print(c) #Output: 200

# d. Division (/):
a = 10
b = 20
c = a / b
print(c) #Output: 0.5

# e. Modulus (%):
a = 10
b = 20
c = a % b #Remainder when a is divided by b
print(c) #Output: 10

# f. Exponentiation (**):
a = 10
b = 2
c = a ** b #a raised to the power b
print(c) #Output: 100

# g. Floor division (//):
a = 10
b = 3
c = a // b #Quotient when a is divided by b
print(c) #Output: 3


# 2. Assignment operators:
# Assignment operators are used to assign values to variables. Python supports the following assignment operators:
# a. = (Assignment operator)
# b. += (Addition assignment)
# c. -= (Subtraction assignment)
# d. *= (Multiplication assignment)
# e. /= (Division assignment)
# f. %= (Modulus assignment)
# g. **= (Exponentiation assignment)
# h. //= (Floor division assignment)

# a. = (Assignment operator):
a = 10
print(a) #Output: 10

# b. += (Addition assignment):
a = 10
a += 20 #Equivalent to a = a + 20
print(a) #Output: 30

# c. -= (Subtraction assignment):
a = 10
a -= 20 #Equivalent to a = a - 20
print(a) #Output: -10

# d. *= (Multiplication assignment):
a = 10
a *= 20 #Equivalent to a = a * 20
print(a) #Output: 200

# e. /= (Division assignment):
a = 10
a /= 20 #Equivalent to a = a / 20
print(a) #Output: 0.5

# f. %= (Modulus assignment):
a = 10
a %= 20 #Equivalent to a = a % 20
print(a) #Output: 10

# g. **= (Exponentiation assignment):
a = 10
a **= 2 #Equivalent to a = a ** 2
print(a) #Output: 100

# h. //= (Floor division assignment):
a = 10
a //= 3 #Equivalent to a = a // 3
print(a) #Output: 3



# 3. Comparison operators:
# Comparison operators are used to compare two values. Python supports the following comparison operators:
# a. == (Equal to)
# b. != (Not equal to)
# c. > (Greater than)
# d. < (Less than)
# e. >= (Greater than or equal to)
# f. <= (Less than or equal to)

# a. == (Equal to):
a = 10
b = 20
c = a == b #Returns True if a is equal to b, False otherwise
print(c) #Output: False

# b. != (Not equal to):
a = 10
b = 20
c = a != b #Returns True if a is not equal to b, False otherwise
print(c) #Output: True

# c. > (Greater than):
a = 10
b = 20
c = a > b #Returns True if a is greater than b, False otherwise
print(c) #Output: False

# d. < (Less than):
a = 10
b = 20
c = a < b #Returns True if a is less than b, False otherwise
print(c) #Output: True

# e. >= (Greater than or equal to):
a = 10
b = 20
c = a >= b #Returns True if a is greater than or equal to b, False otherwise
print(c) #Output: False

# f. <= (Less than or equal to):
a = 10
b = 20
c = a <= b #Returns True if a is less than or equal to b, False otherwise
print(c) #Output: True


# 4. Logical operators:
# Logical operators are used to combine conditional statements. Python supports the following logical operators:
# a. and (Logical AND)
# b. or (Logical OR)
# c. not (Logical NOT)

# a. and (Logical AND):
a = True
b = False
c = a and b #Returns True if both a and b are True, False otherwise
print(c) #Output: False

# b. or (Logical OR):
a = True
b = False
c = a or b #Returns True if either a or b is True, False otherwise
print(c) #Output: True

# c. not (Logical NOT):
a = True
c = not a #Returns True if a is False, False otherwise
print(c) #Output: False


# 5. Identity operators:
# Identity operators are used to compare the memory locations of two objects. Python supports the following identity operators:
# a. is (Returns True if both variables point to the same memory location)
# b. is not (Returns True if both variables do not point to the same memory location)

# a. is (Returns True if both variables point to the same memory location):
a = 10
b = 10
c = a is b #Returns True if a and b point to the same memory location, False otherwise
print(c) #Output: True

# b. is not (Returns True if both variables do not point to the same memory location):
a = 10
b = 20
c = a is not b #Returns True if a and b do not point to the same memory location, False otherwise
print(c) #Output: True


# 6. Membership operators:
# Membership operators are used to test if a sequence is present in an object. Python supports the following membership operators:
# a. in (Returns True if a sequence is present in an object)
# b. not in (Returns True if a sequence is not present in an object)

# a. in (Returns True if a sequence is present in an object):
a = [1, 2, 3, 4, 5] # List (a.k.a Array), we will cover lists in the data structures topic
b = 3
c = b in a # Returns True if b is present in a, False otherwise
print(c) #Output: True

# b. not in (Returns True if a sequence is not present in an object):
a = [1, 2, 3, 4, 5] # List (a.k.a Array), we will cover lists in the data structures topic
b = 6
c = b not in a # Returns True if b is not present in a, False otherwise
print(c) #Output: True


# 7. Bitwise operators:
# Bitwise operators are used to perform bitwise operations on integers. Python supports the following bitwise operators:
# a. & (Bitwise AND)
# b. | (Bitwise OR)
# c. ^ (Bitwise XOR)
# d. ~ (Bitwise NOT)
# e. << (Bitwise left shift)
# f. >> (Bitwise right shift)

# a. & (Bitwise AND):
a = 10
b = 20
c = a & b #Bitwise AND of a and b
print(c) #Output: 0

# b. | (Bitwise OR):
a = 10
b = 20
c = a | b #Bitwise OR of a and b
print(c) #Output: 30

# c. ^ (Bitwise XOR):
a = 10
b = 20
c = a ^ b #Bitwise XOR of a and b
print(c) #Output: 30

# d. ~ (Bitwise NOT):
a = 10
c = ~a #Bitwise NOT of a
print(c) #Output: -11

# e. << (Bitwise left shift):
a = 10
b = 2
c = a << b #Bitwise left shift of a by b places
print(c) #Output: 40

# f. >> (Bitwise right shift):
a = 10
b = 2
c = a >> b #Bitwise right shift of a by b places
print(c) #Output: 2

# That's all for the operators in python programming. In the next file, we will cover the basics of strings in python. (strings.py)