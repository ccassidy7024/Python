#Python program that takes entered strings and uses functions and methods to see if password meets the criteria
#importing re module from python allows work with regular expressions
import re

#Defines function to check validations for password entered by user
def valid_password(user_input):
    valid_password = False

    #while loop that iterates through all requirements for password to meet
    while not valid_password:
        if len(user_input) >= 8 or len(user_input) <= 20:
            print("Make sure your password is between 8 and 20 characters long")
            return False
        elif user_input.isupper() is None:
            print(f"{user_input} must contain at least one uppercase")
            return False
        elif user_input.islower() is None:
            print(f"{user_input} must contain at least one uppercase")
            return False
        elif re.search('[0-9]', user_input) is None:
            print("Password must contain at least one number")
            return False
        elif re.search('[!,@,#,$,%,&,*]', user_input) is None:
            print("Password must contain at least one special character")
            return False
    else:
        return True
#Defines main function that calls for user to confirm password once requirements are met or 
# directed to enter a new password if  there is an error
def main():
    while  not valid_password: #try and except block to direct user through instructions based on entry
        try:
            user_input = input("Please enter a valid password: ")
            if not valid_password(user_input):
                print("Please start over and enter a new valid password: ")
            
            password_val = (input("Please re-enter your new password for confirmation: "))
            if password_val == user_input:
                print("Valid password successfully added!")
            else:
                print("Please re-enter confirmation email")
        except ValueError:
            print("Please enter a valid character, integer, or special character")
        except SyntaxError:
            print("There was an error, please enter a different password")
#Calls main function  
main()