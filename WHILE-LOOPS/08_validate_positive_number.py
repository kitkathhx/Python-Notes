# Topic: while loop | Level: Hard
# Keeps asking until a positive number is entered (input validation).
# (The entries are simulated here. In a real program, use: number = int(input("Enter a positive number: ")))

number = -10

while number <= 0:
    print("You entered", number, "- invalid. The number must be positive.")
    number = number + 6

print("Accepted:", number)

# Output:
# You entered -10 - invalid. The number must be positive.
# You entered -4 - invalid. The number must be positive.
# Accepted: 2