# Quiz: Modify Usernames with Range
# Write a for loop that uses range() to iterate over the positions in usernames to 
# modify the list. Like you did in the previous quiz, change each name to be lowercase 
# and replace spaces with underscores. After running your loop, this list

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")

print(usernames)
