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