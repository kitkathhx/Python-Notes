# Topic: for loop | Level: Intermediate
# The third value in range() is the step size. A negative step counts down.

print("Counting by 5s:")
for i in range(0, 51, 5):
    print(i, end=" ")

print()
print("Countdown from 10 to 1:")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# Output:
# Counting by 5s:
# 0 5 10 15 20 25 30 35 40 45 50
# Countdown from 10 to 1:
# 10 9 8 7 6 5 4 3 2 1