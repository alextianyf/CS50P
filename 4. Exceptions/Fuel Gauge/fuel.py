userInput = input("Fraction: ")
while True:
    try:
        x, y = map(int, userInput.split('/'))
        # You can also set this type error as ValueError instead of using ZeroDivisionError
        # if y == 0:
        #     raise ValueError
        percentage = (x / y)*100

        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{round(percentage)}%")
        break
    except (ValueError, ZeroDivisionError):
        userInput = input("Fraction: ")

    # Alternatively you can do this
    # except ValueError:
    # ...
    # except ZeroDivisionError:
    # ...
