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
