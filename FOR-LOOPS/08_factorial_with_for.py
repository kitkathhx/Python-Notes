# Topic: for loop | Level: Hard
# Factorial: n! = 1 x 2 x 3 x ... x n. Shows every step of the multiplication.

n = 6
factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i
    print("Step", i, "- factorial is", factorial)

print(n, "! =", factorial)

# Output: ends with: 6 ! = 720