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
# https://www.youtube.com/watch?v=rrBJVMyD-Gs&feature=youtu.be

# Here's a great blog post about yield and generators from Jeff Knupp.
# https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/


how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""


print(snake_string * how_many_snakes)




# Quiz Solution: Generate Messages
# Here's one way you can implement this program!

names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))

# Errors And Exceptions

# Syntax errors occur when Python can’t interpret our code, since we didn’t
# follow the correct syntax for Python. These are errors you’re likely to get
# when you make a typo, or you’re first starting to learn Python.

# Exceptions occur when unexpected things happen during execution of a program,
# even if the code is syntactically correct. There are different types of
# built-in exceptions in Python, and you can see which exception is thrown in
# the error message.

# QUESTION 1 OF 2
# The following statements are true

# (1) Any syntax error can be detected before running your program.
# (2) An exception occurs during run time.
# (3) There are many types of exceptions.

# QUESTION 2 OF 2
# Here are some of the common exceptions programmers run into in Python. Do
# some research online to match the appropriate description for each.

# BUILT-IN EXCEPTION    |    DESCRIPTION
#                       |
# ValueError            | An object of the correct type but inappropriate value
#                       | is passed as input to a built-in operation or function
#                       |
# AssertionError        | An assert statement fails
#                       |
# IndexError            | A sequence subscript is out of range
#                       |
# KeyError              | A key can't be found in a dictionary
#                       |
# TypeError             | An object of an unsupported type is passed as input
#                       | to an operation or function


# Handling Errors

# Try Statement
# We can use try statements to handle exceptions. There are four clauses you
# can use (one more in addition to those shown in the video).

# (1) try: This is the only mandatory clause in a try statement. The code in this
# block is the first thing that Python runs in a try statement.

# (2) except: If Python runs into an exception while running the try block, it
# will jump to the except block that handles that exception.

# (3) else: If Python runs into no exceptions while running the try block, it
# will run the code in this block after running the try block.

# (4) finally: Before Python leaves this try statement, it will run the code
# in this finally block under any conditions, even if it's ending the program. e.g.,
# if Python ran into an error while running code in the except or else block, this
# finally block will still be executed before stopping the program.

# Why do we need the finally clause in Python?

# why python needs finally clause

# code below will continue to run even when press ctrl-c

# why python needs finally clause

# code below will continue to run even when press ctrl-c

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except :
        print('That\'s not a valid number!')
    finally:
        print('\nAttempted Input\n')

# code below will interrupt when press ctrl-c
# specifies which error to handle
# with tuple

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except (ValueError, KeyboardInterrupt):
        print('That\'s not a valid number!')
    finally:
        print('\nAttempted Input\n')

# code below will interrupt when press ctrl-c
# specifies which error to handle
# with multiple except blocks

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except ValueError:
        print('That\'s not a valid number!')
    except  KeyboardInterrupt:
        print('\nNo input taken!')
        break
    finally:
        print('\nAttempted Input\n')






# Specifying Exceptions
# We can actually specify which error we want to handle in an except block like this:

try:
    # some code
except ValueError:
    # some code

# Now, it catches the ValueError exception, but not other exceptions. If we
# want this handler to address more than one type of exception, we can include a
# parenthesized tuple after the except with the exceptions.

try:
    # some code
except (ValueError, KeyboardInterrupt):
    # some code

# or, if we want to execute different blocks of code depending on the exception,
# you can have multiple except blocks.

try:
    # some code
except ValueError:
    # some code
except KeyboardInterrupt:
    # some code



# Handling Input Errors

# The party_planner function below takes as input a number of party people and
# cookies and figures out how many cookies each person gets at the party, assuming
# equitable distribution of cookies. Then, it returns that number along with how
# many cookies will be left over.

# Right now, calling the function with an input of 0 people will cause an error,
# because it creates a ZeroDivisionError exception. Edit the party_planner function
# to handle this invalid input. If it runs into this exception, it should print a
# warning message to the user and request they input a different number of people.

# After you've edited the function, try running the file again and make sure it
# does what you intended. Try it with several different input values, including 0
# and other values for the number of people.

def party_planner(cookies, people):
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")

    return(num_each, leftovers)

# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")



# Accessing Error Messages
# When you handle an exception, you can still access its error message like this:

try:
    # some code
except ZeroDivisionError as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))

# This would print something like this:

# ZeroDivisionError occurred: integer division or modulo by zero

# So you can still access error messages, even if you handle them to keep your
# program from crashing!

# If you don't have a specific error you're handling, you can still access the
# message like this:

try:
    # some code
except Exception as e:
   # some code
   print("Exception occurred: {}".format(e))

# Exception is just the base class for all built-in exceptions. You can learn
# more about Python's exceptions here.
# https://docs.python.org/3/library/exceptions.html#bltin-exceptions



# Reading and Writing Files

# Using Files

# Create a new file in Atom, copy the following text into it, and save it
# as some_file.txt!

# Hello!!

# You've read the contents of this file!
# Here's how we read and write files in Python.

# Reading a File
f = open('my_path/my_file.txt', 'r')
file_data = f.read()
f.close()

# First open the file using the built-in function, open. This requires a string
# that shows the path to the file. The open function returns a file object, which
# is a Python object through which Python interacts with the file itself. Here,
#we assign this object to the variable f.

# There are optional parameters you can specify in the open function. One is
# the mode in which we open the file. Here, we use r or read only. This is
# actually the default value for the mode argument.

# Use the read method to access the contents from the file object. This read
# method takes the text contained in a file and puts it into a string. Here,
# we assign the string returned from this method into the variable file_data.

# When finished with the file, use the close method to free up any system
# resources taken up by the file.

# Writing to a File

f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()

# Open the file in writing ('w') mode. If the file does not exist, Python will
# create it for you. If you open an existing file in writing mode, any content
# that it had contained previously will be deleted. If you're interested in
# adding to an existing file, without deleting its content, you should use the
# append ('a') mode instead of write.

# Use the write method to add text to the file.
# Close the file when finished.
# Too Many Open Files

# Run the following script in Python to see what happens when you open too many
# files without closing them!

files = []
for i in range(10000):
    files.append(open('some_file.txt', 'r'))
    print(i)

# With

# Python provides a special syntax that auto-closes a file for you once you're
# finished using it.

with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()

# This with keyword allows you to open a file, do operations on it, and
# automatically close it after the indented code is executed, in this case,
# reading from the file. Now, we don’t have to call f.close()! You can only
# access the file object, f, within this indented block.  This is another kind of
# scope. Once you leave this indented block the file is closed and cannot interact
# with it. Trying to call f.read() outside this block will return an error.
# However just because you close the file does not mean you lose the data.
# Calling the file data outside the block works fine.


# Quiz: Reading and Writing Files

# Calling the read Method with an Integer

# In the code you saw earlier, the call to f.read() had no arguments passed to
# it. This defaults to reading all the remainder of the file from its current
# position - the whole file. If you pass the read method an integer argument,
# it will read up to that number of characters, output all of them, and keep
# the 'window' at that position ready to read on.

# Let's see this in an example that uses the following file, camelot.txt:

# We're the knights of the round table
# We dance whenever we're able

# Here's a script that reads in the file a little at a time by passing an integer
# argument to .read().

with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())

# Outputs:

# We
# 're the
# knights of the round table
# We dance whenever we're able

# You can try out this example by creating your own camelot.txt and example.py
# files with the text above.

# Each time we called read on the file with an integer argument, it read up to
# that number of characters, outputted them, and kept the 'window' at that
# position for the next call to read. This makes moving around in the open
# file a little tricky, as there aren't many landmarks to navigate by.

# Reading Line by Line

# \ns in blocks of text are newline characters. The newline character marks the
# end of a line, and tells a program (such as a text editor) to go down to the
# next line. However, looking at the stream of characters in the file, \n is just
# another character.

# Fortunately, Python knows that these are special characters and you can ask
# it to read one line at a time. Let's try it!

# Conveniently, Python will loop over the lines of a file using the syntax for
# line in file. I can use this to create a list of lines in the file. Because
# each line still has its newline character attached, I remove this using .strip().

camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)

# Outputs:

# ["We're the knights of the round table", "We dance whenever we're able"]

# Quiz: Flying Circus Cast List
# You're going to create a list of the actors who appeared in the television
# programme Monty Python's Flying Circus.

# Write a function called create_cast_list that takes a filename as input and
# returns a list of actors' names. It will be run on the file flying_circus_cast.txt
# (this information was collected from imdb.com). Each line of that file consists
# of an actor's name, a comma, and then some (messy) information about roles they
# played in the programme. You'll need to extract only the name and add it to a
# list. You might use the .split() method to process each line.

def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)


# Importing Local Scripts

# We can actually import Python code from other scripts, which is helpful if
# you are working on a bigger project where you want to organize your code
# into multiple files and reuse code in those files. If the Python script you
# want to import is in the same directory as your current script, you just type
# import followed by the name of the file, without the .py extension.

import useful_functions

# It's the standard convention for import statements to be written at the top
# of a Python script, each one on a separate line. This import statement creates
# a module object called useful_functions. Modules are just Python files that
# contain definitions and statements. To access objects from an imported module,
# you need to use dot notation.

import useful_functions
useful_functions.add_five([1, 2, 3, 4])

# We can add an alias to an imported module to reference it with a different name.

import useful_functions as uf
uf.add_five([1, 2, 3, 4])

# Using a main block
# To avoid running executable statements in a script when it's imported as a
# module in another script, include these lines in an if __name__ == "__main__" block.
# Or alternatively, include them in a function called main() and call this in
# the if main block.

# Generally it is good practice to write executable statements inside an:
# if __name__ == "__main__" block;
# or alterantovely include them in a function called main() and call this in
# the if main block.

# Whenever we run a script like this, Python actually sets a special built-in
# variable called __name__ for any module. When we run a script, Python recognizes
# this module as the main program, and sets the __name__ variable for this module
# to the string "__main__". For any modules that are imported in this script,
# this built-in __name__ variable is just set to the name of that module.
# Therefore, the condition if __name__ == "__main__"is just checking whether
# this module is the main program.

# Try It Out!

# Here's the code I used in the video above. Create these scripts in the same
# directory and run them in your terminal! Experiment with the if main block and
# accessing objects from the imported module!

# demo.py

import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)
print(uf.__name__)
# useful_functions.py

def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

if __name__ == '__main__':
    main()

# The Standard Library
# You can discover new modules at the Python Module of the Week blog.
# https://pymotw.com/3/

# Quiz: The Standard Linrary

# Quiz: Compute an Exponent

# It's your turn to import and use the math module. Use the math module to
# calculate e to the power of 3. print the answer.

# Refer to the math module's documentation to find the function you need!
# https://docs.python.org/3.6/library/math.html?highlight=math%20module#module-math

# print e to the power of 3 using the math module

import math

e_3 = math.exp(3)

print(e_3)

# Quiz: Password Generator
# Write a function called generate_password that selects three random words from
# the list of words word_list and concatenates them into a single string. Your
# function should not accept any arguments and should reference the global variable
# word_list to build the password.

# version 1
# Use an import statement at the top
import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces

def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

# test your function
print(generate_password())

# version 2
# Use an import statement at the top
import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces

def generate_password():
    return ''.join(random.sample(word_list,3))

# test your function
print(generate_password())

# Explore the Standard Library
# Every module in the standard library is lowercased.
# You can browse the library documentation here.
# https://docs.python.org/3/library/

# Our favourite modules
# The Python Standard Library has a lot of modules! To help you get familiar
# with what's available, here are a selection of our favourite Python Standard
# Library modules and why we use them!

# (1) csv: very convenient for reading and writing csv files
# (2) collections: useful extensions of the usual data types including OrderedDict,
# defaultdict and namedtuple
# (3) random: generates pseudo-random numbers, shuffles sequences randomly and
# (4) chooses random items
# (5) string: more functions on strings. This module also contains useful
# collections of letters like string.digits (a string containing all characters
# which are valid digits).
# (6) re: pattern-matching in strings via regular expressions
# (7) math: some standard mathematical functions
# (8) os: interacting with operating systems
# (9) os.path: submodule of os for manipulating path names
# (10) sys: work directly with the Python interpreter
# (11)json: good for reading and writing json files (good for web work)


# Techniques for Importing Modules
# There are other variants of import statements that are useful in different
# situations.

# importing individual objects from a module means you only take
# what you need and you don;t need to use notation to access them
# To import an individual function or class from a module:
from module_name import object_name

from collections import defaultdict
collections.defaultdict() # returns error
defaultdict() # no error

# To import multiple individual objects from a module separte them with commas:
from module_name import first_object, second_object

# when possible use standard abbreviations
# To rename a module:
import module_name as new_name

from csv import reader as csvreader

# To import an object from a module and rename it:
from module_name import object_name as new_name

# if you really want to use all the objects from a module use the standard
# import instead and access each of the objects with the notation
# To import every object individually from a module (DO NOT DO THIS):
from module_name import *

# If you really want to use all of the objects from a module, use the standard
# import module_name statement instead and access each of the objects with the
# dot notation.
import module_name

# Modules, Packages, and Names

# In order to manage the code better, modules in the Python Standard Library
# are split down into sub-modules that are contained within a package. A package
# is simply a module that contains sub-modules. A sub-module is specified with
# the usual dot notation.

# Modules that are submodules are specified by the package name and then the
# submodule name separated by a dot. You can import the submodule like this.

import package_name.submodule_name

import os.path

os.path.isdir('my_path')

# namimg can sometimes be a point of confusion when working with modules
# for example, a module might be named after one of the important classes or
# functions within it, and will then need to think carefully about the import
# statements.

from datetime imprt datetime # datetime will now refer to class not module

# Quiz: Techniques for Importing Modules

# Importing and accessing from modules
# In this quiz, you'll be using different methods to import and use the
# random.randint() function from the random module. Your task is to match the
# import statement with the way you would then call the function itself.

# QUIZ QUESTION
# Match the import statement with the way that random.randint() is called.

#These are the correct matches.

# IMPORT STATEMENT                    |   CALLING THE FUNCTION
# import random                       |   random.randint(0,10)
# from random import randint          |   randint(0,10)
# import random as rd                 |   rd.randint(0,10)
# from random import randint as rint  |   rint(0,10)
# from random import *                |   Don't use this import statement!


# Third-Party Libraries
# There are tens of thousands of third-party libraries written by independent
# developers! You can install them using pip, a package manager that is included
# with Python 3. pip is the standard package manager for Python, but it isn't
# the only one. One popular alternative is Anaconda which is designed specifically
# for data science.

# To install a package using pip, just enter "pip install" followed by the
# name of the package in your command line like this: pip install package_name.
# This downloads and installs the package so that it's available to import in
# your programs. Once installed, you can import third-party packages using the
# same syntax used to import from the standard library.

# Using a requirements.txt File

# Larger Python programs might depend on dozens of third party packages. To make
# it easier to share these programs, programmers often list a project's dependencies
#in a file called requirements.txt. This is an example of a requirements.txt file.

beautifulsoup4==4.5.1
bs4==0.0.1
pytz==2016.7
requests==2.11.1

# Each line of the file includes the name of a package and its version number.
# The version number is optional, but it usually should be included. Libraries
# can change subtly, or dramatically, between versions, so it's important to use
# the same library versions that the program's author used when they wrote the program.

# You can use pip to install all of a project's dependencies at once by typing
# pip install -r requirements.txt in your command line.

# Useful Third-Party Packages
# Being able to install and import third party libraries is useful, but to be an
# effective programmer you also need to know what libraries are available for you
# to use. People typically learn about useful new libraries from online
# recommendations or from colleagues. If you're a new Python programmer you may
# not have many colleagues, so to get you started here's a list of packages that
# are popular with engineers at Udacity.

# (1) IPython - A better interactive Python interpreter
# # https://ipython.org/

# (2) requests - Provides easy to use methods to make web requests. Useful for
# accessing web APIs.
# http://docs.python-requests.org/en/master/

# (3) Flask - a lightweight framework for making web applications and APIs.
# http://flask.pocoo.org/

# (4) Django - A more featureful framework for making web applications. Django
# is particularly good for designing complex, content heavy, web applications.
# https://www.djangoproject.com/

# (5) Beautiful Soup - Used to parse HTML and extract information from it. Great
# for web scraping.
# https://www.crummy.com/software/BeautifulSoup/

# (6) pytest - extends Python's builtin assertions and unittest module.
# https://docs.pytest.org/en/latest/

# (7) PyYAML - For reading and writing YAML files.
# https://pyyaml.org/wiki/PyYAML

# (8) NumPy - The fundamental package for scientific computing with Python. It
# contains among other things a powerful N-dimensional array object and useful
# linear algebra capabilities.
# http://www.numpy.org/

# (9) pandas - A library containing high-performance, data structures and data
# analysis tools. In particular, pandas provides dataframes!
#

# (10) matplotlib - a 2D plotting library which produces publication quality
# figures in a variety of hardcopy formats and interactive environments.
# https://matplotlib.org/

# (11) ggplot - Another 2D plotting library, based on R's ggplot2 library.
# http://ggplot.yhathq.com/

# (12) Pillow - The Python Imaging Library adds image processing capabilities
# to your Python interpreter.
# https://python-pillow.org/

# (13) pyglet - A cross-platform application framework intended for game development.
# https://bitbucket.org/pyglet/pyglet/wiki/Home

# (14) Pygame - A set of Python modules designed for writing games.
# https://www.pygame.org/news

# (15) pytz - World Timezone Definitions for Python
# http://pytz.sourceforge.net/

# Experimenting with an Interpreter

# Start your Python interactive interpreter by entering the command python in
# your terminal. You can type here to interact with Python directly. This is an
# awesome place to experiment and try bits of Python code at a time. Just enter
# Python code, and the output will appear on the next line.

>>> type(5.23)
<class 'float'>

# In the interpreter, the value of the last line in a prompt will be outputted
# automatically. If you had multiple lines where you’d want to output values,
# you’d still have to use print.

# If you start to define a function you will see a change in the prompt, to
# signify that this is a continuation line. You'll have to include your own
# indentation as you define the function.

>>> def cylinder_volume(height, radius):
...         pi = 3.14159
...         return height * pi * radius ** 2

# A drawback of the interpreter is that it’s tricky to edit code. If you made
# a mistake when typing this function, or forgot to indent the body of the
# function, you can't use the mouse to click your cursor where you want it.
# You have to navigate with arrow keys to move the cursor forwards and backwards
# through the line itself for editing. It would be helpful for you to learn
# useful shortcuts for actions like moving to the beginning or end of the line.

# Notice I can reference any objects I defined earlier in the interpreter!

>>> cylinder_volume(10, 3)
282.7431

# One useful trick is using the up and down arrow to cycle through your recent
# commands at the interactive prompt. This can be useful to re-run or adapt code
# you've already tried.

# To quit the Python interactive interpreter, use the command exit() or hit
# ctrl-D on mac or linux, and ctrl-Z then Enter for windows.

# IPython

# There is actually an awesome alternative to the default Python interactive
# interpreter, IPython, which comes with many additional features.

    # (1) tab completion
    # (2) ? for details about an object
    # (3) ! to execute system shell commands
    # (4) syntax highlighting!
    # (5) and a lot more you can find here!:
        # https://ipython.org/ipython-doc/3/interactive/tutorial.html



# Online Resources
# Getting the information you need to know

# It takes an enormous amount of knowledge to be a skilled programmer. There's
# libraries to know, syntax to remember, and myriad other details. To add to
# the difficulty, the technology landscape is constantly shifting as new techniques
# and tools are invented.

# To a novice programmer, learning all of these details and keeping abreast of
# new developments seems like an impossible task. And it is! Expert programmers
# who have been working for years don't actually carry an encyclopedia's worth
# of knowledge in their heads. Instead they have mastered the task of finding
# information quickly.

# How to Search

# Here are some techniques for effective web searching:

# (1) Try using "Python" or the name of the library you're using as the first word
# of your query. This tells the search engine to prioritize results that are
# explicitly related to the tools you're using.

# (2) Writing a good search query can take multiple attempts. If you don't find helpful
# results on your first attempt, try again.

# (3) Try using keywords found on the pages you found in your initial search to direct
# the search engine to better resources in the subsequent search.

# (4) Copy and paste error messages to use as search terms. This will lead you to
# explanations of the error and potential causes. An error message might include
# references to specific line numbers of code that you wrote. Only include the
# part of the error message that comes before this in your search.

# (5) If you can't find an answer to your question, ask it yourself! Communities
# like StackOverflow have etiquette rules you must learn if you want to participate,
# but don't let this stop you from using these resources.

# QUIZ QUESTION

# While coding I encountered this error message.

# UnboundLocalError: local variable 'egg_count' referenced before assignment

# Which of these search terms is mostly likely to yield helpful results?

# Python UnboundLocalError: local variable

# Hierarchy of Online Resources

# While there are many online resources about programming, not all of the them
# are created equal. This list of resources is in approximate order of reliability.

# (1) The Python Tutorial - This section of the official documentation surveys
# Python's syntax and standard library. It uses examples, and is written using
# less technical language than the main documentation. Make sure you're reading
# the Python 3 version of the docs!
# https://docs.python.org/3/tutorial/

# (2) The Python Language and Library References - The Language Reference and Library
# Reference are more technical than the tutorial, but they are the definitive
# sources of truth. As you become increasingly acquainted with Python you should
# use these resources more and more.
# https://docs.python.org/3/index.html

# (3) Third-Party Library Documentation - Third-party libraries publish their
# documentation on their own websites, and often times at https://readthedocs.org/.
# You can judge the quality of a third-party library by the quality of its
# documentation. If the developers haven't found time to write good docs,
# they probably haven't found the time to polish their library either.
# https://readthedocs.org/

# (4) The websites and blogs of prominent experts - The previous resources are
# primary sources, meaning that they are documentation from the same people who
# wrote the code being documented. Primary sources are the most reliable. Secondary
# sources are also extremely valuable. The difficulty with secondary sources is
# determining the credibility of the source. The websites of authors like Doug
# Hellmann and developers like Eli Bendersky are excellent. The blog of an
# unknown author might be excellent, or it might be rubbish.
# https://doughellmann.com/blog/
# https://eli.thegreenplace.net/

# (5) StackOverflow - This question and answer site has a good amount of traffic,
# so it's likely that someone has asked (and someone has answered) a related question
# before! However, answers are provided by volunteers and vary in quality. Always
# understand solutions before putting them into your program. One line answers
# without any explanation are dubious. This is a good place to find out more
# about your question or discover alternative search terms.
# https://stackoverflow.com/

# (6) Bug Trackers - Sometimes you'll encounter a problem so rare, or so new,
# that no one has addressed it on StackOverflow. You might find a reference to
# your error in a bug report on GitHub for instance. These bug reports can be
# helpful, but you'll probably have to do some original engineering work to solve the problem.

# (7) Random Web Forums - Sometimes your search yields references to forums that
# haven't been active since 2004, or some similarly ancient time. If these are
# the only resources that address your problem, you should rethink how you're
# approaching your solution.


# NumPy

# Python offers many libraries to work with, one of which is Numpy. Here you
# will learn how Numpy offers support for large amounts of data, which will
# come in handy later!

# Introduction to NumPy
# NumPy stands for Numerical Python and it's a fundamental package for scientific
# computing in Python. NumPy provides Python with an extensive math library capable
# of performing numerical computations effectively and efficiently. These lessons
# are intended as a basic overview of NumPy and introduces some of its most
# important features.

# In the following lessons you will learn:

# (1) How to import NumPy
# (2) How to create multidimensional NumPy ndarrays using various methods
# (3) How to access and change elements in ndarrays
# (4) How to load and save ndarrays
# (5) How to use slicing to select or change subsets of an ndarray
# (6) Understand the difference between a view and a copy an of ndarray
# (7) How to use Boolean indexing and set operations to select or change subsets
# of an ndarray
# (8) How to sort ndarrays
# (9) How to perform element-wise operations on ndarrays
# (10) Understand how NumPy uses broadcasting to perform operations on ndarrays
# of different sizes.

# Downloading NumPy

# NumPy is included with Anaconda. If you don't already have Anaconda installed
# on your computer, please refer to the Anaconda section to get clear instructions
# on how to install Anaconda on your PC or Mac.

# NumPy Versions

# As with many Python packages, NumPy is updated from time to time. The following
# lessons were created using NumPy version 1.13.0. You can check which version of
# NumPy you have by typing !conda list numpy in your Jupyter Notebook or by
# typing conda list numpy in the Anaconda prompt. If you have another version of
# NumPy installed in your computer, you can update your version by typing conda
# install numpy=1.13 in the Anaconda prompt. As newer versions of NumPy are released,
# some functions may become obsolete or replaced, so make sure you have the correct
# NumPy version before running the code. This will guarantee your code will run smoothly.

# NumPy Documentation

# NumPy is a remarkable math library and it has many functions and features. In
# these introductory lessons we will only scratch the surface of what NumPy can
# do. If you want to learn more about NumPy, make sure you check out the NumPy
# Documentation:

# NumPy Manual
# https://docs.scipy.org/doc/numpy-1.13.0/contents.html

# NumPy User Guide
# https://docs.scipy.org/doc/numpy-1.13.0/user/index.html

# NumPy Reference
# https://docs.scipy.org/doc/numpy-1.13.0/reference/index.html#reference

# Scipy Lectures
# http://scipy-lectures.org/intro/numpy/index.html


# Why Use NumPy

# NumPy stands for Numerical Python and it is a library designed for effcient
# scientific computation.  It is built on top of the programmming language C,

# You may be wondering why people use NumPy - after all, Python can handle
# lists, as you learned in the Intro to Python lessons.

# Even though Python lists are great on their own, NumPy has a number of key
# features that give it great advantages over Python lists. One such feature is
# speed. When performing operations on large arrays NumPy can often perform
# several orders of magnitude faster than Python lists. This speed comes from
# the nature of NumPy arrays being memory-efficient and from optimized algorithms
# used by NumPy for doing arithmetic, statistical, and linear algebra operations.

# Another great feature of NumPy is that it has multidimensional array data
# structures that can represent vectors and matrices. You will learn all about
# vectors and matrices in the Linear Algebra section of this course later on,
# and as you will soon see, a lot of machine learning algorithms rely on
# matrix operations. For example, when training a Neural Network, you often
# have to carry out many matrix multiplications. NumPy is optimized for matrix
# operations and it allows us to do Linear Algebra operations effectively and
# efficiently, making it very suitable for solving machine learning problems.

# At the core of Numpy is its N-dimensional array object ( a multi-dimensinal array
# that holds a group of elements that all have the same data type.)  It is like
# a grid that can take on may shapes and enforces every element in that grid to have
# the same type.  Making arrays ony able to hold one data type at a time helps NumPy
# make very quick computations with vector operations to optimize and simplify operations
# on data.

# Another great advantage of NumPy over Python lists is that NumPy has a large
# number of optimized built-in mathematical functions. These functions allow
# you to do a variety of complex mathematical computations very fast and with
# very little code (avoiding the use of complicated loops) making your programs
# more readable and easier to understand.

# These are just some of the key features that have made NumPy an essential
# package for scientific computing in Python. In fact, NumPy has become so
# popular that a lot of Python packages, such as Pandas, are built on top of NumPy.

import time
import numpy as np

x = np.random.random(100000000)

start = time.time()
sum(x) / len(x)
print(time.time() - start)

Start = time.time
np.mean(x)
print(time.time() - start)


# Creating and Saving NumPy ndarrays

# At the core of NumPy is the ndarray, where nd stands for n-dimensional. An
# ndarray is a multidimensional array of elements all of the same type. In other
# words, an ndarray is a grid that can take on many shapes and can hold either
# numbers or strings. In many Machine Learning problems you will often find
# yourself using ndarrays in many different ways. For instance, you might use
# an ndarray to hold the pixel values of an image that will be fed into a Neural
# Network for image classification.

# But before we can dive in and start using NumPy to create ndarrays we need to
# import it into Python. We can import packages into Python using the import
# command and it has become a convention to import NumPy as np. Therefore, you
# can import NumPy by typing the following command in your Jupyter notebook:

import numpy as np

# There are several ways to create ndarrays in NumPy. In the following lessons
# we will see two ways to create ndarrays:

# Using regular Python lists

# Using built-in NumPy functions

# In this section, we will create ndarrays by providing Python lists to the
#NumPy np.array() function. This can create some confusion for beginners, but
# is important to remember that np.array() is NOT a class, it is just a function
# that returns an ndarray. We should note that for the purposes of clarity, the
# examples throughout these lessons will use small and simple ndarrays. Let's
# start by creating 1-Dimensional (1D) ndarrays.

# We import NumPy into Python
import numpy as np

# We create a 1D ndarray that contains only integers
x = np.array([1, 2, 3, 4, 5])

# Let's print the ndarray we just created using the print() command
print('x = ', x)
x = [1 2 3 4 5]

# Let's pause for a second to introduce some useful terminology.
# We refer to 1D arrays as rank 1 arrays. In general N-Dimensional arrays have rank N.
#Therefore, we refer to a 2D array as a rank 2 array. Another important property
# of arrays is their shape. The shape of an array is the size along each of its
# dimensions. For example, the shape of a rank 2 array will correspond to the
# number of rows and columns of the array. As you will see, NumPy ndarrays have
# attributes that allows us to get information about them in a very intuitive way.
# For example, the shape of an ndarray can be obtained using the .shape attribute.
# The shape attribute returns a tuple of N positive integers that specify the sizes
# of each dimension. In the example below we will create a rank 1 array and learn
# how to obtain its shape, its type, and the data-type (dtype) of its elements.

# We create a 1D ndarray that contains only integers
x = np.array([1, 2, 3, 4, 5])

# We print x
print()
print('x = ', x)
print()

# We print information about x
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
x = [1 2 3 4 5]

# x has dimensions: (5,)
# x is an object of type: class 'numpy.ndarray'
# The elements in x are of type: int64

# We can see that the shape attribute returns the tuple (5,) telling us that x
# is of rank 1 (i.e. x only has 1 dimension ) and it has 5 elements. The type()
#function tells us that x is indeed a NumPy ndarray. Finally, the .dtype attribute
#tells us that the elements of x are stored in memory as signed 64-bit integers.
# Another great advantage of NumPy is that it can handle more data-types than
# Python lists. You can check out all the different data types NumPy supports in
# the link below:

# NumPy Data Types
# https://docs.scipy.org/doc/numpy-1.13.0/user/basics.types.html

# As mentioned earlier, ndarrays can also hold strings. Let's see how we can
# create a rank 1 ndarray of strings in the same manner as before, by providing
# the np.array() function a Python list of strings.

# We create a rank 1 ndarray that only contains strings
x = np.array(['Hello', 'World'])

# We print x
print()
print('x = ', x)
print()

# We print information about x
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
x = ['Hello' 'World']

# x has dimensions: (2,)
# x is an object of type: class 'numpy.ndarray'
# The elements in x are of type: U5

# As we can see the shape attribute tells us that x now has only 2 elements,
# and even though x now holds strings, the type() function tells us that x is
# still an ndarray as before. In this case however, the .dtype attribute tells
# us that the elements in x are stored in memory as Unicode strings of 5
# characters.

# It is important to remember that one big difference between Python lists and
# ndarrays, is that unlike Python lists, all the elements of an ndarray must be
# of the same type. So, while we can create Python lists with both integers and
# strings, we can't mix types in ndarrays. If you provide the np.array() function
# with a Python list that has both integers and strings, NumPy will interpret all
# elements as strings. We can see this in the next example:

# We create a rank 1 ndarray from a Python list that contains integers and strings
x = np.array([1, 2, 'World'])

# We print the ndarray
print()
print('x = ', x)
print()

# We print information about x
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
x = ['1' '2' 'World']

# x has dimensions: (3,)
# x is an object of type: class 'numpy.ndarray'
# The elements in x are of type: U21

# We can see that even though the Python list had mixed data types, the elements
# in x are all of the same type, namely, Unicode strings of 21 characters. We
# won't be using ndarrays with strings for the remaining of this introduction to
# NumPy, but it's important to remember that ndarrays can hold strings as well.

# Let us now look at how we can create a rank 2 ndarray from a nested Python list.

# We create a rank 2 ndarray that only contains integers
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])

# We print Y
print()
print('Y = \n', Y)
print()

# We print information about Y
print('Y has dimensions:', Y.shape)
print('Y has a total of', Y.size, 'elements')
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype)
Y =
[[ 1 2 3]
 [ 4 5 6]
 [ 7 8 9]
 [10 11 12]]

# Y has dimensions: (4, 3)
# Y has a total of 12 elements
# Y is an object of type: class 'numpy.ndarray'
# The elements in Y are of type: int64

# We can see that now the shape attribute returns the tuple (4,3) telling us
# that Y is of rank 2 and it has 4 rows and 3 columns. The .size attribute
# tells us that Y has a total of 12 elements.

#  Notice that when NumPy creates an ndarray it automatically assigns its dtype
# based on the type of the elements you used to create the ndarray. Up to now,
# we have only created ndarrays with integers and strings. We saw that when we
# create an ndarray with only integers, NumPy will automatically assign the
# dtype int64 to its elements. Let's see what happens when we create ndarrays
# with floats and integers.

# We create a rank 1 ndarray that contains integers
x = np.array([1,2,3])

# We create a rank 1 ndarray that contains floats
y = np.array([1.0,2.0,3.0])

# We create a rank 1 ndarray that contains integers and floats
z = np.array([1, 2.5, 4])

# We print the dtype of each ndarray
print('The elements in x are of type:', x.dtype)
print('The elements in y are of type:', y.dtype)
print('The elements in z are of type:', z.dtype)

# The elements in x are of type: int64
# The elements in y are of type: float64
# The elements in z are of type: float64

# We can see that when we create an ndarray with only floats, NumPy stores the
# elements in memory as 64-bit floating point numbers (float64). However, notice
# that when we create an ndarray with both floats and integers, as we did with
# the z ndarray above, NumPy assigns its elements a float64 dtype as well. This
# is called upcasting. Since all the elements of an ndarray must be of the same
# type, in this case NumPy upcasts the integers in z to floats in order to avoid
# losing precision in numerical computations.

# Even though NumPy automatically selects the dtype of the ndarray, NumPy also
# allows you to specify the particular dtype you want to assign to the elements
# of the ndarray. You can specify the dtype when you create the ndarray using
# the keyword dtype in the np.array() function. Let's see an example:

# We create a rank 1 ndarray of floats but set the dtype to int64
x = np.array([1.5, 2.2, 3.7, 4.0, 5.9], dtype = np.int64)

# We print x
print()
print('x = ', x)
print()

# We print the dtype x
print('The elements in x are of type:', x.dtype)
x = [1 2 3 4 5]

# The elements in x are of type: int64

# We can see that even though we created the ndarray with floats, by specifying
# the dtype to be int64, NumPy converted the floating point numbers into integers
# by removing their decimals. Specifying the data type of the ndarray can be
# useful in cases when you don't want NumPy to accidentally choose the wrong
# data type, or when you only need certain amount of precision in your calculations
# and you want to save memory.

# Once you create an ndarray, you may want to save it to a file to be read later
# or to be used by another program. NumPy provides a way to save the arrays into
# files for later use - let's see how this is done.

# We create a rank 1 ndarray
x = np.array([1, 2, 3, 4, 5])

# We save x into the current directory as
np.save('my_array', x)
# The above saves the x ndarray into a file named my_array.npy. You can load
# the saved ndarray into a variable by using the load() function.

# We load the saved array from our current directory into variable y
y = np.load('my_array.npy')

# We print y
print()
print('y = ', y)
print()

# We print information about the ndarray we loaded
print('y is an object of type:', type(y))
print('The elements in y are of type:', y.dtype)
y = [1 2 3 4 5]

# y is an object of type: class 'numpy.ndarray'
# The elements in y are of type: int64

# When loading an array from a file, make sure you include the name of the
# file together with the extension .npy, otherwise you will get an error.


# Using Built-in Functions to Create ndarrays

# One great time-saving feature of NumPy is its ability to create ndarrays using
# built-in functions. These functions allow us to create certain kinds of ndarrays
# with just one line of code. Below we will see a few of the most useful built-in
# functions for creating ndarrays that you will come across when doing AI programming.

# Let's start by creating an ndarray with a specified shape that is full of zeros.
# We can do this by using the np.zeros() function. The function np.zeros(shape)
# creates an ndarray full of zeros with the given shape. So, for example, if you
# wanted to create a rank 2 array with 3 rows and 4 columns, you will pass the
# shape to the function in the form of (rows, columns), as in the example below:

# We create a 3 x 4 ndarray full of zeros.
X = np.zeros((3,4))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)
X =
[[ 0. 0. 0. 0.]
 [ 0. 0. 0. 0.]
 [ 0. 0. 0. 0.]]

# X has dimensions: (3, 4)
# X is an object of type: class 'numpy.ndarray'
# The elements in X are of type: float64

# As we can see, the np.zeros() function creates by default an array with dtype
# float64. If desired, the data type can be changed by using the keyword dtype.

# Similarly, we can create an ndarray with a specified shape that is full of
# ones. We can do this by using the np.ones() function. Just like the np.zeros()
# function, the np.ones() function takes as an argument the shape of the ndarray
# you want to make. Let's see an example:

# We create a 3 x 2 ndarray full of ones.
X = np.ones((3,2))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)
X =
[[ 1. 1.]
 [ 1. 1.]
 [ 1. 1.]]

# X has dimensions: (3, 2)
# X is an object of type: class 'numpy.ndarray'
# The elements in X are of type: float64

# As we can see, thenp.ones() function also creates by default an array with
# dtype float64. If desired, the data type can be changed by using the keyword dtype.

# We can also create an ndarray with a specified shape that is full of any
# number we want. We can do this by using the np.full() function. The np.full(shape,
# constant value) function takes two arguments. The first argument is the shape
# of the ndarray you want to make and the second is the constant value you want
# to populate the array with. Let's see an example:

# We create a 2 x 3 ndarray full of fives.
X = np.full((2,3), 5)

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)
X =
[[5 5 5]
 [5 5 5]]

# X has dimensions: (2, 3)
# X is an object of type: class 'numpy.ndarray'
# The elements in X are of type: int64

# The np.full() function creates by default an array with the same data type as
# the constant value used to fill in the array. If desired, the data type can be
# changed by using the keyword dtype.

# As you will learn later, a fundamental array in Linear Algebra is the Identity
# Matrix. An Identity matrix is a square matrix that has only 1s in its main
# diagonal and zeros everywhere else. The function np.eye(N) creates a square
# N x N ndarray corresponding to the Identity matrix. Since all Identity Matrices
# are square, the np.eye() function only takes a single integer as an argument.
# Let's see an example:

# We create a 5 x 5 Identity matrix.
X = np.eye(5)

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)
X =
[[ 1. 0. 0. 0. 0.]
 [ 0. 1. 0. 0. 0.]
 [ 0. 0. 1. 0. 0.]
 [ 0. 0. 0. 1. 0.]
 [ 0. 0. 0. 0. 1.]]

# X has dimensions: (5, 5)
# X is an object of type: class 'numpy.ndarray'
# The elements in X are of type: float64

# As we can see, the np.eye() function also creates by default an array with
# dtype float64. If desired, the data type can be changed by using the keyword
# dtype. You will learn all about Identity Matrices and their use in the Linear
# Algebra section of this course. We can also create diagonal matrices by using
# the np.diag() function. A diagonal matrix is a square matrix that only has
# values in its main diagonal. The np.diag() function creates an ndarray
# corresponding to a diagonal matrix , as shown in the example below:

# Create a 4 x 4 diagonal matrix that contains the numbers 10,20,30, and 50
# on its main diagonal
X = np.diag([10,20,30,50])

# We print X
print()
print('X = \n', X)
print()
X =
[[10 0 0 0]
 [ 0 20 0 0]
 [ 0 0 30 0]
 [ 0 0 0 50]]

# NumPy also allows you to create ndarrays that have evenly spaced values
# within a given interval. NumPy's np.arange() function is very versatile and
# can be used with either one, two, or three arguments. Below we will see examples
# of each case and how they are used to create different kinds of ndarrays.

# Let's start by using np.arange() with only one argument. When used with only
# one argument, np.arange(N) will create a rank 1 ndarray with consecutive integers
# between 0 and N - 1. Therefore, notice that if I want an array to have integers
# between 0 and 9, I have to use N = 10, NOT N = 9, as in the example below:

# We create a rank 1 ndarray that has sequential integers from 0 to 9
x = np.arange(10)
​
# We print the ndarray
print()
print('x = ', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
x = [0 1 2 3 4 5 6 7 8 9]

# x has dimensions: (10,)
# x is an object of type: class 'numpy.ndarray'
# The elements in x are of type: int64

# When used with two arguments, np.arange(start,stop) will create a rank 1
# ndarray with evenly spaced values within the half-open interval [start, stop).
# This means the evenly spaced numbers will include start but exclude stop. Let's
# see an example

# We create a rank 1 ndarray that has sequential integers from 4 to 9.
x = np.arange(4,10)

# We print the ndarray
print()
print('x = ', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
x = [4 5 6 7 8 9]

# x has dimensions: (6,)
# x is an object of type: class 'numpy.ndarray'
# The elements in x are of type: int64

# As we can see, the function np.arange(4,10) generates a sequence of integers
# with 4 inclusive and 10 exclusive.

# Finally, when used with three arguments, np.arange(start,stop,step) will
# create a rank 1 ndarray with evenly spaced values within the half-open interval
# [start, stop) with step being the distance between two adjacent values. Let's see an example:

# We create a rank 1 ndarray that has evenly spaced integers from 1 to 13 in steps of 3.
x = np.arange(1,14,3)

# We print the ndarray
print()
print('x = ', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
x = [ 1 4 7 10 13]

# x has dimensions: (5,)
# x is an object of type: class 'numpy.ndarray'
# The elements in x are of type: int64

# We can see that x has sequential integers between 1 and 13 but the difference
# between all adjacent values is 3.

# Even though the np.arange() function allows for non-integer steps, such as 0.3,
# the output is usually inconsistent, due to the finite floating point precision.
# For this reason, in the cases where non-integer steps are required, it is usually
# better to use the function np.linspace(). The np.linspace(start, stop, N) function
# returns N evenly spaced numbers over the closed interval [start, stop]. This means
# that both the start and thestop values are included. We should also note the
# np.linspace() function needs to be called with at least two arguments in the
# form np.linspace(start,stop). In this case, the default number of elements in
# the specified interval will be N= 50. The reason np.linspace() works better than
# the np.arange() function, is that np.linspace() uses the number of elements we
# want in a particular interval, instead of the step between values. Let's see some examples:

# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25.
x = np.linspace(0,25,10)

# We print the ndarray
print()
print('x = \n', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
x = [ 0. 2.77777778 5.55555556 8.33333333 11.11111111 13.88888889 16.66666667 19.44444444 22.22222222 25. ]

# x has dimensions: (10,)
# x is an object of type: class 'numpy.ndarray'
# The elements in x are of type: float64

# As we can see from the above example, the function np.linspace(0,25,10) returns
# an ndarray with 10 evenly spaced numbers in the closed interval [0, 25]. We can
# also see that both the start and end points, 0 and 25 in this case, are included.
# However, you can let the endpoint of the interval be excluded (just like in the
# np.arange() function) by setting the keyword endpoint = False in the np.linspace()
# function. Let's create the same x ndarray we created above but now with the endpoint
# excluded:

# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25,
# with 25 excluded.
x = np.linspace(0,25,10, endpoint = False)

# We print the ndarray
print()
print('x = ', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
x = [ 0. 2.5 5. 7.5 10. 12.5 15. 17.5 20. 22.5]

# x has dimensions: (10,)
# x is an object of type: class 'numpy.ndarray'
# The elements in x are of type: float64

# As we can see, because we have excluded the endpoint, the spacing between
# values had to change in order to fit 10 evenly spaced numbers in the given interval.

# So far, we have only used the built-in functions np.arange() and np.linspace()
# to create rank 1 ndarrays. However, we can use these functions to create rank 2
# ndarrays of any shape by combining them with the np.reshape() function. The
# np.reshape(ndarray, new_shape) function converts the given ndarray into the
# specified new_shape. It is important to note that the new_shape should be
# compatible with the number of elements in the given ndarray. For example,
# you can convert a rank 1 ndarray with 6 elements, into a 3 x 2 rank 2 ndarray,
# or a 2 x 3 rank 2 ndarray, since both of these rank 2 arrays will have a total
# of 6 elements. However, you can't reshape the rank 1 ndarray with 6 elements
# into a 3 x 3 rank 2 ndarray, since this rank 2 array will have 9 elements, which
# is greater than the number of elements in the original ndarray. Let's see some examples:

# We create a rank 1 ndarray with sequential integers from 0 to 19
x = np.arange(20)

# We print x
print()
print('Original x = ', x)
print()

# We reshape x into a 4 x 5 ndarray
x = np.reshape(x, (4,5))

# We print the reshaped x
print()
print('Reshaped x = \n', x)
print()

# We print information about the reshaped x
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
Original x = [ 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19]

Reshaped x =
[[ 0 1 2 3 4]
 [ 5 6 7 8 9]
 [10 11 12 13 14]
 [15 16 17 18 19]]

# x has dimensions: (4, 5)
# x is an object of type: class 'numpy.ndarray'
# The elements in x are of type: int64

# One great feature about NumPy, is that some functions can also be applied as
# methods. This allows us to apply different functions in sequence in just one
# line of code. ndarray methods are similar to ndarray attributes in that they
# are both applied using dot notation (.). Let's see how we can accomplish the
# same result as in the above example, but in just one line of code:

# We create a a rank 1 ndarray with sequential integers from 0 to 19 and
# reshape it to a 4 x 5 array
Y = np.arange(20).reshape(4, 5)

# We print Y
print()
print('Y = \n', Y)
print()

# We print information about Y
print('Y has dimensions:', Y.shape)
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype)
Y =
[[ 0 1 2 3 4]
 [ 5 6 7 8 9]
 [10 11 12 13 14]
 [15 16 17 18 19]]

# Y has dimensions: (4, 5)
# Y is an object of type: class 'numpy.ndarray'
# The elements in Y are of type: int64

# As we can see, we get the exact same result as before. Notice that when we
# use reshape() as a method, it's applied as ndarray.reshape(new_shape). This
# converts the ndarray into the specified shape new_shape. As before, it is
# important to note that the new_shape should be compatible with the number of
# elements in ndarray. In the example above, the function np.arange(20) creates
# an ndarray and serves as the ndarray to be reshaped by the reshape() method.
# Therefore, when using reshape() as a method, we don't need to pass the ndarray
# as an argument to the reshape() function, instead we only need to pass the
# new_shape argument.

# In the same manner, we can also combine reshape() with np.linspace() to
# create rank 2 arrays, as shown in the next example.

# We create a rank 1 ndarray with 10 integers evenly spaced between 0 and 50,
# with 50 excluded. We then reshape it to a 5 x 2 ndarray
X = np.linspace(0,50,10, endpoint=False).reshape(5,2)

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)
X =
 [[ 0. 5.]
 [ 10. 15.]
 [ 20. 25.]
 [ 30. 35.]
 [ 40. 45.]]

# X has dimensions: (5, 2)
# X is an object of type: class 'numpy.ndarray'
# The elements in X are of type: float64

# The last type of ndarrays we are going to create are random ndarrays. Random
# ndarrays are arrays that contain random numbers. Often in Machine Learning,
# you need to create random matrices, for example, when initializing the weights
# of a Neural Network. NumPy offers a variety of random functions to help us
# create random ndarrays of any shape.

# Let's start by using the np.random.random(shape) function to create an ndarray
# of the given shape with random floats in the half-open interval [0.0, 1.0).

# We create a 3 x 3 ndarray with random floats in the half-open interval [0.0, 1.0).
X = np.random.random((3,3))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in x are of type:', X.dtype)
X =
[[ 0.12379926 0.52943854 0.3443525 ]
 [ 0.11169547 0.82123909 0.52864397]
 [ 0.58244133 0.21980803 0.69026858]]

# X has dimensions: (3, 3)
# X is an object of type: class 'numpy.ndarray'
# The elements in x are of type: float64

# NumPy also allows us to create ndarrays with random integers within a particular
# interval. The function np.random.randint(start, stop, size = shape) creates an
# ndarray of the given shape with random integers in the half-open interval
# [start, stop). Let's see an example:

# We create a 3 x 2 ndarray with random integers in the half-open interval [4, 15).
X = np.random.randint(4,15,size=(3,2))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)
X =
[[ 7 11]
 [ 9 11]
 [ 6 7]]

# X has dimensions: (3, 2)
# X is an object of type: class 'numpy.ndarray'
# The elements in X are of type: int64

# In some cases, you may need to create ndarrays with random numbers that
# satisfy certain statistical properties. For example, you may want the random
# numbers in the ndarray to have an average of 0. NumPy allows you create
# random ndarrays with numbers drawn from various probability distributions.
# The function np.random.normal(mean, standard deviation, size=shape), for
# example, creates an ndarray with the given shape that contains random numbers
# picked from a normal (Gaussian) distribution with the given mean and standard
# deviation. Let's create a 1,000 x 1,000 ndarray of random floating point
# numbers drawn from a normal distribution with a mean (average) of zero and a
# standard deviation of 0.1.

# We create a 1000 x 1000 ndarray of random floats drawn from normal (Gaussian) distribution
# with a mean of zero and a standard deviation of 0.1.
X = np.random.normal(0, 0.1, size=(1000,1000))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)
print('The elements in X have a mean of:', X.mean())
print('The maximum value in X is:', X.max())
print('The minimum value in X is:', X.min())
print('X has', (X < 0).sum(), 'negative numbers')
print('X has', (X > 0).sum(), 'positive numbers')
X =
[[ 0.04218614 0.03247225 -0.02936003 ..., 0.01586796 -0.05599115 -0.03630946]
 [ 0.13879995 -0.01583122 -0.16599967 ..., 0.01859617 -0.08241612 0.09684025]
 [ 0.14422252 -0.11635985 -0.04550231 ..., -0.09748604 -0.09350044 0.02514799]
 ...,
 [-0.10472516 -0.04643974 0.08856722 ..., -0.02096011 -0.02946155 0.12930844]
 [-0.26596955 0.0829783 0.11032549 ..., -0.14492074 -0.00113646 -0.03566034]
 [-0.12044482 0.20355356 0.13637195 ..., 0.06047196 -0.04170031 -0.04957684]]

# X has dimensions: (1000, 1000)
# X is an object of type: class 'numpy.ndarray'
# The elements in X are of type: float64
# The elements in X have a mean of: -0.000121576684405
# The maximum value in X is: 0.476673923106
# The minimum value in X is: -0.499114224706
# X has 500562 negative numbers
# X has 499438 positive numbers

# As we can see, the average of the random numbers in the ndarray is close to
# zero, both the maximum and minimum values in X are symmetric about zero
# (the average), and we have about the same amount of positive and negative numbers.


# Quiz
# Using the Built-in functions you learned about in the
# previous lesson, create a 4 x 4 ndarray that only
# contains consecutive even numbers from 2 to 32 (inclusive)

import numpy as np

X = np.arange(2,34,2).reshape(4,4)

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)


Y = np.linspace(2,32,16).reshape(4,4)

# We print Y
print()
print('Y = \n', Y)
print()

# We print information about X
print('Y has dimensions:', Y.shape)
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype)



# Accessing, Deleting, and Inserting Elements Into ndarrays

# Now that you know how to create a variety of ndarrays, we will now see how
# NumPy allows us to effectively manipulate the data within the ndarrays. NumPy
# ndarrays are mutable, meaning that the elements in ndarrays can be changed
# after the ndarray has been created. NumPy ndarrays can also be sliced, which
# means that ndarrays can be split in many different ways. This allows us, for
# example, to retrieve any subset of the ndarray that we want. Often in Machine
# Learning you will use slicing to separate data, as for example when dividing
# a data set into training, cross validation, and testing sets.

# We will start by looking at how the elements of an ndarray can be accessed or
# modified by indexing. Elements can be accessed using indices inside square
# brackets, [ ]. NumPy allows you to use both positive and negative indices to
# access elements in the ndarray. Positive indices are used to access elements
# from the beginning of the array, while negative indices are used to access
# elements from the end of the array. Let's see how we can access elements in
# rank 1 ndarrays:

# We create a rank 1 ndarray that contains integers from 1 to 5
x = np.array([1, 2, 3, 4, 5])

# We print x
print()
print('x = ', x)
print()

# Let's access some elements with positive indices
print('This is First Element in x:', x[0])
print('This is Second Element in x:', x[1])
print('This is Fifth (Last) Element in x:', x[4])
print()

# Let's access the same elements with negative indices
print('This is First Element in x:', x[-5])
print('This is Second Element in x:', x[-4])
print('This is Fifth (Last) Element in x:', x[-1])
x = [1 2 3 4 5]

# This is First Element in x: 1
# This is Second Element in x: 2
# This is Fifth (Last) Element in x: 5

# This is First Element in x: 1
# This is Second Element in x: 2
# This is Fifth (Last) Element in x: 5

# Notice that to access the first element in the ndarray we have to use the
# index 0 not 1. Also notice, that the same element can be accessed using both
# positive and negative indices. As mentioned earlier, positive indices are
# used to access elements from the beginning of the array, while negative
# indices are used to access elements from the end of the array.

# Now let's see how we can change the elements in rank 1 ndarrays. We do this
# by accessing the element we want to change and then using the = sign to assign
# the new value:

# We create a rank 1 ndarray that contains integers from 1 to 5
x = np.array([1, 2, 3, 4, 5])

# We print the original x
print()
print('Original:\n x = ', x)
print()

# We change the fourth element in x from 4 to 20
x[3] = 20

# We print x after it was modified
print('Modified:\n x = ', x)
# Original:
# x = [1 2 3 4 5]

# Modified:
# x = [ 1 2 3 20 5]

# Similarly, we can also access and modify specific elements of rank 2 ndarrays.
# To access elements in rank 2 ndarrays we need to provide 2 indices in the form
# [row, column]. Let's see some examples

# We create a 3 x 3 rank 2 ndarray that contains integers from 1 to 9
X = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We print X
print()
print('X = \n', X)
print()

# Let's access some elements in X
print('This is (0,0) Element in X:', X[0,0])
print('This is (0,1) Element in X:', X[0,1])
print('This is (2,2) Element in X:', X[2,2])

# X =
# [[1 2 3]
# [4 5 6]
# [7 8 9]]

# This is (0,0) Element in X: 1
# This is (0,1) Element in X: 2
# This is (2,2) Element in X: 9

# Remember that the index [0, 0] refers to the element in the first row, first column.

# Elements in rank 2 ndarrays can be modified in the same way as with rank 1
# ndarrays. Let's see an example:

# We create a 3 x 3 rank 2 ndarray that contains integers from 1 to 9
X = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We print the original x
print()
print('Original:\n X = \n', X)
print()

# We change the (0,0) element in X from 1 to 20
X[0,0] = 20

# We print X after it was modified
print('Modified:\n X = \n', X)

# Original:
# X =
# [[1 2 3]
# [4 5 6]
# [7 8 9]]

# Modified:
# X =
# [[20 2 3]
# [ 4 5 6]
# [ 7 8 9]]

# Now, let's take a look at how we can add and delete elements from ndarrays.
# We can delete elements using the np.delete(ndarray, elements, axis) function.
# This function deletes the given list of elements from the given ndarray along
# the specified axis. For rank 1 ndarrays the axis keyword is not required. For
# rank 2 ndarrays, axis = 0 is used to select rows, and axis = 1 is used to
# select columns. Let's see some examples:

# We create a rank 1 ndarray
x = np.array([1, 2, 3, 4, 5])

# We create a rank 2 ndarray
Y = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We print x
print()
print('Original x = ', x)

# We delete the first and last element of x
x = np.delete(x, [0,4])

# We print x with the first and last element deleted
print()
print('Modified x = ', x)

# We print Y
print()
print('Original Y = \n', Y)

# We delete the first row of y
w = np.delete(Y, 0, axis=0)

# We delete the first and last column of y
v = np.delete(Y, [0,2], axis=1)

# We print w
print()
print('w = \n', w)

# We print v
print()
print('v = \n', v)

# Original x = [1 2 3 4 5]

# Modified x = [2 3 4]

# Original Y =
# [[1 2 3]
# [4 5 6]
# [7 8 9]]

# w =
# [[4 5 6]
# [7 8 9]]

# v =
# [[2]
# [5]
# [8]]

# Now, let's see how we can append values to ndarrays. We can append values to
# ndarrays using the np.append(ndarray, elements, axis) function. This function
# appends the given list of elements to ndarray along the specified axis. Let's
# see some examples:

# We create a rank 1 ndarray
x = np.array([1, 2, 3, 4, 5])

# We create a rank 2 ndarray
Y = np.array([[1,2,3],[4,5,6]])

# We print x
print()
print('Original x = ', x)

# We append the integer 6 to x
x = np.append(x, 6)

# We print x
print()
print('x = ', x)

# We append the integer 7 and 8 to x
x = np.append(x, [7,8])

# We print x
print()
print('x = ', x)

# We print Y
print()
print('Original Y = \n', Y)

# We append a new row containing 7,8,9 to y
v = np.append(Y, [[7,8,9]], axis=0)

# We append a new column containing 9 and 10 to y
q = np.append(Y,[[9],[10]], axis=1)

# We print v
print()
print('v = \n', v)

# We print q
print()
print('q = \n', q)

# Original x = [1 2 3 4 5]

# x = [1 2 3 4 5 6]

# x = [1 2 3 4 5 6 7 8]

# Original Y =
# [[1 2 3]
# [4 5 6]]

# v =
#[[1 2 3]
# [4 5 6]
# [7 8 9]]

# q =
# [[ 1 2 3 9]
# [ 4 5 6 10]]

# Notice that when appending rows or columns to rank 2 ndarrays the rows or
# columns must have the correct shape, so as to match the shape of the rank 2 ndarray.

# Now let's see now how we can insert values to ndarrays. We can insert values
# to ndarrays using the np.insert(ndarray, index, elements, axis) function.
# This function inserts the given list of elements to ndarray right before the
# given index along the specified axis. Let's see some examples:

# We create a rank 1 ndarray
x = np.array([1, 2, 5, 6, 7])

# We create a rank 2 ndarray
Y = np.array([[1,2,3],[7,8,9]])

# We print x
print()
print('Original x = ', x)

# We insert the integer 3 and 4 between 2 and 5 in x.
x = np.insert(x,2,[3,4])

# We print x with the inserted elements
print()
print('x = ', x)

# We print Y
print()
print('Original Y = \n', Y)

# We insert a row between the first and last row of y
w = np.insert(Y,1,[4,5,6],axis=0)

# We insert a column full of 5s between the first and second column of y
v = np.insert(Y,1,5, axis=1)

# We print w
print()
print('w = \n', w)

# We print v
print()
print('v = \n', v)

# Original x = [1 2 5 6 7]

# x = [1 2 3 4 5 6 7]

# Original Y =
# [[1 2 3]
#  [7 8 9]]

# w =
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# v =
# [[1 5 2 3]
#  [7 5 8 9]]

# NumPy also allows us to stack ndarrays on top of each other, or to stack
# them side by side. The stacking is done using either the np.vstack() function
# for vertical stacking, or the np.hstack() function for horizontal stacking.
# It is important to note that in order to stack ndarrays, the shape of the
# ndarrays must match. Let's see some examples:

# We create a rank 1 ndarray
x = np.array([1,2])

# We create a rank 2 ndarray
Y = np.array([[3,4],[5,6]])

# We print x
print()
print('x = ', x)

# We print Y
print()
print('Y = \n', Y)

# We stack x on top of Y
z = np.vstack((x,Y))

# We stack x on the right of Y. We need to reshape x in order to stack it on
# the right of Y.
w = np.hstack((Y,x.reshape(2,1)))

# We print z
print()
print('z = \n', z)

# We print w
print()
print('w = \n', w)

# x = [1 2]

# Y =
# [[3 4]
# [5 6]]

# z =
# [[1 2]
#  [3 4]
#  [5 6]]

# w =
# [[3 4 1]
# [5 6 2]]



# Slicing ndarrays

# As we mentioned earlier, in addition to being able to access individual elements
# one at a time, NumPy provides a way to access subsets of ndarrays. This is known
# as slicing. Slicing is performed by combining indices with the colon : symbol
# inside the square brackets. In general you will come across three types of slicing:

# 1. ndarray[start:end]
# 2. ndarray[start:]
# 3. ndarray[:end]

# The first method is used to select elements between the start and end indices.
# The second method is used to select all elements from the start index till the
# last index. The third method is used to select all elements from the first index
# till the end index. We should note that in methods one and three, the end index
# is excluded. We should also note that since ndarrays can be multidimensional,
# when doing slicing you usually have to specify a slice for each dimension of the array.

# We will now see some examples of how to use the above methods to select different
# subsets of a rank 2 ndarray.

# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(20).reshape(4, 5)

# We print X
print()
print('X = \n', X)
print()

# We select all the elements that are in the 2nd through 4th rows and in the 3rd to 5th columns
Z = X[1:4,2:5]

# We print Z
print('Z = \n', Z)

# We can select the same elements as above using method 2
W = X[1:,2:5]

# We print W
print()
print('W = \n', W)

# We select all the elements that are in the 1st through 3rd rows and in the 3rd to 4th columns
Y = X[:3,2:5]

# We print Y
print()
print('Y = \n', Y)

# We select all the elements in the 3rd row
v = X[2,:]

# We print v
print()
print('v = ', v)

# We select all the elements in the 3rd column
q = X[:,2]

# We print q
print()
print('q = ', q)

# We select all the elements in the 3rd column but return a rank 2 ndarray
R = X[:,2:3]

# We print R
print()
print('R = \n', R)
X =
[[ 0 1 2 3 4]
 [ 5 6 7 8 9]
 [10 11 12 13 14]
 [15 16 17 18 19]]

Z =
[[ 7 8 9]
 [12 13 14]
 [17 18 19]]

W =
[[ 7 8 9]
 [12 13 14]
 [17 18 19]]

Y =
[[ 2 3 4]
 [ 7 8 9]
 [12 13 14]]

v = [10 11 12 13 14]

q = [ 2 7 12 17]

R =
[[ 2]
 [ 7]
 [12]
 [17]]

# Notice that when we selected all the elements in the 3rd column, variable q
# above, the slice returned a rank 1 ndarray instead of a rank 2 ndarray. However,
# slicing X in a slightly different way, variable R above, we can actually get a
# rank 2 ndarray instead.

# It is important to note that when we perform slices on ndarrays and save them
# into new variables, as we did above, the data is not copied into the new variable.
# This is one feature that often causes confusion for beginners. Therefore, we
# will look at this in a bit more detail.

# In the above examples, when we make assignments, such as:

Z = X[1:4,2:5]
# the slice of the original array X is not copied in the variable Z. Rather, X
# and Z are now just two different names for the same ndarray. We say that
# slicing only creates a view of the original array. This means that if you
# make changes in Z you will be in effect changing the elements in X as well.
# Let's see this with an example:

# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(20).reshape(4, 5)

# We print X
print()
print('X = \n', X)
print()

# We select all the elements that are in the 2nd through 4th rows and in the
# 3rd to 4th columns
Z = X[1:4,2:5]

# We print Z
print()
print('Z = \n', Z)
print()

# We change the last element in Z to 555
Z[2,2] = 555

# We print X
print()
print('X = \n', X)
print()
X =
[[ 0 1 2 3 4]
 [ 5 6 7 8 9]
 [10 11 12 13 14]
 [15 16 17 18 19]]

Z =
[[ 7 8 9]
 [12 13 14]
 [17 18 19]]

X =
[[ 0 1 2 3 4]
 [ 5 6 7 8 9]
 [ 10 11 12 13 14]
 [ 15 16 17 18 555]]

# We can clearly see in the above example that if we make changes to Z, X changes as well.

# However, if we want to create a new ndarray that contains a copy of the values
# in the slice we need to use the np.copy() function. The np.copy(ndarray) function
# creates a copy of the given ndarray. This function can also be used as a method,
# in the same way as we did before with the reshape function. Let's do the same example
# we did before but now with copies of the arrays. We'll use copy both as a function and as a method.

# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(20).reshape(4, 5)

# We print X
print()
print('X = \n', X)
print()

# create a copy of the slice using the np.copy() function
Z = np.copy(X[1:4,2:5])

#  create a copy of the slice using the copy as a method
W = X[1:4,2:5].copy()

# We change the last element in Z to 555
Z[2,2] = 555

# We change the last element in W to 444
W[2,2] = 444

# We print X
print()
print('X = \n', X)

# We print Z
print()
print('Z = \n', Z)

# We print W
print()
print('W = \n', W)
# X =
# [[ 0 1 2 3 4]
# [ 5 6 7 8 9]
# [10 11 12 13 14]
# [15 16 17 18 19]]

# X =
# [[ 0 1 2 3 4]
# [ 5 6 7 8 9]
# [10 11 12 13 14]
# [15 16 17 18 19]]

# Z =
# [[ 7 8 9]
# [ 12 13 14]
# [ 17 18 555]]

# W =
# [[ 7 8 9]
# [ 12 13 14]
# [ 17 18 444]]

# We can clearly see that by using the copy command, we are creating new ndarrays
# that are completely independent of each other.

# It is often useful to use one ndarray to make slices, select, or change elements
# in another ndarray. Let's see some examples:

# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(20).reshape(4, 5)

# We create a rank 1 ndarray that will serve as indices to select elements from X
indices = np.array([1,3])

# We print X
print()
print('X = \n', X)
print()

# We print indices
print('indices = ', indices)
print()

# We use the indices ndarray to select the 2nd and 4th row of X
Y = X[indices,:]

# We use the indices ndarray to select the 2nd and 4th column of X
Z = X[:, indices]

# We print Y
print()
print('Y = \n', Y)

# We print Z
print()
print('Z = \n', Z)

# X =
# [[ 0 1 2 3 4]
# [ 5 6 7 8 9]
# [10 11 12 13 14]
# [15 16 17 18 19]]

# indices = [1 3]

# Y =
# [[ 5 6 7 8 9]
# [15 16 17 18 19]]

# Z =
# [[ 1 3]
# [ 6 8]
# [11 13]
# [16 18]]

# NumPy also offers built-in functions to select specific elements within
# ndarrays. For example, the np.diag(ndarray, k=N) function extracts the
# elements along the diagonal defined by N. As default is k=0, which refers
# to the main diagonal. Values of k > 0 are used to select elements in diagonals
# above the main diagonal, and values of k < 0 are used to select elements in d
# iagonals below the main diagonal. Let's see an example:

# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(25).reshape(5, 5)

# We print X
print()
print('X = \n', X)
print()

# We print the elements in the main diagonal of X
print('z =', np.diag(X))
print()

# We print the elements above the main diagonal of X
print('y =', np.diag(X, k=1))
print()

# We print the elements below the main diagonal of X
print('w = ', np.diag(X, k=-1))

# X =
# [[ 0 1 2 3 4]
# [ 5 6 7 8 9]
# [10 11 12 13 14]
# [15 16 17 18 19]
# [20 21 22 23 24]]

# z = [ 0 6 12 18 24]

# y = [ 1 7 13 19]

# w = [ 5 11 17 23]

# It is often useful to extract only the unique elements in an ndarray. We can
# find the unique elements in an ndarray by using the np.unique() function.
# The np.unique(ndarray) function returns the unique elements in the given ndarray,
# as in the example below:

# Create 3 x 3 ndarray with repeated values
X = np.array([[1,2,3],[5,2,8],[1,2,3]])

# We print X
print()
print('X = \n', X)
print()

# We print the unique elements of X
print('The unique elements in X are:',np.unique(X))

# X =
# [[1 2 3]
# [5 2 8]
# [1 2 3]]

# The unique elements in X are: [1 2 3 5 8]


# Boolean Indexing, Set Operations, and Sorting

# Up to now we have seen how to make slices and select elements of an ndarray
# using indices. This is useful when we know the exact indices of the elements
# we want to select. However, there are many situations in which we don't know
# the indices of the elements we want to select. For example, suppose we have a
# 10,000 x 10,000 ndarray of random integers ranging from 1 to 15,000 and we
# only want to select those integers that are less than 20. Boolean indexing can
# help us in these cases, by allowing us select elements using logical arguments
# instead of explicit indices. Let's see some examples:

# We create a 5 x 5 ndarray that contains integers from 0 to 24
X = np.arange(25).reshape(5, 5)

# We print X
print()
print('Original X = \n', X)
print()

# We use Boolean indexing to select elements in X:
print('The elements in X that are greater than 10:', X[X > 10])
print('The elements in X that less than or equal to 7:', X[X <= 7])
print('The elements in X that are between 10 and 17:', X[(X > 10) & (X < 17)])

# We use Boolean indexing to assign the elements that are between 10 and 17
# the value of -1
X[(X > 10) & (X < 17)] = -1

# We print X
print()
print('X = \n', X)
print()

# Original X =
# [[ 0 1 2 3 4]
# [ 5 6 7 8 9]
# [10 11 12 13 14]
# [15 16 17 18 19]
# [20 21 22 23 24]]

# The elements in X that are greater than 10: [11 12 13 14 15 16 17 18 19 20 21 22 23 24]
# The elements in X that less than or equal to 7: [0 1 2 3 4 5 6 7]
# The elements in X that are between 10 and 17: [11 12 13 14 15 16]

# X =
# [[ 0 1 2 3 4]
# [ 5 6 7 8 9]
# [10 -1 -1 -1 -1]
# [-1 -1 17 18 19]
# [20 21 22 23 24]]

# In addition to Boolean Indexing NumPy also allows for set operations. This
# useful when comparing ndarrays, for example, to find common elements between
# two ndarrays. Let's see some examples:

# We create a rank 1 ndarray
x = np.array([1,2,3,4,5])

# We create a rank 1 ndarray
y = np.array([6,7,2,8,4])

# We print x
print()
print('x = ', x)

# We print y
print()
print('y = ', y)

# We use set operations to compare x and y:
print()
print('The elements that are both in x and y:', np.intersect1d(x,y))
print('The elements that are in x that are not in y:', np.setdiff1d(x,y))
print('All the elements of x and y:',np.union1d(x,y))
x = [1 2 3 4 5]

y = [6 7 2 8 4]

# The elements that are both in x and y: [2 4]
# The elements that are in x that are not in y: [1 3 5]
# All the elements of x and y: [1 2 3 4 5 6 7 8]

# We can also sort ndarrays in NumPy. We will learn how to use the np.sort()
# function to sort rank 1 and rank 2 ndarrays in different ways. Like with other
# functions we saw before, the sort function can also be used as a method.
# However, there is a big difference on how the data is stored in memory in
# this case. When np.sort() is used as a function, it sorts the ndrrays out of
# place, meaning, that it doesn't change the original ndarray being sorted.
# However, when you use sort as a method, ndarray.sort() sorts the ndarray in
# place, meaning, that the original array will be changed to the sorted one.
# Let's see some examples:

# We create an unsorted rank 1 ndarray
x = np.random.randint(1,11,size=(10,))

# We print x
print()
print('Original x = ', x)

# We sort x and print the sorted array using sort as a function.
print()
print('Sorted x (out of place):', np.sort(x))

# When we sort out of place the original array remains intact. To see this we print x again
print()
print('x after sorting:', x)
# riginal x = [9 6 4 4 9 4 8 4 4 7]

Sorted x (out of place): [4 4 4 4 4 6 7 8 9 9]

# x after sorting: [9 6 4 4 9 4 8 4 4 7]

# Notice that np.sort() sorts the array but, if the ndarray being sorted has
# repeated values, np.sort() leaves those values in the sorted array. However,
# if desired, we can sort only the unique elements in x by combining the sort
# function with the unique function. Let's see how we can sort the unique elements
# of x above:

# We sort x but only keep the unique elements in x
print(np.sort(np.unique(x)))
[4 6 7 8 9]

# Finally, let's see how we can sort ndarrays in place, by using sort as a method:

# We create an unsorted rank 1 ndarray
x = np.random.randint(1,11,size=(10,))

# We print x
print()
print('Original x = ', x)

# We sort x and print the sorted array using sort as a method.
x.sort()

# When we sort in place the original array is changed to the sorted array. To see this we print x again
print()
print('x after sorting:', x)
# Original x = [9 9 8 1 1 4 3 7 2 8]

# x after sorting: [1 1 2 3 4 7 8 8 9 9]

# When sorting rank 2 ndarrays, we need to specify to the np.sort() function
# whether we are sorting by rows or columns. This is done by using the axis
# keyword. Let's see some examples:

# We create an unsorted rank 2 ndarray
X = np.random.randint(1,11,size=(5,5))

# We print X
print()
print('Original X = \n', X)
print()

# We sort the columns of X and print the sorted array
print()
print('X with sorted columns :\n', np.sort(X, axis = 0))

# We sort the rows of X and print the sorted array
print()
print('X with sorted rows :\n', np.sort(X, axis = 1))

# Original X =
# [6 1 7 6 3]
# [3 9 8 3 5]
# [6 5 8 9 3]
# [2 1 5 7 7]
# [9 8 1 9 8]]

# X with sorted columns :
# [[2 1 1 3 3]
# [3 1 5 6 3]
# [6 5 7 7 5]
# [6 8 8 9 7]
# [9 9 8 9 8]]

# X with sorted rows :
# [[1 3 6 6 7]
# [3 3 5 8 9]
# [3 5 6 8 9]
# [1 2 5 7 7]
# [1 8 8 9 9]]


# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
# Afterwards use Boolean indexing to pick out only the odd numbers in the array

import numpy as np

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
X = np.arange(1, 26).reshape(5, 5)

print()
print('Original X = \n', X)
print()
print('The elements in X that are odd:', X[X % 2 != 0])
print()

# Use Boolean indexing to pick out only the odd numbers in the array
Y = X[X % 2 != 0]

print()
print('Original Y = \n', Y)
print()


# Arithmetic operations and Broadcasting

# We have reached the last lesson in this Introduction to NumPy. In this last
# lesson we will see how NumPy does arithmetic operations on ndarrays. NumPy
# allows element-wise operations on ndarrays as well as matrix operations.
# In this lesson we will only be looking at element-wise operations on ndarrays.
# In order to do element-wise operations, NumPy sometimes uses something called
# Broadcasting. Broadcasting is the term used to describe how NumPy handles
# element-wise arithmetic operations with ndarrays of different shapes. For
# example, broadcasting is used implicitly when doing arithmetic operations
# between scalars and ndarrays.

# Let's start by doing element-wise addition, subtraction, multiplication, and
# division, between ndarrays. To do this, NumPy provides a functional approach,
# where we use functions such as np.add(), or by using arithmetic symbols, such
# as +, that resembles more how we write mathematical equations. Both forms will
# do the same operation, the only difference is that if you use the function
# approach, the functions usually have options that you can tweak using keywords.
# It is important to note that when performing element-wise operations, the shapes
# of the ndarrays being operated on, must have the same shape or be broadcastable.
# We'll explain more about this later in this lesson. Let's start by performing
# element-wise arithmetic operations on rank 1 ndarrays:

# We create two rank 1 ndarrays
x = np.array([1,2,3,4])
y = np.array([5.5,6.5,7.5,8.5])

# We print x
print()
print('x = ', x)

# We print y
print()
print('y = ', y)
print()

# We perfrom basic element-wise operations using arithmetic symbols and functions
print('x + y = ', x + y)
print('add(x,y) = ', np.add(x,y))
print()
print('x - y = ', x - y)
print('subtract(x,y) = ', np.subtract(x,y))
print()
print('x * y = ', x * y)
print('multiply(x,y) = ', np.multiply(x,y))
print()
print('x / y = ', x / y)
print('divide(x,y) = ', np.divide(x,y))
x = [1 2 3 4]

y = [ 5.5 6.5 7.5 8.5]

x + y = [ 6.5 8.5 10.5 12.5]
add(x,y) = [ 6.5 8.5 10.5 12.5]

x - y = [-4.5 -4.5 -4.5 -4.5]
subtract(x,y) = [-4.5 -4.5 -4.5 -4.5]

x * y = [ 5.5 13. 22.5 34. ]
multiply(x,y) = [ 5.5 13. 22.5 34. ]

x / y = [ 0.18181818 0.30769231 0.4 0.47058824]
divide(x,y) = [ 0.18181818 0.30769231 0.4 0.47058824]

# We can also perform the same element-wise arithmetic operations on rank 2
# ndarrays. Again, remember that in order to do these operations the shapes of
# the ndarrays being operated on, must have the same shape or be broadcastable.

# We create two rank 2 ndarrays
X = np.array([1,2,3,4]).reshape(2,2)
Y = np.array([5.5,6.5,7.5,8.5]).reshape(2,2)

# We print X
print()
print('X = \n', X)

# We print Y
print()
print('Y = \n', Y)
print()

# We perform basic element-wise operations using arithmetic symbols and functions
print('X + Y = \n', X + Y)
print()
print('add(X,Y) = \n', np.add(X,Y))
print()
print('X - Y = \n', X - Y)
print()
print('subtract(X,Y) = \n', np.subtract(X,Y))
print()
print('X * Y = \n', X * Y)
print()
print('multiply(X,Y) = \n', np.multiply(X,Y))
print()
print('X / Y = \n', X / Y)
print()
print('divide(X,Y) = \n', np.divide(X,Y))

# X =
# [[1 2]
# [3 4]]

# Y =
# [[ 5.5 6.5]
#  [ 7.5 8.5]]

# X + Y =
# [[ 6.5 8.5]
#  [ 10.5 12.5]]

# add(X,Y) =
# [[ 6.5 8.5]
#  [ 10.5 12.5]]

# X - Y =
# [[-4.5 -4.5]
#  [-4.5 -4.5]]

# subtract(X,Y) =
# [[-4.5 -4.5]
#  [-4.5 -4.5]]

# X * Y =
# [[ 5.5 13. ]
#  [ 22.5 34. ]]

# multiply(X,Y) =
# [[ 5.5 13. ]
#  [ 22.5 34. ]]

# X / Y =
# [[ 0.18181818 0.30769231]
#  [ 0.4 0.47058824]]

#  divide(X,Y) =
# [[ 0.18181818 0.30769231]
#  [ 0.4 0.47058824]]

# We can also apply mathematical functions, such as sqrt(x), to all elements of
# an ndarray at once.

# We create a rank 1 ndarray
x = np.array([1,2,3,4])

# We print x
print()
print('x = ', x)

# We apply different mathematical functions to all elements of x
print()
print('EXP(x) =', np.exp(x))
print()
print('SQRT(x) =',np.sqrt(x))
print()
print('POW(x,2) =',np.power(x,2)) # We raise all elements to the power of 2
x = [1 2 3 4]

EXP(x) = [ 2.71828183 7.3890561 20.08553692 54.59815003]

SQRT(x) = [ 1. 1.41421356 1.73205081 2. ]

POW(x,2) = [ 1 4 9 16]

# Another great feature of NumPy is that it has a wide variety of statistical
# functions. Statistical functions provide us with statistical information about
# the elements in an ndarray. Let's see some examples:

# We create a 2 x 2 ndarray
X = np.array([[1,2], [3,4]])

# We print x
print()
print('X = \n', X)
print()

print('Average of all elements in X:', X.mean())
print('Average of all elements in the columns of X:', X.mean(axis=0))
print('Average of all elements in the rows of X:', X.mean(axis=1))
print()
print('Sum of all elements in X:', X.sum())
print('Sum of all elements in the columns of X:', X.sum(axis=0))
print('Sum of all elements in the rows of X:', X.sum(axis=1))
print()
print('Standard Deviation of all elements in X:', X.std())
print('Standard Deviation of all elements in the columns of X:', X.std(axis=0))
print('Standard Deviation of all elements in the rows of X:', X.std(axis=1))
print()
print('Median of all elements in X:', np.median(X))
print('Median of all elements in the columns of X:', np.median(X,axis=0))
print('Median of all elements in the rows of X:', np.median(X,axis=1))
print()
print('Maximum value of all elements in X:', X.max())
print('Maximum value of all elements in the columns of X:', X.max(axis=0))
print('Maximum value of all elements in the rows of X:', X.max(axis=1))
print()
print('Minimum value of all elements in X:', X.min())
print('Minimum value of all elements in the columns of X:', X.min(axis=0))
print('Minimum value of all elements in the rows of X:', X.min(axis=1))

# X =
#  [[1 2]
#  [3 4]]

# Average of all elements in X: 2.5
# Average of all elements in the columns of X: [ 2. 3.]
# Average of all elements in the rows of X: [ 1.5 3.5]

# Sum of all elements in X: 10
# Sum of all elements in the columns of X: [4 6]
# Sum of all elements in the rows of X: [3 7]

# Standard Deviation of all elements in X: 1.11803398875
# Standard Deviation of all elements in the columns of X: [ 1. 1.]
# Standard Deviation of all elements in the rows of X: [ 0.5 0.5]

# Median of all elements in X: 2.5
# Median of all elements in the columns of X: [ 2. 3.]
# Median of all elements in the rows of X: [ 1.5 3.5]

# Maximum value of all elements in X: 4
# Maximum value of all elements in the columns of X: [3 4]
# Maximum value of all elements in the rows of X: [2 4]

# Minimum value of all elements in X: 1
# Minimum value of all elements in the columns of X: [1 2]
# Minimum value of all elements in the rows of X: [1 3]

# Finally, let's see how NumPy can add single numbers to all the elements of an
# ndarray without the use of complicated loops.

# We create a 2 x 2 ndarray
X = np.array([[1,2], [3,4]])

# We print x
print()
print('X = \n', X)
print()

print('3 * X = \n', 3 * X)
print()
print('3 + X = \n', 3 + X)
print()
print('X - 3 = \n', X - 3)
print()
print('X / 3 = \n', X / 3)

# X =
# [[1 2]
# [3 4]]

# 3 * X =
# [[ 3 6]
#  [ 9 12]]

# 3 + X =
# [[4 5]
#  [6 7]]

# X - 3 =
# [[-2 -1]
#  [ 0 1]]

# X / 3 =
# [[ 0.33333333 0.66666667]
#  [ 1. 1.33333333]]

# In the examples above, NumPy is working behind the scenes to broadcast 3 along
# the ndarray so that they have the same shape. This allows us to add 3 to each
# element of X with just one line of code.

# Subject to certain constraints, Numpy can do the same for two ndarrays of
# different shapes, as we can see below.

# We create a rank 1 ndarray
x = np.array([1,2,3])

# We create a 3 x 3 ndarray
Y = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We create a 3 x 1 ndarray
Z = np.array([1,2,3]).reshape(3,1)

# We print x
print()
print('x = ', x)
print()

# We print Y
print()
print('Y = \n', Y)
print()

# We print Z
print()
print('Z = \n', Z)
print()

print('x + Y = \n', x + Y)
print()
print('Z + Y = \n',Z + Y)
x = [1 2 3]

# Y =
# [[1 2 3]
# [4 5 6]
# [7 8 9]]

# Z =
# [[1]
# [2]
# [3]]

# x + Y =
# [[ 2 4 6]
# [ 5 7 9]
# [ 8 10 12]]

# Z + Y =
# [[ 2 3 4]
#  [ 6 7 8]
#  [10 11 12]]

# As before, NumPy is able to add 1 x 3 and 3 x 1 ndarrays to 3 x 3 ndarrays by
# broadcasting the smaller ndarrays along the big ndarray so that they have
# compatible shapes. In general, NumPy can do this provided that the smaller
# ndarray, such as the 1 x 3 ndarray in our example, can be expanded to the shape
# of the larger ndarray in such a way that the resulting broadcast is unambiguous.

# Make sure you check out the NumPy Documentation for more information on
# Broadcasting and its rules:

# Broadcasting
# https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html




# Use Broadcasting to create a 4 x 4 ndarray that has its first
# column full of 1s, its second column full of 2s, its third
# column full of 3s, etc..

import numpy as np

# We create a 4 x 4 ndarray full of ones.
# X = np.full((4,4), 1)


X = np.ones((4,4))

# We print X
print()
print('X = \n', X)
print()

# We print information about Z
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)

Y =  np.arange(1,5)

# We print Y
print()
print('Y = \n', Y)
print()

# We print information about Y
print('Y has dimensions:', Y.shape)
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype)



Z = np.ones((4,4)) * np.arange(1,5)

# We print Z
print()
print('Z = \n', Z)
print()

# We print information about Z
print('Z has dimensions:', Z.shape)
print('Z is an object of type:', type(Z))
print('The elements in Z are of type:', Z.dtype)


# Introduction to Pandas

# Pandas is a package for data manipulation and analysis in Python. The name
# Pandas is derived from the econometrics term Panel Data. Pandas incorporates
# two additional data structures into Python, namely Pandas Series and Pandas
# DataFrame. These data structures allow us to work with labeled and relational
# data in an easy and intuitive manner. These lessons are intended as a basic
# overview of Pandas and introduces some of its most important features.

# In the following lessons you will learn:

# How to import Pandas
# How to create Pandas Series and DataFrames using various methods
# How to access and change elements in Series and DataFrames
# How to perform arithmetic operations on Series
# How to load data into a DataFrame
# How to deal with Not a Number (NaN) values

# The following lessons assume that you are already familiar with NumPy and have
# gone over the previous NumPy lessons. Therefore, to avoid being repetitive we
# will omit a lot of details already given in the NumPy lessons. Consequently, if
# you haven't seen the NumPy lessons we suggest you go over them first.

# Downloading Pandas

# Pandas is included with Anaconda. If you don't already have Anaconda installed
# on your computer, please refer to the Anaconda section to get clear instructions
# on how to install Anaconda on your PC or Mac.

# Pandas Versions

# As with many Python packages, Pandas is updated from time to time. The following
# lessons were created using Pandas version 0.22. You can check which version of
# Pandas you have by typing !conda list pandas in your Jupyter notebook or by
# typing conda list pandas in the Anaconda prompt. If you have another version
# of Pandas installed in your computer, you can update your version by typing conda
# install pandas=0.22 in the Anaconda prompt. As newer versions of Pandas are
# released, some functions may become obsolete or replaced, so make sure you
# have the correct Pandas version before running the code. This will guarantee
# your code will run smoothly.

# Pandas Documentation
# Pandas is remarkable data analysis library and it has many functions and features.
# In these introductory lessons we will only scratch the surface of what Pandas can do.
# If you want to learn more about Pandas, make sure you check out the Pandas Documentation:
# https://pandas.pydata.org/pandas-docs/stable/



# Why Use Pandas?

# The recent success of machine learning algorithms is partly due to the huge
# amounts of data that we have available to train our algorithms on. However,
# when it comes to data, quantity is not the only thing that matters, the quality
# of your data is just as important. It often happens that large datasets don’t
# come ready to be fed into your learning algorithms. More often than not, large
# datasets will often have missing values, outliers, incorrect values, etc… Having
# data with a lot of missing or bad values, for example, is not going to allow
# your machine learning algorithms to perform well. Therefore, one very important
# step in machine learning is to look at your data first and make sure it is well
# suited for your training algorithm by doing some basic data analysis. This is
# where Pandas come in. Pandas Series and DataFrames are designed for fast data
# analysis and manipulation, as well as being flexible and easy to use. Below are
# just a few features that makes Pandas an excellent package for data analysis:

# (1) Allows the use of labels for rows and columns
# (2) Can calculate rolling statistics on time series data
# (3) Easy handling of NaN values
# (4) Is able to load data of different formats into DataFrames
# (5) Can join and merge different datasets together
# (6) It integrates with NumPy and Matplotlib

# For these and other reasons, Pandas DataFrames have become one of the most
# commonly used Pandas object for data analysis in Python.


# Creating Pandas Series

# A Pandas series is a one-dimensional array-like object that can hold many data
# types, such as numbers or strings. One of the main differences between Pandas
# Series and NumPy ndarrays is that you can assign an index label to each element
# in the Pandas Series. In other words, you can name the indices of your Pandas
# Series anything you want. Another big difference between Pandas Series and NumPy
# ndarrays is that Pandas Series can hold data of different data types.

# Let's start by importing Pandas into Python. It has become a convention to
# import Pandas as pd, therefore, you can import Pandas by typing the following
# command in your Jupyter notebook:

import pandas as pd

# Let's begin by creating a Pandas Series. You can create Pandas Series by using
# the command pd.Series(data, index), where index is a list of index labels. Let's
# use a Pandas Series to store a grocery list. We will use the food items as index
# labels and the quantity we need to buy of each item as our data.

# We import Pandas as pd into Python
import pandas as pd

# We create a Pandas Series that stores a grocery list
groceries = pd.Series(data = [30, 6, 'Yes', 'No'], index = ['eggs', 'apples', 'milk', 'bread'])

# We display the Groceries Pandas Series
# groceries
# eggs           30
# apples         6
# milk         Yes
# bread       No
# dtype: object

# We see that Pandas Series are displayed with the indices in the first column
# and the data in the second column. Notice that the data is not indexed 0 to 3
# but rather it is indexed with the names of the food we put in, namely eggs,
# apples, etc... Also notice that the data in our Pandas Series has both integers
# and strings.

# Just like NumPy ndarrays, Pandas Series have attributes that allows us to get
# information from the series in an easy way. Let's see some of them:

# We print some information about Groceries
print('Groceries has shape:', groceries.shape)
print('Groceries has dimension:', groceries.ndim)
print('Groceries has a total of', groceries.size, 'elements')
# Groceries has shape: (4,)
# Groceries has dimension: 1
# Groceries has a total of 4 elements

# We can also print the index labels and the data of the Pandas Series separately.
# This is useful if you don't happen to know what the index labels of the Pandas Series are.

# We print the index and data of Groceries
print('The data in Groceries is:', groceries.values)
print('The index of Groceries is:', groceries.index)
# The data in Groceries is: [30 6 'Yes' 'No']
# The index of Groceries is: Index(['eggs', 'apples', 'milk', 'bread'], dtype='object')

# If you are dealing with a very large Pandas Series and if you are not sure
# whether an index label exists, you can check by using the in command

# We check whether bananas is a food item (an index) in Groceries
x = 'bananas' in groceries

# We check whether bread is a food item (an index) in Groceries
y = 'bread' in groceries

# We print the results
print('Is bananas an index label in Groceries:', x)
print('Is bread an index label in Groceries:', y)
# Is bananas an index label in Groceries: False
# Is bread an index label in Groceries: True



# Accessing and Deleting Elements in Pandas Series

# Now let's look at how we can access or modify elements in a Pandas Series.
# One great advantage of Pandas Series is that it allows us to access data in
# many different ways. Elements can be accessed using index labels or numerical
# indices inside square brackets, [ ], similar to how we access elements in NumPy
# ndarrays. Since we can use numerical indices, we can use both positive and
# negative integers to access data from the beginning or from the end of the
# Series, respectively. Since we can access elements in various ways, in order
# to remove any ambiguity to whether we are referring to an index label or
# numerical index, Pandas Series have two attributes, .loc and .iloc to
# explicitly state what we mean. The attribute .loc stands for location and it
# is used to explicitly state that we are using a labeled index. Similarly, the
# attribute .iloc stands for integer location and it is used to explicitly state
# that we are using a numerical index. Let's see some examples:

# We access elements in Groceries using index labels:

# We use a single index label
print('How many eggs do we need to buy:', groceries['eggs'])
print()

# we can access multiple index labels
print('Do we need milk and bread:\n', groceries[['milk', 'bread']])
print()

# we use loc to access multiple index labels
print('How many eggs and apples do we need to buy:\n', groceries.loc[['eggs', 'apples']])
print()

# We access elements in Groceries using numerical indices:

# we use multiple numerical indices
print('How many eggs and apples do we need to buy:\n',  groceries[[0, 1]])
print()

# We use a negative numerical index
print('Do we need bread:\n', groceries[[-1]])
print()

# We use a single numerical index
print('How many eggs do we need to buy:', groceries[0])
print()
# we use iloc to access multiple numerical indices
print('Do we need milk and bread:\n', groceries.iloc[[2, 3]])
# How many eggs do we need to buy: 30

# Do we need milk and bread:
# milk       Yes
# bread     No
# dtype: object

# How many eggs and apples do we need to buy:
# eggs       30
# apples     6
# dtype: object

# How many eggs and apples do we need to buy:
# eggs       30
# apples     6
# dtype: object

# Do we need bread:
# bread     No
# dtype: object

# How many eggs do we need to buy: 30

# Do we need milk and bread:
# milk       Yes
# bread     No
# dtype: object

# Pandas Series are also mutable like NumPy ndarrays, which means we can change
# the elements of a Pandas Series after it has been created. For example, let's
# change the number of eggs we need to buy from our grocery list

# We display the original grocery list
print('Original Grocery List:\n', groceries)

# We change the number of eggs to 2
groceries['eggs'] = 2

# We display the changed grocery list
print()
print('Modified Grocery List:\n', groceries)
# Original Grocery List:
# eggs           30
# apples         6
# milk         Yes
# bread       No
# dtype: object

# Modified Grocery List:
# eggs             2
# apples         6
# milk         Yes
# bread       No
# dtype: object

# We can also delete items from a Pandas Series by using the .drop() method.
# The Series.drop(label) method removes the given label from the given Series.
# We should note that the Series.drop(label) method drops elements from the
# Series out of place, meaning that it doesn't change the original Series being
# modified. Let's see how this works:

# We display the original grocery list
print('Original Grocery List:\n', groceries)

# We remove apples from our grocery list. The drop function removes elements out of place
print()
print('We remove apples (out of place):\n', groceries.drop('apples'))

# When we remove elements out of place the original Series remains intact. To see this
# we display our grocery list again
print()
print('Grocery List after removing apples out of place:\n', groceries)
# Original Grocery List:
# eggs           30
# apples         6
# milk         Yes
# bread       No
# dtype: object

# We remove apples (out of place):
# eggs           30
# milk         Yes
# bread       No
# dtype: object

# Grocery List after removing apples out of place:
# eggs           30
# apples         6
# milk         Yes
# bread       No
# dtype: object

# We can delete items from a Pandas Series in place by setting the keyword
# inplace to True in the .drop() method. Let's see an example:

# We display the original grocery list
print('Original Grocery List:\n', groceries)

# We remove apples from our grocery list in place by setting the inplace keyword to True
groceries.drop('apples', inplace = True)

# When we remove elements in place the original Series its modified. To see this
# we display our grocery list again
print()
print('Grocery List after removing apples in place:\n', groceries)
# Original Grocery List:
# eggs           30
# apples         6
# milk         Yes
# bread       No
# dtype: object

# Grocery List after removing apples in place:
# eggs           30
# milk         Yes
# bread       No
# dtype: object




# Arithmetic Operations on Pandas Series

# Just like with NumPy ndarrays, we can perform element-wise arithmetic
# operations on Pandas Series. In this lesson we will look at arithmetic
# operations between Pandas Series and single numbers. Let's create a new
# Pandas Series that will hold a grocery list of just fruits.

# We create a Pandas Series that stores a grocery list of just fruits
fruits= pd.Series(data = [10, 6, 3,], index = ['apples', 'oranges', 'bananas'])

# We display the fruits Pandas Series
# fruits
# apples         10
# oranges        6
# bananas       3
# dtype: int64

# We can now modify the data in fruits by performing basic arithmetic operations.
# Let's see some examples

# We print fruits for reference
print('Original grocery list of fruits:\n ', fruits)

# We perform basic element-wise operations using arithmetic symbols
print()
print('fruits + 2:\n', fruits + 2) # We add 2 to each item in fruits
print()
print('fruits - 2:\n', fruits - 2) # We subtract 2 to each item in fruits
print()
print('fruits * 2:\n', fruits * 2) # We multiply each item in fruits by 2
print()
print('fruits / 2:\n', fruits / 2) # We divide each item in fruits by 2
print()
# Original grocery list of fruits:
# apples         10
# oranges        6
# bananas       3
# dtype: int64

# fruits + 2:
# apples         12
# oranges        8
# bananas       5
# dtype: int64

# fruits - 2:
# apples           8
# oranges        4
# bananas       1
# dtype: int64

# fruits * 2:
# apples         20
# oranges      12
# bananas       6
# dtype: int64

# fruits / 2:
# apples           5.0
# oranges        3.0
# bananas       1.5
# dtype: float64

# You can also apply mathematical functions from NumPy, such assqrt(x), to all
# elements of a Pandas Series.

# We import NumPy as np to be able to use the mathematical functions
import numpy as np

# We print fruits for reference
print('Original grocery list of fruits:\n', fruits)

# We apply different mathematical functions to all elements of fruits
print()
print('EXP(X) = \n', np.exp(fruits))
print()
print('SQRT(X) =\n', np.sqrt(fruits))
print()
print('POW(X,2) =\n',np.power(fruits,2)) # We raise all elements of fruits to the power of 2

# Original grocery list of fruits:
# apples         10
# oranges        6
# bananas       3
# dtype: int64

# EXP(X) =
# apples        22026.465795
# oranges         403.428793
# bananas          20.085537
# dtype: float64

# SQRT(X) =
# apples            3.162278
# oranges         2.449490
# bananas        1.732051
# dtype: float64

# POW(X,2) =
# apples         100
# oranges        36
# bananas         9
# dtype: int64

# Pandas also allows us to only apply arithmetic operations on selected items
# in our fruits grocery list. Let's see some examples

# We print fruits for reference
print('Original grocery list of fruits:\n ', fruits)
print()

# We add 2 only to the bananas
print('Amount of bananas + 2 = ', fruits['bananas'] + 2)
print()

# We subtract 2 from apples
print('Amount of apples - 2 = ', fruits.iloc[0] - 2)
print()

# We multiply apples and oranges by 2
print('We double the amount of apples and oranges:\n', fruits[['apples', 'oranges']] * 2)
print()

# We divide apples and oranges by 2
print('We half the amount of apples and oranges:\n', fruits.loc[['apples', 'oranges']] / 2)

# Original grocery list of fruits:
# apples         10
# oranges        6
# bananas       3
# dtype: int64

# Amount of bananas + 2 = 5

# Amount of apples - 2 = 8

# We double the amount of apples and oranges:
# apples         20
# oranges      12
# dtype: int64

# We half the amount of apples and oranges:
# apples         5.0
# oranges      3.0
# dtype: float64

# You can also apply arithmetic operations on Pandas Series of mixed data type
# provided that the arithmetic operation is defined for all data types in the
# Series, otherwise you will get an error. Let's see what happens when we multiply
# our grocery list by 2

# We multiply our grocery list by 2
groceries * 2

# eggs                 60
# apples             12
# milk         YesYes
# bread        NoNo
# dtype: object

# As we can see, in this case, since we multiplied by 2, Pandas doubles the
# data of each item including the strings. Pandas can do this because the
# multiplication operation * is defined both for numbers and strings. If you
# were to apply an operation that was valid for numbers but not strings, say
# for instance, / you will get an error. So when you have mixed data types in
# your Pandas Series make sure the arithmetic operations are valid on all the
# data types of your elements.




# Create a Pandas Series that contains the distance of some planets from the Sun.
# Use the name of the planets as the index to your Pandas Series, and the distance
# from the Sun as your data. The distance from the Sun is in units of 10^6 km

import pandas as pd
import numpy as np

distance_from_sun = [149.6, 1433.5, 227.9, 108.2, 778.6]

planets = ['Earth','Saturn', 'Mars','Venus', 'Jupiter']

# Create a Pandas Series using the above data, with the name of the planets as
# the index and the distance from the Sun as your data.
dist_planets = pd.Series(data = distance_from_sun, index = planets)

print("Planet Distance from Sun")
print(dist_planets)
print()

# Calculate the number of minutes it takes sunlight to reach each planet. You can
# do this by dividing the distance from the Sun for each planet by the speed of light.
# Since in the data above the distance from the Sun is in units of 10^6 km, you can
# use a value for the speed of light of c = 18, since light travels 18 x 10^6 km/minute.

speed_of_light = 18
time_light = dist_planets / speed_of_light
print("Number of Minutes of Sunlight to Planet")
print(time_light)
print()

# Use Boolean indexing to select only those planets for which sunlight takes less
# than 40 minutes to reach them.
close_planets = time_light[time_light < 40]
print("Planets Close to the Sun")
print(close_planets)



# Creating Pandas DataFrames

# Pandas DataFrames are two-dimensional data structures with labeled rows and
# columns, that can hold many data types. If you are familiar with Excel, you
# can think of Pandas DataFrames as being similar to a spreadsheet. We can create
# Pandas DataFrames manually or by loading data from a file. In these lessons we
# will start by learning how to create Pandas DataFrames manually from dictionaries
# and later we will see how we can load data into a DataFrame from a data file.

# We will start by creating a DataFrame manually from a dictionary of Pandas Series.
# In this case the first step is to create the dictionary of Pandas Series. After
# the dictionary is created we can then pass the dictionary to the pd.DataFrame()
# function.

# We will create a dictionary that contains items purchased by two people, Alice
# and Bob, on an online store. The Pandas Series will use the price of the items
# purchased as data, and the purchased items will be used as the index labels to
# the Pandas Series. Let's see how this done in code:

# We import Pandas as pd into Python
import pandas as pd

# We create a dictionary of Pandas Series
items = {'Bob' : pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch']),
         'Alice' : pd.Series(data = [40, 110, 500, 45], index = ['book', 'glasses', 'bike', 'pants'])}

# We print the type of items to see that it is a dictionary
print(type(items))
class 'dict'

# Now that we have a dictionary, we are ready to create a DataFrame by passing
# it to the pd.DataFrame() function. We will create a DataFrame that could
# represent the shopping carts of various users, in this case we have only two
# users, Alice and Bob.

# We create a Pandas DataFrame by passing it a dictionary of Pandas Series
shopping_carts = pd.DataFrame(items)

# We display the DataFrame
shopping_carts

#           |    Alice   |    Bob
# ----------|------------|-----------
# bike	    |    500.0	 |    245.0
# book	    |    40.0	 |    NaN
# glasses   |	 110.0	 |    NaN
# pants	    |    45.0	 |    25.0
# watch	    |    NaN	 |    55.0

# There are several things to notice here that are worth pointing out. We see
# that DataFrames are displayed in tabular form, much like an Excel spreadsheet,
# with the labels of rows and columns in bold. Also notice that the row labels of
# the DataFrame are built from the union of the index labels of the two Pandas
# Series we used to construct the dictionary. And the column labels of the
# DataFrame are taken from the keys of the dictionary. Another thing to notice
# is that the columns are arranged alphabetically and not in the order given in
# the dictionary. We will see later that this won't happen when we load data into
# a DataFrame from a data file. The last thing we want to point out is that we see
# some NaN values appear in the DataFrame. NaN stands for Not a Number, and is
# Pandas way of indicating that it doesn't have a value for that particular row
# and column index. For example, if we look at the column of Alice, we see that
# it has NaN in the watch index. You can see why this is the case by looking at
# the dictionary we created at the beginning. We clearly see that the dictionary
# has no item for Alice labeled watches. So whenever a DataFrame is created, if
# a particular column doesn't have values for a particular row index, Pandas will
# put a NaN value there. If we were to feed this data into a machine learning
# algorithm we will have to remove these NaN values first. In a later lesson we
# will learn how to deal with NaN values and clean our data. For now, we will
# leave these values in our DataFrame.

# In the above example we created a Pandas DataFrame from a dictionary of Pandas
# Series that had clearly defined indexes. If we don't provide index labels to the
# Pandas Series, Pandas will use numerical row indexes when it creates the DataFrame.
# Let's see an example:

# We create a dictionary of Pandas Series without indexes
data = {'Bob' : pd.Series([245, 25, 55]),
        'Alice' : pd.Series([40, 110, 500, 45])}

# We create a DataFrame
df = pd.DataFrame(data)

# We display the DataFrame
df

#           |    Alice   |    Bob
# ----------|------------|-----------
#  0	    |    40.0	 |    245.0
#  1        |	 110.0	 |    25.0
#  2  	    |    500.0	 |    55.0
#  3        |    45.0	 |    NaN

# We can see that Pandas indexes the rows of the DataFrame starting from 0, just
# like NumPy indexes ndarrays.


# Now, just like with Pandas Series we can also extract information from DataFrames
# using attributes. Let's print some information from our shopping_carts DataFrame

# We print some information about shopping_carts
print('shopping_carts has shape:', shopping_carts.shape)
print('shopping_carts has dimension:', shopping_carts.ndim)
print('shopping_carts has a total of:', shopping_carts.size, 'elements')
print()
print('The data in shopping_carts is:\n', shopping_carts.values)
print()
print('The row index in shopping_carts is:', shopping_carts.index)
print()
print('The column index in shopping_carts is:', shopping_carts.columns)

# shopping_carts has shape: (5, 2)
# shopping_carts has dimension: 2
# shopping_carts has a total of: 10 elements

# The data in shopping_carts is:
# [[    500.    245.]
# [       40.     nan]
# [     110.     nan]
# [       45.      25.]
# [     nan       55.]]

# The row index in shopping_carts is: Index(['bike', 'book', 'glasses', 'pants', 'watch'], dtype='object')

# The column index in shopping_carts is: Index(['Alice', 'Bob'], dtype='object')

# When creating the shopping_carts DataFrame we passed the entire dictionary to
# the pd.DataFrame() function. However, there might be cases when you are only
# interested in a subset of the data. Pandas allows us to select which data we
# want to put into our DataFrame by means of the keywords columns and index.
# Let's see some examples:

# We Create a DataFrame that only has Bob's data
bob_shopping_cart = pd.DataFrame(items, columns=['Bob'])

# We display bob_shopping_cart
bob_shopping_cart

#        |  Bob
# -------|------
# bike	 |  245
# pants	 |  25
# watch	 |  55

# We Create a DataFrame that only has selected items for both Alice and Bob
sel_shopping_cart = pd.DataFrame(items, index = ['pants', 'book'])

# We display sel_shopping_cart
sel_shopping_cart


#       | Alice	|   Bob
# ------|-------|-------
# pants	| 45    |	25.0
# book	| 40	|   NaN

# We Create a DataFrame that only has selected items for Alice
alice_sel_shopping_cart = pd.DataFrame(items, index = ['glasses', 'bike'], columns = ['Alice'])

# We display alice_sel_shopping_cart
alice_sel_shopping_cart

#         | Alice
# --------|-------
# glasses |	110
# bike	  | 500

# You can also manually create DataFrames from a dictionary of lists (arrays). The
# procedure is the same as before, we start by creating the dictionary and then
# passing the dictionary to the pd.DataFrame() function. In this case, however,
# all the lists (arrays) in the dictionary must be of the same length. Let' see an example:

# We create a dictionary of lists (arrays)
data = {'Integers' : [1,2,3],
        'Floats' : [4.5, 8.2, 9.6]}

# We create a DataFrame
df = pd.DataFrame(data)

# We display the DataFrame
df

#           |    Floats  |  Integers
# ----------|------------|-------------
#  0        |    4.5	 |   1
#  1        |    8.2	 |   2
#  2        |    9.6	 |   3


# Notice that since the data dictionary we created doesn't have label indices,
# Pandas automatically uses numerical row indexes when it creates the DataFrame.
# We can however, put labels to the row index by using the index keyword in the
# pd.DataFrame() function. Let's see an example

# We create a dictionary of lists (arrays)
data = {'Integers' : [1,2,3],
        'Floats' : [4.5, 8.2, 9.6]}

# We create a DataFrame and provide the row index
df = pd.DataFrame(data, index = ['label 1', 'label 2', 'label 3'])

# We display the DataFrame
df

#           |    Floats  |  Integers
# ----------|------------|-------------
#  label 1  |    4.5	 |   1
#  label 2  |    8.2	 |   2
#  label 3  |    9.6	 |   3

# The last method for manually creating Pandas DataFrames that we want to look at,
# is by using a list of Python dictionaries. The procedure is the same as before,
# we start by creating the dictionary and then passing the dictionary to the
# pd.DataFrame() function.

# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35},
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]

# We create a DataFrame
store_items = pd.DataFrame(items2)

# We display the DataFrame
store_items


#       | bikes	| glasses | pants  | watches |
# ------|-------|---------|--------|---------|
#  0    | 20    |	NaN   |   30   |  35     |
#  1    | 15	|   50.0  |   5    |  10     |

# Again, notice that since the items2 dictionary we created doesn't have label
# indices, Pandas automatically uses numerical row indexes when it creates the
# DataFrame. As before, we can put labels to the row index by using the index
# keyword in the pd.DataFrame() function. Let's assume we are going to use this
# DataFrame to hold the number of items a particular store has in stock. So, we
# will label the row indices as store 1 and store 2.

# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35},
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2'])

# We display the DataFrame
store_items

#         | bikes | glasses | pants  | watches |
# --------|-------|---------|--------|---------|
# store 1 | 20    |	NaN     |   30   |  35     |
# store 2 | 15	  | 50.0    |   5    |  10     |



# Accessing Elements in Pandas DataFrames

# We can access elements in Pandas DataFrames in many different ways. In general,
# we can access rows, columns, or individual elements of the DataFrame by using
# the row and column labels. We will use the same store_items DataFrame created
# in the previous lesson. Let's see some examples:

# We print the store_items DataFrame
print(store_items)

# We access rows, columns and elements using labels
print()
print('How many bikes are in each store:\n', store_items[['bikes']])
print()
print('How many bikes and pants are in each store:\n', store_items[['bikes', 'pants']])
print()
print('What items are in Store 1:\n', store_items.loc[['store 1']])
print()
print('How many bikes are in Store 2:', store_items['bikes']['store 2'])

#         | bikes | glasses | pants  | watches |
# --------|-------|---------|--------|---------|
# store 1 | 20    |	NaN     |   30   |  35     |
# store 2 | 15	  | 50.0    |   5    |  10     |

# How many bikes are in each store:

#         | bikes |
# --------|-------|
# store 1 | 20    |
# store 2 | 15	  |

# How many bikes and pants are in each store:

#         | bikes | pants  |
# --------|-------|--------|
# store 1 | 20    |   30   |
# store 2 | 15	  |   5    |

# What items are in Store 1:

#         | bikes | glasses | pants  | watches |
# --------|-------|---------|--------|---------|
# store 1 | 20    |	NaN     |   30   |  35     |

# How many bikes are in Store 2: 15

# It is important to know that when accessing individual elements in a DataFrame,
# as we did in the last example above, the labels should always be provided with
# the column label first, i.e. in the form dataframe[column][row]. For example,
# when retrieving the number bikes in store 2, we first used the column label
# bikes and then the row label store 2. If you provide the row label first you
# will get an error.

# We can also modify our DataFrames by adding rows or columns. Let's start by
# learning how to add new columns to our DataFrames. Let's suppose we decided to
# add shirts to the items we have in stock at each store. To do this, we will
# need to add a new column to our store_items DataFrame indicating how many
# shirts are in each store. Let's do that:

# We add a new column named shirts to our store_items DataFrame indicating the number of
# shirts in stock at each store. We will put 15 shirts in store 1 and 2 shirts in store 2
store_items['shirts'] = [15,2]

# We display the modified DataFrame
store_items

#         | bikes | glasses | pants  | watches | shirts |
# --------|-------|---------|--------|---------|--------|
# store 1 | 20    |	NaN     |   30   |  35     |  15    |
# store 2 | 15	  | 50.0    |   5    |  10     |  2     |

# We can see that when we add a new column, the new column is added at the end
# of our DataFrame.

# We can also add new columns to our DataFrame by using arithmetic operations
# between other columns in our DataFrame. Let's see an example:

# We make a new column called suits by adding the number of shirts and pants
store_items['suits'] = store_items['pants'] + store_items['shirts']

# We display the modified DataFrame
store_items

#         | bikes | glasses | pants  | watches | shirts | suits |
# --------|-------|---------|--------|---------|--------|-------|
# store 1 | 20    |	NaN     |   30   |  35     |  15    |  45   |
# store 2 | 15	  | 50.0    |   5    |  10     |  2     |  7    |

# Suppose now, that you opened a new store and you need to add the number of
# items in stock of that new store into your DataFrame. We can do this by adding
# a new row to the store_items Dataframe. To add rows to our DataFrame we
# first have to create a new Dataframe and then append it to the original
# DataFrame. Let's see how this works

# We create a dictionary from a list of Python dictionaries that will number of
# items at the new store
new_items = [{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4}]

# We create new DataFrame with the new_items and provide and index labeled store 3
new_store = pd.DataFrame(new_items, index = ['store 3'])

# We display the items at the new store
new_store


#         | bikes | glasses | pants  | watches |
# --------|-------|---------|--------|---------|
# store 3 | 20    |	NaN     |   30   |  35     |


# We now add this row to our store_items DataFrame by using the .append() method.

# We append store 3 to our store_items DataFrame
store_items = store_items.append(new_store)

# We display the modified DataFrame
store_items

#         | bikes | glasses | pants  | watches | shirts | suits |
# --------|-------|---------|--------|---------|--------|-------|
# store 1 | 20    |	NaN     |   30   |  35     |  15    |  45   |
# store 2 | 15	  | 50.0    |   5    |  10     |  2     |  7    |
# store 3 | 20	  | 4.0     |   30   |  NaN    |  NaN   |  35   |

# Notice that by appending a new row to the DataFrame, the columns have been
# put in alphabetical order.

# We can also add new columns of our DataFrame by using only data from particular
# rows in particular columns. For example, suppose that you want to stock stores
# 2 and 3 with new watches and you want the quantity of the new watches to be
# the same as the watches already in stock for those stores. Let's see how we
# can do this

# We add a new column using data from particular rows in the watches column
store_items['new watches'] = store_items['watches'][1:]

# We display the modified DataFrame
store_items

#         | bikes | glasses | pants  | shirts  | suits  | watches | new watches |
# --------|-------|---------|--------|---------|--------|---------|-------------|
# store 1 | 20    |	NaN     |   30   |  15.0   |  45    |  35     |   NaN       |
# store 2 | 15	  | 50.0    |   5    |  2.0    |  7.0   |  10     |   10.0      |
# store 3 | 20	  | 4.0     |   30   |  NaN    |  NaN   |  35     |   35.0      |


# It is also possible, to insert new columns into the DataFrames anywhere we want.
# The dataframe.insert(loc,label,data) method allows us to insert a new column
# in the dataframe at location loc, with the given column label, and given data.
# Let's add new column named shoes right before the suits column. Since suits has
# numerical index value 4 then we will use this value as loc. Let's see how this works:

# We insert a new column with label shoes right before the column with numerical index 4
store_items.insert(4, 'shoes', [8,5,0])

# we display the modified DataFrame

#         | bikes | glasses | pants  | shirts  | shoes  | suits   | watches  | new watches |
# --------|-------|---------|--------|---------|--------|---------|----------|-------------|
# store 1 | 20    |	NaN     |   30   |  15.0   |  8     |  45.0   |   35     |   NaN       |
# store 2 | 15	  | 50.0    |   5    |  2.0    |  5     |  7.0    |   10     |   10.0      |
# store 3 | 20	  | 4.0     |   30   |  NaN    |  0     |  NaN    |   35     |   35.0      |


# Just as we can add rows and columns we can also delete them. To delete rows
# and columns from our DataFrame we will use the .pop() and .drop() methods.
# The .pop() method only allows us to delete columns, while the .drop() method
# can be used to delete both rows and columns by use of the axis keyword. Let's
# see some examples

# We remove the new watches column
store_items.pop('new watches')

# we display the modified DataFrame
store_items

#         | bikes | glasses | pants  | shirts  | shoes  | suits   | watches  |
# --------|-------|---------|--------|---------|--------|---------|----------|
# store 1 | 20    |	NaN     |   30   |  15.0   |  8     |  45.0   |   35     |
# store 2 | 15	  | 50.0    |   5    |  2.0    |  5     |  7.0    |   10     |
# store 3 | 20	  | 4.0     |   30   |  NaN    |  0     |  NaN    |   35     |



# We remove the watches and shoes columns
store_items = store_items.drop(['watches', 'shoes'], axis = 1)

# we display the modified DataFrame
store_items

#         | bikes | glasses | pants  | shirts  | suits   |
# --------|-------|---------|--------|---------|---------|
# store 1 | 20    |	NaN     |   30   |  15.0   |  45.0   |
# store 2 | 15	  | 50.0    |   5    |  2.0    |  7.0    |
# store 3 | 20	  | 4.0     |   30   |  NaN    |  NaN    |

# We remove the store 2 and store 1 rows
store_items = store_items.drop(['store 2', 'store 1'], axis = 0)

# we display the modified DataFrame
store_items

#         | bikes | glasses | pants  | shirts  | suits   |
# --------|-------|---------|--------|---------|---------|
# store 3 | 20	  | 4.0     |   30   |  NaN    |  NaN    |

# Sometimes we might need to change the row and column labels. Let's change
# the bikes column label to hats using the .rename() method

# We change the column label bikes to hats
store_items = store_items.rename(columns = {'bikes': 'hats'})

# we display the modified DataFrame
store_items

#         | hats  | glasses | pants  | shirts  | suits   |
# --------|-------|---------|--------|---------|---------|
# store 3 | 20	  | 4.0     |   30   |  NaN    |  NaN    |

Now let's change the row label using the .rename() method again.

# We change the row label from store 3 to last store
store_items = store_items.rename(index = {'store 3': 'last store'})

# we display the modified DataFrame
store_items

#            | hats  | glasses | pants  | shirts  | suits   |
# -----------|-------|---------|--------|---------|---------|
# last store | 20	 | 4.0     |   30   |  NaN    |  NaN    |

You can also change the index to be one of the columns in the DataFrame.

# We change the row index to be the data in the pants column
store_items = store_items.set_index('pants')

# we display the modified DataFrame
store_items

#   | pants | hats    | glasses  | shirts  | suits   |
#   |-------|---------|----------|---------|---------|
#   | 30    | 20      |   4.0    |  NaN    |  NaN    |




# Dealing with NaN

# As mentioned earlier, before we can begin training our learning algorithms
# with large datasets, we usually need to clean the data first. This means we
# need to have a method for detecting and correcting errors in our data. While
# any given dataset can have many types of bad data, such as outliers or
# incorrect values, the type of bad data we encounter almost always is missing
# values. As we saw earlier, Pandas assigns NaN values to missing data. In this
# lesson we will learn how to detect and deal with NaN values.

# We will begin by creating a DataFrame with some NaN values in it.

# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
{'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2', 'store 3'])

# We display the DataFrame
store_items

#         | bikes | glasses | pants  | shirts  | shoes  | suits   | watches  |
# --------|-------|---------|--------|---------|--------|---------|----------|
# store 1 | 20    |	NaN     |   30   |  15.0   |  8     |  45.0   |   35     |
# store 2 | 15	  | 50.0    |   5    |  2.0    |  5     |  7.0    |   10     |
# store 3 | 20	  | 4.0     |   30   |  NaN    |  0     |  NaN    |   35     |


# We can clearly see that the DataFrame we created has 3 NaN values: one in
# store 1 and two in store 3. However, in cases where we load very large
# datasets into a DataFrame, possibly with millions of items, the number of
# NaN values is not easily visualized. For these cases, we can use a combination
# of methods to count the number of NaN values in our data. The following
# example combines the .isnull() and the sum() methods to count the number of
# NaN values in our DataFrame

# We count the number of NaN values in store_items
x =  store_items.isnull().sum().sum()

# We print x
print('Number of NaN values in our DataFrame:', x)
# Number of NaN values in our DataFrame: 3

# In the above example, the .isnull() method returns a Boolean DataFrame of the
# same size as store_items and indicates with True the elements that have NaN
# values and with False the elements that are not. Let's see an example:

store_items.isnull()

#             bikes	| glasses |	pants |	shirts	| shoes | suits	| watches
# ------------------|---------|-------|---------|-------|-------|---------
# store 1	  False	| True	  | False |	False	| False	| False	| False
# store 2	  False	| False	  | False |	False	| False	| False	| False
# store 3	  False	| False	  | False |	True	| False	| True	| False

# In Pandas, logical True values have numerical value 1 and logical False
# values have numerical value 0. Therefore, we can count the number of NaN
# values by counting the number of logical True values. In order to count the
# total number of logical True values we use the .sum() method twice. We have
# to use it twice because the first sum returns a Pandas Series with the sums
# of logical True values along columns, as we see below:

store_items.isnull().sum()

# bikes        0
# glasses      1
# pants        0
# shirts       1
# shoes        0
# suits        1
# watches      0
# dtype: int64

# The second sum will then add up the 1s in the above Pandas Series.

# Instead of counting the number of NaN values we can also do the opposite, we
# can count the number of non-NaN values. We can do this by using the .count()
# method as shown below:

# We print the number of non-NaN values in our DataFrame
print()
print('Number of non-NaN values in the columns of our DataFrame:\n', store_items.count())

# Number of non-NaN values in the columns of our DataFrame:
# bikes          3
# glasses        2
# pants          3
# shirts         2
# shoes          3
# suits          2
# watches        3
# dtype: int64

# Now that we learned how to know if our dataset has any NaN values in it, the
# next step is to decide what to do with them. In general we have two options,
# we can either delete or replace the NaN values. In the following examples we
# will show you how to do both.

# We will start by learning how to eliminate rows or columns from our DataFrame
# that contain any NaN values. The .dropna(axis) method eliminates any rows with
# NaN values when axis = 0 is used and will eliminate any columns with NaN values
# when axis = 1 is used. Let's see some examples

# We drop any rows with NaN values
store_items.dropna(axis = 0)

#         | bikes | glasses | pants  | shirts  | shoes  | suits   | watches  |
# --------|-------|---------|--------|---------|--------|---------|----------|
# store 2 | 15	  | 50.0    |   5    |  2.0    |  5     |  7.0    |   10     |


# We drop any columns with NaN values
store_items.dropna(axis = 1)

#         | bikes | pants  | shoes  | watches  |
# --------|-------|--------|--------|----------|
# store 1 | 20    |	  30   |  8     |   35     |
# store 2 | 15	  |   5    |  5     |   10     |
# store 3 | 20	  |   30   |  0     |   35     |

# Notice that the .dropna() method eliminates (drops) the rows or columns with
# NaN values out of place. This means that the original DataFrame is not modified.
# You can always remove the desired rows or columns in place by setting the keyword
# inplace = True inside the dropna() function.

# Now, instead of eliminating NaN values, we can replace them with suitable values.
# We could choose for example to replace all NaN values with the value 0. We can do
# this by using the .fillna() method as shown below.

# We replace all NaN values with 0
store_items.fillna(0)

#         | bikes | glasses | pants  | shirts  | shoes  | suits   | watches  |
# --------|-------|---------|--------|---------|--------|---------|----------|
# store 1 | 20    |	0.0     |   30   |  15.0   |  8     |  45.0   |   35     |
# store 2 | 15	  | 50.0    |   5    |  2.0    |  5     |  7.0    |   10     |
# store 3 | 20	  | 4.0     |   30   |  0.0    |  10    |  0.0    |   35     |

# We can also use the .fillna() method to replace NaN values with previous values
# in the DataFrame, this is known as forward filling. When replacing NaN values
# with forward filling, we can use previous values taken from columns or rows.
# The .fillna(method = 'ffill', axis) will use the forward filling (ffill) method
# to replace NaN values using the previous known value along the given axis. Let's
# see some examples:

# We replace NaN values with the previous value in the column
store_items.fillna(method = 'ffill', axis = 0)

#         | bikes | glasses | pants  | shirts  | shoes  | suits   | watches  |
# --------|-------|---------|--------|---------|--------|---------|----------|
# store 1 | 20    |	0.0     |   30   |  15.0   |  8     |  45.0   |   35     |
# store 2 | 15	  | 50.0    |   5    |  2.0    |  5     |  7.0    |   10     |
# store 3 | 20	  | 4.0     |   30   |  NaN    |  10    |  NaN    |   35     |

# Notice that the two NaN values in store 3 have been replaced with previous
# values in their columns. However, notice that the NaN value in store 1 didn't
# get replaced. That's because there are no previous values in this column, since
# the NaN value is the first value in that column. However, if we do forward fill
# using the previous row values, this won't happen. Let's take a look:

# We replace NaN values with the previous value in the row
store_items.fillna(method = 'ffill', axis = 1)

#         | bikes | glasses | pants    | shirts  | shoes    | suits   | watches  |
# --------|-------|---------|----------|---------|----------|---------|----------|
# store 1 | 20.0  |	20.0    |   30.0   |  15.0   |  8.0     |  45.0   |   35.0   |
# store 2 | 15.0  | 50.0    |   5.0    |  2.0    |  5.0     |  7.0    |   10.0   |
# store 3 | 20.0  | 4.0     |   30.0   |  30.0   |  10.0    |  7.0    |   35.0   |

# We see that in this case all the NaN values have been replaced with the previous row values.

# Similarly, you can choose to replace the NaN values with the values that go
# after them in the DataFrame, this is known as backward filling. The
# .fillna(method = 'backfill', axis) will use the backward filling (backfill)
# method to replace NaN values using the next known value along the given axis.
# Just like with forward filling we can choose to use row or column values. Let's
# see some examples:

# We replace NaN values with the next value in the column
store_items.fillna(method = 'backfill', axis = 0)


#         | bikes | glasses | pants  | shirts  | shoes  | suits   | watches  |
# --------|-------|---------|--------|---------|--------|---------|----------|
# store 1 | 20    |	50.0    |   30   |  15.0   |  8     |  45.0   |   35     |
# store 2 | 15	  | 50.0    |   5    |  2.0    |  5     |  7.0    |   10     |
# store 3 | 20	  | 4.0     |   30   |  NaN    |  10    |  NaN    |   35     |


# Notice that the NaN value in store 1 has been replaced with the next value in
# its column. However, notice that the two NaN values in store 3 didn't get replaced.
# That's because there are no next values in these columns, since these NaN values are
# the last values in those columns. However, if we do backward fill using the next
# row values, this won't happen. Let's take a look:

# We replace NaN values with the next value in the row
store_items.fillna(method = 'backfill', axis = 1)

#         | bikes | glasses | pants  | shirts  | shoes  | suits   | watches  |
# --------|-------|---------|--------|---------|--------|---------|----------|
# store 1 | 20.0  |	50.0    |   30.0 |  15.0   |  8.0   |  45.0   |   35.0   |
# store 2 | 15.0  | 50.0    |   5.0  |  2.0    |  5.0   |  7.0    |   10.0   |
# store 3 | 20.0  | 4.0     |   30.0 |  10.0   |  10.0  |  35.0   |   35.0   |

# Notice that the .fillna() method replaces (fills) the NaN values out of place.
# This means that the original DataFrame is not modified. You can always replace
# the NaN values in place by setting the keyword inplace = True inside the fillna() function.

# We can also choose to replace NaN values by using different interpolation methods.
# For example, the .interpolate(method = 'linear', axis) method will use linear
# interpolation to replace NaN values using the values along the given axis. Let's
# see some examples:

# We replace NaN values by using linear interpolation using column values
store_items.interpolate(method = 'linear', axis = 0)

#         | bikes | glasses | pants  | shirts  | shoes  | suits   | watches  |
# --------|-------|---------|--------|---------|--------|---------|----------|
# store 1 | 20    |	NaN     |   30   |  15.0   |  8     |  45.0   |   35     |
# store 2 | 15	  | 50.0    |   5    |  2.0    |  5     |  7.0    |   10     |
# store 3 | 20	  | 4.0     |   30   |  2.0    |  10    |  7.0    |   35     |


# Notice that the two NaN values in store 3 have been replaced with linear
# interpolated values. However, notice that the NaN value in store 1 didn't get
# replaced. That's because the NaN value is the first value in that column, and
# since there is no data before it, the interpolation function can't calculate
# a value. Now, let's interpolate using row values instead:

# We replace NaN values by using linear interpolation using row values

store_items.interpolate(method = 'linear', axis = 1)

#         | bikes | glasses | pants  | shirts  | shoes  | suits   | watches  |
# --------|-------|---------|--------|---------|--------|---------|----------|
# store 1 | 20.0  |	25.0    |   30.0 |  15.0   |  8.0   |  45.0   |   35.0   |
# store 2 | 15.0  | 50.0    |   5.0  |  2.0    |  5.0   |  7.0    |   10.0   |
# store 3 | 20.0  | 4.0     |   30.0 |  20.0   |  10.0  |  22.5   |   35.0   |


# Just as with the other methods we saw, the .interpolate() method replaces NaN
# values out of place.

import pandas as pd
import numpy as np

# Since we will be working with ratings, we will set the precision of our
# dataframes to one decimal place.
pd.set_option('precision', 1)

# Create a Pandas DataFrame that contains the ratings some users have given to a
# series of books. The ratings given are in the range from 1 to 5, with 5 being
# the best score. The names of the books, the authors, and the ratings of each user
# are given below:

books = pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
authors = pd.Series(data = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])

user_1 = pd.Series(data = [3.2, np.nan ,2.5])
user_2 = pd.Series(data = [5., 1.3, 4.0, 3.8])
user_3 = pd.Series(data = [2.0, 2.3, np.nan, 4])
user_4 = pd.Series(data = [4, 3.5, 4, 5, 4.2])

# Users that have np.nan values means that the user has not yet rated that book.
# Use the data above to create a Pandas DataFrame that has the following column
# labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3', 'User 4'. Let Pandas
# automatically assign numerical row indices to the DataFrame.

# Create a dictionary with the data given above
dat = {'Book Title' : books,
       'Author' : authors,
       'User 1' : user_1,
       'User 2' : user_2,
       'User 3' : user_3,
       'User 4' : user_4}

# Use the dictionary to create a Pandas DataFrame
book_ratings = pd.DataFrame(dat)

# If you created the dictionary correctly you should have a Pandas DataFrame
# that has column labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3',
# 'User 4' and row indices 0 through 4.

print(book_ratings)
print()

# Now replace all the NaN values in your DataFrame with the average rating in
# each column. Replace the NaN values in place. HINT: you can use the fillna()
# function with the keyword inplace = True, to do this. Write your code below:

book_ratings.fillna(book_ratings.mean(), inplace = True)
print(book_ratings)
print()

# From the DataFrame above you can now pick all the books that had a rating of 5.
# You can do this in just one line of code. Try to do it yourself first, you'll
# find the answer below:

best_rated = book_ratings[(book_ratings == 5).any(axis = 1)]['Book Title'].values

# The code above returns a NumPy ndarray that only contains the names of the books
# that had a rating of 5.

print(best_rated)



# Loading Data into a Pandas DataFrame

# In machine learning you will most likely use databases from many sources to
# train your learning algorithms. Pandas allows us to load databases of different
# formats into DataFrames. One of the most popular data formats used to store
# databases is csv. CSV stands for Comma Separated Values and offers a simple
# format to store data. We can load CSV files into Pandas DataFrames using the
# pd.read_csv() function. Let's load Google stock data into a Pandas DataFrame.
# The GOOG.csv file contains Google stock data from 8/19/2004 till 10/13/2017
# taken from Yahoo Finance.

# We load Google stock data in a DataFrame
Google_stock = pd.read_csv('./GOOG.csv')

# We print some information about Google_stock
print('Google_stock is of type:', type(Google_stock))
print('Google_stock has shape:', Google_stock.shape)

# Google_stock is of type: class 'pandas.core.frame.DataFrame'
# Google_stock has shape: (3313, 7)

# We see that we have loaded the GOOG.csv file into a Pandas DataFrame and it
# consists of 3,313 rows and 7 columns. Now let's look at the stock data

Google_stock

#      | Dat        | Open	    |   High	 |    Low	  |    Close   |	Adj Close |	Volume
# -----|------------|-----------|------------|------------|------------|--------------|----------
#  0   | 2004-08-19	| 49.676899	| 51.693783	 | 47.669952  |	49.845802  | 49.845802    |	44994500
#  1   | 2004-08-20	| 50.178635	| 54.187561	 | 49.925285  |	53.805050  | 53.805050    |	23005800
#  2   | 2004-08-23	| 55.017166	| 56.373344	 | 54.172661  |	54.346527  | 54.346527    |	18393200
# ... ...
# 3311 | 2017-10-12	|987.450012 | 994.119995 | 985.000000 | 987.830017 | 987.830017	  | 1262400
# 3312 | 2017-10-13	|992.000000	| 997.210022 | 989.000000 |	989.679993 | 989.679993	  | 1157700
#
# 3313 rows × 7 columns

# We see that it is quite a large dataset and that Pandas has automatically assigned
# numerical row indices to the DataFrame. Pandas also used the labels that appear in
# the data in the CSV file to assign the column labels.

# When dealing with large datasets like this one, it is often useful just to take
# a look at the first few rows of data instead of the whole dataset. We can take a
# look at the first 5 rows of data using the .head() method, as shown below

Google_stock.head()

#   |     Date  | Open     |   	High	|    Low    | Close     | Adj Close	| Volume
# --|-----------|----------|------------|-----------|-----------|-----------|--------
# 0	|2004-08-19	|49.676899 |51.693783	|47.669952	|49.845802	|49.845802	|44994500
# 1	|2004-08-20	|50.178635 |54.187561	|49.925285	|53.805050	|53.805050	|23005800
# 2	|2004-08-23	|55.017166 |56.373344	|54.172661	|54.346527	|54.346527	|18393200
# 3	|2004-08-24	|55.260582 |55.439419	|51.450363	|52.096165	|52.096165	|15361800
# 4	|2004-08-25	|52.140873 |53.651051	|51.604362	|52.657513	|52.657513	|9257400

# We can also take a look at the last 5 rows of data by using the .tail() method:

Google_stock.tail()

#       | Date	    | Open      |	High	| Low       |	Close	|Adj Close	|Volume
#  3308	|2017-10-09	|980.000000	|985.424988	|976.109985	|977.000000	|977.000000	|891400
#  3309	|2017-10-10	|980.000000	|981.570007	|966.080017	|972.599976	|972.599976	|968400
#  3310	|2017-10-11	|973.719971	|990.710022	|972.250000	|989.250000	|989.250000	|1693300
#  3311	|2017-10-12	|987.450012	|994.119995	|985.000000	|987.830017	|987.830017	|1262400
#  3312	|2017-10-13	|992.000000	|997.210022	|989.000000	|989.679993	|989.679993	|1157700

# We can also optionally use .head(N) or .tail(N) to display the first and last N rows of
# data, respectively.

# Let's do a quick check to see whether we have any NaN values in our dataset. To do
# this, we will use the .isnull() method followed by the .any() method to check whether
# any of the columns contain NaN values.

Google_stock.isnull().any()

# Date           False
# Open           False
# High           False
# Low            False
# Close          False
# Adj Close      False
# Volume         False
# dtype: bool

# We see that we have no NaN values.

# When dealing with large datasets, it is often useful to get statistical information
# from them. Pandas provides the .describe() method to get descriptive statistics on
# each column of the DataFrame. Let's see how this works:

# We get descriptive statistics on our stock data
Google_stock.describe()

#         | Open        | High	        | Low	    | Close        |Adj Close	\  Volume
#  -------|-------------|---------------|-----------|--------------|------------|------------
#  count  |3313.000000	|3313.000000	3313.000000	|3313.000000   |3313.000000	|3.313000e+03
#  mean	  |380.186092	|383.493740	    376.519309	|380.072458	   |380.072458	|8.038476e+06
#  std	  |223.818650	|224.974534	    222.473232	|223.853780	   |223.853780	|8.399521e+06
#  min	  |49.274517	|50.541279	    47.669952	|49.681866	   |49.681866	|7.900000e+03
#  25%	  |226.556473	|228.394516	    224.003082	|226.407440	   |226.407440	|2.584900e+06
#  50%	  |293.312286	|295.433502	    289.929291	|293.029114	   |293.029114	|5.281300e+06
#  75%	  |536.650024	|540.000000	    532.409973	|536.690002	   |536.690002	|1.065370e+07
#  max	  |992.000000	|997.210022	    989.000000	|989.679993	   |989.679993	|8.276810e+07

# If desired, we can apply the .describe() method on a single column as shown below:

# We get descriptive statistics on a single column of our DataFrame
Google_stock['Adj Close'].describe()

# count         3313.000000
# mean          380.072458
# std           223.853780
# min           49.681866
# 25%           226.407440
# 50%           293.029114
# 75%           536.690002
# max           989.679993
# Name: Adj Close, dtype: float64

# Similarly, you can also look at one statistic by using one of the many
# statistical functions Pandas provides. Let's look at some examples:

# We print information about our DataFrame
print()
print('Maximum values of each column:\n', Google_stock.max())
print()
print('Minimum Close value:', Google_stock['Close'].min())
print()
print('Average value of each column:\n', Google_stock.mean())

# Maximum values of each column:
# Date          2017-10-13
# Open          992
# High          997.21
# Low           989
# Close         989.68
# Adj Close     989.68
# Volume        82768100
# dtype: object

# Minimum Close value: 49.681866

# Average value of each column:
# Open          3.801861e+02
# High          3.834937e+02
# Low           3.765193e+02
# Close         3.800725e+02
# Adj Close     3.800725e+02
# Volume        8.038476e+06
# dtype: float64

# Another important statistical measure is data correlation. Data correlation
# can tell us, for example, if the data in different columns are correlated. We
# can use the .corr() method to get the correlation between different columns, as shown below:

# We display the correlation between columns
Google_stock.corr()

#            | Open	    | High	    |   Low	     |   Close	  | Adj Close | Volume
# -----------|----------|-----------|------------|------------|-----------|-----------
#  Open	     | 1.000000	| 0.999904	|  0.999845	 |  0.999745  |	0.999745  |	-0.564258
#  High	     | 0.999904	| 1.000000	|  0.999834	 |  0.999868  |	0.999868  |	-0.562749
#  Low       | 0.999845	| 0.999834	|  1.000000	 |  0.999899  |	0.999899  |	-0.567007
#  Close     | 0.999745	| 0.999868	|  0.999899	 |  1.000000  |	1.000000  |	-0.564967
#  Adj Close | 0.999745	| 0.999868	|  0.999899	 |  1.000000  |	1.000000  |	-0.564967
#  Volume    |-0.564258 |-0.562749  | -0.567007  | -0.564967  |-0.564967  |	 1.000000

# A correlation value of 1 tells us there is a high correlation and a correlation
# of 0 tells us that the data is not correlated at all.

# We will end this Introduction to Pandas by taking a look at the .groupby() method.
# The .groupby() method allows us to group data in different ways. Let's see how we
# can group data to get different types of information. For the next examples we
# are going to load fake data about a fictitious company.

# We load fake Company data in a DataFrame
data = pd.read_csv('./fake_company.csv')
data

#       |Year	|Name	 |Department   |Age	  |Salary
#  -----|-------|--------|-------------|------|-------
#  0	|1990	|Alice	 |  HR	       |  25  |	50000
#  1	|1990	|Bob	 |  RD	       |  30  |	48000
#  2	|1990	|Charlie |	Admin	   |  45  |	55000
#  3	|1991	|Alice	 |  HR	       |  26  |	52000
#  4	|1991	|Bob	 |  RD	       |  31  |	50000
#  5	|1991	|Charlie |	Admin	   |  46  |	60000
#  6	|1992	|Alice	 |  Admin	   |  27  |	60000
#  7	|1992	|Bob	 |  RD	       |  32  |	52000
#  8	|1992	|Charlie |	Admin	   |  28  |	62000

# We see that the data contains information for the year 1990 through 1992.
# For each year we see name of the employees, the department they work for,
# their age, and their annual salary. Now, let's use the .groupby() method to get
# information.

# Let's calculate how much money the company spent in salaries each year. To do
# this, we will group the data by Year using the .groupby() method and then we
# will add up the salaries of all the employees by using the .sum() method.

# We display the total amount of money spent in salaries each year
data.groupby(['Year'])['Salary'].sum()

# Year
# 1990     153000
# 1991     162000
# 1992     174000
# Name: Salary, dtype: int64

# We see that the company spent a total of 153,000 dollars in 1990, 162,000
# in 1991, and 174,000 in 1992.

# Now, let's suppose I want to know what was the average salary for each year.
# In this case, we will group the data by Year using the .groupby() method, just
# as we did before, and then we use the .mean() method to get the average salary.
# Let's see how this works

# We display the average salary per year
data.groupby(['Year'])['Salary'].mean()

# Year
# 1990     51000
# 1991     54000
# 1992     58000
# Name: Salary, dtype: int64

# We see that the average salary in 1990 was 51,000 dollars, 54,000 in 1991,
# and 58,000 in 1992.

# Now let's see how much did each employee get paid in those three years. In this
# case, we will group the data by Name using the .groupby() method and then we will
# add up the salaries for each year. Let's see the result

# We display the total salary each employee received in all the years they worked for the company

data.groupby(['Name'])['Salary'].sum()

#  Name
#  Alice       162000
#  Bob         150000
#  Charlie     177000
#  Name: Salary, dtype: int64

# We see that Alice received a total of 162,000 dollars in the three years she
# worked for the company, Bob received 150,000, and Charlie received 177,000.

# Now let's see what was the salary distribution per department per year. In this
# case we will group the data by Year and by Department using the .groupby()
# method and then we will add up the salaries for each department. Let's see the result

# We display the salary distribution per department per year.
data.groupby(['Year', 'Department'])['Salary'].sum()

# Year     Department
# 1990     Admin         55000
#          HR            50000
#          RD            48000
# 1991     Admin         60000
#          HR            52000
#          RD            50000
# 1992     Admin        122000
#          RD            52000
# Name: Salary, dtype: int64

# We see that in 1990 the Admin department paid 55,000 dollars in salaries,the
# HR department paid 50,000, and the RD department 48,0000. While in 1992 the Admin
# department paid 122,000 dollars in salaries and the RD department paid 52,000.

# Supporting Materials
#  GOOG.csv
#  https://s3.amazonaws.com/video.udacity-data.com/topher/2018/May/5b08e099_goog-1/goog-1.csv
