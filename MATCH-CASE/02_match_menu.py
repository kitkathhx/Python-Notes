# Topic: match-case | Level: Easy
# A simple menu: the number chosen decides what is shown.

choice = 2

match choice:
    case 1:
        print("Starting a new game...")
    case 2:
        print("Loading saved game...")
    case 3:
        print("Opening settings...")
    case 4:
        print("Goodbye!")
    case _:
        print("Invalid choice. Pick 1 to 4.")

# Output: Loading saved game...