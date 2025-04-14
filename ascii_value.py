#Python program that provides ASCII value of any character entered by user

#Dictionary to hold key:value pairings of ASCII values table
ascii_values = {
        "A": "65",
        "B": "66",
        "C": "67",
        "D": "68",
        "E": "69",
        "F": "70",
        "G": "71",
        "H": "72",
        "I": "73",
        "J": "74",
        "K": "75",
        "L": "76",
        "M": "77",
        "N": "78",
        "O": "79",
        "P": "80",
        "Q": "81",
        "R": "82",
        "S": "83",
        "T": "84",
        "U": "85",
        "V": "86",
        "W": "87",
        "X": "88",
        "Y": "89",
        "Z": "90"
}
#Main function to take user input and convert character into ASCII value
def main():
    user_input = input("Enter a character: ").upper()
    while len(user_input) != 1:
        print("Please enter exactly one character.")
        user_input = input("Enter a character: ").upper()
    ascii_value = ord(user_input)
    print(f"The ASCII value of {user_input} is {ascii_value}")
#Calls main function
main()
