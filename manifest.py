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
