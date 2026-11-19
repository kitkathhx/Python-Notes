# Topic: match-case | Level: Intermediate
# Chooses the operation from the symbol. Division checks for zero first.

a = 20
b = 5
operator = "/"

match operator:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b == 0:
            print("Error: cannot divide by zero.")
        else:
            print(a / b)
    case _:
        print("Unknown operator")

# Output: 4.0