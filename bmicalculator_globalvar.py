#Python program that creates a BMI calculator using functions and global variables

#Declares global variable for conversion kg to lb in weight
global kgs
kgs = 0.4535592 
#Declares global variable for conversion in to m in height
global meters
meters = 0.0254

#Defines function to convert lbs to kgs
def calculate_weight(lbs):
    weight = lbs * kgs
    return weight

#Defines function to convert inches to meters
def calculate_height(inches):
    height = inches * meters
    return height

#Defines function to calculate BMI based on weight and height formula
def calculate_bmi(weight, height):
    bmi_total = weight / (height * height)
    return bmi_total

#Defines function that asks for user input for weight and returns calculated BMI and what category user falls in
def program():
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    print(f"Your BMI is: {calculate_bmi(weight, height)} ") #Prints calculated BMI of user
    if weight < 18.5:
        user_bmi = "underweight"
    elif weight < 24.9:
        user_bmi = "normal weight"
    elif weight < 29.9:
        user_bmi = "overweight"
    else:
        user_bmi = "obese" #Checks user BMI to sort into proper category
    print(f"You are in the {user_bmi} category")
#Calls function
program()  



