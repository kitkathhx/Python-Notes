# Topic: Nested if | Level: Hard
# Free shipping above the minimum. Otherwise the fee depends on region, weight, and express.

order_total = 900
region = "provincial"
weight = 4
express = True

if order_total >= 2000:
    fee = 0
else:
    if region == "metro":
        if weight <= 2:
            fee = 80
        else:
            fee = 120
    else:
        if weight <= 2:
            fee = 150
        else:
            fee = 220
    if express:
        fee = fee + 100

print("Shipping fee: PHP", fee)

# Output: Shipping fee: PHP 320