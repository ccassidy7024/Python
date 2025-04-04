#Python program that uses a created dictionary  to translate letters to NATO Phonetic Alphabet terms 
# and returns word input by user in NATO codes

#Program logic organized in main function
def main():
    #Dictionary with key:value pairs of letters and NATO codes for conversion
    nato_alphabet = {
        "A": "Alpha",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliet",
        "K": "Kilo",
        "L": "Lima",
        "M":"Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "X-ray",
        "Y": "Yankee",
        "Z": "Zulu"
    }
    word = input("Enter a word to translate to the NATO Phonetic Alphabet: ").upper() #takes user input for word to covert spelling in NATO codes
    word_list = [nato_alphabet[letter] for letter in word] #searches dictionary to pair key of letter with NATO code value
    print(word_list) #prints the entered word by listing NATO code values
#calls main function to run program
main()