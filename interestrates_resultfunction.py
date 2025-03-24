#Python program that calculates and returns simple interest based on parameters using functions and return

#Creates function to take inputs to calculate simple interest by applying formula to input values and returning calculated total
def calculate_interest(amount, interest, investment):
    principal = amount
    rate = interest
    time = investment
    simple_interest = (principal * rate * time)/100
    print(f"The simple interest for ${principal} at {rate}% over {time} years is ${simple_interest}.")
    return simple_interest

#Allows for user input to be used for calculations of calculate_interest function
result = calculate_interest(5000, 4, 3)