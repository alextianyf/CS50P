calories = {
    "banana": "110",
    "apple": "130",
    "avocado": "50",
}

userInput = input("item: ").lower()

if calories.get(userInput):
    result = calories.get(userInput)
    print(f"Calories: {result}")
