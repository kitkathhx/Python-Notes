# Topic: Nested if | Level: Intermediate
# The password is checked only if the username exists. Wrong tries are counted.

username = "student01"
password = "py2026"
attempts = 2

if attempts < 3:
    if username == "student01":
        if password == "py2026":
            print("Login successful.")
        else:
            print("Wrong password. Attempts left:", 3 - attempts)
    else:
        print("Username not found.")
else:
    print("Account locked. Too many attempts.")

# Output: Login successful.