# Topic: match-case | Level: Easy
# Matches a number (1-7) to the name of the day. _ is the default case.

# Topic: match-case | Level: Easy
# Matches a number (1-7) to the name of the day. _ is the default case.

day = 5

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")

# Output: Friday
# Output: Friday