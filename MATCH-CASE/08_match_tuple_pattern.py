# Topic: match-case | Level: Hard
# Matches a point (x, y) against patterns. x and y capture the values.

point = (3, -4)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print("On the x-axis at", x)
    case (0, y):
        print("On the y-axis at", y)
    case (x, y) if x > 0 and y > 0:
        print("Quadrant I")
    case (x, y) if x < 0 and y > 0:
        print("Quadrant II")
    case (x, y) if x < 0 and y < 0:
        print("Quadrant III")
    case (x, y):
        print("Quadrant IV")

# Output: Quadrant IV