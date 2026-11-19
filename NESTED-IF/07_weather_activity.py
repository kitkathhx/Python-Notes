# Topic: Nested if | Level: Hard
# Suggests an activity based on the weather, then on temperature or wind.

weather = "sunny"
temperature = 33
windy = False

if weather == "sunny":
    if temperature >= 30:
        print("Go swimming.")
    else:
        print("Have a picnic.")
elif weather == "rainy":
    if windy:
        print("Stay home and watch a movie.")
    else:
        print("Visit a museum.")
else:
    print("Check the forecast again.")

# Output: Go swimming.