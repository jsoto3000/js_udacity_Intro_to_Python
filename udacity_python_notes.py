# LESSON 01
# Introduction

# Programming In Python
# As you learn Python throughout this course, there are a few things you should
# keep in mind.

# 1. Python is case sensitive.
# 2. Spacing is important.
# 3. Use error messages to help you learn.

# Lesson 2: Data Types and Operators
# 1. Data Types: Integers, Floats, Booleans, Strings, Lists, Tuples, Sets, Dictionaries
# 2. Operators: Arithmetic, Assignment, Comparison, Logical, Membership, Identity
# 3. Built-In Functions, Compound Data Structures, Type Conversion
# 4. Whitespace and Style Guidelines

# Lesson 3: Control Flow
# 1. Conditional Statements
# 2. Boolean Expressions
# 3. For and While Loops
# 4. Break and Continue
# 5. Zip and Enumerate
# 6. List Comprehensions

# Lesson 4: Functions
# 1. Defining Functions
# 2. Variable Scope
# 3. Documentation
# 4. Lambda Expressions
# 5. Iterators and Generators

# Lesson 5: Scripting
# 1. Python Installation and Environment Setup
# 2. Running and Editing Python Scripts
# 3. Interacting with User Input
# 4. Handling Exceptions
# 5. Reading and Writing Files
# 6. Importing Local, Standard, and Third-Party Modules
# 7. Experimenting with an Interpreter


# LESSON 02

# Data Types And Operators
# Welcome to this lesson on Data Types and Operators! You'll learn about:

# Data Types: Integers, Floats, Booleans, Strings, Lists, Tuples, Sets, Dictionaries
# Operators: Arithmetic, Assignment, Comparison, Logical, Membership, Identity
# Built-In Functions, Compound Data Structures, Type Conversion
# Whitespace and Style Guidelines

# Arithmetic Operators

# + Addition
# - Subtraction
# * Multiplication
# / Division
# % Mod (the remainder after dividing)
# ** Exponentiation (note that ^ does not do this operation, as you might have seen in other languages)
# // Divides and rounds down to the nearest integer

print(1+1)
print(5-2)
print(10*10)
print(25/5)
print(11/2)
print(10**2)
print(11//2)

# The usual order of mathematical operations holds in Python (PEMDAS)

# Bitwise operators are special operators in Python
# https://wiki.python.org/moin/BitwiseOperators

# Write an expression that calculates the average of 23, 32 and 64
# Place the expression in this print statement
print((23+32+64)/3)

# Fill this in with an expression that calculates how many tiles are needed.
print(9*7 + 5*7)

# Fill this in with an expression that calculates how many tiles will be left over.
print(17*6 - (9*7 + 5*7))


# Which of these lines of Python code are well formatted?
# How would you improve the readability of the codes that don't use good formatting?

print((17 - 6)%(5 + 2))

print(4/2 - 7*7)

# variables and assignment operators

x = 2
y = x
print(y)

mv_population = 74728

x = 3
y = 4
z = 5

x, y, z = 3, 4, 5

# write varaible names that are descriptive
# use only ordinary letters, numbers and underscores in variable names
# they cannot have spaces, and need to start with a letter or underscore

# cannot use reserved words or built-in identifiers that have important purposes
# in Python

# Reserved Words
# You may not name your variables any of the following words as they mean
# special things in Python:

# and	assert	break	class	continue
# def	del	elif	else	except
# exec	finally	for	from	global
# if	import	in	is	lambda
# not	or	pass	print	raise
# return	try	while

# Do NOT use any of the following words either (although they are not strictly
# Python reserved words, they conflict with the names of commonly-used Python functions):

# Data	Float	Int	Numeric	Oxphys
# array	close	float	int	input
# open	range	type	write	zeros

# You should also avoid all the names defined in the math library (you must
# avoid them if you import the library):

# acos	asin	atan	cos	e
# exp	fabs	floor	log	log10
# pi	sin	sqrt	tan

# keywords in Python:
# False class finally is return
# None continue for lambda try
# True def from nonlocal while
# and del global not with
# as elif if or yield
# assert else import pass
# break except in raise

# create variable names that are descriptive

# name varaibles using all lowercase letters and underscores to separate words
# snake case

# YES

my_height = 58
my_lat = 40
my_long = 105

# NO

my height = 58
MYLONG = 40
MyLat =

# assignment operators
mv_population = 74728
mv_population = 74728 + 4000 - 600
print(mv_population)

mv_population = 74728
mv_population += 4000 - 600
print(mv_population

# https://www.programiz.com/python-programming/operators

x = 2
x = 2

x += 2
x = x + 2

x - = 2
x = x - 2


# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall *= .9

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)


# quiz - changing variable names
carrots = 24
rabbits = 8
crs_per_rab = carrots/rabbits

rabbits = 12

print(crs_per_rab) # returns 3

# Integers and Floats
# There are two Python data types that could be used for numeric values:

# int - for integer values
# float - for decimal or floating point values; floating point number
# operation including int and float always produces float
# can convert from one type to another by constructing new objects
# when convert float to int no rounding occurs
# when convert int to float add decimal zero to end


# You can create a value that follows the data type by using the following syntax:

x = int(4.7)   # x is now an integer 4
y = float(4)   # y is now a float of 4.0

# You can check the type by using the type function:

print(type(x))
# returns int

print(type(y))
# returns float

x = 4
y= 4.

print(type(x))
print(type(y))


# returns float
# Because the float, or approximation, for 0.1 is actually slightly more than
# 0.1, when we add several of them together we can see the difference between
# the mathematically correct answer and the one that Python creates.
# https://docs.python.org/3/tutorial/floatingpoint.html

print(.1 + .1 + .1 == .3)
# returns false

# whitespace
# whitespace doesnt affect how code works

# Python Best Practices
# For all the best practices, see the PEP8 Guidelines.
# https://www.python.org/dev/peps/pep-0008/

# You can use the atom package linter-python-pep8 to use pep8 within your own
# programming environment in the Atom text editor.

# Good
print(4 + 5)

# Bad
print(                       4 + 5)

# You should limit each line of code to 80 characters, though 99 is okay for
# certain use cases. You can thank IBM for this ruling.

# Why are these conventions important? Although how you format the code doesn’t
# affect how it runs, following standard style guidelines makes code easier to
# read and consistent among different developers on a team.

# divide by zero error
print(5/0)

# In general, there are two types of errors to look out for

# 1. Exceptions
# 2. Syntax

# An Exception is a problem that occurs when the code is running,
# but a 'Syntax Error' is a problem detected when Python checks the code before
# it runs it.

# For more information see the Python tutorial page on Errors and Exceptions.
# https://docs.python.org/3/tutorial/errors.html


# Booleans, Comparison Operators, and Logical Operators
# The bool data type holds one of the values True or False, which are often
# encoded as 1 or 0, respectively.

# There are 6 comparison operators that are common to see in order to obtain a bool value:

# Comparison Operators

# Symbol Use Case	Bool	Operation
print(5 < 3)	# False	Less Than
print(5 > 3)	# True	Greater Than
print(3 <= 3)	# True	Less Than or Equal To
print(3 >= 5)	# False	Greater Than or Equal To
print(3 == 5)	# False	Equal To
print(3 != 5)	# True	Not Equal To

# And there are three logical operators you need to be familiar with:

# Logical Use	Bool	Operation
print(5 < 3 and 5 == 5)	# False	and - Evaluates if all provided statements are True
print(5 < 3 or 5 == 5)	# True	or - Evaluates if at least one of many statements is True
print(not 5 < 3)	# True	not - Flips the Bool Value

# = used to assign variables
# == used to check for equality

# Here is more information on how George Boole changed the world!

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise

print(san_francisco_pop_density > rio_de_janeiro_pop_density)


# alternative solution (but less efficient)

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise

if (san_francisco_pop_density > rio_de_janeiro_pop_density):
    print (True)
else:
    print (False)


# Strings
# Strings in Python are shown as the variable type str. You can define a
# string with either double quotes " or single quotes '. If the string you are
# creating actually has one of these two values in it, then you need to be
# careful to assure your code doesn't give an error.

my_string = 'this is a string!'
my_string2 = "this is also a string!!!"

# You can also include a \ (escape) in your string to be able to include one of these quotes:

this_string = 'Simon\'s skateboard is in the garage.'
print(this_string)


# returns Simon's skateboard is in the garage.

# If we don't use this, notice we get a syntax error:

this_string = 'Simon's skateboard is in the garage.'

# There are a number of other operations you can use with strings as well

first_word = 'Hello'
second_word = 'There'
print(first_word + second_word)
# returns HelloThere

print(first_word + ' ' + second_word)
# returns Hello There

print(first_word * 5)
# returns HelloHelloHelloHelloHello

print(len(first_word))
# returns 5

# Unlike the other data types you have seen so far, you can also index into
# strings, but you will see more on this soon! For now, here is a small example.
# Notice Python uses 0 indexing

first_word[0]

# returns H

first_word[1]

# returns e

# The len() function
# len() is a built-in Python function that returns the length of an object,
# like a string. The length of a string is the number of characters in the
# string. This will always be an integer.

# There is an example above, but here's another one:

print(len("ababa") / len("ab"))
# returns 2.5

# You know what the data types are for len("ababa") and len("ab").
# Notice the data type of their resulting quotient here (float).

# quiz

# TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
print(ford_quote)

# question
coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)
# returns 3415 (and tropical_fruit_count is a string)

# quiz
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username + ' accessed the site ' + url + ' at ' + timestamp + '.')

# quiz
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length =  len(given_name) + len(middle_names) + len(family_name) + 2 #todo: calculate how long this name is
print(name_length)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

# QUESTION
# We've just used the len function to find the length of strings. What does the
# len function return when we give it the integer 835 instead of a string?
# returns error

# Type And Type Conversion

# You have seen four data types so far:

# int
# float
# bool
# string

# You got a quick look at type() from an earlier video, and it can be used to
# check the data type of any variable you are working with.

print(type(4))
# returns int

print(type(3.7))
# returns float

print(type('this'))
# returns str

print(type(True))
# returns bool

# You saw that you can change variable types to perform different operations.
# For example,

print("0" + "5")
# provides completely different output than

print(0 + 5)
# What do you think the below would provide?

print("0" + 5)
# returns TypeError: cannot concatenate 'str' and 'int' objects

#How about the code here:
print(0 + "5")
# returns TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Checking your variable types is really important to assure that you are
# retrieving the results you want when programming.

print(type(len("my_string")))
# returns int

print(type("hippo" * 12))
# returns str

# quiz
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"
sales_string = "This week's total sales: "

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

total_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
total_sales = str(total_sales)

print(sales_string + total_sales + ".")


# String Methods

# Methods are related to functions, but unlike functions, they are associated
# with specific types of objects.
# Methods are functions that "belong" to an object.
# Inputs in parentheses are called arguments
# Since methods or special types of functions belong to an object, then the
# object is always the first argument to a method.
# For methods the argument is 'disguised' as the associated object.

# title method
print("sebastian thrun".title())
# returns Sebastian Thrun

# lower method
full_name = "sebastian thrun"
print(full_name.islower())
# returns True

# count method takes in more arguments than the object.
print("one fish, two fish, red fish, blue fish.".count("fish"))
# returns how many times the substring fish occurs in string

# Methods are like some of the functions you have already seen:

len("this")
type(12)
print("Hello world")

# These three above are functions - notice they use parentheses, and accept one
# or more arguments. Functions will be studied in much more detail in a later lesson!

# A method in Python behaves similarly to a function. Methods actually are
# functions that are called using dot notation. For example, lower() is a string
# method that can be used like this, on a string called
# "sample string": sample_string.lower().

# Methods are specific to the data type for a particular variable. So there are
# some built-in methods that are available for all strings, different methods
# that are available for all integers, etc.

# Below are some methods that are possible with any string.

my.string = "sebastian thrun"

my_string.capitalize()
my_string.casefold()
my_string.center()
my_string.count()
my_string.encode()
my_string.endswith()
my_string.expandtabs()
my_string.find()
my_string.format()
my_string.format_map()
my_string.index()
my_string.isalnum()
my_string.isalpha()
my_string.isDecimal()
my_string.isdigit()
my_string.isidentifier()
my_string.islower()
my_string.isnumeric()
my_string.isprintable()
my_string.isspace()
my_string.istitle()
my_string.isupper()
my_string.join()
my_string.ljust()

# Each of these methods accepts the string itself as the first argument of the
# method. However, they also could receive additional arguments, that are passed i
# nside the parentheses.

my_string.islower()
# returns True

my_string.count('a')
# returns 2

my_string.find('a')
# returns 3

# You can see that the count and find methods both take another argument.
# However, the .islower() method does not accept another argument.

# No professional has all the methods memorized, which is why understanding how
# to use documentation and find answers is so important. Gaining a strong grasp
# of the foundations of programming will allow you to use those foundations to
# use documentation to build so much more than someone who tries to memorize
# all the built-in methods in Python.

# One important string method:
my_string.format()

# We will be using the format() string method a good bit in our future work in
# Python, and you will find it very valuable in your coding, especially with
# your print statements.

# We can best illustrate how to use format() by looking at some examples:

# Example 1
print("Mohammed has {} balloons".format(27))
# returns Mohammed has 27 balloons

# Example 2
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))
# returns Does your dog bite?

# Example 3
maria_string = "Maria loves {} and {}"
print(maria_string.format("math","statistics"))
# returns Maria loves math and statistics

# Notice how in each example, the number of pairs of curly braces {} you use
# inside the string is the same as the number of replacements you want to make
# using the values inside format().

# More advanced students can learn more about the formal syntax for using the
# format() string method here.
# https://docs.python.org/3.6/library/string.html#format-string-syntax

# You can learn more about strings and string methods by looking at the string
# method documentation.
# https://docs.python.org/3/library/stdtypes.html#string-methods

# quiz
# Write two lines of code below, each assigning a value to a variable
first_name = "Juan"
last_name = "Doe"

# Now write a print statement using .format() to print out a sentence and the
# values of both of the variables
print("My name is {} {}.".format(first_name, last_name))

# Another important string method: split()

# A helpful string method when working with strings is the .split method. This
# function or method returns a data container called a list that contains the
# words from the input string.

# The split method has two additional arguments (sep and maxsplit). The sep
# argument stands for "separator". It can be used to identify how the string
# should be split up (e.g., whitespace characters like space, tab, return,
# newline; specific punctuation (e.g., comma, dashes)). If the sep argument is
# not provided, the default separator is whitespace.

# True to its name, the maxsplit argument provides the maximum number of splits.
# The argument gives maxsplit + 1 number of elements in the new list, with the
# remaining string being returned as the last element in the list.

# Here are some examples for the .split() method.


# A basic split method:

new_str = "The cow jumped over the moon."
new_str.split()
# Output is:
# ['The', 'cow', 'jumped', 'over', 'the', 'moon.']
# Here the separator is space, and the maxsplit argument is set to 3.

new_str.split(' ', 3)
# Output is:
# ['The', 'cow', 'jumped', 'over the moon.']
# Using '.' or period as a separator.

new_str.split('.')
# Output is:
# ['The cow jumped over the moon', '']
# Using no separators but having a maxsplit argument of 3.

new_str.split(None, 3)
# Output is:
# ['The', 'cow', 'jumped', 'over the moon.']

# Lists

# Data structures are containers that organize and group data types together in
# different ways. A list is one of the most common and basic data structures in
# Python.

# A list is a data type for mutable ordered sequences of elements.
# Uses zero based

months = [
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
]

print(months[0])
print(months[1])
print(months[7])
print(months[-2])
print(months[-1])
print(months[25])

# You saw here that you can create a list with square brackets. Lists can
# contain any mix and match of the data types you have seen so far.

list_of_random_things = [1, 3.4, 'a string', True]
# This is a list of 4 elements. All ordered containers (like lists) are
# indexed in python using a starting index of 0. Therefore, to pull the first
# value from the above list, we can write:

print(list_of_random_things[0])
# returns 1

print(len(list_of_random_things))
# returns 4

# It might seem like you can pull the last element with the following code, but
# this actually won't work:

print(list_of_random_things[len(list_of_random_things)])
# returns error list index out of range

# However, you can retrieve the last element by reducing the index by 1.
# Therefore, you can do the following:

print(list_of_random_things[len(list_of_random_things) - 1])
# returns True

# Alternatively, you can index from the end of a list by using negative values,
# where -1 is the last element, -2 is the second to last element and so on.

print(list_of_random_things[-1])
# returns True

print(list_of_random_things[-2])
# returns a string


# Slice and Dice with Lists

# Use Python slicing notation to access a subsequence of a list. Slicing means
# using indices to slice parts of object loke a string or a list.

greeting = "Hello there"

months = [
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
]

q3 = months[6:9]
print(q3)
# return ['July', 'August','September']

first_half = months[:6]
print(first_half)
# returns ['January', 'February', 'March', 'April', 'May', 'June']

second_half = months[6:]
# returns ['July', 'August', 'September, 'October, 'November', 'December']

print(greeting[6:9], months[6:9])
# returns 'the' ['July', 'August', 'September']

# Membership Operators
# Keyword Operation
# in - evaluates if object on left side IS included in object on right side
# not in - evaluates if object on left side IS NOT included in object on right side

print('her' in greeting, 'her' not in greeting)
# returns True False

# You saw that we can pull more than one value from a list at a time by using
# slicing. When using slicing, it is important to remember that the lower index
# is inclusive and the upper index is exclusive.


# Therefore, this:
list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[1:2])

# returns [3.4]
# will only return 3.4 in a list.
# Notice this is still different than just indexing a single element, because
# you get a list back with this indexing. The colon tells us to go from the
# starting value on the left of the colon up to, but not including, the element
# on the right.

# If you know that you want to start at the beginning, of the list you can also
# leave out this value.

print(list_of_random_things[:2])
# returns [1, 3.4]
# or to return all of the elements to the end of the list, we can leave off a
# final element.

print(list_of_random_things[1:])
# returns [3.4, 'a string', True]

# This type of indexing works exactly the same on strings, where the returned
# value will be a string.

# Are you in OR not in?

# You saw that we can also use in and not in to return a bool of whether an
# element exists within our list, or if one string is a substring of another.

print('this' in 'this is a string')
# returns True

print('in' in 'this is a string')
# returns True

print('isa' in 'this is a string')
# returns False

print(5 not in [1, 2, 3, 4, 6])
# returns True

print(5 in [1, 2, 3, 4, 6])
# returns False

# Mutability and Order

# strings are sequences of letters
# list elements can be any type of object
# lists can be modified, but strings can't

greeting = "Hello there"

months = [
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
]

months[3] = 'Friday'
print(months)
# returns ['January', 'February', 'March', 'Friday', 'May', 'June', 'July',
# 'August', 'September', 'October', 'November', 'December']

greeting[3] = 'i'
# returns TypeError: 'str' object does not support item assignment
print(greeting)
# returns Hello There

# Mutability - whether an object can change its values after it has been created

# lists are mutable
# strings are immutable

# Order - whether the order of elements in an object matters (and wheter this can
# be used to access elements)

# lists are ordered
# strings are ordered

# Mutability is about whether or not we can change an object once it has been
# created. If an object (like a list or string) can be changed (like a list can),
# then it is called mutable. However, if an object cannot be changed without
# creating a completely new object (like strings), then the object is considered
# immutable.

my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
print(my_lst)
# returns ['one', 2, 3, 4, 5]

# As shown above, you are able to replace 1 with 'one' in the above list. This
# is because lists are mutable.

# However, the following does not work:

greeting = "Hello there"
greeting[0] = 'M'
# returns TypeError: 'str' object does not support item assignment
print(greeting)
# returns Hello There

# This is because strings are immutable. This means to change this string, you
# will need to create a completely new string.

# There are two things to keep in mind for each of the data types you are using:

# Are they mutable?
# Are they ordered?

# Order is about whether the position of an element in the object can be used
# to access the element. Both strings and lists are ordered. We can use the
# order to access parts of a list and string.

# However, you will see some data types in the next sections that will be
# unordered. For each of the upcoming data structures you see, it is useful to
# understand how you index, are they mutable, and are they ordered. Knowing this
# about the data structure is really useful!

# Additionally, you will see how these each have different methods, so why you
# would use one data structure vs. another is largely dependent on these
# properties, and what you can easily do with it

# quiz
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month

num_days = days_in_month[month - 1]
print(num_days)

# quiz
eclipse_dates = [
'June 21, 2001',
'December 4, 2002',
'November 23, 2003',
'March 29, 2006',
'August 1, 2008',
'July 22, 2009',
'July 11, 2010',
'November 13, 2012',
'March 20, 2015',
'March 9, 2016'
]

# TODO: Modify this line so it prints the last three elements of the list
#print(eclipse_dates)
print(eclipse_dates[-3:])

# TODO: Modify this line so it prints the last three elements of the list
#print(eclipse_dates)
print(eclipse_dates[-3:])

# question
sentence1 = "I wish to register a complaint."
sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]

sentence2[6]="!"
print(sentence2)
# returns ['I', 'wish', 'to', 'register', 'a', 'complaint', '!']

sentence2[0]= "Our Majesty"
print(sentence2)
# returns ['Our Majesty', 'wish', 'to', 'register', 'a', 'complaint', '.']

sentence1[30]="!"
print(sentence1)
# returns TypeError: 'str' object does not support item assignment

sentence2[0:2] = ["We", "want"]
print(sentence2)
# returns ['We', 'want', 'to', 'register', 'a', 'complaint', '.']

# List Methods

# strings are not mutable

name = 'Jim'
student = name
name = 'Tim'

print(name)
# returns Tim
print(student)
# returns Jim

# lists are mutable

scores = [
"B",
"C",
"A",
"D",
"B",
"A"
]
grades = scores
print("scores: " + str(scores))
#returns scores: ['B', 'C', 'A', 'D', 'B', 'A']
print("grades: " + str(grades))
#returns scores: ['B', 'C', 'A', 'D', 'B', 'A']
scores[3] = "B"
print("scores: " + str(scores))
#returns scores: ['B', 'C', 'A', 'B', 'B', 'A']
print("grades: " + str(grades))
#returns scores: ['B', 'C', 'A', 'B', 'B', 'A']

# behavior of variables containing mutable and immutable objects, are very
# different and might even seem surprising at times.

#  Useful Functions for Lists I
len() # returns how many elements are in a list.

max() # returns the greatest element of the list. How the greatest element is
      # determined depends on what type objects are in the list. The maximum
      # element in a list of numbers is the largest number. The maximum elements
      # in a list of strings is element that would occur last if the list were
      # sorted alphabetically. This works because the the max function is
      # defined in terms of the greater than comparison operator. The max
      # function is undefined for lists that contain elements from different,
      # incomparable types
      # defined in terms of the > (greater than) comparison operator

batch_sizes = [15, 6, 89, 34, 65, 35]
print(max(batch_sizes))
# returns 89

python_varieties = [
"Burmese Python",
"African Rock Python",
"Ball Python",
"Reticulated Python",
"Angolan Python"
]
print(max(python_varieties))
# returns Reticulated Python

print(max([int(42), 'African Swallow']))
# returns African Swallow version 2.7
# returns TypeError: '>' not supported between instances of 'str' and 'int' version 3.5
# max function is undefined for lists containing elements from different incomparable types


min() # returns the smallest element in a list. min is the opposite of max,
      # which returns the largest element in a list.

sorted() # returns a copy of a list in order from smallest to largest,
         #leaving the list unchanged

sizes = [15, 6, 89, 34, 65, 35]
print(sorted(sizes))
# returns [6, 15, 34, 35, 65, 89] in ascending order

sizes = [15, 6, 89, 34, 65, 35]
print(sorted(sizes, reverse=True))
# returns [89, 65, 35, 34, 15, 6] in descending order


# Useful Functions for Lists II

# join method
# join is a string method that works with lists
# join takrs a list as an argument and returns string comprising list elements
# will return error if try to join anythong other than strings

nautical_directions = "\n".join(["fore", "aft", "starboard", "port"])
print(nautical_directions)
# returns string of the list elements joined by separator string

nautical_directions = ",".join(["fore", "aft", "starboard", "port"])
print(nautical_directions)
# returns string of the list elements joined by separator string

names = ["Garcia", "O'Kelly", "Davis"]
print("-".join(names))
# returns Garcia-O'Kelly-Davis

names = ["Garcia" "O'Kelly" "Davis"]
print("-".join(names))
# returns GarciaO'KellyDavis
# default string literal appending

stuff = ["thing", 42, "nope"]
print(" and ".join(stuff))
# returns TypeError: sequence item 1: expected string, int found

# append
# adds an element to end of the list

python_varieties = [
"Burmese Python",
"African Rock Python",
"Ball Python",
"Reticulated Python",
"Angolan Python"
]

python_varieties.append('Blood Python')

print(python_varieties)
# returns ['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python', 'Blood Python']

# Join is a string method that takes a list of strings as an argument, and
# returns a string consisting of the list elements joined by a separator string.

new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)
# Output:
# fore
# aft
# starboard
# port

# In this example we use the string "\n" as the separator so that there is a
# newline between each element. We can also use other strings as separators with
# .join. Here we use a hyphen.

name = "-".join(["García", "O'Kelly"])
print(name)
# Output:
# García-O'Kelly

# It is important to remember to separate each of the items in the list you are
# joining with a comma (,). Forgetting to do so will not trigger an error,
# but will also give you unexpected results.

# append method

# A helpful method called append adds an element to the end of a list.

letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)
# Output:
# ['a', 'b', 'c', 'd', 'z']

# question

a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

# returns 4, 2

# question

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

# returns Albert & Ben & Carol & Donna

names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))

# returns ['Albert', 'Ben', 'Carol', 'Donna', 'Eugenia']

# Python has a set of built-in methods that you can use on lists/arrays.
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# Tuples

# Tuple is a data structure in Python that is an immutable ordered sequence of
# elements

AngKorWat = (13.4125, 103.866667)

print(type(AngKorWat))
# returns class 'tuple'

print("Angkor Wat is at latitude: {}".format(AngKorWat[0]))
# returns Angkor Wat is at latitude: 13.4125
print("Angkor Wat is at longitude: {}".format(AngKorWat[1]))
# returns Angkor Wat is at longitude: 103.866667

# tuples similar to loists in that they store an ordered collection of objects
# that can be accessed by their indices.
# tuples however are immutable.
# cannot add or remove items from tuples or sort them in place
# tuples are useful when you two or more values that are so closely related that
# they will always be used together
# tuples can be used to assign multiple variables in a compact way
# parentheses are optional when making tuples
# use tuple unpacking to assign information from a tuple into multiple variables
# without having to access them one by one and make multiple assignment statements

dimensions = 52, 40, 100
length, width, height = dimensions # tuple unpacking
print("The dimensions are {}*{}*{}".format(length, width, height))
# returns The dimensions are 52*40*100

# A tuple is another useful container. It's a data type for immutable ordered
# sequences of elements. They are often used to store related pieces of
# information. Consider this example involving latitude and longitude:

location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

# Tuples are similar to lists in that they store an ordered collection of objects
# which can be accessed by their indices. Unlike lists, however, tuples are
# immutable - you can't add and remove items from tuples, or sort them in place.

# Tuples can also be used to assign multiple variables in a compact way.

dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))

# The parentheses are optional when defining tuples, and programmers frequently
# omit them if parentheses don't clarify the code.

# In the second line, three variables are assigned from the content of the tuple
# dimensions. This is called tuple unpacking. You can use tuple unpacking to
# assign the information from a tuple into multiple variables without having to
# access them one by one and make multiple assignment statements.

# If we won't need to use dimensions directly, we could shorten those two lines
# of code into a single line that assigns three variables in one go!

length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))

# question

# Tuples - ordered
# Tuples - immutable
# Lists - ordered
# Lists - immutable

# question

tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b)
# returns True
print(tuple_a[1])
# returns 2


# Sets

# set is a data type for mutable unordered collections of unique elements

countries = [
'Angola',
'Maldives',
'India',
'United States',
'India',
'Denmark',
'Sweden',
'Ghana'
]

country_set = set(countries)
print(len(countries))
# returns 8
print(len(country_set))
# returns 7
print(country_set)
# returns set(['Ghana', 'Maldives', 'Angola', 'Denmark', 'India',
# 'United States', 'Sweden'])

print('India' in countries)
# returns True
print('India' in country_set)
# returns True

# do not use append method to add elements to sets; use add method

country_set.add('Italy')
print(country_set)
# returns set(['Ghana', 'Maldives', 'Angola', 'Denmark', 'India',
# 'United States', 'Sweden', 'Italy'])

# sets also have a pop method just like lists
# when you pop an element from sets a random element is removed
# sets, unlike lists, are unordered, so there is no last element
# other operations you can perform on sets include those of mathematical sets
# methods include union, intersection, nad difference

# A set is a data type for mutable unordered collections of unique elements.
# One application of a set is to quickly remove duplicates from a list.

numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)

# This would output:
# {1, 2, 3, 6}

# Sets support the in operator the same as lists do. You can add elements to
# sets using the add method, and remove elements using the pop method, similar
# to lists. Although, when you pop an element from a set, a random element is
# removed. Remember that sets, unlike lists, are unordered so there is
# no "last element".

fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)
# This outputs:
# False
# {'grapefruit', 'orange', 'watermelon', 'banana', 'apple'}
# grapefruit
# {'orange', 'watermelon', 'banana', 'apple'}

# Other operations you can perform with sets include those of mathematical sets.
# Methods like union, intersection, and difference are easy to perform with
# sets, and are much faster than such operators with other containers.

# question

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))

# returns 6

# quiz: add and pop

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()

# maybe


# Dictionaries And Identity Operators

# Dictionary - a data type for mutable objects that store mappings of unique
# keys to values
# dictionaries store pairs of elements: keys and values

elements = {
'hydrogen': 1,
'helium': 2,
'carbon': 6
}

print(elements['carbon'])
# returns 6
elements['lithium'] = 3
print(elements)
# returns {'helium': 2, 'lithium': 3, 'hydrogen': 1, 'carbon': 6}
print('mithril' in elements)
# returns False
print(elements.get('dilithium'))
# returns None
print(elements['dilithium'])
# returns KeyError: 'dilithium'

x = elements.get('dilithium')
is_null = x is None
print(is_null)
# returns True

x = elements.get('dilithium')
is_null = x is not None
print(is_null)
# returns False

# dictionary keys are similar to list indices
# can select elements from the data structure by putting the key in square brackets
# unlike lists, dictionaries can have keys of any immutable type, not just integers
# element dictionary uses strings for its keys
# it's not necessary for every key to have the same type
# check whether a value is in a dictionary ith the IN keyword
# can verify if a key is in the dictonary before looking it up
# dictionaries have the get method
# if expect lookups to fail get method is a better tool than square bracket lookups
# can check if a key returns none with the IS operator or opposite with IS NOT operator

# Identity Operators

# Keyword Operation
# is      evaluates if both sides have the same identity
# is not  evaluates if both sides have different identities

# Dictionaries
# A dictionary is a mutable data type that stores mappings of unique keys to
# values. Here's a dictionary that stores elements and their atomic numbers.

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

# Dictionaries can have keys of any immutable type, like integers or tuples,
# not just strings. It's not even necessary for every key to have the same type!
# We can look up values or insert new values in the dictionary using square
# brackets that enclose the key.

print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary

# We can check whether a value is in a dictionary the same way we check whether a
# value is in a list or set with the in keyword. Dicts have a related method that's
# also useful, get. get looks up values in a dictionary, but unlike square brackets,
# get returns None (or a default value of your choice) if the key isn't found.

print("carbon" in elements)
print(elements.get("dilithium"))

# This would output:
# True
# None

# Carbon is in the dictionary, so True is printed. Dilithium isn’t in our
# dictionary so None is returned by get and then printed. If you expect
# lookups to sometimes fail, get might be a better tool than normal square
# bracket lookups because errors can crash your program.

# Identity Operators

# Keyword	Operator
# is    	evaluates if both sides have the same identity
# is not	evaluates if both sides have different identities

# You can check if a key returned None with the is operator. You can check for
# the opposite using is not.

n = elements.get("dilithium")
print(n is None)
print(n is not None)
# This would output:
# True
# False

# quiz

# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {
'Shanghai': 17.8,
'Istanbul': 13.3,
'Karachi': 13.0,
'Mumbai': 12.5
}

print(population)

# question

# Which of these could be used as the key for a dictionary?
# (Choose all that apply.)
# Hint: Dictionary keys must be immutable, that is, they must be of a type
# that is not modifiable.

# str
# int
# float

# QUESTION

# What will the output of the following code be? (Treat the commas in the
# multiple choice answers as newlines.)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)

# returns True, True, True, False

# quiz

animals = {
'dogs': [20, 10, 15, 8, 32, 15],
'cats': [3,4,2,8,2,4],
'rabbits': [2, 3, 3],
'fish': [0.3, 0.5, 0.8, 0.3, 1]
}


# DESCRIPTION                                     | VALUE
# The data type of the keys in the dictionary     | string
# The data type of the values in the dictionary   | list
# The result of animals['dogs']                   | [20, 10, 15, 8, 32, 15]
# The result of animals['dogs'][3]                | 8
# The result of animals[3]                        | Error
# The result of animals['fish']                   | [0.3, 0.5, 0.8, 0.3, 1]



# Compound Data Structures

# We can include containers in other containers to create compound data
# structures. For example, this dictionary maps keys to values that are also
# dictionaries!

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

# We can access elements in this nested dictionary like this.

helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight

# You can also add a new key to the element dictionary.

oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print('elements = ', elements)

# Output is:
# elements =  {"hydrogen": {"number": 1,
#                          "weight": 1.00794,
#                          "symbol": 'H'},
#               "helium": {"number": 2,
#                          "weight": 4.002602,
#                          "symbol": "He"},
#               "oxygen": {"number": 8,
#                          "weight": 15.999,
#                          "symbol": "O"}}


# quiz

elements = {
'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}
}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True

print(elements['hydrogen']['is_noble_gas'])
# False
print(elements['helium']['is_noble_gas'])
# True


# Collections
# When we have a group of data we can think about it as a collection
# (of data elements).

# In this lesson, we have seen many different data structures that Python
# provides for storing, accessing and manipulating collections of data.
# In particular, we have seen lists, sets, and dictionaries.

# In the next few quizzes, you will have a chance to practice and review the
# properties of lists, sets, and dictionaries.

# QUESTION

# Check the attributes of a collection for which using a Python list
# would be appropriate.

# Items are always indexed with numbers starting at 0
# Sortable
# Add items with .append


# QUESTION

# Check the attributes of a collection for which using a Python set would be
# appropriate.

# Order in which items appear can be inconsistent
# Mutable (you can change it)
# Add items with .add


# QUESTION

# Check the attributes of a collection for which using a Python dictionary
# would be appropriate.

# Each item contains two parts
# Order in which items appear can be inconsistent
# Can be nested

# Summary

# You will need to practice! Use this FREE site to practice the skills you see
# in this course.
# https://www.hackerrank.com/domains/python

# Below is a review of the things you learned in this lesson. I know when I
# was getting started, I always wanted more practice. This course will move
# pretty fast from this point forward, so if you feel like you just want more
# practice problems on a topic, there are a number of free courses on the web.
# Two that you should definitely take advantage of (for the benefit of this
# program, but also for finding a job afterward) are:

# HackerRank - https://www.hackerrank.com/domains/python
# Codewars - https://www.codewars.com/users/sign_in

# Within each of these, you should create a profile and work on mastering Python!
# I was obsessed with these websites for getting all the practice I needed when
# I first started programming. As you get better, you can advance to harder
# problems and sites with even greater challenges.
# Happy coding!

# Lesson Summary
# You learned a ton in this lesson - here are a few of the big ideas to make
# sure you take them with you!

# Data Structures

# There are a number of built in python data structures that you will use all
# the time when programming. You can find a table of them available below:


# Data Structure | Ordered | Mutable  | Constructor         | Example
# int	         | NA	   | NA	      | int()	            | 5
# float	         | NA	   | NA	      | float()	            | 6.5
# string	     | Yes	   | No	      | ' ' or " " or str()	| "this is a string"
# bool	         | NA	   | NA	      | NA	                |True or False
# list	         | Yes	   | Yes	  | [ ] or list()	    | [5, 'yes', 5.7]
# tuple	         | Yes	   | No	      | ( ) or tuple()	    | (5, 'yes', 5.7)
# set	         | No	   | Yes	  | { } or set()	    | {5, 'yes', 5.7}
# dictionary	 | No	   | Keys: No |	{ } or dict()	    | {'Jun':75, 'Jul':89}

# Mathematical, Comparison, and Logical Operators

# You also learned about mathematical operators, as shown in the table below
# and logical operators shown in the table below that! Awesome job!

# Mathematical Operators

  # Arithmetic Operators
  # Symbol | Operation
  # +      | addition
  # -      | subtraction
  # *      | multiplication
  # /      | division
  # **     | exponentiation
  # %      | modulo
  # //     | integer division

# Comparison and Logical Operators

  # Comparison Operators
  # Symbol | Operation
  # <      | less than
  # >      | greater than
  # <=     | less than or equal to
  # >=     | greater than or equal to
  # ==     | equal to
  # !=     | not equal to

# Booleans, Comparison Operators, and Logical Operators

# The bool data type holds one of the values True or False, which are often
# encoded as 1 or 0, respectively.

# There are 6 comparison operators that are common to see in order to obtain
# a bool value:

# Comparison Operators
# Symbol Use Case	| Bool  | Operation
# 5 < 3             | False	| Less Than
# 5 > 3	            | True	| Greater Than
# 3 <= 3	        | True	| Less Than or Equal To
# 3 >= 5	        | False	| Greater Than or Equal To
# 3 == 5	        | False	| Equal To
# 3 != 5	        | True	| Not Equal To

# And there are three logical operators you need to be familiar with:

# Logical Use      | Bool  | Operation
# 5 < 3 and 5 == 5 | False | and - Evaluates if all provided statements are True
# 5 < 3 or 5 == 5  | True  | or - Evaluates if at least one of many statements is True
# not 5 < 3	       | True  | not - Flips the Bool Value

# Here is more information on how George Boole changed the world!
# https://www.irishtimes.com/news/science/how-george-boole-s-zeroes-and-ones-changed-the-world-1.2014673

# At this point, you have learned a lot of skills to build on. The next
# lessons move pretty quickly to help you understand a number of coding
# practices that you will see in a job, as well as help you get prepared
# for the project.



# LESSON 03

# Introduction

# Control Flow

# Welcome to this lesson on Control Flow! Control flow is the sequence in which
# your code is run. Here, we'll learn about several tools in Python we can use to
# affect our code's control flow:

# Conditional Statements

# 1. Boolean Expressions
# 2. For and While Loops
# 3. Break and Continue
# 4. Zip and Enumerate
# 5. List Comprehensions


# Conditional Statements

# If Statement

# An if statement is a conditional statement that runs or skips code based on
# whether a condition is true or false. Here's a simple example.

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

# Let's break this down.

# An if statement starts with the if keyword, followed by the condition to be
# checked, in this case phone_balance < 5, and then a colon. The condition is
# specified in a boolean expression that evaluates to either True or False.

# After this line is an indented block of code to be executed if that condition
# is true. Here, the lines that increment phone_balance and decrement bank_balance
# only execute if it is true that phone_balance is less than 5. If not, the code
# in this if block is simply skipped.

phone_balance = 8
bank_balance = 100

print(phone_balance, bank_balance)

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance, bank_balance)

#Use Comparison Operators in Conditional Statements

# You have learned about Python's comparison operators (e.g. == and !=) and
# how they are different from assignment operators (e.g. =). In conditional
# statements, you want to use comparison operators. For example, you'd want to
# use if x == 5 rather than if x = 5. If your conditional statement is causing
# a syntax error or doing something unexpected, check whether you have
# written == or =!

n = 5

if n % 2 == 0:
    print("Number " + str(n) + " is even.")
else:
    print("Number " + str(n) + " is odd.")

# If, Elif, Else

# In addition to the if clause, there are two other optional clauses often
# used with an if statement. For example:

season = 'spring'

if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')

# if: An if statement must always start with an if clause, which contains the
# first condition that is checked. If this evaluates to True, Python runs the
# code indented in this if block and then skips to the rest of the code after
# the if statement.

# elif: elif is short for "else if." An elif clause is used to check for an
# additional condition if the conditions in the previous clauses in the if
# statement evaluate to False. As you can see in the example, you can have
# multiple elif blocks to handle different situations.

# else: Last is the else clause, which must come at the end of an if statement
# if used. This clause doesn't require a condition. The code in an else block
# is run if all conditions above that in the if statement evaluate to False.

# remember
# = is an assignment operator that assigns value on the left to the name on the right
# == is a comparison operator that evaluates whether objects on both sides are equal

# Indentation

# Some other languages use braces to show where blocks of code begin and end.
# In Python we use indentation to enclose blocks of code. For example, if
# statements use indentation to tell Python what code is inside and outside of
# different clauses.

# In Python, indents conventionally come in multiples of four spaces. Be strict
# about following this convention, because changing the indentation can completely
# change the meaning of the code. If you are working on a team of Python
# programmers, it's important that everyone follows the same indentation convention!

# Spaces or Tabs?

# The Python Style Guide recommends using 4 spaces to indent, rather than using
# a tab. Whichever you use, be aware that "Python 3 disallows mixing the use of
# tabs and spaces for indentation."

#First Example - try changing the value of phone_balance
phone_balance = 10
bank_balance = 50

if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance)
print(bank_balance)

#Second Example - try changing the value of number

number = 145
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")

#Third Example - try to change the value of age
age = 35

# Here are the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# These lines determine the bus fare prices
concession_ticket = 1.25
adult_ticket = 2.50

# Here is the logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)


# Practice: Which Prize

# Write an if statement that lets a competitor know which of these prizes
# they won based on the number of points they scored, which is stored in the
# integer variable points.

# Points    |  Prize
# 1 - 50	|  wooden rabbit
# 51 - 150	|  no prize
# 151 - 180	|  wafer-thin mint
# 181 - 200	|  penguin

# All of the lower and upper bounds here are inclusive, and points can only
# take on positive integer values up to 200.

# In your if statement, assign the result variable to a string holding the appropriate
# message based on the value of points. If they've won a prize, the message should
# state "Congratulations! You won a [prize name]!" with the prize name. If there's no prize,
# the message should state "Oh dear, no prize this time."

# Note: Feel free to test run your code with other inputs, but when you submit your answer,
# only use the original input of points = 174. You can hide your other inputs by
# commenting them out.


points = 174  # use this input to make your submission


# write your if statement here

points = 174

if points <= 50:
	result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
	result = "Oh dear, no prize this time."
elif points <= 180:
	result = "Congratulations! You won a wafer-thin mint!"
else:
	result = "Congratulations! You won a penguin!"

print(result)

# Output:
# Congratulations! You won a wafer-thin mint!

# We use <= instead of the < operator, since it was stated that the upper bound
# is inclusive. Notice that in each condition, we check if points is in a prize
# bracket by checking if points is less than or equal to the upper bound; we
# didn't have to check if it was greater than the lower bound. Let's see why this
# is the case.

# When points = 174, it first checks if points <= 50, which evaluates to False.
# We don't have to check if it is also greater than 0, since it is stated in
# the problem that points will always be a positive integer up to 200.

# Since the first condition evaluates to False, it moves on to check the next
# condition, points <= 150. We don't need to check if it is also greater than
# 50 here! We already know this is the case because the first condition has to
# have evaluated to False in order to get to this point. If we know points <= 50
# is False, then points > 50 must be True!

# Finally, we check if points <= 180, which evaluates to True. We now know that
# points is in the 151 - 180 bracket.

# The last prize bracket, 181-200, is caught in the else clause, since there is
# no other possible value of the prize after checking the previous conditions.

# '''
# You decide you want to play a game where you are hiding
# a number from someone.  Store this number in a variable
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 35
guess = 30   # this is just a sample answer and guess

if guess < answer:
	result = "Oops!  Your guess was too low."
elif guess > answer:
	result = "Oops!  Your guess was too high."
elif guess==answer:
	result = "Nice!  Your guess matched the answer!"
print(result)

# '''
# Depending on where an individual is from we need to tax them
# appropriately.  The states of CA, MN, and
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = 'CA'
purchase_amount = 20.00    # a sample state and purchase amount

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)


# Boolean Expressions for Conditions

# Complex Boolean Expressions

# If statements sometimes use more complicated boolean expressions for their
# conditions. They may contain multiple comparisons operators, logical operators,
# and even calculations. Examples:

if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

if is_raining and is_sunny:
    print("Is there a rainbow?")

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")

# For really complicated conditions you might need to combine some ands, ors and
# nots together. Use parentheses if you need to make the combinations clear.

# However simple or complex, the condition in an if statement must be a boolean
# expression that evaluates to either True or False and it is this value that
# decides whether the indented block in an if statement executes or not.


# Good and Bad Examples

# Here are some things to keep in mind while writing boolean expressions for
# your if statements.

# 1. Don't use True or False as conditions
# Bad example
if True:
    print("This indented code will always get run.")

# While "True" is a valid boolean expression, it's not useful as a condition
# since it always evaluates to True, so the indented code will always get run.
# Similarly, if False is not a condition you should use either - the statement
# following this if statement would never be executed.

# Another bad example
if is_cold or not is_cold:
    print("This indented code will always get run.")

# Another bad example
is_cold = True

if is_cold or not is_cold:
    print("The weather is cold or not cold.")

# Similarly, it's useless to use any condition that you know will always evaluate
# to True, like this example above. A boolean variable can only be True or False,
# so either is_cold or not is_cold is always True, and the indented code will
# always be run.

# 2. Be careful writing expressions that use logical operators

# Logical operators and, or and not have specific meanings that aren't quite the
# same as their meanings in plain English. Make sure your boolean expressions are
# being evaluated the way you expect them to.

# Bad example
if weather == "snow" or "rain":
    print("Wear boots!")

# This code is valid in Python, but it is not a boolean expression, although it
# reads like one. The reason is that the expression to the right of the or
# operator, "rain", is not a boolean expression - it's a string! Later we'll
# discuss what happens when you use non-boolean-type objects in place of booleans.

# Good example
if weather == "snow" or weather == "rain":
    print("Wear boots!")

# 3. Don't compare a boolean variable with == True or == False
# This comparison isn’t necessary, since the boolean variable itself is a
# boolean expression.

# Bad example
if is_cold == True:
    print("The weather is cold!")

# This is a valid condition, but we can make the code more readable by using
# the variable itself as the condition instead, as below.

# Good example
if is_cold:
    print("The weather is cold!")

# If you want to check whether a boolean is False, you can use the not operator.

# Summary Lessons learned
# 1. Don't use if: True or if: False
# 2. Be carefule writing expressions that use logical operators: and, or, not
# 3. Do not evaluate the truth of a boolean variable with ==.  The variable itself
# is a boolean expression

# Truth Value Testing

# If we use a non-boolean object as a condition in an if statement in place of
# the boolean expression, Python will check for its truth value and use that to
# decide whether or not to run the indented code. By default, the truth value of
# an object in Python is considered True unless specified as False in the
# documentation.

# Here are most of the built-in objects that are considered False in Python:

# constants defined to be false: None and False
# zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# empty sequences and collections: '"", (), [], {}, set(), range(0)

# Example:

errors = 3
if errors:
    print("You have {} errors to fix!".format(errors))
else:
    print("No errors to fix!")

# In this code, errors has the truth value True because it's a non-zero number,
# so the error message is printed. This is a nice, succinct way of writing an
# if statement.

# Python documentation on Truth Value Testing
# https://docs.python.org/3/library/stdtypes.html

# question

altitude = 10000
speed = 250
propulsion = "Propeller"

# Match
# Expression                      |  True or False
#                                 |
# altitude < 1000 and speed > 100 |  False
#                                 |
# (propulsion == "Jet" or         |  False
# propulsion == "Turboprop") and  |
# speed < 300 and                 |
# altitude > 20000                |
#                                 |
# not (speed > 400 and            |  True
# propulsion == "Propeller")      |
#                                 |
# (altitude > 500 and             |  True
# speed > 100) or                 |
# not propulsion == "Propeller"   |


# Quiz: Using Truth Values of Objects
# The code below is the solution to the Which Prize quiz you've seen previously.
# You're going to rewrite this based on what you've learned about truth values.

points = 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)

# You will use a new variable prize to store a prize name if one was won, and
# then use the truth value of this variable to compose the result message. This
# will involve two if statements.

# 1st conditional statement: update prize to the correct prize name based on points.
# 2nd conditional statement: set result to the correct phrase based on whether
# prize is evaluated as True or False.

# If prize is None, result should be set to "Oh dear, no prize this time."
# If prize contains a prize name, result should be set to "Congratulations!
# You won a {}!".format(prize). This will avoid having the multiple result
# assignments for different prizes.
# At the beginning of your code, set prize to None, as the default value.

points = 174  # use this as input for your submission

# establish the default prize value to None


# use the points value to assign prizes to the correct prize names


# use the truth value of prize to assign result to the correct prize

points = 174  # use this input when submitting your answer

# set prize to default value of None
prize = None

# use the value of points to assign prize to the correct prize name
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"

# use the truth value of prize to assign result to the correct message
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."


# For Loops

# Python has two kinds of loops - for loops and while loops. A for loop is
# used to "iterate", or do something repeatedly, over an iterable.

# An iterable is an object that can return one of its elements at a time.
# This can include sequence types, such as strings, lists, and tuples, as
# well as non-sequence types, such as dictionaries and files.

# You can define objects within an iter method to allow them to be used as iterable.
# https://www.programiz.com/python-programming/methods/built-in/iter

# Example

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city.title())


# Example

# Let's break down the components of a for loop, using this example with
# the list cities:

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
print("Done!")

# Components of a for Loop

# 1. The first line of the loop starts with the for keyword, which signals that
# this is a for loop

# 2.  Following that is city in cities, indicating city is the iteration variable,
# and cities is the iterable being looped over (the variable that represents the
# element in the iterable that the loop is currently processing). In the first
# iteration of the loop, city gets the value of the first element in cities,
# which is “new york city”.

# 3. The for loop heading line always ends with a colon :

# 4. Following the for loop heading is an indented block of code, the body of the
# loop, to be executed in each iteration of this loop. There is only one line in
# the body of this loop - print(city).  Here this indented body is executed once
# for each element in cities.

# 5. After the body of the loop has executed, we don't move on to the next line
# yet; we go back to the for heading line, where the iteration variable takes
# the value of the next element of the iterable. In the second iteration of the
# loop above, city takes the value of the next element in cities, which is
# "mountain view".

# 6. This process repeats until the loop has iterated through all the elements
# of the iterable. Then, we move on to the line that follows the body of the
# loop - in this case, print("Done!"). We can tell what the next line after the
# body of the loop is because it is unindented. Here is another reason why
# paying attention to your indentation is very important in Python!

# Executing the code in the example above produces this output:

# new york city
# mountain view
# chicago
# los angeles
# Done!

# You can name iteration variables however you like. A common pattern is to give
# the iteration variable and iterable the same names, except the singular and
# plural versions respectively (e.g., 'city' and 'cities').

# The loop above extracts information from a list.  You can also use For Loops
# to create lists and to modify lists.  Start with an empty list and use the
# append method to add new items.

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())

print(capitalized_cities)

# Modifying a list is a bit more involved and requires a use of a new function:

range(start, stop, step)

# Range is a butit in function used to create immutable sequences of numbers.
# Has three arguments which must all be integers: start, stop, step

    # start is first number of sequence
        # if unspecified defaults to zero
    # stop is one above the last mumber of the sequence
        # if unspecified defaults to one
    # step is the difference between start and stop

# 1. Calling range with one integer will make that the stop arfument and
# return a sequence of

# so range four returns zero through three

print(list(range(4)))
# returns [0, 1, 2, 3]

# 2. Caliing range with two integers will make those start and stop and
# return a sequence of numbers from the first number to second number minus one

# so range 2, 6 returns a sequence from 2 to 5

print(list(range(2, 6)))
# returns [2, 3, 4, 5]

# 3. Calling range with three integers will return a sequence of numbers from
# the first to the second minus one seperated by the third

# so range 1, 10, 2 returns a sequence from 1 to 9, incremented by 2

print(list(range(1, 10, 2)))
# returns [1, 3, 5, 7, 9]

# Using the range() Function with for Loops
# range() is a built-in function used to create an iterable sequence of numbers.
# You will frequently use range() with a for loop to repeat an action a certain
# number of times, as in this example:

# Note printing just the output of range only shows you a range object

print(range(4))
# returns range(0, 4)

# You can view the values in a range object by converting it to a ist or iterating
# through it in a for loop

for i in range(3):
    print("Hello!")

# Output:

# Hello!
# Hello!
# Hello!

for number in range (4)
    print(number)

# Output:

# 0
# 1
# 2
# 3


cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for index in range(len(cities)): # len cities equals 4
    cities[index] = cities[index].title()
    print(index)

print(cities)
# Output:

# 0
# 1
# 2
# 3

range(start=0, stop, step=1)

# The range() function takes three integer arguments, the first and third of
#which are optional:

# 1. The 'start' argument is the first number of the sequence. If unspecified,
# 'start' defaults to 0.
# 2. The 'stop' argument is 1 more than the last number of the sequence. This
# argument must be specified.
# 3. The 'step' argument is the difference between each number in the sequence.
# If unspecified, 'step' defaults to 1.

# Notes on using range():

# 1. If you specify one integer inside the parentheses withrange(), it's used as
# the value for 'stop,' and the defaults are used for the other two.
# e.g. - range(4) returns 0, 1, 2, 3
# 2. If you specify two integers inside the parentheses withrange(), they're
# used for 'start' and 'stop,' and the default is used for 'step.'
# e.g. - range(2, 6) returns 2, 3, 4, 5
# 3. Or you can specify all three integers for 'start', 'stop', and 'step.'
# e.g. - range(1, 10, 2) returns 1, 3, 5, 7, 9

# Creating and Modifying Lists

# In addition to extracting information from lists, as we did in the first
# example above, you can also create and modify lists with for loops. You can
# create a list by appending to a new list at each iteration of the for loop
# like this:

# Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())

# Modifying a list is a bit more involved, and requires the use of the range()
# function.

# We can use the range() function to generate the indices for each value in the
# cities list. This lets us access the elements of the list with cities[index]
# so that we can modify the values in the cities list in place.

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()


# for loop practice

sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line

sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

for word in sentence:
    print(word)


# Write a for loop using range() to print out multiples of 5 up to 30 inclusive

for i in range(5, 35, 5):
    print(i)


# Quiz: Create Usernames
# Write a for loop that iterates over the names list to create a usernames list.
# https://stackoverflow.com/questions/12723751/replacing-instances-of-a-character-in-a-string/12723785#12723785
# To create a username for each name, make everything lowercase and replace spaces
# with underscores. Running your for loop over the list:

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here

for name in names:
    usernames.append(name.lower().replace(" ", "_"))

print(usernames)


# question

# Let's say instead of creating a new list, we want to modify the names list
# itself with the changes and write the following code. What would this do?

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(names)

# printed output for nanes list will look exactly like it did in the first line

# Quiz: Modify Usernames with Range
# Write a for loop that uses range() to iterate over the positions in usernames to
# modify the list. Like you did in the previous quiz, change each name to be lowercase
# and replace spaces with underscores. After running your loop, this list

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")

print(usernames)


# Quiz: Tag Counter
# Write a for loop that iterates over a list of strings, tokens, and counts
# how many of them are XML tags. XML is a data language similar to HTML. You
# can tell if a string is an XML tag if it begins with a left angle bracket "<"
# and ends with a right angle bracket ">". Keep track of the number of tags using
# the variable count.

# You can assume that the list of strings will not contain empty strings.


tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)


# Quiz: Create an HTML List
# Write some code, including a for loop, that iterates over a list of strings
# and creates a single string, html_str, which is an HTML list. For example, if
# the list is items = ['first string', 'second string'], printing html_str
# should output:

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)

print(html_str)


# QUESTION
# Practice with range
# For each below, match the input code to the appropriate output.

print(list(range(4)))
# outputs [0,1,2,3]

print(list(range(4,8)))
# outputs [4,5,6,7]

print(list(range(4,10,2)))
# outputs [4,6,8]

print(list(range(0,-5)))
# outputs [ ]


# Use the code below to complete the next question.

colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = [ ]

for color in colors:
    #finish this part
    lower_colors.append(color.lower())


# QUESTION
# If you want to create a new list called lower_colors, where each color in
# colors is lower cased, which code line should be inserted into the code
# block above?

lower_colors.append(color.lower())


# Building Dictionaries

# By now you are familiar with two important concepts: 1) counting with for
# loops and 2) the dictionary get method. These two can actually be combined
# to create a useful counter dictionary, something you will likely come across
# again. For example, we can create a dictionary, word_counter, that keeps track
# of the total count of each word in a string.

# The following are a couple of ways to do it:

# Method 1: Using a for loop to create a set of counters
# Let's start with a list containing the words in a series of book titles:

book_title =  [
'great',
'expectations',
'the',
'adventures',
'of',
'sherlock',
'holmes',
'the',
'great',
'gasby',
'hamlet',
'adventures',
'of',
'huckleberry',
'fin']

# Step 1: Create an empty dictionary.

word_counter = {}

# Step 2. Iterate through each element in the list. If an element is already
# included in the dictionary, add 1 to its value. If not, add the element to
# the dictionary and set its value to 2.

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1

print(word_counter)

# What's happening here?
# The for loop iterates through each element in the list. For the first
# iteration, word takes the value 'great'.
# Next, the if statement checks if word is in the word_counter dictionary.
# Since it doesn't yet, the statement word_counter[word] = 1 adds great as a
# key to the dictionary with a value of 1.
# Then, it leaves the if else statement and moves on to the next iteration of
# the for loop. word now takes the value expectations and repeats the process.
# When the if condition is not met, it is because that word already exists in
# the word_counter dictionary, and the statement word_counter[word] =
# word_counter[word] + 1 increases the count of that word by 1.
# Once the for loop finishes iterating through the list, the for loop is complete.
# We can see the output by printing out the dictionary. Printing word_counter
# results in the following output:

{
'great': 2,
'expectations': 1,
'the': 2,
'adventures': 2,
'of': 2,
'sherlock': 1,
'holmes': 1,
'gasby': 1,
'hamlet': 1,
'huckleberry': 1,
'fin': 1
}

# Method 2: Using the get method
# We will use the same list for this example:

book_title =  [
'great',
'expectations',
'the',
'adventures',
'of',
'sherlock',
'holmes',
'the',
'great',
'gasby',
'hamlet',
'adventures',
'of',
'huckleberry',
'fin'
]

# Step 1: Create an empty dictionary.
word_counter = {}

# Step 2. Iterate through each element, get() its value in the dictionary,
# and add 1.
# Recall that the dictionary get method is another way to retrieve the value of
# a key in a dictionary. Except unlike indexing, this will return a default value
# if the key is not found. If unspecified, this default value is set to None.
# We can use get with a default value of 0 to simplify the code from the first
# method above.

for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1
    print(word_counter)

print(word_counter)

# What's happening here?
# The for loop iterates through the list as we saw earlier. The for loop feeds
# 'great' to the next statement in the body of the for loop.
# In this line: word_counter[word] = word_counter.get(word,0) + 1, since the
# key 'great' doesn't yet exist in the dictionary, get() will return the value
# 0 and word_counter[word] will be set to 1.
# Once it encounters a word that already exists in word_counter (e.g. the
# second appearance of 'the'), the value for that key is incremented by 1. On
# the second appearance of 'the', the key's value would add 1 again, resulting in 2.
# Once the for loop finishes iterating through the list, the for loop is complete.
# Printing word_counter shows us we get the same result as we did in method 1.

{
'great': 2,
'expectations': 1,
'the': 2,
'adventures': 2,
'of': 2,
'sherlock': 1,
'holmes': 1,
'gasby': 1,
'hamlet': 1,
'huckleberry': 1,
'fin': 1
}

# Iterating Through Dictionaries with For Loops

# When you iterate through a dictionary using a for loop, doing it the normal
# way (for n in some_dict) will only give you access to the keys in the
# dictionary - which is what you'd want in some situations. In other cases,
# you'd want to iterate through both the keys and values in the dictionary.
# Let's see how this is done in an example. Consider this dictionary that uses
# names of actors as keys and their characters as values.

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

# Iterating through it in the usual way with a for loop would give you just
# the keys, as shown below:

for key in cast:
    print(key)

# This outputs:

# Jerry Seinfeld
# Julia Louis-Dreyfus
# Jason Alexander
# Michael Richards

# If you wish to iterate through both keys and values, you can use the
# built-in method items like this:

for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

# This outputs:

# Actor: Jerry Seinfeld    Role: Jerry Seinfeld
# Actor: Julia Louis-Dreyfus    Role: Elaine Benes
# Actor: Jason Alexander    Role: George Costanza
# Actor: Michael Richards    Role: Cosmo Kramer

# items is an awesome method that returns tuples of key, value pairs, which
# you can use to iterate over dictionaries in for loops.

# Quiz: Fruit Basket - Task 1
# You would like to count the number of fruits in your basket. In order to do this,
# you have the following dictionary and list of fruits. Use the dictionary and list
#to count the total number of fruits, but you do not want to count the other items
# in your basket.


#Example 1

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here

for fruit, count in basket_items.items():
   if fruit in fruits:
       result += count

print("There are {} fruits in the basket.".format(result))

print(result)

# Quiz: Fruit Basket - Task 2
# If your solution is robust, you should be able to use it with any dictionary of
# items to count the number of fruits in the basket. Try the loop for each of the
# dictionaries below to make sure it always works.

#Example 2

result = 0
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here

for fruit, count in basket_items.items():
   if fruit in fruits:
       result += count

print("There are {} fruits in the basket.".format(result))


# Quiz: Fruit Basket - Task 3
# So, a couple of things about the above examples:

# 1. It is a bit annoying having to copy and paste all the code to each spot - wouldn't
# it be nice to have a way to repeat the process without copying all the code? Don't worry!
# You will learn how to do this in the next lesson!


# 2. It would be nice to keep track of both the number of fruits and other items in the basket.

#Example 3

result = 0
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here

#Iterate through the dictionary
for fruit, count in basket_items.items():
    if fruit in fruits:
       fruit_count += count
    else:
        not_fruit_count += count

print("The number of fruits is {}.  There are {} items that are not fruits.".format(fruit_count, not_fruit_count))


# While Loops

# For loops are an example of "definite iteration" meaning that the loop's body
# is run a predefined number of times.
# A for loop
# This differs from "indefinite iteration"
# which is when a loop repeats an unknown number of times and ends when some condition
# is met, which is what happens in a while loop. Here's an example of a while loop.

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand)  < 17:
    hand.append(card_deck.pop())

print(hand)

# This example features two new functions. sum returns the sum of the elements in
# a list, and pop is a list method that removes the last element from a list and returns it.

# Components of a While Loop

# 1. The first line starts with the while keyword, indicating this is a while loop.

# 2. Following that is a condition to be checked. In this example, that's sum(hand) <= 17.

# 3. The while loop heading always ends with a colon :.

# 4. Indented after this heading is the body of the while loop. If the condition
# for the while loop is true, the code lines in the loop's body will be executed.

# 5. We then go back to the while heading line, and the condition is evaluated again.
# This process of checking the condition and then executing the loop repeats until
# the condition becomes false.


# 6. When the condition becomes false, we move on to the line following the body of
# the loop, which will be unindented.

# The indented body of the loop should modify at least one variable in the test
# condition. If the value of the test condition never changes, the result is an
# infinite loop!



# Practice: Factorials with While Loops
# Find the factorial of a number using a while loop.

# A factorial of a whole number is that number multiplied by every whole number
# between itself and 1. For example, 6 factorial (written "6!") equals
# 6 x 5 x 4 x 3 x 2 x 1 = 720. So 6! = 720.

# We can write a while loop to take any given number and figure out what its
# factorial is.

# Example: If number is 6, your code should compute and print the product, 720.

# number to find the factorial of
number = 6
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1

while  current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1

# print the factorial of number
print(product)


# Practice: Factorials with For Loops
# Now use a for loop to find the factorial!

# It will now be great practice for you to try to revise the code you wrote
# above to find the factorial of a number, but this time, using a for loop.
# Try it in the code editor below!

# number we'll find the factorial of
number = 6
# start with our product equal to one
product = 1

# calculate factorial of number with a for loop
for num in range(2, number + 1):
    product *= num

# print the factorial of number
print(product)



# write Fibonacci series up to n

def fib(n):
#Print a Fibonacci series up to n.
    n=2000
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b
# Now call the function we just defined
fib(2000)


# Quiz: Count By
# Suppose you want to count from some number start_num by another number
# count_by until you hit a final number end_num. Use break_num as the variable
# that you'll change each time through the loop. For simplicity, assume that
# end_num is always larger than start_num and count_by is always positive.

# Before the loop, what do you want to set break_num equal to? How do you want
# to change break_num each time through the loop? What condition will you use
# to see when it's time to stop looping?

# After the loop is done, print out break_num, showing the value that indicated
# it was time to stop looping. It is the case that break_num should be a number
# that is the first number larger than end_num.

start_num = 5
end_num = 100
count_by = 2

break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)


# Quiz: Count By Check
# Suppose you want to count from some number start_num by another number count_by
# until you hit a final number end_num, and calculate break_num the way you did in
# the last quiz.

# Now in addition, address what would happen if someone gives a start_num that
# is greater than end_num. If this is the case, set result to "Oops! Looks like
# your start value is greater than the end value. Please try again." Otherwise,
# set result to the value of break_num.

start_num = 5
end_num = 100
count_by = 2

if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)


# Quiz: Nearest Square
# Write a while loop that finds the largest square number less than an integerlimit
# and stores it in a variable nearest_square. A square number is the product of an
# integer multiplied by itself, for example 36 is a square number because it equals 6*6.

# For example, if limit is 40, your code should set the nearest_square to 36.

limit = 40

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)



# Break, Continue
# Sometimes we need more control over when a loop should end, or skip an iteration.
# In these cases, we use the break and continue keywords, which can be used in both
# for and while loops.

# break terminates a for loop or while loop
# continue skips one iteration of a for loop or while loop

# debugging with break

manifest = [("bananas", 15),
("mattresses", 34),
("dog kennels", 42),
("machine", 120),
("cheeses", 5)]

weight = 0
items = []

for cargo in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("breaking loop now")
        break
    else:
        print(" adding {} ({})".format(cargo[0], cargo[1]))
        items.append(cargo[0])
        weight += cargo[1]

print(weight)
print(items)

# continue

fruit = ["orange", "strawberry", "apple"]
foods = ["apple", "apple", "humus", "toast"]

fruit_count = 0
for food in foods:
    if food not in fruit:
        print("Not a fruit")
        continue
    fruit_count += 1
    print("Found a fruit")

print("total fruit ", fruit_count)


# Quiz: Break the String
# Write a loop with a break statement to create a string, news_ticker, that is
# exactly 140 characters long. You should create the news ticker by adding
# headlines from the headlines list, inserting a space in between each headline.
# If necessary, truncate the last headline in the middle so that news_ticker is
# exactly 140 characters long.

# Remember that break works in both for and while loops. Use whichever loop seems
# most appropriate. Consider adding print statements to your code to help you
# resolve bugs.

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)


# Zip and Enumerate

# zip and enumerate are useful built-in functions that can come in handy when
# dealing with loops.

# Zip

# zip returns an iterator that combines multiple iterables into one sequence of
# tuples. Each tuple contains the elements in that position from all the iterables.

manifest = [("bananas", 15),
("mattresses", 34),
("dog kennels", 42),
("machine", 120),
("cheeses", 5)]

items, weights = zip(*manifest)

print(items)
print(weights)


# For example, printing

list(zip(['a', 'b', 'c'], [1, 2, 3]))
# would output [('a', 1), ('b', 2), ('c', 3)].

# Like we did for range() we need to convert it to a list or iterate through it
# with a loop to see the elements.

# You could unpack each tuple in a for loop like this.

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

# In addition to zipping two lists together, you can also unzip a list into
# tuples using an asterisk.

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
# This would create the same letters and nums tuples we saw earlier.

# Enumerate

# items zip

item = ["bananas",
"mattresses",
"dog kennels",
"machine",
"cheeses"
]

for i, item in zip(range(len(items)), items):
    print(i, item)

# items enumerate

items = ["bananas",
"mattresses",
"dog kennels",
"machine",
"cheeses"
]

for i, item in enumerate(items):
    print(i, item)


# enumerate is a built in function that returns an iterator of tuples containing
# indices and values of a list. You'll often use this when you want the index along
# with each element of an iterable in a loop.

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
# This code would output:

# 0 a
# 1 b
# 2 c
# 3 d
# 4 e



# Quiz: Zip Coordinates
# Use zip to write a for loop that creates a string specifying the label and
# coordinates of each point and appends it to the list points. Each string
# should be formatted as label: x, y, z. For example, the string for the first
# coordinate should be F: 23, 677, 4.

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)

# Quiz: Zip Lists to a Dictionary
# Use zip to create a dictionary cast that uses names as keys and heights as values

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)

# Quiz: Unzip Tuples
# Unzip the cast tuple into two names and heights tuples.

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

names, heights = zip(*cast)
print(names)
print(heights)

# Quiz: Transpose with Zip
# Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. There's
# actually a cool trick for this! Feel free to look at the solutions if you
# can't figure it out.

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)

# Quiz: Enumerate
# Use enumerate to modify the cast list so that each element contains the name
# followed by the character's corresponding height. For example, the first element
# of cast should change from "Barney Stinson" to "Barney Stinson 72".

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

print(cast)


# List Comprehensions

cities = [
"new york city",
"mountain view",
"chicago",
"los angeles"
]

capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())

print(capitalized_cities)

# In Python, you can create lists really quickly and concisely with list
# comprehensions. This example from earlier:

capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())

# can be reduced to:

capitalized_cities = [city.title() for city in cities]

# list of squares

squares = []

for x in range(9)
    squares.append(x*2)
print(squares)

# reduces to

squares = [x**2 for x in range(9)]
print(squares)

# List comprehensions allow us to create a list using a for loop in one step.

# You create a list comprehension with brackets [], including an expression to
# evaluate for each element in an iterable. This list comprehension above calls
# city.title() for each element city in cities, to create each element in the
# new list, capitalized_cities.

# Conditionals in List Comprehensions

# You can also add conditionals to list comprehensions (listcomps). After the
# iterable, you can use the if keyword to check a condition in each iteration.

squares = [x**2 for x in range(9) if x % 2 == 0]
# The code above sets squares equal to the list [0, 4, 16, 36, 64], as x to the
# power of 2 is only evaluated if x is even. If you want to add an else, you will
# get a syntax error doing this.

squares = [x**2 for x in range(9) if x % 2 == 0 else x + 3]
# If you would like to add else, you have to move the conditionals to the
# beginning of the listcomp, right after the expression, like this.

squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
# List comprehensions are not found in other languages, but are very common in
# Python.


# Quiz: Extract First Names
# Use a list comprehension to create a new list first_names containing just the
# first names in names in lowercase.

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)

# Quiz: Multiples of Three
# Use a list comprehension to create a list multiples_3 containing the first 20
# multiples of 3.

multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)

# Quiz: Filter Names by Scores
# Use a list comprehension to create a list of names passed that only include
# those that scored at least 65.

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)


# LESSON 04
# Functions

# Welcome to this lesson on Functions! You'll learn about:

# 1. Defining Functions
# 2. Variable Scope
# 3. Documentation
# 4. Lambda Expressions
# 5. Iterators and Generators

# You can think about functions as a way to take what you have already learned
# how to do, and put it in a holder that allows you to use it over and over again
# in an easy to use container.



# Defining Functions
# Example of a function definition:

def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2
# After defining the cylinder_volume function, we can call the function like this.

cylinder_volume(10, 3)
# This is called a function call statement.

# A function definition includes several important parts.

# Function Header

# 1. Let's start with the function header, which is the first line of a function definition.
# The function header always starts with the def keyword, which indicates that
# this is a function definition

# 2. Then comes the function name (here, cylinder_volume), which follows the same
# naming conventions as variables.
# Needs to be one word with no gaps.
# You can revisit the naming conventions below.

# 3. Immediately after the name are parentheses that may include arguments separated
# by commas (here, height and radius). Arguments, or parameters, are values that
# are passed in as inputs when the function is called, and are used in the function
# body. If a function doesn't take arguments, these parentheses are left empty.

# 4. The header always end with a colon :.

# example fucntion with no arguments

def print_greeting():
    print("Hello World")



# Function Body

# The rest of the function is contained in the body, which is where the function
# does its work.

# 1. The body of a function is the code indented after the header line. Here, it's
# the two lines that define pi and return the volume.

# 2. Within this body, we can refer to the argument variables, and define new
# variables, which can only be used within these indented lines.

# 3. The pi variable in the cylinder_volume functions is a local variable. It can
# only be used within the body of this function.
# The body will often include a return statement, which is used to send back an
# output value from the function to the statement that called the function. A
# return statement consists of the return keyword followed by an expression that
# is evaluated to get the output value for the function. If there is no return
# statement, the function simply returns None.

# Naming Conventions for Functions

# Function names follow the same naming conventions as variables.

# 1. Only use ordinary letters, numbers and underscores in your function names.
# They can’t have spaces, and need to start with a letter or underscore.

# 2. You can’t use reserved words or built-in identifiers that have important purposes
# in Python, which you’ll learn about throughout this course. A list of Python reserved words is described here.

# 3. Try to use descriptive names that can help readers understand what the function does.

# QUESTION 1 OF 2
# Which of the below are acceptable ways to begin a function in Python?

# def my_function(arg1, arg2):
# def my_function(arg2, arg1, arg4):

# Print vs. Return in Functions

# Here are two valid functions. One returns a value and one simply prints a value,
# without returning anything. Test run this code and experiment to understand
# the difference.

# this prints something, but does not return anything
# Some funcrions like print don not return anything at all.
# Print displays text on the output window, but the value it returns is none
# None is what a function will return by default if it does not explicitly return
# anything else.
# The difference between print and return is often confused.
# Print provides output to the console
# Return provides the value that can be stored and worled woth in the code later
def show_plus_ten(num):
    print(num + 10)

# this returns something
def add_ten(num):
    return(num + 10)

print('Calling show_plus_ten...')
return_value_1 = show_plus_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_1))

print('\nCalling add_ten...')
return_value_2 = add_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_2))

# Default Arguments

# We can add default arguments in a function to have default values for parameters
# that are unspecified in a function call.

def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2

# In the example above, radius is set to 5 if that parameter is omitted in a
# function call. If we call cylinder_volume(10), the function will use 10 as the
# height and 5 as the radius. However, if we call cylinder_volume(10, 7) the 7
# will simply overwrite the default value of 5.

# Also notice here we are passing values to our arguments by position. It is
# possible to pass values in two ways - by position and by name. Each of these
# function calls are evaluated the same way.

cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name


# Quiz: Defining Functions

# Lots of Practice

# An excellent resource for putting your skills to use is to join communities
# like the one at HackerRank.
# https://www.hackerrank.com/
# Here you can work through tons of problems at your
# own pace! Once you master writing functions, you will be ready to build full
# applications using Python.

# write your function here


def population_density(population, land_area):
    return population/land_area

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))


# Quiz: Population Density Function

# Write a function named population_density that takes two arguments, population
# and land_area, and returns a population density calculated from those values.
# I've included two test cases that you can use to verify that your function works
# correctly.


# Quiz: readable_timedelta
# Write a function named readable_timedelta. The function should take one
# argument, an integer days, and return a string that says how many weeks and
# days that is. For example, calling the function and printing the result like this:

print(readable_timedelta(10))

# should output the following:
# 1 week(s) and 3 day(s).

# write your function here

def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(10))



# Variable Scope

# Variable scope refers to which parts of a program a variable can be referenced,
# or used, from.

# It's important to consider scope when using variables in functions.

# If a variable
# is created inside a function, it can only be used within that function. Accessing
# it outside that function is not possible.

def word_count(dicument, search_term):
    words = oducment.splits
    answer = 0
    for word in words:
        if word == search_term:
            answer += 1
    return answer


def nearest_square(limit):
    answer = 0
    while (answer +1) ** 2 < limit:
        answer += 1
    return answer ** 2
print(answer)

# both functions above include an answer variable, but they are distinct variables
# that can only be referenced within their respective functions.

ans = 10
def show_ans():
    print(ans)

show_ans()
print(ans)

# Alternatively we migh have a variable defined outside of fucntions, like above.
# It can be accessed anywhere outside or within these functions.

# This will result in an error
def some_function():
    word = "hello"

print(word)

# In the example above and the example below, word is said to have scope that is
# only local to each function. This means you can use the same name for different
# variables that are used in different functions.

# This works fine
def some_function():
    word = "hello"

def another_function():
    word = "goodbye"

# Variables defined outside functions, as in the example below, can still be
# accessed within a function. Here, word is said to have a global scope.

# This works fine
word = "hello"

def some_function():
    print(word)

some_function()

# Notice that we can still access the value of the global variable word within
# this function. However, the value of a global variable can not be modified
# inside the function. If you want to modify that variable's value inside this
# function, it should be passed in as an argument. You'll see more on this in
# the next quiz.

# Scope is essential to understanding how information is passed throughout
# programs in Python and really any programming language.

# More on Variable Scope

# When you program, you'll often find that similar ideas come up again and again.
# You'll use variables for things like counting, iterating and accumulating values
# to return. In order to write readable code, you'll find yourself wanting to use
# similar names for similar ideas. As soon as you put multiple piece of code
# together (for instance, multiple functions or function calls in a single script)
# you might find that you want to use the same name for two separate concepts.

# Fortunately, you don't need to come up with new names endlessly. Reusing names
# for objects is OK as long as you keep them in separate scope.

# Good practice: It is best to define variables in the smallest scope they will
# be needed in. While functions can refer to variables defined in a larger scope,
# this is very rarely a good idea since you may not know what variables you have
# defined if your program has a lot of variables.

# QUIZ QUESTION

# Read through this code snippet:

egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()

# What is the result of running this code? If you aren't sure, try running it
# on your own computer!

# An error occurs

# This code causes an UnboundLocalError, because the variable egg_count in the
# first line has global scope. Note that it is not passed as an argument into
# the function, so the function assumes the egg_count being referred to is the
# global variable.

# In the last video, you saw that within a function, we can print a global
# variable's value successfully without an error. This worked because we were
# simply accessing the value of the variable. If we try to change or reassign
# this global variable, however, as we do in this code, we get an error. Python
# doesn't allow functions to modify variables that aren't in the function's scope.

# A better way to write this would be:

egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)


# Documentation

# One of the key advantages of functions is that they can help break a program
# down into smaller chunks. This makes code easier to write and also easier to
# read because the pieces of your code, the functions, are resuable.

def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

# using a function three times
cylinder_volume(10, 3)

cylinder_volume(11, 4)

cylinder_volume(12, 5)

# writing the cylinder volume formula three timestamp
pi = 3.14159
10 * pi * 3 ** 2
11 * pi * 4 ** 2
12 * pi * 5 ** 2

# If a program needs to calculate volumes of multiple cylinders, it can call the
# cylinder vlume fucntion multiple times, which is much cleaner than writing out
# the formula over and over again.

# Functions make code easier to read because they give human readable names to
# processes.

# Documentation is used to make your code easier to understand and use. Functions
# are especially readable because they often use documentation strings, or docstrings.

# Docstrings are a type of comment used to explain the purpose of a function, and
# how it should be used. Here's a function for population density with a docstring.

def population_density(population, land_area):
    """Calculate the population density of an area. """
    return population / land_area

# Docstrings are surrounded by triple quotes. The first line of the docstring is
# a brief explanation of the function's purpose. If you feel that this is sufficient
# documentation you can end the docstring at this point; single line docstrings are
# perfectly acceptable, as in the example above.

def population_density(population, land_area):
    """Calculate the population density of an area.

    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.

    OUTPUT:
    population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area

# If you think that a longer description would be appropriate for the function,
# you can add more information after the one-line summary. In the example above,
# you can see that we wrote an explanation of the function's arguments, stating
# the purpose and types of each one. It's also common to provide some description
# of the function's output.

# Every piece of the docstring is optional, however, docstrings are a part of good
# coding practice. You can read more about docstring conventions here.
# https://www.python.org/dev/peps/pep-0257/


# Quiz: Documentation
# Quiz: Write a Docstring

# Write a docstring for the readable_timedelta function you defined earlier!
# Remember the way you write your docstrings is pretty flexible! Look through
# Python's docstring conventions here and check out this Stack Overflow page
# for some inspiration!

def readable_timedelta_01(days):
    """Return a string of the number of weeks and days included in days."""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

def readable_timedelta_02(days):
    """Return a string of the number of weeks and days included in days.

    Args:
        days (int): number of days to convert
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)


# Lambda Expressions

# You can use lambda expressions to create anonymous functions. That is,
# functions that don’t have a name. They are helpful for creating quick
# functions that aren’t needed later in your code. This can be especially
# useful for higher order functions, or functions that take in other functions
# as arguments.

# With a lambda expression, this function:

def double(x)
    return x * 2

# can be reduced to:

double = lambda x: x + 2

# With a lambda expression, this function:

def multiply(x, y):
    return x * y

# can be reduced to:

multiply = lambda x, y: x * y

# Both of these functions are used in the same way. In either case, we can
# call multiply like this:

multiply(4, 7)

# This returns 28.

# Components of a Lambda Function

# The lambda keyword is used to indicate that this is a lambda expression.

# Following lambda are one or more arguments for the anonymous function separated
# by commas, followed by a colon :. Similar to functions, the way the arguments are
# named in a lambda expression is arbitrary.

# Last is an expression that is evaluated and returned in this function. This is
# a lot like an expression you might see as a return statement in a function.

# With this structure, lambda expressions aren’t ideal for complex functions,
# but can be very useful for short, simple functions.


# Quiz: Lambda Expressions

# Quiz: Lambda with Map
# map() is a higher-order built-in function that takes a function and iterable
# as inputs, and returns an iterator that applies the function to each element
# of the iterable. The code below uses map() to find the mean of each list in
# numbers to create the list averages. Give it a test run to see what happens.

# Rewrite this code to be more concise by replacing the mean function with a
# lambda expression defined within the call to map().

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)

# Quiz: Lambda with Filter
# filter() is a higher-order built-in function that takes a function and iterable
# as inputs and returns an iterator with the elements from the iterable for which
# the function returns True. The code below uses filter() to get the names in
# cities that are fewer than 10 characters long to create the list short_cities.
# Give it a test run to see what happens.

# Rewrite this code to be more concise by replacing the is_short function with
# a lambda expression defined within the call to filter().

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)

# [Optional] Iterators and Generators

# Iterators And Generators
# Iterables are objects that can return one of their elements at a time, such
# as a list. Many of the built-in functions we’ve used so far, like 'enumerate,'
# return an iterator.

# An iterator is an object that represents a stream of data. This is different
# from a list, which is also an iterable, but not an iterator because it is not
# a stream of data.

# Iterators are favored in different situations.

# Generators are a simple way to create iterators using functionsself.
# Generator is a function that creates an iterator.
# You can also
# define iterators using classes, which you can read more about here.
# https://docs.python.org/3/tutorial/classes.html#iterators

# The term generator is often used to refer to the generator function.\; but
# it's also used to refer to the iterator object produced by hte function

# We can differentiate between the two by referring to the function as a
# generator function, and what it produces as the iterator.

# Here is an example of a generator function called my_range, which produces an
# iterator that is a stream of numbers from 0 to (x - 1).

def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

# Notice that instead of using the return keyword, it uses yield. This allows
# the function to return values one at a time, and start where it left off each
# time it’s called. This yield keyword is what differentiates a generator from
# a typical function.

# Remember, since this returns an iterator, we can convert it to a list or
# iterate through it in a loop to view its contents. For example, this code:

for x in my_range(5):
    print(x)

# outputs:

# 0
# 1
# 2
# 3
# 4

print(my_range(4))

# Also, calling my range four returns an iterator that we can then iterate
# through. Using a for loop we can print values from this stream of data

for n in my_range(4):
    print(n)

# outputs:

# 0
# 1
# 2
# 3

# Why Generators?
# You may be wondering why we'd use generators over lists. Here’s an excerpt
# from a stack overflow page that addresses this:

# https://softwareengineering.stackexchange.com/questions/290231/when-should-i-use-a-generator-and-when-a-list-in-python/290235

# Generators are a lazy way to build iterables. They are useful when the fully
# realized list would not fit in memory, or when the cost to calculate each list
# element is high and you want to do it as late as possible. But they can only be
# iterated over once.


# [Optional] Quiz: Iterators and Generators

# Quiz: Implement my_enumerate
# Write your own generator function that works like the built-in function enumerate.

# Calling the function like this:

lessons = [
"Why Python Programming",
"Data Types and Operators",
"Control Flow",
"Functions",
"Scripting"
]

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

# should output:

# Lesson 1: Why Python Programming
# Lesson 2: Data Types and Operators
# Lesson 3: Control Flow
# Lesson 4: Functions
# Lesson 5: Scripting

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

# Quiz: Chunker
# If you have an iterable that is too large to fit in memory in full (e.g.,
# when dealing with large files), being able to take and use chunks of it at a
# time can be very valuable.

# Implement a generator function, chunker, that takes in an iterable and yields
# a chunk of a specified size at a time.

# Calling the function like this:

for chunk in chunker(range(25), 4):
    print(list(chunk))

# should output:

# [0, 1, 2, 3]
# [4, 5, 6, 7]
# [8, 9, 10, 11]
# [12, 13, 14, 15]
# [16, 17, 18, 19]
# [20, 21, 22, 23]
# [24]

def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))



# Generator Expressions

# Here's a cool concept that combines generators and list comprehensions! You
# can actually create a generator in the same way you'd normally write a list
# comprehension, except with parentheses instead of square brackets. For example:

sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares

# This can help you save time and create efficient code!

# Additional Resources

# If you want to learn more about writing functions, check out this talk from
# PyCon by Jack Diederich. Diederich covers best practices for writing functions
# in Python that also apply to all code in Python.
https://www.youtube.com/watch?v=rrBJVMyD-Gs&feature=youtu.be

# Here's a great blog post about yield and generators from Jeff Knupp.
https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
