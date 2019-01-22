manifest = [("bananas", 15),
("mattresses", 34),
("dog kennels", 42),
("machine", 120),
("cheeses", 5)]

items, weights = zip(*manifest)

print(items)
print(weights)
