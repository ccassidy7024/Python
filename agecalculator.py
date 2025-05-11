#Python program that asks user for their birthday and calculates their age in different units using datetime and timedelta

# 30.41 days in a month
# 7 days in a week 

from datetime import datetime  #imports datetime module offering date and time
#Creates main function for program
def main():
   
    print("\n\n")
    try:
        today = datetime.today()        #uses datetime module to capture the current day today
        birth_year = int(input("What year were you born?  "))       #takes user input to store birth year
        month = int(input("What Month were you born (as a number. May would be 5)  "))      #takes user input to store birth month
        day = int(input("What day of the month were you born?  "))      #takes user input to store birth date
        # just need datetime not datetime.date
        # because we imported datetime from datetime

        birthday = datetime(birth_year, month, day)     #formats the user input birthday into a readable date/time format
        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d") #formats the date
        print(birthday_output) #prints user's birthday in correct format

        delta = today - birthday        #calculates the difference between the current date and the input birthday to calculate how many days old the user is
        print(f'Difference is {delta.days} days')
        delta_years = delta.days // 365.2425
        print(f'You are {delta_years} years old')       #prints user's age in years

        remaining_months = 12 - month       #formula to account for the rest of the months in a year
        months = delta_years * 12 + remaining_months    #formula to calculate user's age in months by multiplying the user's age in years by 12 (months in a year) and adds the remaining months
        print(f'You are {months} months old')   #prints user's age in months

        weeks = delta.days // 7     #formula to calculate how many weeks old user is by dividing how many days old they are by 7 (7 days in a week)
        print(f'You are {weeks} weeks old')     #prints user's age in weeks

        hours = delta.days * 24     #formula to calculate how many hours old user is by multiplying days old by 24(24 hours in a day)
        print(f'You are {hours} hours old')     #prints user's age in hours

        minutes = delta.days * 1440     #formula to calculate how many minutes old user is by multiplying days old by 1440(1440 minutes in a day)
        print(f'You are {minutes} minutes old')     #prints user's age in minutes
    #exception error handling if characters or incorrect inputs occur
    except ValueError:
        print("Please enter a valid character or integer")
    except SyntaxError:
        print("Oops, error!! Please make sure entries are valid integers")
    except Exception as e:
        print(f"ooooops!!!:  {e}") 
#calls main function        
main()
