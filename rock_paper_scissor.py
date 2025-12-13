import random

emojis = {'r': '🪨' , 's': '✂️' , 'p': '📃'}
choices = ('r' , 'p' , 's')
player1_correct_attempts = 0
player2_correct_attempts = 0
no_of_ties = 0
print("Rock, Paper, Scissor Game:")
player1_name = input("Enter the name of the first player: ").strip()
player2_name = input("Enter the name of the second player: ").strip()
while(True):
    user1_choice = input("Rock, paper or scissors? (r/p/s): ").strip()
    if(user1_choice not in choices):
        print("Invalid choice!")
        continue
    user2_choice = input("Rock, paper or scissors? (r/p/s): ").strip()
    if(user2_choice not in choices):
        print("Invalid choice!")
        continue
    print(f"{player1_name} chose {emojis[user1_choice]}")
    print(f"{player2_name} chose {emojis[user2_choice]}")
    if((user1_choice == "r" and user2_choice == "s") or
       (user1_choice == "s" and user2_choice == "p") or 
       (user1_choice == "p" and user2_choice == "r")):
        print(f"{player1_name} wins")
        player1_correct_attempts+=1
    elif(user1_choice == user2_choice):
        print("It's a draw!")
        no_of_ties+=1
    else:
        print(f"{player2_name} wins")
        player2_correct_attempts+=1
    play_again = input("Continue? (y/n): ").strip()
    if(play_again.lower() == "y"):
        continue 
    elif(play_again.lower() == "n"):
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
        break 
    else:
        print("Invalid choice!")