# Scripting With Raw Input
# We can get raw input from the user with the built-in function input, which 
# takes in an optional string argument that you can use to specify a message 
# to show to the user when asking for input.

name = input("Enter your name: ")
print("Hello there, {}!".format(name.title()))

# This prompts the user to enter a name and then uses the input in a greeting. 
# The input function takes in whatever the user types and stores it as a string. 
# If you want to interpret their input as something other than a string, like 
# an integer, as in the example below, you need to wrap the result with the 
# new type to convert it from a string.

num = int(input("Enter an integer"))
print("hello" * num)
# We can also interpret user input as a Python expression using the built-in 
# function eval. This function evaluates a string as a line of Python.

result = eval(input("Enter an expression: "))
print(result)

# If the user inputs 2 * 3, this outputs 6.
