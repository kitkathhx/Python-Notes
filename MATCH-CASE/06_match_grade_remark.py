# Topic: match-case | Level: Intermediate
# Gives a remark for each letter grade. Several letters share one remark.

grade = "B"

match grade:
    case "A":
        print("Outstanding!")
    case "B" | "C":
        print("Good job. Keep it up.")
    case "D":
        print("Passed, but you can do better.")
    case "F":
        print("Failed. Please try again.")
    case _:
        print("Invalid grade")

# Output: Good job. Keep it up.