#Python program that runs trough a game of rock, paper, scissors using try and except blocks
#imports random module so computer can make random choice from list of options
import random

#Creates list of choices for computer to choose from
turns = ['Rock', 'Paper', 'Scissors']
same_guess = False
#tells the computer to choose a random choice from list for computer to return
def computer_choice():
     return random.choice(turns)
print("Let's play a game of Rock, Paper Scissors!")
#sets the random computer choice as computer's turn and takes input from user for player turn
computer = computer_choice()
player_choice = input("Enter your choice: Rock, Paper, or Scissors?: ").lower()
#creates function that goes through options between computer choice and player input for who won
def game(player, computer):
        if player == computer:
            print("It's a tie! Try again!")
            same_guess = True
        elif player == "Rock" and computer == "Scissors":
                print("\nYou win!! {player} smashes {computer}")
        elif player == "Paper" and computer == "Rock":
                print("\nYou win!! {player} covers {computer}")
        elif player == "Scissors" and computer == "Paper":
                print("\nYou lose! {computer} cuts {player}")
        else:
              print("Let's play again!")
#creates main function with try and except block in case of value or syntax errors
def main():       
        while not game:
            try:
                if not player(user_input):
                    print("Please enter a valid choice between 'Rock', 'Paper', or 'Scissors': ")
            except ValueError:
                print("Please check all spelling and try entering your choice again")
            except SyntaxError:
                print("Please check all spelling and try entering your choice again")
        result = game(player_choice, computer)
        print(result)
#Calls main function  
main()