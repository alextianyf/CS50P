def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[:2].isalpha():
        return False

    if not s[:2].isupper():
        return False
    # he isalnum() method returns True if all the characters are alphanumeric,
    # meaning alphabet letter (a-z) and numbers (0-9).
    if not s[2:].isalnum():
        return False

    if s[2] == '0':
        return False

    return True


main()
