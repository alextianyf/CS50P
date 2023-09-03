userInput = input("Input:")

output = ''
for char in userInput:
    if char.upper() not in ['A', 'E', 'I', 'O', 'U']:
        output += char

print(output)
