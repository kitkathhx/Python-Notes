# Topic: if-elif-else | Level: Hard
# The fee depends on the order total, the destination, and the package weight.

order_total = 1200
destination = "provincial"
weight = 3.5

if order_total >= 2000:
    fee = 0
elif destination == "metro" and weight <= 2:
    fee = 80
elif destination == "metro":
    fee = 120
elif destination == "provincial" and weight <= 2:
    fee = 150
elif destination == "provincial":
    fee = 220
else:
    fee = 500

print("Shipping fee: PHP", fee)

# Output: Shipping fee: PHP 220