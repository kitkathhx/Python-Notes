# Topic: while loop | Level: Hard
# A menu that keeps showing until the user picks 4 (Exit).
# (The choices are simulated here. In a real program, use: choice = int(input("Choose: ")))

choice = 0

while choice != 4:
    choice = choice + 1
    print("--- MENU ---")
    print("1. Say hello | 2. Show time | 3. Show date | 4. Exit")
    print("You chose:", choice)
    if choice == 1:
        print("Hello!")
    elif choice == 2:
        print("It is time to learn Python.")
    elif choice == 3:
        print("Today is a good day to code.")
    elif choice == 4:
        print("Goodbye!")
    else:
        print("Invalid choice.")

# Output: the menu appears 4 times, then: Goodbye!