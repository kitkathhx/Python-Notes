# Topic: Nested if | Level: Easy
# Passing grades get an extra check for honors. Failing grades get a second chance check.

grade = 88

if grade >= 75:
    if grade >= 90:
        print("Passed with honors")
    else:
        print("Passed")
else:
    if grade >= 70:
        print("Take the removal exam")
    else:
        print("Failed")

# Output: Passed