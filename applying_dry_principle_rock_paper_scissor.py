import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = {ROCK: '🪨' , SCISSORS: '✂️' , PAPER: '📃'}
choices = tuple(emojis.keys())
player1_correct_attempts = 0
player2_correct_attempts = 0
no_of_ties = 0
print("Rock, Paper, Scissor Game:")
player1_name = input("Enter the name of the first player: ").strip()
player2_name = input("Enter the name of the second player: ").strip()

def get_user_choice():
    user_choice = input("Rock, paper or scissors? (r/p/s): ").strip()
    if(user_choice in choices):
        return user_choice
    else:
        print("Invalid choice!")

def display_choices(user1_choice , user2_choice):
    print(f"{player1_name} chose {emojis[user1_choice]}")
    print(f"{player2_name} chose {emojis[user2_choice]}")

def determine_winner(user1_choice , user2_choice):
    if((user1_choice == ROCK and user2_choice == SCISSORS) or
       (user1_choice == SCISSORS and user2_choice == PAPER) or 
       (user1_choice == PAPER and user2_choice == ROCK)):
        print(f"{player1_name} wins")
        player1_correct_attempts+=1
    elif(user1_choice == user2_choice):
        print("It's a draw!")
        no_of_ties+=1
    else:
        print(f"{player2_name} wins")
        player2_correct_attempts+=1

def display_statistics():
    print("Game Over!")
    print(f"{player1_name} wins: {player1_correct_attempts}")
    print(f"{player2_name} wins: {player2_correct_attempts}")
    print(f"Ties: {no_of_ties}")
    if(player1_correct_attempts > player2_correct_attempts):
        print(f"{player1_name} won the game!")
    elif(player1_correct_attempts < player2_correct_attempts):
        print(f"{player2_name} won the game!")
    else:
        print("Match is draw!")

def play_game():
    while(True):
        user1_choice = get_user_choice()
        user2_choice = get_user_choice()
        display_choices(user1_choice , user2_choice)
        determine_winner(user1_choice , user2_choice)
        
        play_again = input("Continue? (y/n): ").strip()
        if(play_again.lower() == "y"):
            continue 
        elif(play_again.lower() == "n"):
            display_statistics()
            break 
        else:
            print("Invalid choice!")

play_game()

