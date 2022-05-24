# import libraries
import random

#User Input 
def get_user_choice():
    User_choice = input("Please Enter your choice: ")
    return User_choice

#random computer choice 
def get_computer_choice():
    random_lists = ['Rock', 'Paper', 'Scissors','Nothing']
    RPSN_game = random.choice(random_lists)
    return RPSN_game

msg = ""
# Winner
def get_winner():
    User_Input = get_user_choice()
    Computer_input = get_computer_choice()
    print("User's choise is: ", User_Input)
    print("Computer's Choise is: ", Computer_input)
    if (Computer_input != User_Input):
        msg = "Computer Wins"
    else:
        msg = "User Win"
    return msg 
   
winner_game = get_winner()
print(winner_game)
