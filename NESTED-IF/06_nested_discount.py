# Topic: Nested if | Level: Intermediate
# The discount rate depends on membership and on how much was bought.

is_member = True
total = 2500

if is_member:
    if total >= 2000:
        rate = 0.20
    else:
        rate = 0.10
else:
    if total >= 2000:
        rate = 0.05
    else:
        rate = 0

discount = total * rate
print("Discount rate:", rate * 100, "%")
print("You pay:", total - discount)

# Output:
# Discount rate: 20.0 %
# You pay: 2000.0