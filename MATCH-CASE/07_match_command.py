# Topic: match-case | Level: Hard
# A guard (the if after a case) adds an extra condition to a pattern.

command = "say Hello, class!"

match command:
    case "start":
        print("Program started.")
    case "stop" | "quit" | "exit":
        print("Program stopped.")
    case text if text.startswith("say "):
        print("Message:", text[4:])
    case text if text == "":
        print("Please type a command.")
    case _:
        print("Unknown command")

# Output: Message: Hello, class!