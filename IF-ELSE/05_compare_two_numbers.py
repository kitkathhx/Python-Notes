# Topic: if-else | Level: Intermediate
# Finds the larger of two numbers and how far apart they are.

a = 45
b = 28

if a > b:
    larger = a
    smaller = b
else:
    larger = b
    smaller = a

print("Larger number:", larger)
print("Difference:", larger - smaller)

# Output:
# Larger number: 45
# Difference: 17