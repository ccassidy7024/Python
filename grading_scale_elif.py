#Program to accept user input of a numeric grade and return the letter grade associated with that score. Demonstrating elif statement

#asks user to input numeric score of their grade
user_grade = int(input("Enter your numeric grade: "))

#checks if grade is less than 60
if user_grade < 60:
    grade = "F"
    #grade is F if score is below 60
#checks if grade is between 60-69
elif user_grade < 69:
    grade= "D"
    #grade is D if score is between 60-69
#checks if grade is between 70-79
elif user_grade < 79:
    grade= "C"
    #grade is C if score is between 70-79
#checks if grade is between 80-89
elif user_grade < 89:
    grade= "B"
    #grade is B if score is between 80-89
    #checks if grade is 90 or above
else:
    grade= "A"
    #grade is A if score 90 or above

#prints letter grade based on numeric score entered by user
print("Your letter grade is:", str(grade))