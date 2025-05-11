#Python program that uses the calendar and datetime modules to retrieve the calendar of the user's birthday month this year

import calendar     #imports calendar and datetime modules to use
import datetime

#Creates main function to run program
def main():
    year = datetime.datetime.now().year  #fetches the current year using datetime module
    month = int(input("What number month were you born?(1-12):  "))     #takes user input for their birthday month
    #try except block to ensure user inputs valid integer of 1-12 to represent Jan-Dec months of the year. 
    #Will return error message if characters or invalid numbers are entered
    try:
        month >= 0 and month <=12
        print(month)
    except ValueError:
        print("Please enter a valid number between 1-12. January would be 1 and December would be 12")
    except SyntaxError:
        print("Please enter a valid number between 1-12. January would be 1 and December would be 12")
    #calls and prints the calendar month of 2025 with the month entered by user for their birthday month
    calendar.month(2025, month)
    print(f'Your birthday month in the current year is: {calendar.month(2025, month)}')
#Calls main function
main()