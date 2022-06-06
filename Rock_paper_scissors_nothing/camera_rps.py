################################################################################################################
"""
Author : Pratiksha
File name : camera_rps.py
Purpose : human and computer playing Rock Paper Scissors game
 
"""
################################################################################################################
"""
Importing Libraries required to create this game
"""
################################################################################################################
from keras.models import load_model
import cv2
import numpy as np
import random
from random import choice
import time

################################################################################################################

# created dictionary to map prediction values accordingly

REV_CLASS_MAP = {
    0: "Rock",
    1: "Paper",
    2: "Scissors",
    3: "Nothing"
}
# function to get mapping values
def mapper(val):
    return REV_CLASS_MAP[val]

# created function to find the winner wether its computer or User :) 

def calculate_winner(user_move, computer_move):
    if user_move == computer_move:
        return "Tie"

    if user_move == "Rock":
        if computer_move == "Scissors":
            return "User"
        if computer_move == "Paper":
            return "Computer"

    if user_move == "Paper":
        if computer_move == "Rock":
            return "User"
        if computer_move == "Scissors":
            return "Computer"

    if user_move == "Scissors":
        if computer_move == "Paper":
            return "User"
        if computer_move == "Rock":
            return "Computer"


# Used kera_model.h5 which is already test and trained on teachable-machine

model = load_model("/Users/pratiksha/Documents/scratch/Computer_vision_rpsn_game/Rock_paper_scissors_nothing/keras_model.h5")
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

"""
created function to get the prediction and based on that user pass rock paper and scissors expression 
and computer to give random choices 
"""

def get_prediction():
    prev_move = "Nothing"
    computer_move = "Nothing"
    winner = "Nothing"
    Game_Name = "ROCK PAPER SCISSORS"
    print('Welcome to ' +Game_Name+ ' Game! ')
    while True:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        inx_value = np.argmax(prediction)
        user_move = mapper(inx_value)
        if prev_move != user_move:
            if user_move != "Nothing":
                computer_move = choice(["Rock", "Paper", "Scissors"])
                winner = calculate_winner(user_move, computer_move)
            
            else:
                computer_move = "Nothing"
                winner = "Waiting..."
        prev_move = user_move       
           # display the information
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Your Move: " + user_move,
                    (50, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "Computer's Move: " + computer_move,
                    (750, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "Winner: " + winner,
                (400, 600), font, 2, (0, 0, 255), 4, cv2.LINE_AA)
                
        cv2.imshow('Rock Paper Scissors ', frame)

        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break       
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return winner

# calling the functions
winner_game = get_prediction()
print('And the winner is : ', winner_game)


