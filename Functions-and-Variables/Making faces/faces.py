def convert(input_string):
    input_string = input_string.replace(":)", "😊")
    input_string = input_string.replace(":(", "😔")
    return input_string


def main():
    user_input = input("")
    converted_Result = convert(user_input)
    print(converted_Result)


if __name__ == "__main__":
    main()
