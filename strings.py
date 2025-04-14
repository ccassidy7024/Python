#Python program demonstrating the ues of string functions

def main():
    #Example string
    example_string = "Hello, Python programmers!"

    # TODO: Iterate through the string and print each character
    for char in example_string:
        print("Iterating through the string: ", (char))

    # TODO: Find and print the character with the minimum ASCII value in the string
    min_ascii_value = min(example_string)
    print("\nCharacter with the minimum ASCII value: ", (min_ascii_value))

    # TODO: Find and print the character with the maximum ASCII value in the string
    max_ascii_value = max(example_string)
    print("\nCharacter with the maximum ASCII value: ", (max_ascii_value))

    # TODO: Find and print the index of the first occurrence of 'o' in the string
    index = example_string.index("o")
    print("\nIndex of 'o': ", (index))

    # TODO: Convert the string into a list of characters and print the list
    list_of_chars = list(example_string)
    print("\nConverting string to a list of characters: ", (list_of_chars))

    # TODO: Count and print the number of occurrences of 'o' in the string
    count = example_string.count("o")
    print("\nCount of 'o' in the string: ",(count))


main()
