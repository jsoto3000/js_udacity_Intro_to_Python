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
