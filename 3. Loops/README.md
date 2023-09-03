# 1. Camel Case

- In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.<br.>
  
### Expecting Output:
- Run your program with python `camel.py`. Type `name` and press Enter. Your program should output:
  
        name
    <br/>

- Run your program with python camel.py. Type `firstName` and press Enter. Your program should output:

        first_name
    <br/>

- Run your program with python camel.py. Type `preferredFirstName` and press Enter. Your program should output
  
        preferred_first_name
<br/>

---
<br/>

# 2. Coke Machine

- Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
- n a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
  
### Expecting Output:

- Run your program with python coke.py. At your Insert Coin: prompt, type `25` and press Enter. Your program should output:

        Amount Due: 25  
    
    and continue prompting the user for coins.<br/>
    Run your program with python coke.py. At your Insert Coin: prompt, type `10` and press Enter. Your program should output:

        Amount Due: 15
    
    and continue prompting the user for coins.<br/>
    Run your program with python coke.py. At your Insert Coin: prompt, type `5` and press Enter. Your program should output:

        Amount Due: 10
    
    and continue prompting the user for coins.<br/>
    Run your program with python coke.py. At your Insert Coin: prompt, type `30` and press Enter. Your program should output:

        Amount Due: 10

    because the machine doesn’t accept 30-cent coins! Your program should then continue prompting the user for coins.<br/>
    Run your program with python coke.py. At your Insert Coin: prompt, type `10` and press Enter, then type 25 again and press Enter. Your program should halt and display:

        Amount Owed: 0
    
    Program ends
<br/>
- Run your program with python coke.py. At your Insert Coin: prompt, type `25` and press Enter. Your program should output:

        Amount Due: 25  
    
    and continue prompting the user for coins.<br/>
    Run your program with python coke.py. At your Insert Coin: prompt, type `10` and press Enter. Your program should output:

        Amount Due: 15
    
    and continue prompting the user for coins.<br/>
    Run your program with python coke.py. At your Insert Coin: prompt, type `25` and press Enter. Your program should output:

        Amount Owed:-10

    Program ends
<br/>

---

<br/>

# 3. Twitter

- When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
  
### Expecting Output: 
- Run your program with python twttr.py. Type `Twitter` and press Enter. Your program should output:

        Twttr
    <br/>

- Run your program with python twttr.py. Type `What's your name?` and press Enter. Your program should output:

        Wht's yr nm?
    <br/>

- Run your program with python twttr.py. Type `CS50` and press Enter. Your program should output
  
        CS50
<br/>

---

<br/>

# 4. 