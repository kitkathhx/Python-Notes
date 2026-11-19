# Topic: while loop | Level: Intermediate
# Prints the even numbers from 2 to 20 and counts how many there are.

number = 2
count = 0

while number <= 20:
    print(number, end=" ")
    count = count + 1
    number = number + 2

print()
print("Total even numbers:", count)

# Output:
# 2 4 6 8 10 12 14 16 18 20
# Total even numbers: 10