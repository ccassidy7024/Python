#Python program that generates a random  number and takes user input guesses 
#to verify if user's guess is the same as the randomly generated number

#Use Python modules to import random module in order to use randint function
import random

#Define a main function that generates a random number and compares the difference between that 
#and the number input by user in order to allow user to continue guessing until guessing the correct 
#random generated number
def main():
    random_number = random.randint(1, 100) #uses randint() function found in random module to generate number
    print("Let's play a number guessing game!")
    print("The computer has selected a number between 1 and 100. See if you can guess the number!")
    attempts=0 #starts the user at 0 guess attempts which will increment as user has to keep guessing
    correct_guess = False 

    #while loop that takes number input by user then uses abs() function to find absolute value of the 
    # difference between the generated number and the number guessed by the user. Based on the 
    # difference between guess and generated number, user receives message indicating how close they are to 
    # the correct answer of the generated number. Main function prints message and total attempts to guess 
    # once number is correctly guessed 
    while not correct_guess:
            user_guess = int(input("Please enter a number between 1 and 100: "))
            variation = abs(user_guess - random_number)
            if user_guess == random_number:
                print("Congratulations! You guess the right number!")
                correct_guess = True
            elif variation  <= 5:
                print("Very Hot")
                attempts +=1
            elif variation <= 15:
                 print("Hot")
                 attempts +=1
            elif variation <=25:
                 print("Cool")
                 attempts +=1
            elif variation > 25:
                 print("Cold")
                 attempts +=1
            else:
                print("Please enter a valid integer between 1 and 100")
    print("\nNumber of attempted guesses: ", attempts+1)

#Calls main function
main()