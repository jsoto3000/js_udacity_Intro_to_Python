given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length =  len(given_name) + len(middle_names) + len(family_name) + 2 #todo: calculate how long this name is
print(name_length)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)