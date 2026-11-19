# Topic: if-elif-else | Level: Intermediate
# Finds the largest of three numbers using the and operator.

a = 12
b = 47
c = 30

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("The largest number is", largest)

# Output: The largest number is 47