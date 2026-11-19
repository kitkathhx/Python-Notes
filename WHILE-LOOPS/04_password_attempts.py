# Topic: while loop | Level: Intermediate
# The user gets 3 tries. The loop stops when the password is correct or the tries run out.
# (The typed passwords are simulated here. In a real program, use: guess = input("Password: "))

correct_password = "python123"
attempts = 0
max_attempts = 3
granted = False

while attempts < max_attempts and not granted:
    attempts = attempts + 1
    guess = "abc"
    if attempts == 3:
        guess = "python123"
    print("Attempt", attempts, "- you typed:", guess)
    if guess == correct_password:
        print("Access granted.")
        granted = True
    else:
        print("Wrong password.")

if not granted:
    print("Account locked.")

# Output:
# Attempt 1 - you typed: abc
# Wrong password.
# Attempt 2 - you typed: abc
# Wrong password.
# Attempt 3 - you typed: python123
# Access granted.