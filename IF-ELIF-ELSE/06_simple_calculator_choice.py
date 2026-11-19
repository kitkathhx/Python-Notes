# Topic: if-elif-else | Level: Intermediate
# Picks the operation from a symbol and protects against dividing by zero.

a = 20
b = 0
operator = "/"

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b == 0:
        print("Error: cannot divide by zero.")
    else:
        print(a / b)
else:
    print("Unknown operator")

# Output: Error: cannot divide by zero.