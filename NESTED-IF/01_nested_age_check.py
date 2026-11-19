# Topic: Nested if | Level: Easy
# Sorts a person into an age group using an if inside an if.

age = 25

if age >= 18:
    if age >= 60:
        print("Senior adult")
    else:
        print("Adult")
else:
    print("Minor")

# Output: Adult