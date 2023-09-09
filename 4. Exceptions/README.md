# 1. Fuel Gauge
- Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

- In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

- If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.<br/>
  
### Expecting Output:
- Run your program with python fuel.py. Type `3/4` and press Enter. Your program should output:
  
        75%
    <br/>

- Run your program with python fuel.py. Type `a/b` and press Enter. Your program shoud continue as you same question, and type `0/1`. You program should output:
  
        E
    <br/>

- Run your program with python fuel.py. Type `1/0` and press Enter. Your program shoud continue as you same question, and type `1/1`. You program should output:
  
        F
<br/>

---

<br/>

# 2. Felipe’s Taqueria

- One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, which offers a menu of entrees, per the dict below, wherein the value of each key is a price in dollars:

- In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.<br/>

### Expecting Output:
- Run your program with python taqueria.py. Type `Taco` and press Enter, then type `Taco` again and press Enter. Your program should output:

        Total: $6.00  
    <br/>
- Run your program with python taqueria.py. Type `Baja Taco` and press Enter, then type `Tortilla Salad` again and press Enter. Your program should output:

        Total: $12.00  
<br/>

---

