# list of squares

# squares = []

# for x in range(9):
#    squares.append(x**2)
# print(squares)

squares_if = [x**2 for x in range(9) if x % 2 == 0]
print(squares_if)


squares_ifelse = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares_ifelse)
