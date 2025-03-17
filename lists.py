#Python program that takes user input of steps and returns total and average steps in a day/week

#Creates a list of days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#Creates an empty list to store steps
steps = []

#Loops through each day to get user input
for day in days:
    while True:
        try:
            step_count = int(input(f"Enter the number of steps for {day}: "))
            if step_count < 0:
                print("Please enter a non-negative number.")
                continue
            steps.append(step_count)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#Displays daily steps
print("\nSteps recorded for each day:")
for day, step in zip(days, steps):
    print(f"{day}: {step} steps")

#Calculates total and average steps
total_steps = sum(steps)
average_steps = total_steps / len(steps)

#Displays results
print(f"\nTotal steps taken in the week: {total_steps}")
print(f"Average steps per day: {average_steps:.2f}")