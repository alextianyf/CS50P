# 1. Lines of Code
-  in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.
-  Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.<br/>

### Expecting Output:
- Run your program with python lines.py. Your program should exit with sys.exit and provide an error message:

        Too few command-line arguments
    <br/>

- Create two python programs, `Hello.py` and `goodbye.py`. Run your program with python lines.py. Your program should exit with sys.exit and provide an error message:

        Too few command-line arguments
    <br/>

- Create two python programs, `Hello.py`. Run your program with python lines.py. Your program should output:
 
        Number of lines of code (excluding comments and blank lines): 2

<br/>

---

<br/>

# 2. 
