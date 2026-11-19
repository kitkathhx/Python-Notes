# Topic: Nested if | Level: Easy
# First check if the number is positive, then check if it is even or odd.

number = 15

if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Zero or negative number")

# Output: Positive odd number