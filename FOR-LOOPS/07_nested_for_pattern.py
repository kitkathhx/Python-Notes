# Topic: for loop | Level: Hard
# Nested loops: the outer loop controls the rows, the inner loop controls the stars.

rows = 5

print("Right triangle:")
for row in range(1, rows + 1):
    for star in range(row):
        print("*", end="")
    print()

print()
print("Number pyramid:")
for row in range(1, rows + 1):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()

# Output: a triangle of stars, then a triangle of numbers