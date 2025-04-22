#Python program that handles exceptions related to list operations using a list of performing artist with functionality to modify list
def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    # Your code goes here
    while not main(top_artists): 
        #try and except blocks to take user input as a replacement value for an existing artist name on the list using its index number
        try:
            index_input = input("What index number on the Top 10 Artists list would you like to replace?: ") #asks user what index number or number on list the artist they want to replace is
            index = int(index_input)
            if 0 <= len(top_artists):
                new_artist = input("\nPlease enter a new music artist to add to the list: ").title() #asks user to input new artists name to add to list instead
                top_artists[index] = new_artist
                print("\nMusic artist {new_artist} has been added to the {index} spot on the list!")
                for artist in top_artists:
                    print("The updated artist list is: ", {artist}) #prints newly updated list with updated new artist name
            else: 
                print("Please try again") #message that will print when if cause is not met
        except ValueError: 
            print("Invalid input. Please check spelling and enter a valid name.") #error message that will print if valid string of characters isn't entered for name
        except IndexError:
            print("Invalid number. Please enter a number from 1-10 corresponding with the artist name you would like to replace.") #error message that will print if valid integer isn't entered for index
        except SyntaxError:
            print("Please enter number values for index and character values for artist name.") #error message that will print if valid characters or integers aren't entered for either response
#Calls main function
main()