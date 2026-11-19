# Topic: if-elif-else | Level: Easy
# Combines conditions with the or operator.

day = "Friday"

if day == "Saturday" or day == "Sunday":
    print("It is the weekend!")
elif day == "Friday":
    print("Almost the weekend!")
else:
    print("It is a weekday.")

# Output: Almost the weekend!