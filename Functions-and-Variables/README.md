# Functions-and-Variables
Harvard CS50 - Python problem set0

# 1. Indoor
- In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.
<br/>
### Expecting output<br/>
- Run your program with python `indoor.py`. Type HELLO and press Enter. Your program should output hello.<br/>
  
    input:
    ```
    python indoor.py
    HELLO, WORLD!
    ```
    expecting output:
    ```
    hello, world!
    ``` 
    <br/>
- Run your program with python `indoor.py`. Type THIS IS CS50 and press Enter. Your program should output this is cs50.
    input:
    ```
    python indoor.py
    THIS IS CS50
    ```
    expecting output:
    ```
    this is cs50
    ``` 
    <br/>
- Run your program with python `indoor.py`. Type 50 and press Enter. Your program should output 50.
    input:
    ```
    python indoor.py
    50
    ```
    expecting output:
    ```
    50
    ``` 
<br/>

---
<br/>

# 2. Playback Speed
- In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).<br/>
### Expecting output<br/>
- Run your program with python `playback.py`. Type HELLO and press Enter. Your program should output hello.<br/>
  
    input:
    ```
    python playback.py
    This is CS50
    ```
    expecting output:
    ```
    This...is...CS50 
    ``` 
    <br/>

    input:
    ```
    python playback.py
    This is our week on functions
    ```
    expecting output:
    ```
    This...is...our...week...on...functions 
    ``` 
<br/>

---
<br/>

# 3. Making faces
- In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.
- Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.<br/>

### Expecting output<br/>
- Run your program with python `faces.py`. Type
  
    input:

        python faces.py
        Hello :)
    
    output:

        Hello 🙂
    <br/>

- Run your program with python faces.py. Type Goodbye :( and press Enter. Your program should output:
  
    input:

        python faces.py
        Goodbye :(
    
    output:

        Goodbye 🙁
    <br/>

- Run your program with python faces.py. Type Hello :) Goodbye :( and press Enter. Your program should output
  
    input:

        python faces.py
        Hello :) Goodbye :(
    
    output:

        Hello 🙂 Goodbye 🙁
<br/>

---
<br/>

# 4. Einstein
- Even if you haven’t studied physics (recently or ever!), you might have heard that 
, wherein 
 represents energy (measured in Joules), 
 represents mass (measured in kilograms), and 
 represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.
- In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
  
### Expecting output <br/>
- Run your program with python `einstein.py`. Type 1 and press Enter
  
    input:

        python einstein.py
        1
    
    output:

        90000000000000000
    <br/>

- Run your program with python `einstein.py`. Type 50 and press Enter
  
    input:

        python einstein.py
        50
    
    output:

        4500000000000000000
<br/>

---

<br/>

# Tip Calculator
- dollars_to_float, which should accept a str as input, remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
- percent_to_float, which should accept a str as input, remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
- Assume that the user will input values in the expected formats.
  
### Expecting output <br/>
- Run your program with python `TipCalculator.py`. Type `$50` and press Enter, and `15%`
  
    input:

        python TipCalculator.py
        ow much was the meal? $50.00
        What percentage would you like to tip? 15%
    
    output:

        Leave $7.50
    <br/>

- Run your program with python `TipCalculator.py`. Type `$15` and press Enter, and `25%`

    input:

        python TipCalculator.py
        ow much was the meal? $15.00
        What percentage would you like to tip? 25%
    
    output:

        Leave $3.75
<br/>

---