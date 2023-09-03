userInput = input("camelCase: ")

snakeName = ''

for char in userInput:
    if char.isupper():
        snakeName = snakeName + '_'
        snakeName = snakeName + char.lower()
    else:
        snakeName = snakeName + char

print(snakeName)
