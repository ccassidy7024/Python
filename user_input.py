#Python Program to calculate percentages of spending categories of a user's budget

#prompt users to enter their total budget
total_budget = float(input("Enter your net monthly income: "))
#prompt users to enter the amounts for spending in the following categories
housing = int(input("Enter amount spent on housing (rent or mortgage): "))
utilities = int(input("Enter amount spent on utilities: "))
groceries = int(input("Enter amount spent on groceries: "))
transportation = int(input("Enter amount spent on transportation: "))
health_care = int(input("Enter amount spent on health care: "))
personal_care = int(input("Enter amount spent on personal care: "))
clothing = int(input("Enter amount spent on clothing: "))
debt = int(input("Enter amount spent on debt: "))

#divide the specific expenses by the total budget and multiply by 100 to see what percentage of spending each category
#makes up the total budget
percentage_of_housing = (housing / total_budget) * 100
percentage_of_utilities = (utilities / total_budget) * 100
percentage_of_groceries = (groceries / total_budget) * 100
percentage_of_transportation = (transportation / total_budget) * 100
percentage_of_health_care = (health_care / total_budget) * 100
percentage_of_personal_care = (personal_care / total_budget) * 100
percentage_of_clothing = (clothing / total_budget) * 100
percentage_of_debt = (debt / total_budget) * 100

#display the results of spending category percentages 
print(f"The expense of housing is {percentage_of_housing:.2f}% of the budget")
print(f"The expense of utilities is {percentage_of_utilities:.2f}% of the budget")
print(f"The expense of groceries is {percentage_of_groceries:.2f}% of the budget")
print(f"The expense of transportation is {percentage_of_transportation:.2f}% of the budget")
print(f"The expense of health care is {percentage_of_health_care:.2f}% of the budget")
print(f"The expense of personal care is {percentage_of_personal_care:.2f}% of the budget")
print(f"The expense of clothing is {percentage_of_clothing:.2f}% of the budget")
print(f"The expense of debt is {percentage_of_debt:.2f}% of the budget")