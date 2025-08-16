# Strings
# Strings are defined either with a single quote or a double quotes.

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

# The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)

mystring = "Don't worry about apostrophes"
print(mystring)

# There are additional variations on defining strings that make it easier to include things such as carriage returns, backslashes and Unicode characters. These are beyond the scope of this tutorial, but are covered in the Python documentation.

# Simple operators can be executed on numbers and strings:

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# Assignments can be done on more than one variable "simultaneously" on the same line like this

a, b = 3, 4
print(a, b)

# Mixing operators between numbers and strings is not supported:

# This will not work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)