# Topic: if-elif-else | Level: Intermediate
# Classifies the temperature into ranges.

temperature = 28

if temperature < 0:
    print("Freezing")
elif temperature < 15:
    print("Cold")
elif temperature < 25:
    print("Cool")
elif temperature < 33:
    print("Warm")
else:
    print("Hot")

# Output: Warm