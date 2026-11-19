# Topic: if-else | Level: Intermediate
# A person can vote at 18 or older. If not, show how many years are left.

age = 16

if age >= 18:
    print("You are eligible to vote.")
else:
    years_left = 18 - age
    print("Not yet eligible. Wait", years_left, "more year(s).")

# Output: Not yet eligible. Wait 2 more year(s).