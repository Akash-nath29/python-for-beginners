# This file contains all the key concepts of 'non-primitive datatypes' in Python. It covers the following topics:
# 1. List
# 2. Dictionary
# 3. Tuple

# 1. List:
# A list is a collection of items that are ordered and changeable. Lists are defined using square brackets([]). The items in a list are separated by commas. Lists can contain items of different data types. Lists are mutable, which means the items in a list can be changed.
# Eg:
fruits = ["apple", "banana", "cherry", "orange"]
print(fruits) #Output: ['apple', 'banana', 'cherry', 'orange']
# Here, we are defining a list of fruits using square brackets. The list contains four items: "apple", "banana", "cherry", "orange". The list is printed using the print function. The output is displayed as ['apple', 'banana', 'cherry', 'orange'].

# Accessing items in a list:
# Items in a list can be accessed using their index. The index of the items in a list starts from 0. We can access an item in a list using its index inside square brackets([]).
# Eg:
fruits = ["apple", "banana", "cherry", "orange"]
print(fruits[0]) #Output: apple
print(fruits[1]) #Output: banana
print(fruits[2]) #Output: cherry

# Changing items in a list:
# Items in a list can be changed by assigning a new value to the item using its index.
# Eg:
fruits = ["apple", "banana", "cherry", "orange"]
fruits[1] = "mango"
print(fruits) #Output: ['apple', 'mango', 'cherry', 'orange']

# Adding items to a list:
# Items can be added to a list using the append() method. The append() method adds the item to the end of the list.
# Eg:
fruits = ["apple", "banana", "cherry", "orange"]
fruits.append("mango")
print(fruits) #Output: ['apple', 'banana', 'cherry', 'orange', 'mango']

# Removing items from a list:
# Items can be removed from a list using the remove() method. The remove() method removes the specified item from the list.
# Eg:
fruits = ["apple", "banana", "cherry", "orange"]
fruits.remove("banana")
print(fruits) #Output: ['apple', 'cherry', 'orange']

# List methods:
# Python provides several built-in methods to work with lists. Some of the commonly used list methods are:
# a. append(): Adds an item to the end of the list.
# b. remove(): Removes the specified item from the list.
# c. pop(): Removes the item at the specified index.
# d. clear(): Removes all the items from the list.
# e. sort(): Sorts the items in the list.
# f. reverse(): Reverses the order of the items in the list.
# g. count(): Returns the number of times the specified item appears in the list.
# h. index(): Returns the index of the specified item in the list.
# i. copy(): Returns a copy of the list.

# We will cover list methods in upcoming files. (list-methods.py)

# 2. Dictionary:
# A dictionary is a collection of key-value pairs that are unordered and changeable. Dictionaries are defined using curly braces({}). Each key-value pair in a dictionary is separated by a colon(:) and the pairs are separated by commas. Dictionaries can contain items of different data types. Dictionaries are mutable, which means the items in a dictionary can be changed. The keys in a dictionary are unique.
# Eg:
person = {"name": "John", "age": 30, "city": "New York"}
print(person) #Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing items in a dictionary:
# Items in a dictionary can be accessed using their keys. We can access the value of a key in a dictionary using the key inside square brackets([]).
# Eg:
person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"]) #Output: John
print(person["age"]) #Output: 30
print(person["city"]) #Output: New York

# Changing items in a dictionary:
# Items in a dictionary can be changed by assigning a new value to the key.
# Eg:
person = {"name": "John", "age": 30, "city": "New York"}
person["age"] = 35
print(person) #Output: {'name': 'John', 'age': 35, 'city': 'New York'}

# Adding items to a dictionary:
# Items can be added to a dictionary by specifying a new key-value pair.
# Eg:
person = {"name": "John", "age": 30, "city": "New York"}
person["country"] = "USA"
print(person) #Output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}

# Removing items from a dictionary:
# Items can be removed from a dictionary using the pop() method. The pop() method removes the item with the specified key.
# Eg:
person = {"name": "John", "age": 30, "city": "New York"}
person.pop("age")
print(person) #Output: {'name': 'John', 'city': 'New York'}

# Dictionary methods:
# Python provides several built-in methods to work with dictionaries. Some of the commonly used dictionary methods are:
# a. get(): Returns the value of the specified key.
# b. pop(): Removes the item with the specified key.
# c. clear(): Removes all the items from the dictionary.
# d. keys(): Returns a list of all the keys in the dictionary.
# e. values(): Returns a list of all the values in the dictionary.
# f. items(): Returns a list of key-value pairs in the dictionary.
# g. copy(): Returns a copy of the dictionary.

# We will cover dictionary methods in upcoming files. (dictionary-methods.py)