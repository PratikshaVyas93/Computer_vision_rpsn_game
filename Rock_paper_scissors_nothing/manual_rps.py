# import libraries
import random

#User Input 
def get_user_choice():
    User_choice = input("Please Enter your choice (Rock, Paper,Scissors,Nothing): ")
    return User_choice

#random computer choice 
def get_computer_choice():
    random_lists = ['Rock', 'Paper', 'Scissors','Nothing']
    RPSN_game = random.choice(random_lists)
    return RPSN_game

msg = ""
# Winner
def get_winner():
    user_Input = get_user_choice()
    computer_input = get_computer_choice()
    print(f"\nYou chose {user_Input}, computer chose {computer_input}.\n")
    if (computer_input == user_Input):
        msg = "Both players selected "+ user_Input +". It's a tie!"
    elif(computer_input != user_Input):
        msg = "Computer Win"    
    return msg 
   
winner_game = get_winner()
print(winner_game)
