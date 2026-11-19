# Topic: Nested if | Level: Intermediate
# A loan applicant must pass age, income, and credit checks, in that order.

age = 28
monthly_income = 22000
has_good_credit = True

if age >= 21:
    if monthly_income >= 15000:
        if has_good_credit:
            print("Loan approved.")
        else:
            print("Denied: poor credit history.")
    else:
        print("Denied: income is too low.")
else:
    print("Denied: applicant is too young.")

# Output: Loan approved.