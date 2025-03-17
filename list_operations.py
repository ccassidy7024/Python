#Python program that returns available seats

#Creates a list of available seats numbered 1 to 20
available_seats = list(range(1, 21))

#Displays the list of available seats
def display_seats():
    print("\nCurrently available seats:", available_seats)
 

#Loop to handle seat selection
while True:
    try:
        #Prompts user to select a seat
        seat_choice = int(input("\nEnter a seat number to book (or enter 0 to finish): "))

        #Ends booking process if user enters 0
        if seat_choice == 0:
            print("Thank you for booking! Enjoy your event.")
            break
        
        #Validates seat choice
        if seat_choice not in available_seats:
            print("Invalid choice! The seat is either taken or not within the available seat range. Please select another seat option.")
            continue

        #Removes booked seat and update list
        available_seats.remove(seat_choice)
        print(f"Seat {seat_choice} successfully booked!")

        #Displays updated seat availability without selected seat
        display_seats()

    except ValueError:
        print("Invalid input! Please enter a number between 1 and 20.")