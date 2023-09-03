userInput = input("Expression: ")

x, y, z = userInput.split()

if y == "+":
    print(float(x)+float(z))
elif y == "*":
    print(float(x)*float(z))
elif y == "/":
    print(float(x)/float(z))
elif y == "-":
    print(float(x) - float(z))
