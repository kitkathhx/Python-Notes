# Topic: if-else with logical operators | Level: Hard
# The login works only if the username AND password are correct AND the account is not locked.

username = "admin"
password = "python123"
account_locked = False

if username == "admin" and password == "python123" and not account_locked:
    print("Login successful. Welcome, admin!")
else:
    print("Login failed.")
    if account_locked:
        print("Reason: your account is locked.")

