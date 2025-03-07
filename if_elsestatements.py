# Program to confirm a user's age and if they are old enough to participate in certain legal age milestones

#prompt user to enter their current age
user_age = input("Please enter your age: ")

#use entered age to calculate if user is old enough to drive
if user_age >= '16':
    print("You are old enough to drive")
else:
    print("You are not old enough to drive yet")

#use entered age to calculate if user is old enough to vote
if user_age >= '18':
    print("You are old enough to vote")
else:
    print("You are not old enough to vote yet")

#use entered age to calculate if user is old enough to buy alcohol
if user_age >= '21':
    print("You are old enough to legally buy alcohol")
else:
    print("You are not old enough to legally buy alcohol yet")

#use entered age to calculate if user is old enough to qualify for a senior discount
if user_age >= '55':
    print("You are eligible for senior discounts based on your age")
else:
    print("You are not eligible for senior discounts based on your age")