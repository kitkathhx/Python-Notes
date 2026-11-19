# Topic: for loop | Level: Intermediate
# Adds the numbers from 1 to 100 and finds the average.

total = 0

for number in range(1, 101):
    total = total + number

print("Sum of 1 to 100:", total)
print("Average:", total / 100)

# Output:
# Sum of 1 to 100: 5050
# Average: 50.5