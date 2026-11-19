# Topic: match-case | Level: Intermediate
# The | symbol lets one case match several values.

day = "Sunday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend: time to rest!")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday":
        print("Weekday: keep working.")
    case "Friday":
        print("Almost the weekend!")
    case _:
        print("Not a valid day")

# Output: Weekend: time to rest!