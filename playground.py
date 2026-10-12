#added some extra features, such as input validation,
#  a winning streak bonus, a scoreboard, and the option to restart the game.
import random

# created a dictionary to connect each player’s choice to its 
# corresponding ASCII art, to display the appropriate 
# image after the user makes a choice.
from art import *

#used to create the scoreboard.
from prettytable import PrettyTable

#each key points to the corresponding ASCII art.
hand_signs = {"rock": rock, 
              "paper": paper, 
              "scissors": scissors}
# rule
win_condition = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

# predict what could beat the user's choice.
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



# main function: Everything that happens during the game is mostly inside this function.
def rps_game():

    # checks whether the user has won three rounds consecutively.
    def streak_checker():

        nonlocal streak_list
        # streak_list belongs to the surrounding rps_game() 
        # function, rather than creating a new local variable 
        # inside streak_checker().
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
    table = PrettyTable()

    # creates your table headings.
    table.field_names =["Round", "You", "Computer"]

    round = 1
    # Keeps track of consecutive wins.
    streak_list = []

    choice_list = ["rock", "paper", "scissors"]

    # Keeps track of the choices that can 
    # beat the user's previous choices.
    counter_user = []

    # stores the results of each round.
    game_board = {
        "Round": [],
        "You": [],
        "Computer": []
    }


    print(logo)
    print("Welcome to the Rock Paper Scissors game!")
    end_safe = False
    #Check to ensure user doesn't enter an invalid input
    #  (something that cannot be converted to an integer)
    while not end_safe:
        try:
            end = int(input("Play first to: "))
            #Check to make sure the end is a valid integer input
            while end < 1:
                print("Value must be an integer greater than 0: ")
                end = int(input("Play first to: "))
            end_safe = True
            # prevent program from crashing
        except ValueError:
            print("Input must be an integer.")

    mode = input("Select your mode: 1 for Easy or 2 for Hard?: ")

    # keep running as neither player has reached the winning score
    # main loop
    while score_board["user"] != end and score_board["computer"] != end:
        while mode != "1" and mode != "2":
           mode = input("Invalid input. Enter '1' or '2': ")

        if mode == "1":
            c_choice = random.choice(choice_list)
        else:
            # computer has access to the normal choices plus choices 
            # that can counter the user's previous choices.
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

        #determinng the winner
        winner = None
        if u_choice == c_choice:
            winner = "tie"

            # resets the user's winning streak
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

        game_board["Round"].append(round)
        if winner == "tie":
            game_board["You"].append("---")
            game_board["Computer"].append("---")
        elif winner == "user":
            game_board["You"].append(1)
            game_board["Computer"].append(0)
        else:
            game_board["You"].append(0)
            game_board["Computer"].append(1)

        table.add_row([game_board["Round"][round-1], game_board["You"][round-1], game_board["Computer"][round-1]])



        print(f"Your score: {score_board['user']} and Computer's score: {score_board['computer']}")
        print(table)
        round += 1
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


