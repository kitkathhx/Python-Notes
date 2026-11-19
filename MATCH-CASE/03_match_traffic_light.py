# Topic: match-case | Level: Easy
# Matches a string and tells the driver what to do.

light = "yellow"

match light:
    case "red":
        print("Stop")
    case "yellow":
        print("Slow down and get ready")
    case "green":
        print("Go")
    case _:
        print("Invalid light color")

# Output: Slow down and get ready