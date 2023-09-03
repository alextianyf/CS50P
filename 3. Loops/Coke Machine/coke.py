print("Amount Due: 50")

Coin = 50

while True:
    insert = int(input("Insert Coin: "))
    if insert not in [5, 10, 25]:
        print("Invalid coin. Accpet 5, 10, 25 cents")
        print(f"Amount Due: {Coin}")
    else:
        Coin -= insert

        if Coin > 0:
            print(f"Amount Due: {Coin}")
        if Coin < + 0:
            print(f"Amount Owe: {Coin}")
            break
