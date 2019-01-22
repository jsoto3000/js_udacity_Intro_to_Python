cities = [
"new york city",
"mountain view",
"chicago",
"los angeles"
]

# capitalized_cities = []
# for city in cities: 
#    capitalized_cities.append(city.title())

# print(capitalized_cities)


# reduces to

capitalized_cities = [city.title() for city in cities]

print(capitalized_cities)
