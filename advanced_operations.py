#Python program that takes user input of heart rate and displays in list with corresponding time slots during the day.

#Defines a list of times of day
total = 0
average = 0
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rates = []

#Uses a loop to ask user to enter their heart rate (BPM) each time slot
for time in time_slots:
    bpm = input(f"Enter your heart rate for {time}: ")
    heart_rates.append([time, bpm])
print(heart_rates)

#Creates multi-level list to store time slots with corresponding heart rates
for i in range(4):
    time = heart_rates[i][0]
    bpm = heart_rates[i][1]
    total += int(bpm)
    print(f"At {time} your heart rate (BPM) was: {bpm}")

#Displays average heart rate of user across all time slots
average = total / 4
print(f"Your average heart rate was: {average:.0f}")