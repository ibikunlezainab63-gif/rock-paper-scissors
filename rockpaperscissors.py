import random
from art import *

hand_signs = {"rock": rock, 
              "paper": paper, 
              "scissors": scissors}

win_condition = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

opp = {
    "scissors": "rock",
    "rock": "paper",
    "paper": "scissors"
}

#check whether the user's input is one of the allowed choices
def user_validator(user, options):
    if user in options:
        return True
    else:
        return False




def rps_game():
    def streak_checker():
        nonlocal streak_list
        if len(streak_list) < 3:
            return
        if len(streak_list) == 3:
            print("You've earned a streak bonus! +1 point")
            score_board[streak_list[0]] += 1
            print(f"Your score: {score_board['user']} and Computer's score: {score_board['computer']}")
            streak_list = []
    #Keep track of user score and computer score
    score_board = {
        "user": 0,
        "computer": 0
    }

    streak_list = []
    choice_list = ["rock", "paper", "scissors"]
    counter_user = []

    print(logo)
    print("Welcome to the Rock Paper Scissors game!")
    end_safe = False
    #Check to ensure user doesn't enter an invalid input (something that cannot be converted to an integer)
    while not end_safe:
        try:
            end = int(input("Play first to: "))
            #Check to make sure the end is a valid integer input
            while end < 1:
                print("Value must be an integer greater than 0: ")
                end = int(input("Play first to: "))
            end_safe = True
        except ValueError:
            print("Input must be an integer.")

    mode = input("Select your mode: 1 for Easy or 2 for Hard?: ")
    # keep running as neither player has reached the winning score
    while score_board["user"] != end and score_board["computer"] != end:
        while mode != "1" and mode != "2":
           mode = input("Invalid input. Enter '1' or '2': ")

        if mode == "1":
            c_choice = "rock" #random.choice(choice_list)
        else:
            c_choice = random.choice(choice_list + counter_user)

        #Ask the user to make a choice
        u_choice = input("Make your choice, 'rock', 'paper' or 'scissors': ").strip().lower()

        #Check if the user entered a valid input 
        while not user_validator(u_choice, choice_list):
            print(f"You've entered an invalid input: [{u_choice}]. Try again.")
            u_choice = input("Make your choice, 'rock', 'paper' or 'scissors': ").strip().lower()
        
        #Show the user what they picked and what the computer's choice was
        counter_user.append(opp[u_choice])
        print(f"{hand_signs[u_choice]}", "VS", f"{hand_signs[c_choice]}", sep="\n")
        #We need to keep track of who the winner is for a round
        winner = None
        if u_choice == c_choice:
            winner = "tie"
            streak_list = []
            print("It's a tie!")
        else:
            for key, value in win_condition.items():
                if u_choice == key and c_choice == value:
                    winner = "user"
                    streak_list.append(winner)
                    print("You win this round.")
                    break
            if not winner:
                streak_list = []
                winner = "computer"
                print("Computer wins this round.")

        if winner and winner != "tie":
            score_board[winner] +=1

        print(f"Your score: {score_board['user']} and Computer's score: {score_board['computer']}")
        if score_board["user"] + 1 <= end:
            streak_checker()

    if score_board["user"] > score_board["computer"]:
        print("Game over: You Win!")
    else:
        print(f"Game over: Computer Wins")

    if input("Do you want to restart the game? Yes or No: ").strip().lower() == "yes":
        rps_game()
    else:
        print("Goodbye!")

rps_game()
