#Program that uses logical operators to prompt user for two integers and demonstrate the use of operators in Python

#create user inputs for first and second numbers needed
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

#demonstrates AND operator comparison of two numbers
if first_num > 100 and second_num > 100:
    print("Both numbers are greater than 100: True")
else:
    print("Both numbers are greater than 100: False")
if first_num > 0 and second_num > 0:
    print("Both numbers are greater than 0: True")
else:
    print("Both numbers are greater than 0: False")

#demonstrates OR operator comparison of two numbers
if first_num > 10 or second_num > 10:
    print("Are either numbers double digits?: Yes")
else:
    print("Are either numbers double digits?: No")
if first_num < 0 or second_num < 0:
    print("Is either number a negative number?: Yes")
else:
    print("Is either number a negative number?: No")

#demonstrates NOT operator comparison of numbers
if not first_num > second_num:
    print("Is the first number greater than the second number?: No")
else:
    print("Is the first number greater than the second number?: Yes")
if not first_num >= second_num:
    print("Are the first and second numbers equal to each other? No")
else:
    print("Are the first and second numbers equal to each other? No")