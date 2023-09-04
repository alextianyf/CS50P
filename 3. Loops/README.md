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

# 4. Vanity Plates

- In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:<br/>
  - “All vanity plates must start with at least two letters, and all uppercase”
  - “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
  - “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
 - “No periods, spaces, or punctuation marks are allowed.”
In `plates.py`, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

### Expecting Output:

- Run your program with python plates.py. Type `CS50` and press Enter. Your program should output:

        valid
    <br/>

- Run your program with python plates.py. Type `CS05` and press Enter. Your program should output:

        invalid
    <br/>

- Run your program with python plates.py. Type `cs50` and press Enter. Your program should output:

        invalid
    <br/>

- Run your program with python plates.py. Type `CS` and press Enter. Your program should output:

        invalid
    <br/>

---

# 5. Nutrition Facts
- The U.S. Food & Drug Adminstration (FDA) offers [downloadable/printable posters](https://www.fda.gov/food/food-labeling-nutrition/nutrition-information-raw-fruits-vegetables-and-fish) that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”
- In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the [FDA’s poster for fruits](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://cs50.harvard.edu/python/2022/psets/2/nutrition/Nutrition-Information-for-Raw-Fruits---small-PDF-Poster.pdf), which is also [available as text](https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version). Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

### Expecting Output:

- Run your program with python nutrition.py. Type `Apple` and press Enter. Your program should output:

        Calories: 130
    <br/>

- Run your program with python nutrition.py. Type `banana` and press Enter. Your program should output:

        Calories: 110
    <br/>

- Run your program with python nutrition.py. Type `AVOcaDO` and press Enter. Your program should output:

        Calories: 50
<br/>

---