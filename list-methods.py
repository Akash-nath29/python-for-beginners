# This file contains all the key concepts of 'list methods' in Python. It covers the following topics:
# 1. append()
# 2. remove()
# 3. pop()
# 4. clear()
# 5. sort()
# 6. reverse()
# 7. count()
# 8. index()
# 9. copy()

# 1. append():
# The append() method adds an item to the end of the list. The item to be added is passed as an argument to the append() method. The append() method modifies the original list.
# Eg:
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits) #Output: ['apple', 'banana', 'cherry', 'orange']

# 2. remove():
# The remove() method removes the specified item from the list. The item to be removed is passed as an argument to the remove() method. If the specified item is not present in the list, a ValueError is raised. The remove() method modifies the original list.
# Eg:
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits) #Output: ['apple', 'cherry']

# 3. pop():
# The pop() method removes the item at the specified index from the list. The index of the item to be removed is passed as an argument to the pop() method. If the index is not specified, the last item in the list is removed. The pop() method returns the removed item. The pop() method modifies the original list. If the specified index is out of range, an IndexError is raised. 
# Eg:
fruits = ["apple", "banana", "cherry"]
removed_fruit = fruits.pop(1)
print(removed_fruit) #Output: banana
print(fruits) #Output: ['apple', 'cherry']

# 4. clear():
# The clear() method removes all the items from the list. The clear() method does not take any arguments. The clear() method modifies the original list. 
# Eg:
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits) #Output: []

# 5. sort():
# The sort() method sorts the items in the list in ascending order. The sort() method does not take any arguments. The sort() method modifies the original list. If the items in the list are of different data types, a TypeError is raised.
# Eg:
numbers = [3, 1, 2]
numbers.sort()
print(numbers) #Output: [1, 2, 3]

# 6. reverse():
# The reverse() method reverses the order of the items in the list. The reverse() method does not take any arguments. The reverse() method modifies the original list. 
# Eg:
numbers = [1, 2, 3]
numbers.reverse()
print(numbers) #Output: [3, 2, 1]   

# 7. count():
# The count() method returns the number of times the specified item appears in the list. The item to be counted is passed as an argument to the count() method. The count() method does not modify the original list. 
# Eg:
fruits = ["apple", "banana", "cherry", "banana"]
count = fruits.count("banana")
print(count) #Output: 2

# 8. index():
# The index() method returns the index of the first occurrence of the specified item in the list. The item to be searched is passed as an argument to the index() method. The index() method does not modify the original list. If the specified item is not present in the list, a ValueError is raised.
# Eg:
fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")
print(index) #Output: 1

# 9. copy():
# The copy() method returns a copy of the list. The copy() method does not take any arguments. The copy() method does not modify the original list.
# Eg:
fruits = ["apple", "banana", "cherry"]
fruits_copy = fruits.copy()
print(fruits_copy) #Output: ['apple', 'banana', 'cherry']

# This is the end of the 'list methods' file. In the next file we will talk about python dictionay methods. (dictionary-methods.py)