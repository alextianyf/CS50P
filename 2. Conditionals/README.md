# Conditionals
Harvard CS50 - Python problem set1

# 1. Deep thought 

- in `DeepThought.py`, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs `42` or (case-insensitively) `forty-two` or `forty two`. Otherwise output No.

<br/>
  
### Expecting Output

- Run your program with python `DeepThought.py`. Type 42 and press Enter. Your program should output:

        Yes
        
    <br/>

- Run your program with python `DeepThought.py`. Type forty-two and press Enter. Your program should output:
  
        Yes

    <br/>

- Run your program with python `DeepThought.py`. Type forty two and press Enter. Your program should output:
  
        Yes
    
    <br/>

- Run your program with python `DeepThought.py`. Type 50 and press Enter. Your program should output:
  
        No
    
<br/>

---

<br/>

# 2. Saving Bank

- In a file called `bank.py`, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

<br/>

### Expecting output:

- Run your program with python bank.py. Type `Hello` and press Enter. Your program should output:

        $0

    <br/>

- Run your program with python bank.py. Type `Hello, Alex` and press Enter. Your program should output:

        $0

    <br/>

- Run your program with python bank.py. Type `How you doing?` and press Enter. Your program should output:
  
        $20

    <br/>

- un your program with python bank.py. Type `What's happening?` and press Enter. Your program should output:

        $100
    
<br/>

---

<br/>

# 3. File Extension

- In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
  - .gif
  - .jpg
  - .jpeg
  - .png
  - .pdf
  - .txt
  - .zip <br/>

  If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

### Expecting Output:

- Run your program with python `extensions.py`. Type `happy.jpg` and press Enter. Your program should output:

        image/jpeg

    <br/>

- Run your program with python `extensions.py`. Type `document.pdf` and press Enter. Your program should output:

        application/pdf

<br/>

---

<br/>

# 4. Math Interpreter

- n a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:<br/>
  - x is an integer
  - y is +, -, *, or /
  - z is an integer<br/>
  
  For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.<br/>
  Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!

### Expecting output

- Run your program with python interpreter.py. Type `1 + 1` and press Enter. Your program should output:
  
        2.0

    <br/>

- Run your program with python interpreter.py. Type `2 - 3` and press Enter. Your program should output:
  
        -1.0

    <br/>

- Run your program with python interpreter.py. Type `2 * 2` and press Enter. Your program should output

        4.0

    <br/>

- Run your program with python interpreter.py. Type `50 / 5` and press Enter. Your program should output

        10.0

<br/>

---

<br/>

# 5. Meal Time

- n meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast. <br/>
- Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
  
### Expecting Output:

- Run your program with python meal.py. Type `7:00` and press Enter. Your program should output:

        breakfast time

    <br/>

- Run your program with python meal.py. Type `7:30` and press Enter. Your program should output:

        breakfast time

    <br/>

- Run your program with python meal.py. Type `12:42` and press Enter. Your program should output:

        lunch time

    <br/>

- Run your program with python meal.py. Type `18:32` and press Enter. Your program should output:

        dinner time

    <br/>

- Run your program with python meal.py. Type `11:11` and press Enter. Your program should output:

<br/>

---