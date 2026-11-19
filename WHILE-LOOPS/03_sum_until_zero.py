# Topic: while loop | Level: Easy
# Adds numbers to a running total, counting down until the number reaches zero.

number = 5
total = 0

while number != 0:
    total = total + number
    print("Added", number, "- total is now", total)
    number = number - 1

print("Final total:", total)

# Output: ends with: Final total: 15