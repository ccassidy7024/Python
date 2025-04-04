
#Python program that enhances simple code provided to incorporate exceptions in case of input error using try and except statements
# Simple Python program to calculate the square of a number
def square_number():
    #implements try, except, and else statements to handle ValueError from input
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
    #if letters or incorrect values are entered, this error message will print prompting user to enter valid number
    except ValueError:
        print("Letters are not accepted; only integers. Please enter a valid number")
    #if valid number is entered at input, this string with number and squared number values will print 
    else:
        print(f"The square of {number} is {squared_number}.")
#calls function
square_number()