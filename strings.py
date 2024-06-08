# This file contains all the key concepts of Strings in Python. It covers the following topics:
# 1. Strings
# 2. String concatenation
# 3. String indexing
# 4. String slicing
# 5. String methods
# 6. String formatting
# 7. Escape characters
# 8. Raw strings
# 9. Triple quotes

# 1. Strings:
# Strings are sequences of characters. They are enclosed within single quotes('') or double quotes(""). Eg: 'Hello', "World", "123" etc.

#Eg:
a = "Hello"
# Here 'a' is a variable of type str. It is used to store the value "Hello".

b = 'World'
# Here 'b' is a variable of type str. It is used to store the value "World".

c = "123"
# Here 'c' is a variable of type str. It is used to store the value "123".



# 2. String concatenation:
# String concatenation is the process of combining two or more strings together.
# Strings can be concatenated using the '+' operator. Eg: "Hello" + "World" will give "HelloWorld".

#Eg:
a = "Hello"
b = "World"
c = a + b
print(c) #Output: HelloWorld
# Here, 'a' and 'b' are variables of type str. We are concatenating the strings 'a' and 'b' using the '+' operator. The value of 'c' will be "HelloWorld".

d = "123"
e = "456"
f = d + e
print(f) #Output: 123456
# Here, 'd' and 'e' are variables of type str. We are concatenating the strings 'd' and 'e' using the '+' operator. The value of 'f' will be "123456".


# 3. String indexing:
# String indexing is the process of accessing individual characters in a string. Each character in a string has an index associated with it. The index starts from 0.
# Strings can be indexed using square brackets([]). Eg: "Hello"[0] will give 'H'.

#Eg:
a = "Hello"
print(a[0]) #Output: H

b = "World"
print(b[3]) #Output: l


# 4. String slicing:
# String slicing is the process of extracting a substring from a string. It is done by specifying the start and end indices of the substring. The start index is inclusive and the end index is exclusive. Eg: "Hello"[1:4] will give "ell".

#Eg:
a = "Hello"
print(a[1:4]) #Output: ell

b = "World"
print(b[2:5]) #Output: rld


# 5. String methods:
# Strings have several built-in methods that can be used to manipulate them. Some of the commonly used string methods are:
# a. upper(): Converts the string to uppercase.
# b. lower(): Converts the string to lowercase.
# c. strip(): Removes leading and trailing whitespaces.
# d. replace(): Replaces a substring with another substring.
# e. split(): Splits the string into a list based on a delimiter.


# a. upper():
a = "hello"
b = a.upper()
print(b) #Output: HELLO
# Here, 'a' is a variable of type str. We are converting the string to uppercase using the upper() method. The value of 'b' will be "HELLO".

# b. lower():
a = "HELLO"
b = a.lower()
print(b) #Output: hello
# Here, 'a' is a variable of type str. We are converting the string to lowercase using the lower() method. The value of 'b' will be "hello".

# c. strip():
a = "   hello   "
b = a.strip()
print(b) #Output: hello
# Here, 'a' is a variable of type str. We are removing the leading and trailing whitespaces using the strip() method. The value of 'b' will be "hello".

# d. replace():
a = "hello world"
b = a.replace("world", "python")
print(b) #Output: hello python
# Here, 'a' is a variable of type str. We are replacing the substring "world" with "python" using the replace() method. The value of 'b' will be "hello python".

# e. split():
a = "hello,world"
b = a.split(",")
print(b) #Output: ['hello', 'world'] (List)
# Here, 'a' is a variable of type str. We are splitting the string based on the delimiter "," using the split() method. The value of 'b' will be ['hello', 'world'].


# 6. String formatting:
# String formatting is the process of inserting variables into a string. There are several ways to format strings in Python. Some of the common methods are:
# a. Using the % operator
# b. Using the format method
# c. Using f-strings
# d. Using Template strings

# a. Using the % operator:
a = "Hello %s" % "World"
print(a) #Output: Hello World
# Here, we are using the % operator to format the string. The %s is a placeholder for the string "World". The value of 'a' will be "Hello World".

b = "Hello %d" % 123
print(b) #Output: Hello 123
# Here, we are using the % operator to format the string. The %d is a placeholder for the integer 123. The value of 'b' will be "Hello 123".

# b. Using the format method:
a = "Hello {}".format("World")
print(a) #Output: Hello World
# Here, we are using the format method to format the string. The {} is a placeholder for the string "World". The value of 'a' will be "Hello World".

b = "Hello {}".format(123)
print(b) #Output: Hello 123
# Here, we are using the format method to format the string. The {} is a placeholder for the integer 123. The value of 'b' will be "Hello 123".

# c. Using f-strings:
a = "World"
b = f"Hello {a}"
print(b) #Output: Hello World
# Here, we are using f-strings to format the string. The {a} is a placeholder for the variable 'a'. The value of 'b' will be "Hello World".

c = 123
d = f"Hello {c}"
print(d) #Output: Hello 123
# Here, we are using f-strings to format the string. The {c} is a placeholder for the variable 'c'. The value of 'd' will be "Hello 123".

# d. Using Template strings:
from string import Template
a = Template("Hello $name")
b = a.substitute(name="World")
print(b) #Output: Hello World
# Here, we are using Template strings to format the string. The $name is a placeholder for the string "World". The value of 'b' will be "Hello World".

c = Template("Hello $name")
d = c.substitute(name=123)
print(d) #Output: Hello 123
# Here, we are using Template strings to format the string. The $name is a placeholder for the integer 123. The value of 'd' will be "Hello 123".

# 7. Escape characters:
# Escape characters are used to represent characters that are difficult or impossible to type directly. They are used to perform various tasks such as:
# a. Inserting newline characters
# b. Inserting tab characters
# c. Inserting quotes within a string
# d. Inserting backslashes within a string

# a. Inserting newline characters:
a = "Hello\nWorld"
print(a) #Output: Hello 
        #         World

# b. Inserting tab characters:
a = "Hello\tWorld"
print(a) #Output: Hello   World

# c. Inserting quotes within a string:
a = "Hello \"World\""
print(a) #Output: Hello "World"

# d. Inserting backslashes within a string:
a = "C:\\Users\\Desktop"
print(a) #Output: C:\Users\Desktop


# 8. Raw strings:
# Raw strings are used to ignore escape characters. They are prefixed with 'r' or 'R'. Eg: r"Hello\nWorld" will give "Hello\nWorld".

a = r"Hello\nWorld"
print(a) #Output: Hello\nWorld
# Here, we are using raw strings to ignore the newline character. The value of 'a' will be "Hello\nWorld".


# 9. Triple quotes:
# Triple quotes are used to represent multi-line strings. They are enclosed within triple quotes(''' '''). Eg: '''Hello World'''.

a = '''Hello 
       World'''
print(a) #Output: Hello
        #         World
# Here, we are using triple quotes to represent a multi-line string. The value of 'a' will be "Hello\nWorld".

b = """Hello
        World"""
print(b) #Output: Hello 
        #         World
# Here, we are using triple quotes to represent a multi-line string. The value of 'b' will be "Hello\nWorld".

# That's all for the Strings in Python. In the next file, we will make a few simple project using concepts of strings, operators in Python. (project1.py)