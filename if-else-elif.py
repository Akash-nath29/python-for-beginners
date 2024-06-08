# This file contains all the key concepts of 'if-else-elif' statement in Python. It covers the following topics:
# 1. if statement
# 2. else statement
# 3. elif statement
# 4. Nested if-else
# 5. Short-hand if-else

# 1. if statement:
# The 'if' statement is used to execute a block of code only if a certain condition is true. If the condition is false, the block of code is skipped. The 'if' statement is defined using the 'if' keyword followed by the condition and a colon(:). The block of code to be executed is indented. 
# Eg:
a = 10
if a > 5:
    print("a is greater than 5") #This statement will be executed as the condition is true.
# Here, we are checking if the value of 'a' is greater than 5 using the 'if' statement. Since the value of 'a' is 10 which is greater than 5, the statement "a is greater than 5" will be printed on the console.

# 2. else statement:
# The 'else' statement is used to execute a block of code if the condition in the 'if' statement is false. The 'else' statement is defined using the 'else' keyword followed by a colon(:). The block of code to be executed is indented. 
# Eg:
a = 2
if a > 5:
    print("a is greater than 5") #This statement will not be executed as the condition is false.
else:
    print("a is less than or equal to 5") #This statement will be executed as the condition is false.
# Here, we are checking if the value of 'a' is greater than 5 using the 'if' statement. Since the value of 'a' is 2 which is less than 5, the statement "a is less than or equal to 5" will be printed on the console.

# 3. elif statement:
# The 'elif' statement is used to check multiple conditions. If the condition in the 'if' statement is false, the 'elif' statement is checked. If the condition in the 'elif' statement is true, the block of code is executed. The 'elif' statement is defined using the 'elif' keyword followed by the condition and a colon(:). The block of code to be executed is indented.
# Eg:
a = 10
if a > 15:
    print("a is greater than 15") #This statement will not be executed as the condition is false.
elif a > 5:
    print("a is greater than 5") #This statement will be executed as the condition is true.
else:
    print("a is less than or equal to 5")
# Here, we are checking if the value of 'a' is greater than 15 using the 'if' statement. Since the value of 'a' is 10 which is not greater than 15, the 'elif' statement is checked. The value of 'a' is 10 which is greater than 5, so the statement "a is greater than 5" will be printed on the console.

# 4. Nested if-else:
# Nested if-else is when an 'if-else' statement is present inside another 'if-else' statement. It is used to check multiple conditions.
# Eg:
a = 10
if a > 5:
    if a > 15:
        print("a is greater than 15") #This statement will not be executed as the condition is false.
    else:
        print("a is greater than 5") #This statement will be executed as the condition is true.
else:
    print("a is less than or equal to 5")
# Here, we are checking if the value of 'a' is greater than 5 using the 'if' statement. Since the value of 'a' is 10 which is greater than 5, the inner 'if-else' statement is checked. The value of 'a' is 10 which is not greater than 15, so the statement "a is greater than 5" will be printed on the console.

# 5. Short-hand if-else:
# Short-hand if-else is a one-liner if-else statement. It is used when there is only one statement to be executed based on a condition. It is defined using the 'if' keyword followed by the condition, the 'else' keyword and the statement to be executed if the condition is false. 
# Eg:
a = 10
print("a is greater than 5") if a > 5 else print("a is less than or equal to 5") #This statement will be executed as the condition is true.
# Here, we are checking if the value of 'a' is greater than 5 using the short-hand if-else statement. Since the value of 'a' is 10 which is greater than 5, the statement "a is greater than 5" will be printed on the console.

# The above program is equivalent to the following program:
# a = 10
# if a > 5:
#     print("a is greater than 5") #This statement will be executed as the condition is true.
# else:
#     print("a is less than or equal to 5")

# That's all for the 'if-else-elif' statement in Python. In the next file, we will create a simple project to understand the implementations of if-else-elif statements in Python. (project2.py)
