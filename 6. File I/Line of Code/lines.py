import sys
import os


def count_code_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            code_lines = 0
            in_comment_block = False

            for line in file:
                # Remove leading and trailing whitespace
                line = line.strip()

                if line.startswith("#") or in_comment_block:
                    if line.endswith("'''") or line.endswith('"""'):
                        in_comment_block = not in_comment_block
                    continue  # Skip comments

                if line:
                    code_lines += 1  # Non-empty line, count as code

            return code_lines
    except FileNotFoundError:
        sys.exit("Error: Specified file does not exist.")
    except Exception as e:
        sys.exit(f"Error: An error occurred while processing the file: {e}")


def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    if not file_path.endswith('.py'):
        sys.exit("Error: The specified file must have a .py extension.")

    if not os.path.exists(file_path):
        sys.exit("Error: Specified file does not exist.")

    code_lines = count_code_lines(file_path)
    print(
        f"Number of lines of code (excluding comments and blank lines): {code_lines}")


if __name__ == "__main__":
    main()
