# Create a simple program that will take the age of a person as input and print the category of the person based on the age. The categories are as follows:
# 1. Child: Age less than 13
# 2. Teen: Age between 13 and 19
# 3. Adult: Age between 20 and 59
# 4. Senior: Age 60 and above

# Take age as input
age = int(input("Enter your age: "))
# Check the category based on age
if age < 13:
    print("Child")
elif age >= 13 and age <= 19: #We can also write this as 13 <= age <= 19
    print("Teen")
elif age >= 20 and age <= 59: #We can also write this as 20 <= age <= 59
    print("Adult")
else:
    print("Senior")

# Output:
# Enter your age: 25
# Adult

# Enter your age: 10
# Child

# Enter your age: 16
# Teen


# In this program, we are taking the age of a person as input using the input function. We are then checking the category of the person based on the age using the if-elif-else statement. If the age is less than 13, we print "Child". If the age is between 13 and 19, we print "Teen". If the age is between 20 and 59, we print "Adult". If the age is 60 or above, we print "Senior". The output is displayed based on the age entered by the user.

# That's all for the 'if-else-elif' statement in Python. In the next file, we will learn about non-primitive datatypes (List Dictionary, Tuple) in Python. (non-primitive-datatypes.py)