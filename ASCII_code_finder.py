def ascii_code_finder():
    char = input("Enter a character: ")
    if len(char) != 1:
        print("Please enter exactly one character.")
        return
    print(f"The ASCII code for '{char}' is {ord(char)}.")

if __name__ == "__main__":
    ascii_code_finder()