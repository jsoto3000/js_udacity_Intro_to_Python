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
