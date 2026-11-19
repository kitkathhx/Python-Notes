# Topic: if-else | Level: Intermediate
# Purchases of 1000 or more get a 10% discount.

purchase = 1500

if purchase >= 1000:
    discount = purchase * 0.10
else:
    discount = 0

final_price = purchase - discount

print("Purchase:", purchase)
print("Discount:", discount)
print("Total to pay:", final_price)

# Output:
# Purchase: 1500
# Discount: 150.0
# Total to pay: 1350.0