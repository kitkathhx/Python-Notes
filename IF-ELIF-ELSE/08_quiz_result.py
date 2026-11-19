# Topic: if-elif-else | Level: Hard
# Computes the percentage first, then decides the letter grade and a message.

score = 17
total_items = 20

percentage = score / total_items * 100

if percentage == 100:
    letter = "A+"
    message = "Perfect score!"
elif percentage >= 90:
    letter = "A"
    message = "Excellent!"
elif percentage >= 80:
    letter = "B"
    message = "Great job!"
elif percentage >= 70:
    letter = "C"
    message = "Good effort."
elif percentage >= 60:
    letter = "D"
    message = "You passed, barely."
else:
    letter = "F"
    message = "Please review and try again."

print("Score:", score, "/", total_items)
print("Percentage:", percentage, "%")
print("Grade:", letter, "-", message)

# Output:
# Score: 17 / 20
# Percentage: 85.0 %
# Grade: B - Great job!