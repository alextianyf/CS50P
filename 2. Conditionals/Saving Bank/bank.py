userInput = input("Greeting: ")

if userInput.startswith("Hello"):
    print("$0")
elif userInput.startswith("H"):
    print("$20")
else:
    print("$100")
